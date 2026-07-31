"""DATA 608 hex logo: polar sea-ice traces (1979-2024) on an Okabe-Ito hex."""
import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib import font_manager, cm

HEX_BG = "#0072B2"      # Okabe-Ito blue
HEX_BORDER = "#E69F00"  # Okabe-Ito orange
CMAP_LO, CMAP_HI = 0.32, 1.0   # trim viridis dark end (invisible on blue)

df = pd.read_csv(
    __import__("os").path.join(__import__("os").path.dirname(__file__), "../meetups/meetup-4/sea_ice.csv"),
    parse_dates=["date"],
)
df["year"] = df.date.dt.year
df["doy"] = df.date.dt.dayofyear
df = df[(df.year >= 1979) & (df.year <= 2024)]

# radial mapping: leave a central hole for the wordmark
R_HOLE, R_OUTER = 0.42, 0.83
e_lo, e_hi = df.Extent.min(), df.Extent.max()

def radius(extent):
    return R_HOLE + (extent - e_lo) / (e_hi - e_lo) * (R_OUTER - R_HOLE)

years = sorted(df.year.unique())
viridis = cm.get_cmap("viridis")
colors = {
    y: viridis(CMAP_LO + (y - years[0]) / (years[-1] - years[0]) * (CMAP_HI - CMAP_LO))
    for y in years
}

# pointy-top hexagon (hexSticker orientation), circumradius 1, centered at 0
ang = np.deg2rad(np.arange(90, 451, 60))
hex_xy = np.column_stack([np.cos(ang), np.sin(ang)])
hex_path = Path(hex_xy, closed=True)

fig = plt.figure(figsize=(8, 8 * np.sqrt(3) / 2 * (2 / np.sqrt(3))), dpi=300)
fig.set_size_inches(8, 8)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(-1.05, 1.05)
ax.set_ylim(-1.05, 1.05)
ax.set_aspect("equal")
ax.axis("off")

ax.add_patch(PathPatch(hex_path, facecolor=HEX_BG, edgecolor="none", zorder=0))

# sea ice rings, clipped to the hexagon; angle 0 (Jan 1) at top, clockwise
clip = PathPatch(hex_path, transform=ax.transData, facecolor="none", edgecolor="none")
ax.add_patch(clip)
for y in years:
    g = df[df.year == y].sort_values("doy")[["doy", "Extent"]].copy()
    nxt = df[(df.year == y + 1)].sort_values("doy").head(1)
    if len(nxt):  # close the loop through Jan 1 of the following year
        g = pd.concat([g, pd.DataFrame({"doy": [366 + nxt.doy.iloc[0]],
                                        "Extent": [nxt.Extent.iloc[0]]})])
    doy, ext = g.doy.values.astype(float), g.Extent.values
    # break the line where the record has gaps (e.g. Dec 1987 outage)
    gaps = np.where(np.diff(doy) > 6)[0]
    doy = np.insert(doy, gaps + 1, np.nan)
    ext = np.insert(ext, gaps + 1, np.nan)
    ROT = np.deg2rad(72.8)  # puts the Sept minimum at the bottom
    theta = np.pi / 2 - 2 * np.pi * (doy - 1) / 366.0 + ROT
    r = radius(ext)
    DY = -0.05  # drop the ring slightly so the hole centers on the wordmark
    (line,) = ax.plot(
        r * np.cos(theta), r * np.sin(theta) + DY,
        color=colors[y], lw=1.3, alpha=0.88, zorder=1,
        solid_capstyle="round",
    )
    line.set_clip_path(clip)

# border drawn last, on top of clipped traces
ax.add_patch(
    PathPatch(hex_path, facecolor="none", edgecolor=HEX_BORDER, lw=14,
              joinstyle="miter", zorder=3)
)

lato = font_manager.FontProperties(family="Lato", weight="black")
ax.text(
    0, 0, "DATA 608", ha="center", va="center",
    fontproperties=lato, fontsize=50, color="white", zorder=2,
)

out = __import__("os").path.join(__import__("os").path.dirname(__file__), "course_logo.png")
fig.savefig(out, transparent=True)
print("wrote", out)

"""DATA 608 hex logo: polar sea-ice traces (1979-2024) on an Okabe-Ito hex."""
import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib import font_manager, cm
import matplotlib.patheffects as pe

HEX_BG = "#FFFFFF"      # white face; hex shape carried by the border
HEX_BORDER = "#E69F00"  # Okabe-Ito orange
CMAP_LO, CMAP_HI = 0.0, 1.0   # full viridis; dark end reads well on white

df = pd.read_csv(
    __import__("os").path.join(__import__("os").path.dirname(__file__), "../meetups/meetup-4/sea_ice.csv"),
    parse_dates=["date"],
)
df["year"] = df.date.dt.year
df["doy"] = df.date.dt.dayofyear
df = df[(df.year >= 1979) & (df.year <= 2024)]

# radius proportional to extent (true zero) so the seasonal amplitude,
# especially the September minimum, keeps its real proportions.
# SCALE_MAX is the extent (10^6 sq km) that maps to R_OUTER; a value below
# the data max pushes the traces outward so the ring fills the hex.
R_OUTER = 0.78
SCALE_MAX = 14.0

def radius(extent):
    return extent / SCALE_MAX * R_OUTER

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

# center the ring's bounding box in the hexagon (the September pinch
# otherwise pushes the whole loop toward the upper right)
_th = np.pi / 2 - 2 * np.pi * (df.doy - 1) / 366.0
_r = radius(df.Extent.values)
_x, _y = _r * np.cos(_th), _r * np.sin(_th)
XOFF = -(_x.max() + _x.min()) / 2
YOFF = -(_y.max() + _y.min()) / 2

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
    # gg_season orientation: Jan 1 at 12 o'clock, clockwise
    theta = np.pi / 2 - 2 * np.pi * (doy - 1) / 366.0
    r = radius(ext)
    (line,) = ax.plot(
        r * np.cos(theta) + XOFF, r * np.sin(theta) + YOFF,
        color=colors[y], lw=1.9, alpha=0.88, zorder=1,
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
    0.06, 0, "DATA 608", ha="center", va="center",
    fontproperties=lato, fontsize=51, color="#0072B2", zorder=2,
    path_effects=[pe.withStroke(linewidth=9, foreground=HEX_BG)],
)

out = __import__("os").path.join(__import__("os").path.dirname(__file__), "course_logo.png")
fig.savefig(out, transparent=True)
print("wrote", out)

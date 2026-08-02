> **Revision note (2026-07-31):** this detailed report was written assessing plotnine as the
> primary translation path. Per instructor preference for the industry-standard matplotlib/seaborn
> stack, section 5 of `source-audit.md` supersedes the framing here: same feasibility findings, but
> ratings/effort re-cast for idiomatic mpl/seaborn versions (revised total ~4-5 weeks). The per-deck
> technique inventories below remain the authoritative record of what each deck contains.

# Python Parallel Audit — DATA 608 Meetup Decks 1–14

Assessment of replicating each deck's R code in Python, with attention to what
Rougier's *Scientific Visualization: Python + Matplotlib* actually covers
(pure matplotlib: figure anatomy, scales/projections, color, annotation,
animation, 3D — no grammar-of-graphics, no statistical-model helpers).

Deck 15 is a stub (no content) and is excluded.

## Overview table

| Deck | Topic | R stack (actually used) | Python stack needed | Rougier coverage | Rating | Effort |
|---|---|---|---|---|---|---|
| 1 | Critical eye / course intro | ggplot2 bar charts, patchwork, palmerpenguins (1 chunk; rest images) | plotnine (or matplotlib subplots) | Partial — "Anatomy of a figure" frames good/bad/ugly discussion | EASY | Small |
| 2 | Graphical perception (Cleveland) | base `pie()`, ggplot bar/dot plots, facet_wrap (barley), mpg scatter | matplotlib pie + plotnine; seaborn optional | Good — colormap slides already cite matplotlib docs; his Color chapter fits | EASY | Small |
| 3 | Quality features (Tufte, ink, themes) | ggplot bar/line/area, coord_cartesian, scale_size_area, ggthemes (excel/tufte/clean), facet_grid, theme() micro-styling, stat_smooth(lm) | plotnine + statsmodels (lm smoother); matplotlib rcParams for theme demos | Partial — "Better defaults" / figure anatomy chapters are the same lesson; theme_excel/tufte clones need manual rcParams | EASY | Medium |
| 4 | Associations & time series | ggplot scatter/facets, okabe-ito, stat_ellipse, geom_text/ggrepel, log scales, GGally ggpairs, patchwork, annotate rects, feasts/tsibble gg_season (+polar), geom_path | plotnine + seaborn pairplot + adjustText + pandas; matplotlib polar axes for seasonal plot | Partial — polar projection (Projections ch.) and annotation (Ornaments ch.) yes; ggpairs/faceting/repel no | EASY–MODERATE | Large |
| 5 | Geospatial | maps/geom_polygon, sf/geom_sf, nycgeo, rnaturalearth, coord_sf projections, usmap choropleths, statebins, geofacet | geopandas + cartopy (deck already recommends a Cartopy tutorial); manual grid for statebins/facet_geo | Weak — brief projections material; cartopy + geopandas docs are the real source | MODERATE | Large |
| 6 | Narrative structure | ggplot line charts, heavy `annotate()` (text/rect/vline/hline), geom_smooth GAM, facet_grid bars, coord_flip, OWID/nycflights13 data | plotnine + pandas; statsmodels lowess (or pygam) for the GAM smoother; matplotlib annotate | Strong — his annotation/ornaments chapter is exactly this deck's craft | EASY | Medium |
| 7 | Color | RColorBrewer, ggokabeito, colorblindr, colorBlindness, colorspace, paletteer; geojsonsf + sf choropleth | matplotlib colormaps + seaborn/palettable palettes; daltonlens (Python CVD simulator — deck already cites daltonlens.com); geopandas for the geojson map | Strong — Color chapter (sequential/diverging/qualitative, perceptual uniformity) is the closest fit in the whole course | EASY–MODERATE | Medium |
| 8 | Distributions | geom_histogram (bins/binwidth/center/boundary), freqpoly, geom_density (kernel/bw/bounds), stat_ecdf, stat_qq(+line), ggridges | plotnine + seaborn (histplot/kdeplot/ecdfplot); scipy.stats.probplot or statsmodels qqplot; joypy or FacetGrid for ridges | Weak — hist/KDE are one-liners anywhere; seaborn + scipy docs are the workhorse | EASY | Medium |
| 9 | Models & uncertainty | broom (tidy/augment), tidymodels split, lm/glm with interactions, geom_pointrange coef plots, purrr nested models, **marginaleffects** (plot_predictions/comparisons/slopes) | statsmodels (formula API) + sklearn train_test_split + pandas groupby; **marginaleffects Python port exists** (same author, same API, plots via plotnine, includes `get_dataset`) | None — marginaleffects.com book (has Python tabs) + statsmodels docs | MODERATE | Large |
| 10 | Dimensionality reduction (PCA) | prcomp + broom, ggpairs, dviz.supp custom correlogram, scree plots, loadings arrows + ggrepel, plotly 3D scatter | sklearn PCA (explained_variance_ratio_, components_), seaborn pairplot/heatmap, plotnine, plotly.py for 3D | Partial — 3D chapter if you swap plotly for mpl3d (but plotly.py is a drop-in for the deck's plotly figure); anatomy ch. helps the loadings plot | EASY | Medium |
| 11 | Clustering (k-means) | stats::kmeans + broom augment, elbow plots via purrr map, ggforce geom_mark_ellipse, back-transformed center bar facets, rattle wine / cluster ruspini data | sklearn KMeans (inertia_ for elbow) + pandas; matplotlib Ellipse or convex hull for cluster marks | None — sklearn docs are the workhorse | EASY | Medium |
| 12 | Hierarchical clustering | hclust/cutree, ggdendro (manual colored dendrograms), cluster::daisy Gower, **tidyheatmaps** annotated clustered heatmap, usmap + geom_sf cluster choropleths | scipy.cluster.hierarchy (linkage/dendrogram/fcluster), **seaborn clustermap** (row_colors = annotation_row), `gower` pip package, geopandas — the deck itself lists the seaborn/scipy docs as Python readings | None — scipy + seaborn clustermap docs (already cited in the deck) | MODERATE | Medium |
| 13 | Shiny reactivity | quarto `server: shiny`, sliderInput/selectInput, renderPlot, reactive(), reactive-graph theory | **Shiny for Python** — Quarto supports `server: shiny` with `{python}` cells and `#| context: server`; reactive.calc / @render.plot map 1:1 | None — shiny.posit.co/py docs | MODERATE | Medium |
| 14 | Shiny layouts & themes | fluidPage/sidebarLayout/fluidRow/tabsetPanel, bslib bootswatch themes, thematic (all `eval: false` + screenshots) | shiny-python ui.page_fluid/ui.layout_sidebar/ui.navset_tab; **shinyswatch** for bootswatch themes; no direct `thematic` port (set matplotlib style manually) | None — shiny.posit.co/py layout docs | MODERATE | Small |

## Per-deck notes

### Deck 1 — Developing a Critical Eye (Small, EASY)
- Almost entirely image/concept slides. One real chunk: four penguin bar charts
  (good/ugly/bad/wrong) composed with patchwork; loads tidyverse, kableExtra,
  ggrepel, scales, patchwork, ggthemes, DT but uses almost none of them.
- Python: plotnine reproduces all four charts (theme_bw, coord_cartesian trick,
  brewer Pastel1); compose with matplotlib subfigures or just show 4 slides.
- Rougier's "Anatomy of a figure" is good companion reading for the
  good/bad/ugly framing, but plotnine docs do the actual work.

### Deck 2 — Graphical Perception Theory (Small, EASY)
- ~90% images (Cleveland–McGill perceptual tasks). Code: base-R `pie()`,
  ggplot bar chart, Cleveland dot plot, mpg scatter with shape+color, barley
  facet_wrap small multiples.
- Python: `plt.pie`, plotnine geom_point/geom_bar/facet_wrap. Trivial.
- Rougier fit is real here: the colormap-taxonomy slides literally screenshot
  the matplotlib colormaps page, and his Color chapter covers perceptual
  uniformity. Faceting/small-multiples idiom comes from plotnine docs instead.

### Deck 3 — Visualization Quality Features (Medium, EASY)
- All standard ggplot: bar plots at 0 (coord_cartesian), filled area plots,
  scale_size_area vs scale_radius, chartjunk demo via ggthemes::theme_excel,
  progressive cleanup (theme_bw → minimal → tufte), Titanic facet_grid,
  gridline `theme()` surgery, tech-stocks lines, lm scatter via stat_smooth.
- Python: plotnine has theme_bw/minimal/void and full `theme()` element
  control; geom_smooth(method="lm") works (statsmodels under the hood).
  No theme_excel/theme_tufte clones — imitate with a few rcParams (arguably
  a nice teaching moment). scale_size_area exists in plotnine.
- Rougier's "Better defaults" chapter teaches the same de-junking lesson in raw
  matplotlib; effort is mostly volume of chunks, not difficulty.

### Deck 4 — Associations and Time Series (Large, EASY–MODERATE)
- The biggest applied deck: scatter + color/shape/facets, okabe-ito scales,
  grey-background "show all points in every facet" trick, stat_ellipse group
  ellipses + manual label dataframes, gapminder log-scale labeled scatter,
  geom_text check_overlap, ggrepel subset labeling, bubble plots, GGally
  ggpairs, GDP/unemployment lines stacked with patchwork, annotate() recession
  rectangles, direct line labeling with geom_text_repel, feasts/tsibble
  gg_season seasonal plot (rectangular AND polar), lynx-hare geom_path
  connected scatterplot.
- Python mapping: plotnine covers ~80% directly (okabe-ito = manual palette
  list). MODERATE bits: stat_ellipse → matplotlib confidence-ellipse recipe
  (official mpl gallery example); ggrepel → `adjustText`; ggpairs → seaborn
  `pairplot`; gg_season → pandas groupby(year) line plot, and the polar
  version → matplotlib `projection="polar"` axes (this is where Rougier's
  Projections chapter genuinely earns its keep); patchwork → plt.subplots or
  patchworklib.
- Effort Large mainly by figure count (~25 figures), not any single blocker.

### Deck 5 — Geospatial (Large, MODERATE)
- R stack: maps/geom_polygon (county outlines), sf + geom_sf, nycgeo tract
  choropleths (ACS data), rnaturalearth world + coord_sf projections
  (Mollweide, sinusoidal), usmap/usmapdata county choropleths, statebins
  cartogram, geofacet facet_geo (time series per state in a US-shaped grid),
  socviz election dot plot.
- Python: geopandas `.plot(column=…)` for every choropleth; projections via
  geopandas `.to_crs("ESRI:54009")` or cartopy (the deck already assigns a
  Cartopy tutorial to Python users). Data is the bigger cost: nycgeo/socviz/
  usmapdata are R data packages — replace with NYC Open Data geojson, census
  shapefiles, naturalearth via `geodatasets`.
- No maintained Python statebins; facet_geo → manual dict of state grid
  positions + matplotlib subplot grid (fiddly but bounded). These two are the
  closest thing to HARD in the course, though both are rebuildable in a day.
- Rougier: thin. Cartopy + geopandas galleries are the real documentation.

### Deck 6 — Narrative Structure (Medium, EASY)
- Story-arc figures: OWID coal/gas/CO2 line charts driven almost entirely by
  `annotate()` (text, rect shading, vline/hline) — plus one deliberately
  overcomplex nycflights figure (bubble + GAM smoothers + okabe-ito + size
  legend surgery) and facet_grid weekday bar small multiples.
- Python: plotnine annotate() is API-identical; the GAM smoother is the only
  wrinkle (use geom_smooth(method="lowess") or pygam; the pedagogical point
  survives either way).
- This is the deck where Rougier helps most per-slide: his annotation
  chapter is exactly "label the event on the chart" craft, transferable even
  if you build the figures in plotnine.

### Deck 7 — Working with Color (Medium, EASY–MODERATE)
- Palette-tour deck: RColorBrewer swatches/display.brewer.all, ggokabeito,
  colorblindr swatch plots, colorBlindness::displayAllColors CVD simulation,
  colorspace darken(), manual hex + alpha vectors, scale_*_manual accent
  palettes, one geojson sf choropleth (Airbnb occupancy).
- Python: matplotlib colormap registry + seaborn `color_palette`/`palplot`
  (Brewer palettes built in), palettable for paleteer-style breadth; okabe-ito
  as a hex list. CVD simulation: `daltonlens` (Python-native — the deck
  already points students at daltonlens.com) or `colorspacious`; darken() →
  colorsys/seaborn light/dark utilities. geopandas for the map.
- Rougier's Color chapter is the strongest single Rougier↔deck match in the
  course (colormap types, perceptual uniformity, choosing palettes).

### Deck 8 — Visualizing Distributions (Medium, EASY)
- geom_histogram with binwidth/bins/center/boundary, geom_freqpoly, KDE with
  kernel/bandwidth/`bounds`, stat_ecdf, qq-plots (stat_qq + stat_qq_line +
  annotated outlier boxes), faceted histograms, overlapping densities,
  ggridges ridge plots. Uses the Airbnb csv (absolute path — data dependency
  to fix regardless of language).
- Python: seaborn histplot (bins/binwidth/binrange), kdeplot (bw_adjust,
  cut/clip ≈ bounds), ecdfplot; scipy.stats.probplot or statsmodels
  `qqplot` for QQ; ridge plots via joypy or the seaborn FacetGrid ridgeline
  gallery example. plotnine also has geom_histogram/geom_density/stat_ecdf if
  staying grammar-consistent. Bin `center`/`boundary` have no seaborn keyword
  — compute bin edges with numpy (one line).
- Rougier: not really; seaborn + scipy docs carry this deck.

### Deck 9 — Models and Uncertainty (Large, MODERATE)
- Heaviest modeling deck: glm logistic (Thornton HIV data via
  marginaleffects::get_dataset), big lm with interactions on Airbnb data,
  tidymodels initial_split, broom tidy/augment, coefficient dot +
  geom_pointrange plots, purrr nest/map many-models on gapminder, and the
  centerpiece — marginaleffects `plot_predictions` / `plot_comparisons`
  (lift) / `plot_slopes` (elasticity, `eyex`).
- Key fact: **the marginaleffects Python port exists and is maintained**
  (same author; wraps statsmodels/linearmodels models; `plot_predictions`,
  `plot_comparisons`, `plot_slopes`, `get_dataset` all present; returns
  plotnine plots). So the deck's conceptual core transfers almost verbatim:
  statsmodels `smf.ols`/`smf.glm` formulas → marginaleffects-python.
- Manual parts: broom tidy → statsmodels `summary_frame`/params + conf_int
  into pandas; nested models → groupby().apply; initial_split →
  sklearn.model_selection.train_test_split.
- Rougier: nothing. The marginaleffects.com book (which already has Python
  code tabs) + statsmodels docs are the path. Rated MODERATE/Large for the
  volume of data wrangling and model-API translation, not feasibility.

### Deck 10 — Dimensionality Reduction (Medium, EASY)
- ggpairs pair plot, prcomp + broom augment/tidy(matrix="rotation"),
  variance-explained scree plots, PC scatter colored by class (ovarian
  cancer, Australian athletes, wine), loadings-arrow plots with geom_segment
  + ggrepel, a custom dviz.supp correlogram (hclust-ordered dot-correlation
  matrix), and a plotly 3D PC scatter.
- Python: sklearn `PCA` (explained_variance_ratio_ = scree;
  `components_` = rotation; `fit_transform` = embeddings) + pandas; seaborn
  pairplot; loadings arrows via plt.annotate/quiver + adjustText; correlogram
  → seaborn heatmap of hclust-ordered corr (scipy leaves_list) or a manual
  scatter with size=|r|; plotly.py `scatter_3d` is a near copy-paste for the
  3D figure.
- Rougier: 3D chapter applies only if you swap plotly for mpl 3D; the anatomy
  chapter helps the loadings figure. sklearn docs are the workhorse.

### Deck 11 — Clustering / k-means (Medium, EASY)
- kmeans on PCA coordinates (wine), cluster centers overlay, ruspini toy
  data with k = 3/4/5/10, elbow plots via purrr map over k
  (tot.withinss), back-transforming centers to original units for faceted
  signed bar charts, ggforce geom_mark_ellipse cluster annotation.
- Python: sklearn `KMeans(n_clusters=k, n_init=10)`; `inertia_` gives the
  elbow plot in a list comprehension; center back-transform =
  `pca.inverse_transform` (cleaner than the R matrix algebra shown!);
  geom_mark_ellipse → matplotlib Ellipse from group covariance or
  scipy ConvexHull patch (the one MODERATE item).
- Rougier: no. sklearn clustering docs + the mpl confidence-ellipse example.

### Deck 12 — Hierarchical Clustering (Medium, MODERATE)
- hclust (ward/average), cutree at multiple heights, ggdendro `dendro_data`
  for fully manual dendrograms with region-colored, rotated labels and cut
  lines; cluster::daisy Gower distance for mixed types (mall customers);
  tidyheatmaps (pheatmap) clustered heatmap with column scaling and
  region/division annotation bars; k-means cluster choropleths via usmap +
  geom_sf.
- Python: scipy.cluster.hierarchy `linkage`/`dendrogram`/`fcluster`; the
  `gower` pip package for Gower distances; **seaborn `clustermap`** replaces
  tidyheatmaps almost feature-for-feature (`standard_scale`/`z_score` =
  scale="column", `row_colors` = annotation_row, `method="ward"`); geopandas
  for the state maps. The deck already lists seaborn clustermap and scipy
  cluster docs as its official Python readings, so this port is anticipated.
- MODERATE because scipy's dendrogram customization (colored leaf labels by
  external category, cut-height styling) is clunky compared to ggdendro —
  expect matplotlib label post-processing.

### Deck 13 — Shiny (Medium, MODERATE)
- `server: shiny` revealjs deck with live widgets: Old Faithful histogram
  (sliderInput + renderPlot), iris k-means explorer (selectInput,
  numericInput, reactive()), text/numeric input tours, and a freqpoly +
  t-test case study used to teach reactive graphs; plus much eval:false
  teaching code (fluidPage anatomy, reactive expressions, execution order).
- Shiny for Python is feasible and officially supported in Quarto: same
  `server: shiny` YAML with `{python}` cells and `#| context: server`.
  Mappings: sliderInput → ui.input_slider, renderPlot → @render.plot,
  reactive(x) → @reactive.calc; kmeans → sklearn; t.test → scipy.stats
  ttest_ind; freqpoly → matplotlib step/plotnine. The reactive-graph theory
  slides transfer unchanged — that is the point of the deck.
- MODERATE because the idiom differs (decorators vs assignment into
  `output$`), so code slides need rewriting, not transliteration.

### Deck 14 — Shiny Layouts (Small, MODERATE)
- Nearly all screenshots + `eval: false` code: sidebarLayout, fluidRow/column
  12-grid, tabsetPanel (+ tab id reactivity), bslib bootswatch themes,
  custom bs_theme, thematic auto plot theming.
- Shiny-python equivalents exist for everything except `thematic`:
  ui.page_fluid / ui.layout_sidebar / ui.row+ui.column / ui.navset_tab;
  bootswatch themes via the `shinyswatch` package. Plot-theme matching is
  done manually (matplotlib style sheet or plotnine theme) — small gap, easy
  to narrate. Since almost nothing executes, the port is mostly rewriting
  code listings and re-screenshotting.

## Bottom line

- **Roughly 70–75% of the course's R code has an EASY Python path**: it is
  core ggplot2 grammar (scatter/bar/line/facet/theme/scale/annotate), which
  plotnine reproduces nearly token-for-token, plus sklearn/scipy for PCA,
  k-means, and hierarchical clustering and seaborn for pairplot/KDE/
  clustermap. Another ~20% is MODERATE (geospatial data plumbing, scipy
  dendrogram styling, marginaleffects translation, shiny idiom, ellipse/repel
  annotations). Nothing is truly HARD; the only genuine rebuilds are
  statebins/facet_geo cartograms (deck 5) and pixel-faithful ggdendro
  dendrograms (deck 12).
- **Where Rougier genuinely helps**: decks 2 and 7 (color/colormaps — his
  Color chapter is the best single match, and deck 2 already screenshots the
  matplotlib colormap docs), deck 6 (annotation/ornaments), deck 3 (figure
  anatomy / better defaults), and the polar seasonal plot in deck 4
  (Projections chapter). His book teaches the *craft* layer of the course —
  anatomy, defaults, color, annotation.
- **Where he doesn't**: everything grammar- or model-shaped. Faceting and
  aesthetic mappings → plotnine docs; distributions/pairs/heatmaps → seaborn
  docs; PCA/k-means/hclust → sklearn + scipy docs; model interpretation →
  the marginaleffects Python port and its book (which ships Python tabs);
  maps → geopandas/cartopy; interactivity → plotly.py and Shiny-for-Python
  docs. Notably, decks 5 and 12 already cite the Python alternatives
  (cartopy tutorial, seaborn clustermap, scipy cluster), so the course was
  written with this parallel track half in mind.
- **Total effort estimate for full Python parallels of decks 1–14**: two
  Small + eight Medium + four Large ≈ 3–4 focused weeks of work, with decks
  4, 5, 9 dominating.

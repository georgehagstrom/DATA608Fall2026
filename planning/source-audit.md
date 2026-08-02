# DATA 608 Source Audit: Removing Knaflic & the "Data Practitioner's Guide"

*Prepared 2026-07-31. Audit of every module page, story assignment, meetup deck, and course page
in `website/`, plus web verification of all replacement resources. No course materials have been
changed; this document only maps what depends on the sources being removed and what can replace it.*

**Removal targets:**
- **SWD** — Cole Nussbaumer Knaflic, *Storytelling with Data* (paid book; the PDF link in meetup 1 is an unauthorized copy)
- **DPG** — "A Data Practitioner's Guide to Telling Stories With Data Visualizations"
  (`modules/readings/data-practitioners-guide.pdf`, 38-slide deck inherited from the previous instructor's master course)

**Keepers:** Wilke *Fundamentals of Data Visualization* (free), Healy *Data Visualization: A Practical
Introduction* (free), plus Andrew Heiss's course materials (CC BY-NC 4.0) and other free sources below.

---

## 1. Executive summary

The dependency is **narrower than the citation count suggests**. It concentrates in exactly two places:

1. **Week 1 is the real project.** ~16 of ~45 slides in `meetup-1.qmd` are SWD/DPG-derived — the
   who/what/how audience framing, 3-minute story, Big Idea, and storyboard framework (SWD Ch 1),
   Knaflic's signature ticket-trends before/after case study, and the DPG's seven "quality features"
   reproduced verbatim. **Story 1 grades students on the SWD Ch 1 framework by name**
   (`story1.qmd:14`), so the deck and the assignment must change together.
2. **Everything else is shallow.** In modules 2, 3, 6, 7 and meetups 2, 6, 7, SWD appears only as a
   readings-list line; the decks' actual content is already Tufte/Wilke-based (meetup 6's story arcs
   *are* Wilke Ch 29; meetup 7's color content *is* Wilke Ch 4/19; meetup 3 is Tufte + Wilke Ch 17
   despite its DPG-derived title). Removing SWD from these weeks costs one line each plus one
   pie-chart slide in meetup 2.

Every removed item has a free, verified replacement — mostly from Wilke chapters already assigned,
Healy Ch 1, and Heiss's Summer 2026 course (sessions 2 and 15 are near drop-in lecture material for
the design-principles and storytelling roles). Section 3 gives the item-by-item map.

On the Python side: **~70–75% of the R code has an easy Python path** (plotnine translates the ggplot
grammar nearly token-for-token; sklearn/scipy/seaborn cover the ML decks), nothing is truly hard, and
the `marginaleffects` Python port (same author, same API) makes the models deck a translation rather
than a rebuild. **Rougier's book is a craft-layer complement, not a backbone** — it shines for color,
annotation, figure anatomy, and polar projections, but the workhorse docs are plotnine/seaborn/
sklearn/geopandas. A complete parallel track is ~3–4 focused weeks; a high-value partial track
(4 decks) is about a week. Details in section 5.

---

## 2. Dependency inventory

Centrality: **HIGH** = structural, requires redesign; MED = explicit but contained; LOW = one line.

| Location | Source | What depends on it | Centrality |
|---|---|---|---|
| `assignments/stories/story1.qmd:14` | SWD Ch 1 | Graded deliverables defined as storyboard / 3-minute story / big idea, cited to the book | **HIGH** |
| `meetups/meetup-1/meetup-1.qmd:236-316` | SWD Ch 1 | ~11 slides: who/what/how framing, elevator pitch/3-minute story, Big Idea, storyboard | **HIGH** |
| `meetup-1.qmd:63-74` | SWD | Opening hook: ticket-backlog before/after case study (Knaflic's Fig 0.3) | **HIGH** |
| `meetup-1.qmd:383-404` | DPG slide 8 | Three slides reproducing the seven "Visualization Quality Features" (Fidelity, Simplicity, Utility, Saliency, Efficacy, Uniformity, Amity) | **HIGH** |
| `meetup-1.qmd:112-176` | SWD + DPG | Textbook slides (SWD as a "most important textbook", **pirated PDF links at lines 120, 139**), week-plan readings/key-concepts slides | **HIGH** |
| `modules/module1.qmd:15,21,23` | SWD + DPG | Learning objective wording + 2 of 3 required readings | **HIGH** |
| `modules/module2.qmd:16,19` | SWD Ch 2 + DPG 8-11 | Readings items 2 and 5 (DPG 9-11 is redundant with the DataViz Catalogue link already assigned) | MED |
| `modules/module3.qmd:2,15,17` | DPG + SWD Ch 3 | Module *title* "Data Visualization Quality Features" + readings items 1, 3 | MED |
| `meetups/meetup-2/meetup-2.qmd:24-33,38` | SWD Ch 2 | One "Pie Charts are Evil" slide (image likely scanned from the book) + readings line | MED |
| `course/syllabus.qmd:17,64`; `course/overview.qmd:7-9`; `course/textbooks.qmd:13-15` | SWD + DPG | "art of 'Storytelling with Data'" marketing prose; SWD listed as required text #2 | MED |
| `meetups/meetup-3/meetup-3.qmd:2` | DPG | Deck **title only** — content is Tufte/Wilke and survives intact | LOW |
| `modules/module6.qmd:15`, `meetup-6.qmd:10` | SWD Ch 7 | Readings line only — the deck's story arcs are Wilke Ch 29's | LOW |
| `modules/module7.qmd:15`, `meetup-7.qmd:11` | SWD Ch 4 | Readings line only — deck is Wilke Ch 4/19 + R color packages | LOW |
| `course/schedule.qmd:16,19`; `modules/module4.qmd:11` | DPG voice | Module titles; "Know Your Audience..." mantra paragraph | LOW |

Verified clean: stories 2–7, meetups 4, 5, 8–15, and the "Exploration and Explanation in Data-Driven
Storytelling" research paper in module/meetup 14 (unrelated to Knaflic).

**What the DPG actually contains** (why it can't stay even as a stopgap): slides 1–7 are
motivational quotes and a Protégé ontology defining "practitioner-as-storyteller" (typo-ridden);
slide 8 is the seven-feature taxonomy (original to the deck, not from any published framework);
9–11 a tools inventory redundant with the DataViz Catalogue; 12–17 Tufte summaries fully covered by
Wilke Ch 17/24; 18–20 block quotes from one obscure paper (Cavaller 2021); and its unassigned
"techniques" section (21–38) **cites Knaflic throughout** — so the DPG is itself a Knaflic
derivative and cannot serve as her replacement.

---

## 3. Replacement map

All URLs fetch-verified 2026-07-31. Heiss = *Data Visualization with R*, Summer 2026 edition,
https://datavizs26.classes.andrewheiss.com/ — **CC BY-NC 4.0**, so reusing slides/videos/readings
lists in a nonprofit course with attribution is explicitly permitted. Each Heiss session ships free
readings + HTML/PDF slides + a YouTube lecture playlist + an interactive R lesson.

### 3.1 The Week-1 framework (SWD Ch 1) — the one real redesign

| Removed element | Replacement | Notes |
|---|---|---|
| Who/what/how audience framing | **Heiss session 1** "Truth, beauty, and data" (content: `/content/01-content.html`; videos playlist on the page) + **Healy Ch 1** (https://socviz.co/01-look-at-data.html) | Healy Ch 1 also gives the perception grounding that sets up meetup 2 |
| 3-minute story / Big Idea | **Wilke Ch 29** (https://clauswilke.com/dataviz/telling-a-story.html): "clear takeaway", "figure for the generals" | Keep the *deliverable* (a one-sentence takeaway is good pedagogy) — just re-source and rename it, e.g. "takeaway sentence" instead of "Big Idea" |
| Storyboard framework | **Heiss session 15** "Truth, beauty, and data revisited" (his storytelling capstone; slides `/slides/15-slides.html`, video playlist https://www.youtube.com/playlist?list=PLS6tnpTr39sFYqZMtanRbtB1dKRBN2Rzt) + The Pudding's process essay "How to make dope shit, part 1" (https://pudding.cool/process/how-to-make-dope-shit-part-1/) | Story 1 can still require a storyboard — sourced to these instead of SWD Ch 1 |
| Ticket-trends before/after hook | Build your own makeover from **Datawrapper "Datavis Dos and Don'ts"** (https://www.datawrapper.de/blog/category/datavis-dos-and-donts) or a **storytellingwithdata.com blog** makeover (the blog is free/legal even though the book is paid: https://www.storytellingwithdata.com/blog) | Alternative: FlowingData "Why people make bad charts" (https://flowingdata.com/2018/06/28/why-people-make-bad-charts-and-what-to-do-when-it-happens/), assigned in Heiss s15 |
| DPG "seven quality features" slides | **Wilke's ugly/bad/wrong taxonomy** (Ch 1 — already in the deck's penguin slides!) + **CRAP design principles** from Heiss session 2 (see 3.2) | The deck already teaches Wilke's taxonomy 30 slides later; the DPG list is redundant with it |
| Story 1's SWD citation (`story1.qmd:14`) | Reworded to: storyboard + one-paragraph pitch + one-sentence takeaway, citing Wilke Ch 29 and Heiss s15 | Deliverable structure unchanged; only the source and vocabulary change |

### 3.1b Alternative week-1 package without Heiss's "truth & beauty" framing

*(Added 2026-08-01. The "truth, beauty" frame is Heiss's own pedagogical synthesis — built on Cairo's
"The Truthful Art" (which his sessions 1/15 assign) plus his art/rhetoric "content + form for specific
audiences" layer. It is baked into sessions 1 and 15 but NOT into his practical sessions — session 2's
CRAP material, session 9's annotations, etc. carry none of it, so those remain adoptable à la carte.
If the framing is unwanted, the following free, verified, engineering-minded package replaces Knaflic
Ch 1 for week 1 / Story 1:)*

| Role | Resource | Why |
|---|---|---|
| Know your audience (the framework) | **Jean-luc Doumont, "The Three Laws of Professional Communication"** — (1) adapt to your audience, (2) maximize signal-to-noise, (3) use effective redundancy, governed by "law 0": have a purpose. Free paper reprint: https://users.cs.utah.edu/~dejohnso/threelaws.pdf ; his free Nature Scitable ebook *English Communication for Scientists*: https://www.nature.com/scitable/ebooks/english-communication-for-scientists-14053993/ | Audience-first without any beauty rhetoric; physicist-engineer voice (Stanford applied-physics PhD); signal-to-noise law doubles as the data-ink bridge to week 3 |
| Lecture video | **Doumont, "Creating effective slides" (Stanford, free):** https://www.youtube.com/watch?v=meBXuTIPJQk | Communication craft for rational minds; also reusable for the presentation-skills side of the stories |
| Storytelling, academically grounded | **Segel & Heer, "Narrative Visualization: Telling Stories with Data" (2010), free Stanford PDF:** http://vis.stanford.edu/files/2010-Narrative-InfoVis.pdf | The seminal genre/design-space paper (author-driven vs reader-driven narrative); same lineage as the "Exploration and Explanation" paper already assigned in week 14 — gives the course a coherent research thread |
| Practical "communicating numbers" | **Stephen Few's free Perceptual Edge library:** https://www.perceptualedge.com/library.php — esp. "Effectively Communicating Numbers" (https://www.perceptualedge.com/articles/Whitepapers/Communicating_Numbers.pdf), "Selecting the Right Graph for Your Message", "Statistical Narrative: Telling Compelling Stories with Numbers" | No-nonsense industry register; the "Statistical Narrative" piece covers the storytelling role Knaflic played, minus the branding |
| Formal audience/task analysis (optional, grad flavor) | **Tamara Munzner's what/why/how framework** — book is paid, but her complete teaching slides (all 15 chapters) are free at https://www.cs.ubc.ca/~tmm/vadbook/ and the full 2021 lecture series is on YouTube: https://www.youtube.com/playlist?list=PLT4XLHmqHJBeB5LwmRmo6ln-m7K3lGvrk | Treats "who is this for and what task does it serve" as a rigorous analysis step rather than marketing advice |

**Story 1 deliverable rewrite under this package:** audience-and-purpose statement (Doumont laws 0-1)
+ one-sentence takeaway (Wilke Ch 29's "clear message") + storyboard (Segel & Heer's structure /
The Pudding's process essay). Same three artifacts as before, no Knaflic vocabulary, no truth/beauty.

### 3.2 Design principles / "quality features" (DPG) → CRAP + Wilke

- **Heiss session 2 "Graphic design"** (`/content/02-content.html`) is the drop-in replacement for the
  DPG's design role: CRAP (Contrast, Repetition, Alignment, Proximity) from Robin Williams'
  *Non-Designer's Design Book* (book is paid, but two free summary PDFs are linked:
  Presentation Zen spread — https://web.archive.org/web/20170712142203/http://www.presentationzen.com/chapter6_spread.pdf —
  and Lewis University's one-pager — https://www.lewisu.edu/writingcenter/pdf/crap-resource-revised-pub.pdf),
  plus Butterick's "Typography in Ten Minutes" (https://practicaltypography.com/typography-in-ten-minutes.html)
  and Wilke Ch 4/27. Free slides + video playlist
  (https://www.youtube.com/playlist?list=PLS6tnpTr39sEznTwka0EmWfkkphjncq7U).
- Module 3's Tufte content needs nothing new — it is already Wilke Ch 17–26. Suggested readings swap:
  DPG slides 8/12-20 → CRAP handouts + Heiss s2; SWD Ch 3 → drop (Wilke 17–26 already assigned).
- Optional cosmetic: retitle module 3 / meetup 3 from the DPG's "Quality Features" phrase to e.g.
  "Design Principles for Visualization" (schedule row too). The deck content keeps as-is.

### 3.3 Chart choice / charts-to-avoid (SWD Ch 2)

- **Wilke Ch 5** "Directory of visualizations" (already assigned).
- **From Data to Viz** (https://www.data-to-viz.com/) — interactive data-type→chart decision tree
  **with a dedicated caveats/common-mistakes collection**; the R Graph Gallery / Python Graph Gallery
  companions supply working code per chart type.
- **FT Visual Vocabulary** (interactive: https://ft-interactive.github.io/visual-vocabulary/ ;
  poster PDFs: https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary — © FT, link don't rehost).
- Pie-chart slide in meetup 2: re-source to **Wilke Ch 10** (proportions) + Kosara's eagereyes pie
  pieces (https://eagereyes.org/techniques/pie-charts); replace the scanned `PieChartsEvil.png`.
- Schwabish's **Graphic Continuum** (free web version: https://policyviz.com/2014/09/09/graphic-continuum/).

### 3.4 Storytelling / narrative (SWD Ch 7) — module 6

Meetup 6 already teaches Wilke Ch 29 (its three story arcs, the kidney-cancer example, the
build-up-to-complexity flights sequence are all Wilke's). Readings swap: SWD Ch 7 → any/all of:
- **Heiss session 15** slides + videos (see 3.1) — ready-made lecture material on story arcs;
- **Ben Wellington**, "Making data mean more through storytelling" (TEDx, https://www.youtube.com/watch?v=6xsvGYIxJok);
- **Jon Schwabish**, "Better Data Communication" (free talk, https://vimeo.com/230757062) —
  audience-first framing closest in spirit to Knaflic.

### 3.5 Color & emphasis (SWD Ch 4) — module 7

Meetup 7 is already Wilke Ch 4/19 + Okabe-Ito. Readings swap: SWD Ch 4 → :
- **Lisa Charlotte Muth's Datawrapper color series** — especially **"Emphasize what you want readers
  to see with color"** (https://www.datawrapper.de/blog/emphasize-with-color-in-data-visualizations),
  the closest free equivalent of Knaflic's "focus attention" chapter; also "Which color scale to use"
  (https://www.datawrapper.de/blog/which-color-scale-to-use-in-data-vis) and the color-choice guide
  (https://www.datawrapper.de/blog/colorguide);
- **Cara Thompson**, "Using colour and annotations for effective storytelling" (free talk + slides:
  https://www.cararthompson.com/talks/colour-and-annotations/); her annotation talks
  (https://www.cararthompson.com/talks/user2022) also slot into meetups 6/9;
- Heiss sessions 2 (contrast) and 9 (annotations, all-free readings incl. Wilke Ch 20-22/24 and Healy Ch 5).

### 3.6 Course prose & textbook listings

- `syllabus.qmd:17` / `overview.qmd:7-9`: rewrite the "art of 'Storytelling with Data'" sentence
  (e.g. "the craft of storytelling with data" without the title-case book reference) and drop the
  "data practitioner / story request" master-course voice where convenient.
- `textbooks.qmd`: remove SWD from Required; **promote Healy from "Other Important Texts" to
  Required #2**; add as supplemental resources: Heiss's course site (with CC BY-NC attribution),
  From Data to Viz, the Datawrapper Academy (https://www.datawrapper.de/academy), and — if the Python
  track happens — Rougier (see §5).
- `module4.qmd:11` mantra paragraph: generic advice, fine to keep; optionally reworded to shed the
  inherited voice.

---

## 4. Free resources you may have overlooked (beyond the direct replacements)

- **UW Interactive Data Lab, "Visualization Curriculum"** (https://idl.uw.edu/visualization-curriculum/) —
  free Altair/Vega-Lite notebooks; the best open treatment of *encoding theory* (marks/channels,
  scales, multi-view composition, interaction). Natural supplement to meetups 2 and 14.
- **Duke STA 313, vizdata.org** (Mine Çetinkaya-Rundel — whose Data Science in a Box you already
  credit) — open Quarto course with weeks on presentation-ready plots, telling a story, accessibility.
- **Cédric Scherer, "A ggplot2 tutorial for beautiful plotting in R"**
  (https://www.cedricscherer.com/2019/08/05/a-ggplot2-tutorial-for-beautiful-plotting-in-r/) — the
  definitive free "make ggplot publication-quality" reference; also his raincloud-plots tutorial for
  meetup 8 (https://www.cedricscherer.com/2021/06/06/visualizing-distributions-with-raincloud-plots-with-ggplot2/).
- **Nightingale** (Data Visualization Society magazine, https://nightingaledvs.com/) — free articles;
  e.g. "I've stopped using box plots" fits meetup 8.
- **Datawrapper Weekly Chart** (https://www.datawrapper.de/blog/category/weekly-charts) — one worked
  chart per week; good discussion-post fodder.
- **The Pudding** (https://pudding.cool/) — exemplar data-driven visual essays for the storytelling weeks.
- **PolicyViz free resources** (https://policyviz.com/resources/policyviz-data-visualization-catalog/,
  blog, podcast) — Schwabish's books remain paid; his talks/blog are free.
- **daltonlens** (https://daltonlens.org) — Python colorblindness simulator; meetup 7 already links it.
- Checked and *not* recommendable right now: Stephanie Evergreen's checklist (site blocked automated
  verification — test in a browser), Peter Aldhous's old UCB course pages (link-rotted; his workshop
  notes survive at http://paldhous.github.io/kdmc-workshops/2017/intro-dataviz/principles.html).

**Paid items to flag clearly if kept as optional:** Knaflic (SWD), Cairo (*The Truthful Art* — Heiss
assigns it but always pairs free alternatives), Schwabish (*Better Data Visualizations*), Robin
Williams (*Non-Designer's Design Book*). **Action item regardless of the rest: remove the pirated
SWD PDF links at `meetup-1.qmd:120,139`.**

---

## 5. Python parallel track: matplotlib/seaborn-first, with Rougier as the craft text

*(Per instructor direction, this track targets the industry-standard **matplotlib + seaborn** stack
rather than plotnine. plotnine remains the cheapest translation path and is noted per deck as a
fallback, but the assessments below are for idiomatic mpl/seaborn "alternative code versions" of
the course visuals.)*

**Rougier, *Scientific Visualization: Python + Matplotlib*** — free/open (book CC BY-NC-SA 4.0, code
BSD-2): repo + PDF at https://github.com/rougier/scientific-visualization-book. Structure:
Fundamentals (figure anatomy, coordinates, scales & projections, typography, color); Figure design
(ten simple rules, mastering defaults, layout, ornaments/annotation); Advanced (animation, 3D,
optimization); Showcase.

**The mpl/seaborn decision upgrades Rougier from "complement" to the natural primary Python text**:
his entire book is idiomatic matplotlib, so nearly every chapter now maps onto course weeks (whereas
a plotnine track would have used him for only ~5 weeks). What he still does not supply — statistical
charts, faceting idiom, models, maps, interactivity — is covered by seaborn, sklearn/scipy/statsmodels,
geopandas, and Shiny-for-Python docs, all free.

Two structural notes for an mpl/seaborn track:

- **The grammar-of-graphics concepts survive translation.** Aesthetic mappings become seaborn's
  `hue`/`style`/`size` semantics; faceting becomes `FacetGrid`/`relplot(col=…)`/`catplot`; ggplot's
  `theme()` surgery becomes `rcParams`, style sheets, `sns.set_style`/`despine` — arguably a *better*
  vehicle for the meetup-3 de-junking lesson, and exactly Rougier's "Mastering the defaults" chapter.
  Where you want to *teach* layered-grammar thinking explicitly, seaborn's newer `seaborn.objects`
  interface (`so.Plot`, seaborn ≥0.12) is an industry-track middle ground worth a mention.
- **Verbosity is the real cost, not feasibility.** mpl/seaborn versions of the facet-heavy decks
  (3, 4) run longer than the R originals (manual legend handling, per-facet tweaks). That's also the
  pedagogy: students see what the grammar abstracts away.

### Parallel readings (mpl/seaborn track)

| Week | Course topic | Primary Python reading |
|---|---|---|
| 1 | Critical eye | Rougier *Anatomy of a figure* + *Ten simple rules* |
| 2 | Graphical perception | Rougier *A primer on colors*; matplotlib colormap docs (deck already screenshots them) |
| 3 | Design principles | Rougier *Mastering the defaults*, *Size/aspect/layout*; seaborn `set_style`/themes tutorial |
| 4 | Associations & time series | seaborn relational/`FacetGrid` tutorials; Rougier *Scales & projections* (polar seasonal plot) |
| 5 | Geospatial | geopandas user guide + Cartopy tutorial (already assigned in the deck) |
| 6 | Narrative/annotation | Rougier *Ornaments*; matplotlib annotation tutorial |
| 7 | Color | Rougier *A primer on colors*; seaborn color-palette tutorial; daltonlens |
| 8 | Distributions | seaborn distributions tutorial (histplot/kdeplot/ecdfplot); scipy probplot |
| 9 | Models & uncertainty | statsmodels formula API docs; marginaleffects book (**ships Python tabs**, https://marginaleffects.com) |
| 10-12 | PCA & clustering | sklearn PCA/KMeans docs; scipy.cluster.hierarchy docs; seaborn `clustermap` |
| 13-14 | Interactivity | Shiny for Python docs (https://shiny.posit.co/py/) — `@render.plot` **returns matplotlib figures natively** |

### Deck-by-deck: mpl/seaborn alternative code versions

| Deck | mpl/seaborn approach | Rating | Effort | Notes |
|---|---|---|---|---|
| 1 Critical eye | seaborn barplot ×4 + `plt.subplots` | EASY | Small | |
| 2 Perception | `plt.pie`, seaborn pointplot (Cleveland dot plot), `catplot(col=…)` for barley small multiples | EASY | Small | |
| 3 Quality/Tufte | rcParams/style-sheet de-junking (better than ggplot for this lesson), `sns.despine`, `regplot` for lm, `catplot` Titanic facets; `scale_size_area` → normalized `s=` | EASY–MOD | Medium+ | Theme-surgery slides get *more* instructive; volume grows |
| 4 Associations/time series | `relplot` hue/style/col (incl. grey-background trick via `map_dataframe`), mpl confidence-ellipse gallery recipe, `adjustText` for repel, seaborn `pairplot`, `axvspan` recession bands, groupby-year lines + `projection="polar"` seasonal plot | MODERATE | **Large** | ~25 figures; every one feasible, legends/facet annotations are the labor |
| 5 Geospatial | geopandas `.plot()` **is matplotlib** — unchanged; cartopy projections; statebins/facet_geo = manual mpl subplot grids | MODERATE | **Large** | Same as before; R data packages need data swaps |
| 6 Narrative | mpl `annotate`/`axvspan`/`axhline` is the *native* idiom for this deck; statsmodels lowess for the GAM | EASY | Medium | Best deck-level fit with Rougier *Ornaments* |
| 7 Color | mpl colormap registry, `sns.color_palette`/`palplot` (Brewer built in), palettable, daltonlens CVD sim, geopandas map | EASY | Medium | mpl/seaborn is *more* natural than R here |
| 8 Distributions | seaborn histplot/kdeplot/ecdfplot (best-in-class), scipy/statsmodels qq, ridgeline via official seaborn FacetGrid gallery example | EASY | Medium | Bin center/boundary → one line of numpy edges |
| 9 Models/uncertainty | statsmodels `smf.ols/glm` → coefficient plots via seaborn pointplot/`errorbar` from `conf_int()`; predictions via `get_prediction().summary_frame()` → `lineplot` + `fill_between` CI bands; marginaleffects-py for the lift/elasticity concepts (its plots are plotnine — either accept that for 3 figures or hand-plot its DataFrames with seaborn) | MODERATE | **Large** | The compute-then-plot idiom is arguably better teaching than `plot_predictions` magic |
| 10 PCA | sklearn PCA, seaborn pairplot/heatmap, mpl `quiver`/annotate loadings arrows, plotly.py or mpl3d for 3D | EASY | Medium | |
| 11 k-means | sklearn KMeans (`inertia_` elbow, `inverse_transform` centers), mpl Ellipse cluster marks, catplot center bars | EASY | Medium | |
| 12 Hierarchical | scipy `dendrogram` (mpl-native), seaborn **clustermap** (≈ tidyheatmaps feature-for-feature), `gower` pkg, geopandas | MODERATE | Medium | Was already mpl/seaborn-based in the original assessment |
| 13 Shiny | Shiny for Python in Quarto (`server: shiny`, `{python}` cells, `#| context: server`); `@render.plot` yields mpl figures — seaborn drops straight in | MODERATE | Medium | |
| 14 Shiny layouts | shiny-python `ui.*` + shinyswatch themes; no `thematic` port — mpl style sheets instead | MODERATE | Small | |

**Bottom line (mpl/seaborn-first):** feasibility is unchanged — nothing is HARD, and several decks
(6, 7, 8, 12, 13-14) are actually *more* at home in mpl/seaborn than in plotnine; geospatial and
clustering were already headed there (geopandas and scipy plot *through* matplotlib). The costs
move to decks 3 and 4, where manual faceting/legends add volume, and deck 9, where you trade
marginaleffects' one-line plots for an explicit predict-then-plot idiom (a defensible pedagogical
upgrade). **Revised total: ≈ 4-5 focused weeks** for idiomatic, teaching-quality mpl/seaborn
versions of all 14 decks (vs 3-4 for plotnine transliteration). A high-value first tranche —
decks 7, 8, 11, 12, where mpl/seaborn is most natural and python-first students currently have the
least support — is roughly one week, and Rougier can be adopted as the assigned Python text
immediately regardless.

---

## 6. Incidental findings (fix whenever, independent of the source swap)

1. **Pirated SWD PDF** linked at `meetup-1.qmd:120,139` — remove regardless of other decisions.
2. `modules/readings/donahue-visualization.pdf` is **orphaned** (no page links it; textbooks.qmd uses
   an external URL instead) — delete or link it.
3. `modules/readings/choosing_colors.pdf` (module 7) — inherited, provenance unclear, redundant with
   Wilke 4/19 + Okabe-Ito + the Muth series; candidate for removal in the swap.
4. Story 1's scenario is dated (IIJA allocations as of March 2023, "political interests of the Biden
   administration") — consider refreshing the data/framing while the assignment is being re-sourced.
5. History-of-dataviz PDFs in module 1 are inherited but optional/harmless (the Friendly paper is legitimate).
6. Absolute local paths in decks 7/8/9 (`nyc_airbnb_listings.csv`, `train.csv`, `neighbourhoods.geojson`
   under `~/work/Teaching/DATA608/DataStory4|5/`) — will break rendering on any other machine;
   repoint at `website/assignments/stories/data/` when decks are next touched.

## 7. Suggested sequencing (when you decide to act)

1. **Trivial pass (an hour):** delete the SWD readings lines in modules 2/3/6/7 + meetups 2/6/7,
   swap in the §3.3–3.5 replacements; remove pirated links; update textbooks/syllabus/overview prose.
2. **The real work (a focused day or two):** rebuild meetup 1's ~16 slides around Healy Ch 1 +
   Wilke Ch 29 + Heiss s1/s15/s2 material, and reword Story 1's deliverable framing to match.
3. **Optional cosmetics:** retitle module/meetup 3; refresh Story 1's dataset.
4. **Python track:** start with the §5 first tranche if demand warrants; adopt Rougier as assigned
   reading only for weeks 2, 3, 4, 6, 7.

*Full agent reports (verbatim inventories, per-slide line numbers, per-deck code notes) are preserved at:*
`planning/` (alongside this file)
*(dependencies.md, resources.md, python-parallel.md).*

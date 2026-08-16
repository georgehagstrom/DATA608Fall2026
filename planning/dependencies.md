# DATA 608 Dependency Audit: Knaflic "Storytelling with Data" (SWD) and "Data Practitioner's Guide" (DPG)

All paths relative to `/home/georgehagstrom/work/Teaching/2026_Fall/DATA608Fall2026/website/` unless absolute. "SWD" = Knaflic, *Storytelling with Data*. "DPG" = `modules/readings/data-practitioners-guide.pdf` (38-slide inherited deck).

## Summary table

| Location | Source | What depends on it | Centrality |
|---|---|---|---|
| `assignments/stories/story1.qmd:14` | SWD Ch 1 | Required deliverable format: storyboard / 3-minute story / big idea, cited to "Chapter 1 of *Storytelling with Data*" | **High** |
| `meetups/meetup-1/meetup-1.qmd:236-316` | SWD Ch 1 | ~11 slides: Who/What/How audience framing, Elevator Pitch/3-minute story, Big Idea, Storyboard — the core week-1 framework | **High** |
| `meetups/meetup-1/meetup-1.qmd:63-74` | SWD (intro/Ch 1 example) | Opening case study: ticket-backlog before/after charts; image captioned "Storytelling 0.3" — this is Knaflic's signature figure | **High** |
| `meetups/meetup-1/meetup-1.qmd:277` | SWD | `mechanism_fig.png` captioned "Storytelling" (written vs live presentation mechanism spectrum, SWD Ch 1) | Med |
| `meetups/meetup-1/meetup-1.qmd:383-404` | DPG slide 8 | 3 slides listing the seven "Visualization Quality Features" (Fidelity, Simplicity, Utility, Saliency, Efficacy, Uniformity, Amity) verbatim from DPG | **High** |
| `meetups/meetup-1/meetup-1.qmd:112-147,159-176` | SWD + DPG | Textbook slides (SWD listed as one of "two most important textbooks", cover image `storytelling.png`), week-plan readings and key-concepts slides naming both sources | **High** |
| `modules/module1.qmd:15,21,23` | SWD Ch 1 + DPG 1-11 | Learning objective ("data practitioner's role as a storyteller" = DPG framing) and two of three required readings | **High** |
| `modules/module2.qmd:16,19` | SWD Ch 2 + DPG 8-11 | Readings items 2 and 5 | Med |
| `modules/module3.qmd:2,15,17,24` | DPG (title + slides 8, 12-20) + SWD Ch 3 | Module title "Data Visualization Quality Features" is DPG-derived; readings items 1 and 3 | Med |
| `meetups/meetup-3/meetup-3.qmd:2` | DPG (title only) | Deck titled "Visualization Quality Features"; actual content is Tufte/Wilke, not DPG | Low |
| `meetups/meetup-2/meetup-2.qmd:24-30,38` | SWD Ch 2 | One "Pie Charts are Evil" slide attributed to SWD Ch 2 (image `PieChartsEvil.png`), plus readings slide | Med |
| `modules/module6.qmd:15` | SWD Ch 7 | Readings item 1 only; meetup-6 content is Wilke Ch 29 | Low |
| `meetups/meetup-6/meetup-6.qmd:10` | SWD Ch 7 | One line in the week-summary readings list; no SWD-derived slides | Low |
| `modules/module7.qmd:15` | SWD Ch 4 | Readings item 1 only; meetup-7 content is Wilke Ch 4/19 + R color packages | Low |
| `meetups/meetup-7/meetup-7.qmd:11` | SWD Ch 4 | One line in weekly-summary readings list; no SWD-derived slides | Low |
| `course/syllabus.qmd:17,64` | SWD | Course-description phrase "the art of 'Storytelling with Data'"; required-textbook listing | Med |
| `course/textbooks.qmd:13-15` | SWD | Required text #2 with blurb ("eliminating clutter, focusing attention, building a narrative") | Med |
| `course/overview.qmd:7-9` | SWD + DPG | Same inherited prose: "art of 'Storytelling with Data'", "as a data practitioner", "quality features" | Med |
| `course/schedule.qmd:16,19` | DPG / SWD | Module titles "Visualization Quality Features" (9/14) and "Storytelling" (10/5) — titles only | Low |
| `modules/module4.qmd:11` | Inherited master-course prose (DPG-adjacent) | "Know Your Audience and The Context of the Requested Story" mantra paragraph | Low |
| `meetups/meetup-14/meetup-14.qmd:24` | Generic phrase | "Storytelling with data has focused on a controlled narrative" — refers to course theme, not the book | Low |
| `course/syllabus.qmd:21,26`, `modules/module1.qmd:15` | DPG framing | "you as a data practitioner" / "data story process" language inherited from the master course | Low |

Not dependencies (verified clean): `modules/module14.qmd:14` and `meetups/meetup-14/meetup-14.qmd:16` reference the research paper "Exploration and Explanation in Data-Driven Storytelling" (unrelated to Knaflic). Stories 2-7 (`assignments/stories/story2..7.qmd`) contain no SWD/DPG references (grep-verified). Meetups 4, 5, 8-15 contain none.

## Detailed findings per file

### assignments/stories/story1.qmd — HIGH
- Line 14: "To frame your data story, use the storyboard/3-minute story/big idea framework from Chapter 1 of *Storytelling with Data*. Submit your storyboard ... a one-paragraph 3-minute story, and a one sentence big-idea summary..."
- This is the only assignment that cites SWD by name, and the citation is load-bearing: three graded deliverables are defined by SWD Ch 1 terminology. (The IIJA assignment scenario itself is also inherited from the previous instructor's master course.)

### meetups/meetup-1/meetup-1.qmd — HIGH (largest conceptual dependency in the course)
Roughly 16-17 of ~45 slides depend on the two removal targets:

**SWD-derived (explicit + conceptual):**
- Lines 63-74: opening case study ("Your firm had two employees leave in May... backlog") using `TicketTrendsBad.png` / `TicketTrendsGood.png`; line 74 captions the improved chart "Storytelling 0.3" — this is Knaflic's ticket-trend example (her Figure 0.3 / the "please approve the hire" chart, also reproduced in DPG Technique 2). Two slides, and it is the framing hook for the whole course intro.
- Lines 112-147: two Textbook slides listing SWD as one of the "Two most important textbooks", with a GitHub link to a pirated PDF of the book (lines 120, 139) and the cover image `storytelling.png` (line 144).
- Lines 159-176: Week Plan slides — readings "Chapter 1 of Storytelling" (161), "First 11 slides of Data Practitioner's Guide" (163); key concepts "Methods for creating a story (Storytelling)" (175) and "What makes a quality figure (Wilke, Practioner's Guide)" (176).
- Lines 236-288: six "Context: Who, What, and How" slides. The who/what/how audience-framing triad is SWD Ch 1's structure (audience → action → mechanism/data). Line 277 embeds `mechanism_fig.png` captioned "Storytelling" (image taken from the book).
- Lines 290-303: "The Elevator Pitch and Big Idea" + "Big Idea: Single Sentence Summary" — SWD Ch 1's 3-minute story and Big Idea concepts (2 slides).
- Lines 306-316: "The Storyboard" (2 slides, incl. `storyboard.png`) — SWD Ch 1.
- Note: these slides feed directly into Story 1's required deliverables, so meetup-1 and story1 must be changed together.

**DPG-derived:**
- Lines 383-404: three "Visualization Quality Features" slides reproducing DPG slide 8's seven features (Fidelity, Simplicity, Utility, Saliency, Efficacy, Uniformity, Amity) with near-verbatim definitions.

**Not dependent:** bad-chart gallery (31-60), purposes of visualization slides (178-234, exploratory/explanatory/inferential — Wilke-compatible), neuroscience-of-stories slides (318-333, cites neural synchrony research, independent), good/ugly/bad/wrong penguins slide (335-379, Wilke Ch 1 taxonomy).

### meetups/meetup-3/meetup-3.qmd — LOW dependence despite the module name
- Line 2: title "Meetup 3: Visualization Quality Features" — the phrase comes from DPG slide 8, but nothing in the deck uses the DPG's seven features.
- Actual content is Tufte-derived and Wilke-covered: Principle of Uniformity of Graphics / Lie Factor (39-47, matches DPG slide 14 wording but is standard Tufte), Proportional Ink with direct Tufte quote (51-55; Wilke Ch 17 covers this), bars/filled plots start at 0 (72-224), scale area not radius (227-264), Graphical Excellence / data-ink ratio with Tufte quote (266-274), chartjunk example (276-334), theme_tufte and "too minimal" critique (495-543, cites Inbar 2007), data-ink "within reason" Titanic example from Wilke (546-654), gridline and font-size advice (657-883).
- Dependency is essentially just the deck/module title and module3's readings list; the slides themselves survive removal of both sources intact.

### meetups/meetup-6/meetup-6.qmd — LOW
- Line 10: "Read: Chapter 29 of Fundamentals, Chapter 7 of Storytelling" — only SWD mention.
- All conceptual content is Wilke Ch 29, not Knaflic Ch 7: the story definition quote (line 18) is Wilke's; the three story arcs — Opening-Challenge-Action-Resolution (119-124), Lead-Development-Resolution (126-142), Action-Background-Development-Climax-Ending (145-160) — are Wilke Ch 29's arcs; the kidney-cancer example is Gelman & Hill; the NYC flights "too complex / build up to complexity" figures (348-511) are reproduced from Wilke Ch 29.
- Removing SWD costs one line here.

### meetups/meetup-7/meetup-7.qmd — LOW
- Line 11: "Chapter 4 of Storytelling" in the weekly summary readings list — the only mention.
- No SWD Ch 4 content (no preattentive-attributes or "focus attention" slides). The deck is color vision, Okabe-Ito, colorblindness simulation, and R color-scale packages — i.e., Wilke Ch 4/19 plus original practical material.

### meetups/meetup-2/meetup-2.qmd — MED (small but explicit)
- Lines 24-27: slide "Why Are Pie-Charts Terrible?" with bullet `"Pie Charts are Evil" - Chapter 2 Storytelling with Data` and image `PieChartsEvil.png` (likely scanned from the book). One more slide reuses the image (lines 29-33).
- Line 38: readings list 'Chapter 2 of "Storytelling"'.
- Rest of deck is Cleveland graphical-perception material (keep).

### modules/module1.qmd — HIGH
- Line 15: learning objective "Understand a data practitioner's role as a storyteller" — DPG slides 3-6 framing.
- Line 21: reading "__Storytelling with Data__: Chapter 1".
- Line 23: reading "[A Data Practitioner's Guide...]: Slides 1-11 (everything up to Tufte's Principles)".
- Two of the module's three required readings are removal targets; only Wilke Ch 1-2 (line 22) remains.

### modules/module2.qmd — MED
- Line 16: reading 2 "__Storytelling with Data__ - Chapter 2. This is a very good practical guide to the most common types of charts... as well as a list of charts to avoid."
- Line 19: reading 5 "[A Data Practitioner's Guide] - Slides 8-11" (quality features + dataviz catalogue/tools slides; the catalogue itself is independently listed as reading 4, so DPG slides 9-11 are redundant with it).

### modules/module3.qmd — MED
- Line 2: module title "Data Visualization Quality Features" (DPG-derived name, propagated to `course/schedule.qmd:16` and meetup-3 title).
- Line 15: reading 1 "[A Data Practitioner's Guide] - Slides 8, 12-20".
- Line 17: reading 3 "__Storytelling with Data__ - Chapter 3" (declutter chapter; role: reinforcement alongside Wilke 17-26, which line 16 already assigns).

### modules/module6.qmd — LOW
- Line 15: reading "__Storytelling with Data__ - Chapter 7: Lessons in Storytelling"; paired with Wilke Ch 29 (line 16) which the meetup actually follows.

### modules/module7.qmd — LOW
- Line 15: reading "__Storytelling with Data__ - Chapter 4"; paired with Wilke Ch 4/19, Okabe-Ito, and choosing_colors.pdf, which cover the meetup content.

### course/*.qmd — MED (prose + listings)
- `course/syllabus.qmd:17`: "You will learn the skills, techniques and the art of 'Storytelling with Data'" — inherited marketing prose naming the book. Lines 21, 26: "as a data practitioner ... data story process" (DPG framing). Line 64: required-text listing "2. Cole Nussbaumer Knaflic. *Storytelling with Data*".
- `course/textbooks.qmd:13-15`: SWD listed as Required text #2 with description. (Healy and Wilke, the keepers, are at lines 8-11 and 19-21.)
- `course/overview.qmd:7-9`: same inherited sentence as syllabus ("art of 'Storytelling with Data'", "quality features").
- `course/schedule.qmd:16`: 9/14 row "Visualization Quality Features"; line 19: 10/5 row "Storytelling" — module titles only.
- `modules/module4.qmd:11`: inherited paragraph ending in the mantra **"Know Your Audience and The Context of the Requested Story"** — master-course prose in the DPG's voice, though the advice itself is generic.

## Practitioner's Guide content summary (38 slides; assigned: 1-11 in Module 1, 8-11 in Module 2, 8 & 12-20 in Module 3)

**Slides 1-7 (Module 1): "why data stories" + role model.** Title; "The Need for Data Stories" (Gartner quote, Jewish folktale about Truth and Parable via Brent Dykes' *Effective Data Storytelling*); "The Need for a Data Practitioner to be a Storyteller" (MIT Sloan post, James Cook Univ. blog); a "Data Visualization Model" ontology diagram built in Protégé defining Practitioner-as-Storyteller; "The Audience"; "The Storyteller" (identify data, select tools, delivery modality, communicate); "The Data Visualization" (must be faithful — omit nothing, add nothing). Motivational/definitional content, quote-heavy, with typos throughout ("msut", "isnt", "requiered").

**Slide 8 (Modules 1, 2, 3): the seven Quality Features.** Fidelity, Simplicity, Utility, Saliency, Efficacy, Uniformity, Amity — the deck's original taxonomy (not from any published framework). This is the slide that meetup-1 lines 383-404 reproduce and that names Module 3 / Meetup 3.

**Slides 9-11 (Modules 1, 2): tools inventory.** The Data Visualization Catalogue (60 chart types), counts of tools (60 code libraries / 47 web apps / 14 desktop apps), and a claimed shortlist of "eight comprehensive applications and libraries". Redundant with the Catalogue link already assigned directly in module2.qmd:18.

**Slides 12-17 (Module 3): Tufte's Principles.** Section title (12); Graphical Excellence (13); Uniformity of Graphics / Lie Factor / labeling / "show data variation not design variation" (14); Data Variation and Context Preservation (deflated units, avoid areas for 1-D data) (15); Graphical Design (data-ink ratio, erase non-data-ink, chartjunk, data density) (16); Graphic Design Aesthetics (17). Straight summaries of Tufte's *Visual Display of Quantitative Information*; substantially covered by Wilke Ch 17 (proportional ink), Ch 24, and meetup-3's own slides.

**Slides 18-20 (Module 3): Cavaller's Principles.** Cavaller (2021, Front. Res. Metr. Anal.) communication-theory framework: six practical questions (19) and six "principles of interest" for evaluating visualizations (20). Long block quotes from a single obscure paper; nothing else in the course references Cavaller.

**Slides 21-38 (NOT assigned in any module, for context):** "10 Improvement Techniques" — preconscious/preattentive vision (slide 22 cites "Nusbaumer Knaflic ... pg. 105"), KISS/chartjunk, "visual kicker" (reproduces SWD's p.4 ticket chart — the same figure as meetup-1's case study), go-with-the-flow, Gestalt principles (proximity, similarity, enclosure, closure, continuity — several examples credited to Knaflic pp. 74-76), saliency; accessibility (cites Okabe-Ito and Wilke Ch 4/19 — both already assigned directly); Zhang et al. 2022 "contrarian" pictorial-enhancement approach; story development process diagram. Note: the DPG itself leans on Knaflic for its techniques section, so it does not work as a Knaflic replacement.

## Other inherited master-course material (informational, not slated for removal)

- `modules/readings/friendly-history-of-data-visualization.pdf` and `history-of-data-visualization-presentation.pdf` — module1.qmd:27-28 (optional) and meetup-1.qmd:164 ("For fun: Two sets of History of Dataviz slides"). The Friendly paper is a legitimate reference; the "presentation" PDF is likely another inherited deck. Both optional/low-stakes.
- `modules/readings/donahue-visualization.pdf` — orphaned: no .qmd links to it (textbooks.qmd:29-31 links Donahue via an external Vanderbilt URL instead). Dead weight in the repo.
- `modules/readings/choosing_colors.pdf` — module7.qmd:18; provenance unverified, likely inherited; redundant with Wilke Ch 4/19 + Okabe-Ito which are assigned alongside it.
- Story assignment scenarios (e.g., Story 1's IIJA equity/"political interests of the Biden administration" questions, `assignments/stories/story1.qmd:9-12`) are inherited master-course assignments; dated (March 2023 data, Biden administration framing).
- Inherited prose voice: `course/syllabus.qmd:17-26`, `course/overview.qmd:7-9`, `modules/module4.qmd:11` all carry the previous instructor's "data practitioner / story request / quality features" phrasing.
- `meetup-1.qmd:120,139`: the SWD link points to an unauthorized full-book PDF on a third-party GitHub repo — worth removing regardless of the source-removal decision.

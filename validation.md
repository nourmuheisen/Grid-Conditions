# Validation record — version 2

Checked 15 October 2026.

- 12 unique cases, 75 unique claim IDs, 41 unique source IDs. Every claim references an existing source and has a confidence explanation, limitation and access date. Two sources are explicitly discovery-only alternatives.
- Eight provinces and six operators counted from the canonical case data. Counts describe this sample only. No total MW, national market share, feasibility ranking or economic outcome is calculated.
- All cases have the five comparison dimensions. Missing numeric capacity remains null. NorthC figures are installed electrical specifications; AMS11's reported IT capacity stays a separate secondary claim.
- Reviewed factual statements retain sources. Analyst hypotheses and scenario conditions are separate. Publication dates, report dates, undated pages and access dates are distinguished.
- HTML embeds the canonical JSON exactly. Linked documents exist in `dist`. There are no external scripts, fonts, API calls or telemetry.
- Node DOM-stub runtime tests passed for every case/layer/scenario combination, province and investigation-theme filters, search/empty states, the three-case comparison limit, comparison empty state, session note retention and escaping, export handlers, evidence/scenario tabs, and source search.
- Responsive CSS provides a compact single-column mobile workspace, scrollable comparison and sources, labelled controls and visible keyboard focus. Tab arrow-key handling is implemented.
- **Rendered desktop/mobile browser QA remains unavailable.** No visual screenshot check or real-browser download test was performed. Before publication, test approximately 390 px and 1440 px layouts, keyboard navigation, narrow comparison tables, source-anchor scrolling and exports.
- No publication, GitHub push, email or stakeholder contact occurred.

Reproduce data/build checks with `python3 scripts/build.py`; optional runtime checks use `node scripts/check.mjs`.

GitHub package: root index.html and relative document links; no build or dependencies required for initial hosting. Rebuild and runtime checks repeated for this layout. No remote deployment performed.

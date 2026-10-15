# Grid-positive screening — independent portfolio prototype

Version 2 uses a navy/orange electrical-schematic theme, a searchable case directory, province and investigation-theme filters, and a maximum-three-case comparison. Theme labels are analytical lenses, not scores.

This package explores 12 publicly documented cases across eight Dutch provinces. It is independent work for a personal portfolio, not commissioned or endorsed by BCG, the operators or DAMEN. Research cutoff and access date: **15 October 2026**.

## Open or host the prototype

Open **index.html** in a modern browser. No installation, account, external fonts, API or build service is required. Keep all files together for research links to work. JavaScript must be enabled; external source links need internet access.

For GitHub, upload the extracted contents of this package so `index.html` is at the repository root. See [GITHUB_SETUP.md](GITHUB_SETUP.md) for step-by-step instructions. The website is already built.

You can search and filter the national directory, compare up to three selected cases, inspect each claim, filter evidence types, choose three conditional scenarios, enter working assumptions and export those notes or the evidence JSON. Notes exist only in the current page session and are lost on reload unless exported. No information is transmitted by the application; clicking an external source opens that publisher's site.

## Files

- `research-brief.md`: question, feasibility gate, findings and limits.
- `source-register.csv` / `.md`: URLs, publisher, source type, dates, supported claims and retrieval checks.
- `evidence.json`: canonical structured case, claim, source, assumption and gap data.
- `evidence-table.csv`: one row per claim, with joined source URLs and publication dates.
- `cases.csv`: location-level metadata, source identifiers and investigation questions.
- `assumptions-and-gaps.md` / `data-gaps.csv`: assumptions, discrepancies and missing inputs.
- `src/template.html`: editable interface template, including interaction code and styles.
- `scripts/build.py`: standard-library-only builder for HTML and derived exports.
- `index.html`: ready-to-host website.
- `favicon.svg`: circuit-inspired site icon.
- `.nojekyll`: bypasses Jekyll processing for the static site.
- `scripts/check.mjs`: optional interaction and integrity checks.
- `GITHUB_SETUP.md`: repository upload and Pages instructions.
- `selection-register.csv`: included cases and two considered but unselected alternatives.
- `validation.md`: checks completed and verification limitations.

## How the analysis works

Claims reference source IDs, not inferred citations. Five dimensions drive the comparison: grid evidence, flexibility, on-site options, water/local context and delivery. Capacity is additional metadata. Classifications separate source statements, regional context, country/operator precedent, secondary reporting, discrepancies and unknowns. Case hypotheses and next steps are analyst judgements, not source facts. The comparison is not scored or ranked.

“High” confidence means direct, identifiable source support for that particular statement; “Medium” marks an owner design claim, historical specification, secondary account or cross-source inference; “Not established” means the reviewed material cannot answer the question. These labels do not indicate technical feasibility.

Dates retain their actual precision. A page access date is not a publication date. `latest_dated_site_source` is the latest dated site-related source included here, not a claim to have located every publication. Regional sources never overwrite site status. NorthC Groningen's 2.7 MW is combined installed electrical capacity, not measured IT demand or available capacity.

No calculation engine, simulated savings, connection guarantee, emissions result or numerical default is included. Scenario requirements are qualitative because the essential site inputs are missing. User notes remain assumptions and never update the evidence table.

## Rebuild or extend

From this folder run `python3 scripts/build.py`. It reads `evidence.json` and `src/template.html`, checks unique IDs and references, and regenerates exports and root `index.html`. No third-party dependencies are needed. Edit canonical data first; do not edit only the generated HTML. Add a real source before adding a factual claim. Preserve contradictory dated claims and explain their relationship.

This is a geographically broader exploratory sample, not a complete national universe. Eight provinces and six operators are represented; omitted provinces are not assumed to lack data centres. The units vary from individual facilities to campus aggregates, and capacity values are not summed. To expand further, define a complete discovery universe first. Do not add projects simply to fill the screen. A useful next research pass would obtain official site-specific connection and permit documents, confirm the Google Westpoort/TenneT match, and refresh Eemshaven cable status. Do not merge Google and NorthC because both are associated with Westpoort.

## Publication and reuse

Nothing has been published or pushed. See [GITHUB_SETUP.md](GITHUB_SETUP.md) when you decide to publish. Review source freshness and the independent-project statement first. No license has been chosen for your original code or writing; decide how you want others to reuse it before adding a license. Source publishers retain rights in their own material.

Before publishing, test desktop and mobile layouts and all controls in your chosen browser. Run `node scripts/check.mjs` if Node.js is available. Runtime and data-integrity checks passed here; rendered browser QA was unavailable. See `validation.md` for exact coverage.

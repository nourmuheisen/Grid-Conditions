"""Build the static evidence screen and transparent exports. Python standard library only."""
from pathlib import Path
import json,csv
ROOT=Path(__file__).resolve().parent.parent
D=json.loads((ROOT/'evidence.json').read_text())
S={s['id']:s for s in D['sources']}
assert len(S)==len(D['sources'])
assert len({c['id'] for c in D['claims']})==len(D['claims'])
assert len({c['id'] for c in D['cases']})==len(D['cases'])
for c in D['claims']:
    assert c['source_ids'] and all(s in S for s in c['source_ids']),c['id']
    assert c['case_id'] in {x['id'] for x in D['cases']}|{'all'}
    assert c['confidence'] and c['limitation']
for case in D['cases']:
    for dim in ['Delivery','Grid evidence','Flexibility potential','On-site options','Water and local context']:
        assert any(c['case_id']==case['id'] and c['dimension']==dim for c in D['claims']),(case['id'],dim)
def csvout(name,rows):
    with (ROOT/name).open('w',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader()
        for row in rows:w.writerow({k:('; '.join(map(str,v)) if isinstance(v,list) else v) for k,v in row.items()})
claim_rows=[]
for c in D['claims']:
    r=dict(c)
    r['source_urls']=[S[s]['url'] for s in c['source_ids']]
    r['source_publication_dates']=[s+': '+(S[s]['publication_date'] or 'Undated') for s in c['source_ids']]
    claim_rows.append(r)
csvout('evidence-table.csv',claim_rows)
csvout('cases.csv',D['cases'])
csvout('data-gaps.csv',D['gaps'])
source_rows=[dict(s,claim_ids=[c['id'] for c in D['claims'] if s['id'] in c['source_ids']]) for s in D['sources']]
csvout('source-register.csv',source_rows)
md=['# Source register','',f"Accessed {D['as_of']}. Links successfully retrieved on that date; future availability is not guaranteed. Source statements are paraphrased, not archived full texts.",'']
for s in source_rows:
    md.extend([f"## {s['id']} — {s['publisher']}",f"[{s['title']}]({s['url']})",'',f"- Type: {s['type']}",f"- Publication / checked date: {s['publication_date'] or 'Undated'} ({s['date_note']})",f"- Accessed: {s['access_date']}",f"- Supports: {s['supports']}",f"- Claim IDs: {', '.join(s['claim_ids']) or 'Scope / methodology context'}",f"- Link check: {s['link_check']}",''])
md.extend(['## Retrieval limits and excluded leads','','- A Planviewer 220 kV planning-document link returned HTTP 403; no bypass was attempted and its search extract is not used as a substantive source. Secondary cable reporting is explicitly labelled S21/S22.','- A Het Hogeland municipal area-history PDF exceeded the retrieval size limit. Its indexed extract was not used to claim a cadastral match.','- The original Groningen Seaports press-release link cited by S22 returned HTTP 404. S22 remains explicitly secondary, not upgraded to a primary source.','- DDA was used to assess available discovery coverage, not scraped or treated as an exhaustive universe.','- BCG context is based on the public article, not a reconstruction of its model.','- No numeric current grid-map layer or connection queue was extracted. Regional announcements retain their original dates.',''])
(ROOT/'source-register.md').write_text('\n'.join(md),encoding='utf-8')
md=['# Assumptions and data-gap log','',f"Snapshot: {D['as_of']}",'','## Assumptions and analytical boundaries','']
for a in D['assumptions']:md.append(f"- **{a['id']}** — {a['text']}")
md.extend(['','## Open gaps',''])
for g in D['gaps']:md.extend([f"### {g['id']} — {g['cases']}: {g['topic']}",f"Missing: {g['missing']}",f"Verify with: {g['verify_with']}",f"Decision impact: {g['decision_impact']}",f"Status: {g['status']}",''])
md.extend(['## Conflicts and non-equivalent evidence','', '- W06: preserve 2023 / 2024 Winschoten construction milestones (S04–S06).','- E08: retain both 2024 expected cable delivery windows (S21/S22); completion unverified.','- E04: unnamed 380 kV proposal is not assigned to Google (S15); do not merge with 220 kV reporting.','- P02: Google Westpoort to Vierverlaten is a cross-source project match, requiring confirmation (S19/S20).','- Eemshaven municipality is a locality inference, not a cadastral verification (S04/S15).','- N03: current hydrogen technology listing and historical planned 500 kW rating are not equivalent to a current dispatchable capacity.','- Export headroom (S13) and consumption constraints (S11/S12) concern different directions and potentially different network levels.','- D01: AMS11 owner page and industry report describe different opening times / phases (S25/S26); do not silently select a status.','- H04: Bolderhoek revised findings give a later local reinforcement expectation than earlier text on the same page (S39). No PDC2 attribution.','- National sample: regional statements S35–S39 are not facility contracts; Zestienhoven is not assigned Rotterdam-port congestion.','- Solar or air cooling does not establish demand flexibility. Neither an announcement nor an activity notification confirms commissioning or routine-operation permission.',''])
(ROOT/'assumptions-and-gaps.md').write_text('\n'.join(md),encoding='utf-8')
dist=ROOT
template=(ROOT/'src/template.html').read_text()
assert template.count('__DATA__')==1
(dist/'index.html').write_text(template.replace('__DATA__',json.dumps(D,ensure_ascii=False).replace('</','<\\/')),encoding='utf-8')
print(f"Built {len(D['cases'])} cases, {len(D['claims'])} claims, {len(D['sources'])} sources; reference checks passed.")

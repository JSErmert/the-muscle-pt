# THE MUSCLE PT — RESEARCH INDEX

This index is the single source of truth that connects research records, system decisions, and content outputs. Every entry must follow the format defined in `systems/intelligence/research-index-and-traceability-v1.md`.

Forward query: problem → research.
Reverse query: research → system behavior.
Output query: output → research.

Validation rules:
- Each entry references at least one real source with verified PMID
- Each entry maps to at least one system behavior
- Each entry is usable in content generation
- Each entry is traceable to original research

Last updated: 2026-05-03 (**research-009 added — Varovic 2025, Bayesian meta-analysis 12 studies, Medium-High confidence; vertical record (mechanism layer) for Exercise-to-Script Lane biomechanics grounding; first formal execution of corrected Research Authoring Mode per refinement-004**; lane spec language softened — "this is exactly where stretch mediated hypertrophy lives" → "This is the lengthened position. The modest stretch-mediated hypertrophy effect concentrates here.")
Previous: 2026-05-01 (**research-008 added — Spanhove 2023, RCT n=21 hEDS/HSD shoulder instability, Medium confidence; horizontal modifier across other records; M2 closeout-triggered authoring**; M2 closeout document authored; research-005 added — García-Juez 2025, NMA, High confidence; research-002 confidence promoted Low-Medium → Medium-High; research-004 added; research-007 flagged planned; research-003 added; research-002 added; research-001 Fact-or-Fiction L3 corrected per incident-002; query-001 extended to v5; query-006 + query-008 logged; research-006 flagged planned)

---

## Active Records

### research-001 — Thoracic Spine Mobility, Chest Expansion, and Chronic Neck Pain

#### Topic

Relationship between thoracic spine mobility, chest expansion, respiratory mechanics, and chronic non-specific neck pain — and how sustained thoracic flexion vs. extension modulates the cervicothoracic junction.

#### Use Cases

- query-001 — Founder personal case (Josh): chronic right-dominant thoracic + cervicothoracic + posterior chain dysfunction with C-T junction injury history, two prior right shoulder blade dislocations, posterior chain inflammation cycles, and a reproducible provocation (bowl-shaped car seat) / relief (arm-behind-back retraction) pair

#### System Mappings

##### Case Engine Mapping

Cases presenting with chronic non-specific neck pain + restricted thoracic flexion + reduced chest expansion + sustained-flexion provocation + extension-retraction relief should be classified as a single co-dysfunction (cervical + thoracic + respiratory), not as separate problems. Reassessment markers: NDI, thoracic flexion ROM, chest expansion (cm differential).

##### Decision Mapping

Sequencing bias for cases fitting this mechanical signature:
1. Restore thoracic extension mobility before cervical loading
2. Restore chest expansion / respiratory mechanics before strength progression
3. Reposition scapulae (retraction capacity) before loading shoulder/upper-back chains

Sequencing claim, not universal protocol. Applies only to cases matching the Wirth pattern.

##### Rule Candidates

- RC-1. Chronic neck pain + restricted thoracic flexion → assess chest expansion before progressing cervical loading
- RC-2. Sustained seated forward-flexion provocation → screen for the Wirth pattern
- RC-3. Pain relief with thoracic extension + scapular retraction → bias intervention toward extension-restoration sequencing

Promotion path: ≥ 2 validated firings without contradiction → formal rule.

##### Constraint Candidates

- CC-1. Findings do not extend to specific cervical pathologies (radiculopathy, post-dislocation instability, herniation, post-surgical, pediatric)
- CC-2. Correlation ≠ causation — sequencing is bias, not protocol
- CC-3. Non-specific CNP only

#### Content Mappings

- Educational: "Chronic neck pain isn't always a neck problem" / "Why your neck pain might live in your ribs and breathing"
- Fact or Fiction: "Your neck pain has nothing to do with your breathing" (FICTION — Wirth's chest expansion ↔ MVV r = 0.42; Pemax/Pimax ↔ NDI r = -0.58 / -0.46 directly support the verdict). *Replaces prior entry per incident-002.*
- Mechanics Breakdown: Thoracic flexion ROM + chest expansion as upstream variables in chronic neck pain
- Self-Test: Provocation/relief pair as at-home screen

#### Source References

- PMID: 24835338
- Link: https://pubmed.ncbi.nlm.nih.gov/24835338/
- Title: The relation between thoracic spine mobility, chest expansion, respiratory function, and chronic non-specific neck pain
- Authors: Wirth B, Amstalden M, Perk M, Boutellier U, Humphreys BK
- Journal: Manual Therapy, 2014
- Verification: PubMed direct (not Google AI)

Exact figures (from abstract):
- Thoracic flexion mobility ↔ MVV: r = 0.45
- Chest expansion ↔ MVV: r = 0.42
- Pemax ↔ NDI: r = -0.58
- Pimax ↔ NDI: r = -0.46

#### Confidence Level

Medium-High (defer to High after full-text review and ≥ 1 supporting record)

#### File Locations

- Captured: `records/research/captured/research-001-thoracic-chest-mobility-chronic-neck-pain.md`
- Mapped: `records/research/mapped/research-001-thoracic-chest-mobility-chronic-neck-pain.md`
- Query: `records/research/queries/query-001-thoracic-chest-mobility-chronic-neck-pain.md`

#### Last Updated

2026-05-01 — Fact-or-Fiction content mapping corrected per incident-002

---

### research-002 — Cervicothoracic Neuroinflammation and Conservative Care

#### Topic

PET/CT-quantified neuroinflammation at the cervical nerve root and dorsal root ganglion, and its responsiveness to a 6-week conservative neural tissue management intervention in chronic cervical radiculopathy.

#### Use Cases

- query-002 — Founder personal case (Josh): the inflammation-driven nerve compression cascade layer (flare → C-T junction bump enlargement → nerve-like compression and pinching symptoms downstream → recovery with extension + scapular retraction + inflammation reduction). Distinct from disc-driven radiculopathy.

#### System Mappings

##### Case Engine Mapping

Cases presenting with **cyclical** (not constant) nerve-quality symptoms during inflammation flares, with palpable soft-tissue marker change (e.g., C-T junction bump enlargement), no red-flag features, and responsiveness to anti-inflammatory positioning + neural tissue mobilisation should be classified as the **inflammation-driven nerve compression cascade** — distinct from classical disc-driven cervical radiculopathy. Field-usable reassessment proxies for the gold-standard PET/CT VT measurement: palpable soft-tissue marker change, symptom-quality logging (nerve vs. mechanical), provocation/relief response, NDI (shared with research-001).

##### Decision Mapping

For chronic cervical radiculopathy without red flags:
1. Open a **6-week / 12-session conservative trial** (nerve and joint mobilisation) before escalating to imaging or specialist referral
2. Run research-001 sequencing in parallel when the postural-mechanical axis is also positive
3. Track symptom-quality logging alongside NDI
4. Hold escalation trigger active throughout — red-flag features supersede the conservative trial at any point

##### Rule Candidates

- RC-4. Chronic cervical pain + cyclical nerve-quality symptoms tied to inflammation flares (no red flags) → screen for inflammation-driven cascade; do not assume disc-driven by default
- RC-5. Inflammation-driven cascade identified without red flags → 6-week / 12-session conservative trial (nerve and joint mobilisation) before escalation
- RC-6. research-001 mechanical pattern AND research-002 inflammation cascade both present → run sequencing on both axes in parallel, not sequentially

Promotion path: ≥ 2 validated firings without contradiction → formal rule.

##### Constraint Candidates

- CC-4. N=1 case report — do not generalize the conservative trial framework to all chronic radiculopathy without confirming case fits the cascade pattern (research-005 planned)
- CC-5. Red-flag features (progressive motor weakness, severe progressive deficit, bowel/bladder dysfunction, severe pain unresponsive to positional modification, signs of myelopathy) supersede conservative trial → escalate immediately
- CC-6. Inflammation-driven cascade is mechanistically distinct from disc-driven radiculopathy — different sequencing, different prognosis
- CC-7. 6-week / 12-session is the empirical anchor, not a magic dose — earlier responders proceed; earlier plateau evaluates for escalation rather than continuing past planned window
- CC-8. Field-usable reassessment markers are clinical proxies for PET/CT VT — clinically reasonable, not equivalent in evidentiary weight

#### Content Mappings

- Educational: "Why your nerve pain isn't always your discs" / "Mechanical neck pain vs. nerve-driven neck pain — the treatment is different"
- Mechanics Breakdown: How inflammation drives nerve symptoms (and why it is now measurable, not just inferred)
- Fact or Fiction: "If you have nerve pain, you need an MRI / surgery" (fiction-leaning when red flags absent)
- Self-Test: Cyclical inflammation-driven vs. constant disc-driven — does it flare and recede in cycles, or stay constant regardless of position?
- Recovery Window Framework: "The 6-week / 12-session conservative trial — what it is, when it is appropriate, when it is not"

#### Source References

- PMID: 41620319
- Link: https://pubmed.ncbi.nlm.nih.gov/41620319/
- Title: Neuroinflammation in the nerve roots and dorsal root ganglion decreases following 6 weeks of neural tissue management: PET/CT imaging findings in a patient with painful cervical radiculopathy
- Authors: Lutke Schipholt IJ, Coppieters MW, Koop MA, Boellaard R, van de Giessen E, Vleggeert-Lankamp C, Depauw PR, van Berckel BNM, Lammerstma AA, Yaqub M, Scholten-Peeters GGM
- Journal: Musculoskeletal Science and Practice, 2026
- Verification: PubMed direct (not Google AI)

Exact figures (from abstract):
- Neuroinflammation at neuroforamen: VT 12.96 → 6.21 (≈ 52% reduction)
- Neuroinflammation at spinal cord: VT 6.43 → 5.38 (≈ 16% reduction)
- 12 sessions over 6 weeks; reductions maintained at 6-month follow-up
- Patient: 56yo male, 9-month history of left C7 painful radiculopathy

Supplementary context (not seed grounding — narrative reviews, no exact figures):
- PMID 33373515 — Kang et al. 2020, Asian Spine Journal (differential diagnosis)
- PMID 17204882 — Abbed & Coumans 2007, Neurosurgery (pathophysiology overview)

#### Confidence Level

**Medium-High** (updated 2026-05-01). Promoted from Low-Medium after research-005 (García-Juez 2025, NMA of 50 studies on articular + neural mobilization for cervical radicular pain) authored as supporting NMA-level evidence on the intervention class. Effect sizes from research-005: pain MD -3.23 (95% CI -4.33, -2.12) vs. control; disability SMD -1.57 (95% CI -2.53, -0.61) — large effect. **One of two promotion conditions met. Full High pending ≥ 1 dual-stream Phase 2 case demonstrating the cascade pattern with the conservative trial framework (clinical replication).** RC-5 promotion to formal rule is conditional on Phase 2 clinical replication.

#### File Locations

- Captured: `records/research/captured/research-002-cervicothoracic-neuroinflammation-conservative-care.md`
- Mapped: `records/research/mapped/research-002-cervicothoracic-neuroinflammation-conservative-care.md`
- Query: `records/research/queries/query-002-cervicothoracic-nerve-compression-inflammation-cascade.md`

#### Last Updated

2026-05-01 — confidence promoted Low-Medium → Medium-High after research-005 (NMA supporting evidence) authored

---

### research-003 — Central Sensitization and Exercise Interventions in Chronic Musculoskeletal Pain

#### Topic

Comparative effectiveness of exercise intervention types on central sensitization indices in chronic musculoskeletal pain — and the population-level evidence that combined-modality exercise programs produce very large reductions in central sensitization while single-modality stretching alone is insufficient.

#### Use Cases

- query-003 — Founder personal case (Josh): the regional/widespread inflammation-cycle layer (full posterior chain wrap during flares; burning sensation; multi-region simultaneous involvement; flare/quiescent cycling; symptoms resolve to baseline between flares). Distinct from mechanical-dominant cases (research-001) and from localized single-root neuroinflammation (research-002).

#### System Mappings

##### Case Engine Mapping

Cases presenting with **central sensitization features** — regional symptom spreading, burning quality during flares, flare/quiescent cycling, elevated CSI score (≥40 commonly used as clinically significant), multi-region simultaneous involvement, or disproportion between mechanical findings and symptom severity — should be classified as the **inflammation-cycle / sensitization-driven case category**, distinct from mechanical-dominant (research-001) and localized single-root (research-002) categories. Field-usable reassessment markers: CSI (primary); symptom-quality logging, region-of-involvement tracking, flare frequency (secondary). QST is reference standard but research-only in field practice.

##### Decision Mapping

For chronic MSK pain cases without red flags:
1. Screen for CS features first (CSI ≥40, regional spread, burning quality, flare cycling); the screen determines which sequencing applies
2. **CS-positive cases:** prescribe a combined-modality exercise program — combined stretching + strengthening (SMD -1.67) or combined stretching + strengthening + aerobic (SMD -1.61). Single-modality approaches are insufficient
3. **CS-negative cases:** research-001 mechanical sequencing applies cleanly
4. **Mixed cases:** combined-modality program addresses both axes; do not run mechanical sequencing in isolation when CS features are positive
5. Track CS indices alongside primary outcome measures throughout intervention; reclassify if features resolve

##### Rule Candidates

- RC-7. Chronic MSK pain + CS features → classify as inflammation-cycle / sensitization-driven; do not assume mechanical-dominant by default
- RC-8. Sensitization-driven case identified → prescribe combined-modality exercise program; single-modality approaches are insufficient at evidence level
- RC-9. research-001 mechanical pattern AND research-003 CS features both present → run combined-modality program incorporating mobility as a component, not standalone
- RC-10. All chronic MSK cases under conservative trial → track CS indices (CSI primary, symptom-quality logging secondary) alongside primary outcome measures

Promotion path: ≥ 2 validated firings without contradiction → formal rule.

##### Constraint Candidates

- CC-9. Ibrahim measures CS *indices* (CSI, QST) — validated proxies, not direct measurements of burning quality, regional spread, or flare frequency
- CC-10. Findings apply to chronic MSK pain only — acute, post-surgical, post-traumatic acute, and systemic inflammatory disease are out of scope; red flags supersede
- CC-11. Stretching as a component of combined programs is supported; only stretching-as-standalone is shown insufficient for CS reduction
- CC-12. Specific dosing (frequency, intensity, duration) not established at network meta-analysis level — draw from component RCTs and clinical judgment
- CC-13. SMD point estimates' clinical confidence depends on component-RCT methodological quality; treat large effects as "robust evidence of meaningful effect" not "exact magnitude prediction for any individual case"
- CC-14. CS-positive classification is not permanent — re-screen CSI at intervention milestones; reclassify if features resolve

#### Content Mappings

- Educational: "Why your chronic pain might be sensitization, not damage" / "Why combined exercise programs beat any single approach for chronic pain" / "Your nervous system's pain volume can be turned down — the science"
- Mechanics Breakdown: How central sensitization produces regional pain spreading and flare cycling (the dorsal horn explanation, simplified)
- Fact or Fiction: "Exercise can't help chronic pain when you're already too sensitized" → **FICTION** (Ibrahim 2025: SMD -0.81 overall; SMD -1.67 with combined stretching + strengthening — directly supports the verdict)
- Self-Test: Symptom-quality logging (burning vs. mechanical ratio); regional involvement tracking; CSI questionnaire as structured self-screen
- Recovery Window Framework: "Why a single 'fix' rarely works for chronic pain — the combined program logic"

#### Source References

- PMID: 39818121
- Link: https://pubmed.ncbi.nlm.nih.gov/39818121/
- Title: Comparative effectiveness of various exercise interventions on central sensitisation indices: A systematic review and network meta-analysis
- Authors: Ibrahim AAE, McWilliams DF, Smith SL, Chaplin WJ, Salimian M, Georgopoulos V, Kouraki A, Walsh DA
- Journal: Annals of Physical and Rehabilitation Medicine, 2025
- Verification: PubMed direct (not Google AI)

Exact figures (from abstract):
- Any exercise vs. baseline: SMD -0.81 (95% CI -0.93 to -0.70) — large effect
- Combined stretching + strengthening: SMD -1.67 (95% CrI -2.41 to -0.97) — very large effect
- Strengthening + stretching + aerobic: SMD -1.61 (95% CrI -2.74 to -0.56) — very large effect
- 89 RCTs in network meta-analysis (164 total RCTs; 249 eligible studies identified)
- Stretching alone was the only category not shown superior to non-exercise controls

Supplementary context (not seed grounding):
- PMID 38662515 — Chen et al. 2024, European Journal of Pain. Earlier meta-analysis on exercise effects on CS, limited exact figures in abstract
- PMID 36963161 — Verbrugghe et al. 2023, Brazilian Journal of Physical Therapy. Single RCT (n=51), high-intensity training for CS in chronic LBP, mean difference CSI 7.9 (95% CI 2.1, 12.7) at 6-month follow-up

#### Confidence Level

**High.** Network meta-analysis (highest evidence level for comparative effectiveness); 89 RCTs in network; tight confidence intervals on overall effect; combined-modality SMDs in large-effect territory; recent (2025); direct construct match between Ibrahim's CS indices and the case mechanism. Strongest evidence base of any record authored to date.

#### File Locations

- Captured: `records/research/captured/research-003-central-sensitization-exercise-interventions.md`
- Mapped: `records/research/mapped/research-003-central-sensitization-exercise-interventions.md`
- Query: `records/research/queries/query-003-chronic-inflammation-posterior-chain-compensation-cycles.md`

#### Last Updated

2026-05-01

---

### research-004 — Post-Dislocation Scapular Dyskinesis Rehabilitation

#### Topic

Conservative rehabilitation outcomes for chronic post-dislocation scapular dyskinesis — specifically in chronic type III acromioclavicular (AC) dislocation, with broader-population inference flagged for confirmation.

#### Use Cases

- query-004 — Founder personal case (Josh): the chronic post-dislocation instability + scapulothoracic dysfunction layer (two prior dislocations at the right shoulder blade region; suspected chronic scapular dyskinesis and compensatory splinting; symptoms wrap into rear deltoid + subscapular regions during query-001 flares). Anatomically distinct from research-001 (cervical/thoracic), research-002 (cervicothoracic nerve root), research-003 (regional CS), and research-006 (TMJ — same case, different joint).

#### System Mappings

##### Case Engine Mapping

Cases with dislocation history at shoulder/scapular region + chronic post-event state + current scapular dyskinesis features + no red flags should be classified as the **post-dislocation chronic scapular dysfunction case category**. Distinct from mechanical-dominant (research-001), single-root nerve (research-002), and regional CS (research-003) categories. Cases can fit multiple categories — cross-record sequencing addresses this. Field-usable reassessment markers: scapular dyskinesis observation (lateral scapular slide test, scapular dyskinesis test) + SSV self-report. Quantitative: SICK Scapula Rating Scale; Constant Score.

##### Decision Mapping

For chronic post-dislocation cases without red flags:
1. Open structured **12-week+ scapular-focused rehabilitation trial** (12 strengthening + stretching exercises per Carbone) before surgical referral
2. Reassess at 6 weeks, 6 months, 12 months
3. Track SSV + scapular dyskinesis observation as primary outcome markers
4. When research-003 CS features also present → run combined-modality program incorporating scapular work as a component
5. Hold escalation triggers active throughout — red flags supersede

##### Rule Candidates

- RC-11. Chronic post-dislocation case + scapular dyskinesis + no red flags → 12-week structured scapular-focused rehabilitation before surgical referral
- RC-12. Reassessment expectation at 12 months: ~78% scapular dyskinesis resolution; SSV/Constant Score toward 85 points; cases substantially below trajectory at 6-month checkpoint warrant escalation evaluation
- RC-13. High-frequency recurrent dislocation, severe daily-life impact, or imaging-confirmed major lesions (large Hill-Sachs, significant Bankart, posterior labral tear) → escalate; do not run extended conservative trial
- RC-14. research-004 post-dislocation case AND research-003 CS features both present → run combined-modality program incorporating scapular-focused work as a component, not standalone

Promotion path: ≥ 2 validated firings without contradiction → formal rule.

##### Constraint Candidates

- CC-15. Carbone's population is **type III AC dislocation specifically** — generalization to glenohumeral / scapulothoracic / other types is inference, not direct evidence (research-007 planned)
- CC-16. Level IV evidence + n=24 → Confidence Medium; treat 78.2% as "robust evidence of meaningful response" not "exact magnitude prediction"
- CC-17. Acute reducible dislocation requires immediate medical reduction — research-004 applies to chronic post-event states only
- CC-18. High-frequency recurrent dislocation likely warrants surgical evaluation, not extended conservative trial
- CC-19. Specific anatomical lesions (Bankart, large Hill-Sachs, posterior labral tear) may modify rehabilitation expectations downward
- CC-20. Specific exercise prescription details not provided in abstract — defer to full-text review for precise programming

#### Content Mappings

- Educational: "Post-dislocation rehabilitation works — what the evidence says" / "Why scapular function matters after a shoulder dislocation" / "The 12-week framework for chronic shoulder instability — what to expect"
- Mechanics Breakdown: Scapular dyskinesis mechanics post-dislocation (AC suspension vs. glenohumeral kinematics vs. scapulothoracic gliding)
- Fact or Fiction: "Once scapular dyskinesis becomes chronic, it can't be reversed" → **FICTION** (Carbone 2015: 78.2% resolution at 12 months in chronic type III AC dislocation with structured rehabilitation; AC-specific population disclosure required when caption-cited)
- Self-Test: Scapular dyskinesis observation; SSV self-rating
- Recovery Window Framework: "12 weeks of structured scapular rehabilitation — what the outcomes look like" (78% resolution expectation, 6/12 month checkpoints, 85-point functional target)

#### Source References

- PMID: 24458335
- Link: https://pubmed.ncbi.nlm.nih.gov/24458335/
- Title: Scapular dyskinesis and SICK syndrome in patients with a chronic type III acromioclavicular dislocation. Results of rehabilitation
- Authors: Carbone S, Postacchini R, Gumina S
- Journal: Knee Surgery, Sports Traumatology, Arthroscopy, 2015
- Verification: PubMed direct (not Google AI)

Exact figures (from abstract):
- Scapular dyskinesis resolved in 18/23 patients (78.2%) at 12 months
- Mean Constant Score and SSV: improved to 85 points at 12 months
- SICK Scapula Rating Scale: 7.5 points in 4 patients post-treatment
- SICK syndrome observed in 4/8 patients with scapular malposition post-treatment
- Sample: 24 enrolled, 23 analyzed; 14/24 had SICK syndrome at baseline
- Intervention: 12 strengthening + stretching exercises; 6-week, 6-month, 12-month follow-up
- Level of Evidence: IV

Supplementary context (not seed grounding — narrative, no exact figures):
- PMID 27665529 — McIntyre et al. 2016, Physical Therapy in Sport. Posterior glenohumeral instability conservative rehab systematic review (5 studies)
- PMID 15162108 — Gibson et al. 2004, Journal of Hand Therapy. Nonoperative shoulder instability rehab systematic review

#### Confidence Level

**Medium.** Level IV evidence, n=24, AC-specific population. Promotes to High when research-007 (broader-population supporting evidence) is authored AND ≥ 1 dual-stream Phase 2 case demonstrates the rehabilitation-responsiveness pattern with the 12-week framework.

#### File Locations

- Captured: `records/research/captured/research-004-post-dislocation-scapular-dyskinesis-rehabilitation.md`
- Mapped: `records/research/mapped/research-004-post-dislocation-scapular-dyskinesis-rehabilitation.md`
- Query: `records/research/queries/query-004-post-dislocation-scapulothoracic-instability.md`

#### Last Updated

2026-05-01

---

### research-005 — Conservative Articular and Neural Mobilization for Cervical Radicular Pain

#### Topic

Network-meta-analysis-level evidence for conservative articular + neural mobilization in cervical radicular pain. Functions primarily as **confidence-elevation evidence for research-002** — supplies population-level intervention-class effectiveness data that the N=1 mechanism evidence (Lutke Schipholt 2026) could not provide on its own.

#### Use Cases

- query-005 — Research-library structural requirement: research-002's confidence ceiling at Low-Medium (N=1 case report) blocked RC-5 promotion. Research-005 supplies the supporting NMA-level evidence to enable promotion path.

#### System Mappings

##### Case Engine Mapping (Reinforcement, Not New Category)

Research-005 does not introduce a new case category. It reinforces research-002's existing classification (the inflammation-driven nerve compression cascade). What changes: cases classified into this category can now be addressed with **higher confidence** because the intervention class has population-level supporting evidence. Field-usable expected outcome anchors derived from research-005: pain reduction ~MD 1.5–3.2 (vs. standard care or no treatment); disability reduction SMD 1.3–1.6 (large effect).

##### Decision Mapping

For chronic cervical radicular pain without red flags:
1. Classification per research-002 (cyclical nerve-quality symptoms during inflammation flares + soft-tissue marker change + no red flags) remains the screen
2. Conservative trial per research-002 framework (6-week / 12-session articular + neural mobilization) remains the intervention
3. **Expected outcome trajectory now anchored at population level:** large pain and disability reductions per García-Juez NMA — cases substantially below this trajectory at 6-week reassessment warrant escalation evaluation
4. RC-5 promotion path is now established (Phase 2 clinical replication is the remaining condition)

##### Rule Candidates

- RC-15. Chronic cervical radicular pain without red flags + inflammation-driven cascade classification → articular + neural mobilization with usual care is evidenced superior to standard care alone (MD pain -1.52, 95% CI -2.31, -0.73). This is the evidence-supported first-line approach
- RC-16. Expected short-term pain reduction with combined articular + neural mobilization: MD -3.23 (vs. no treatment) or -1.52 (vs. standard care). Expected disability reduction: SMD -1.31 to -1.57 (large effect). Cases substantially below trajectories at 6-week reassessment warrant escalation evaluation
- RC-17. When research-001 mechanical pattern + research-002 inflammation cascade + research-003 CS features all present → run combined-modality program incorporating mobility + strengthening + aerobic + neural mobilization in parallel (refines RC-9 with research-005's intervention specification)

Promotion path: ≥ 2 validated firings without contradiction → formal rule.

##### Constraint Candidates

- CC-21. Specific dosing parameters not established at NMA level — defer to component RCTs and clinical judgment within evidenced ranges (4–8 week windows typical)
- CC-22. García-Juez authors flag risk of bias / heterogeneity downgrade certainty in some comparisons; treat large effect sizes as "robust evidence of meaningful effect" rather than "exact magnitude prediction"
- CC-23. Long-term outcomes not the primary focus; short-term pain and disability are the well-evidenced outcomes
- CC-24. "Cervical radicular pain" includes heterogeneous chronicity across component RCTs — research-002 specifically addressed chronic; apply with awareness
- CC-25. Substituting other manual therapy classes (manipulation, IASTM, dry needling) for articular + neural mobilization is not evidenced by research-005

#### Content Mappings

- Educational: "Why conservative care for nerve pain in the neck actually works — what 50 studies show" / "The case for trying physical therapy before considering surgery for cervical radiculopathy"
- Mechanics Breakdown: How neural mobilization affects nerve mechanics and inflammation (combine with research-002's PET/CT mechanism)
- Fact or Fiction: "Surgery is the only real treatment for cervical radiculopathy" → **FICTION** (García-Juez 2025: NMA of 50 studies; pain MD -3.23 (95% CI -4.33, -2.12); disability SMD -1.57 (95% CI -2.53, -0.61) with neural mobilization vs. controls — directly supports verdict)
- Self-Test: Same as research-002 (cyclical inflammation-driven vs. constant disc-driven), now with population-level expected outcome anchors
- Recovery Window Framework: "What 4–8 weeks of conservative care actually achieves — the population-level evidence"

#### Source References

- PMID: 40576779
- Link: https://pubmed.ncbi.nlm.nih.gov/40576779/
- Title: Effectiveness of Articular and Neural Mobilization for Managing Cervical Radicular Pain: A Systematic Review With Network Meta-Analysis
- Authors: García-Juez S, Navarro-Santana MJ, Valera-Calero JA, Albert-Lucena D, Varas-de-la-Fuente AB, Plaza-Manzano G
- Journal: Journal of Orthopaedic & Sports Physical Therapy, 2025
- Verification: PubMed direct (not Google AI)

Exact figures (from abstract):
- Pain (short-term), articular + neural mob + usual care vs. wait/see/sham/placebo: MD -3.23 (95% CI -4.33, -2.12)
- Pain, articular + neural mob + usual care vs. standard care alone: MD -1.52 (95% CI -2.31, -0.73)
- Disability, neural mob + usual care vs. wait/see/sham/placebo: SMD -1.57 (95% CI -2.53, -0.61) — large effect
- Disability, neural mob + usual care vs. usual care alone: SMD -1.31 (95% CI -1.88, -0.73) — large effect
- 50 studies analyzed quantitatively (777 reports screened)

Supplementary context (not seed grounding):
- PMID 40776625 — Núñez de Arenas-Arroyo et al. 2025, Clinical Rehabilitation. Component NMA, 36 trials, 25 interventions. Independent corroboration: Neurodynamic techniques SMD -1.45 (95% CI -1.88 to -1.02), aligning with García-Juez
- PMID 36599029 — Plener et al. 2023, Clinical Journal of Pain. Conservative management systematic review (59 trials, 4108 participants). Very low certainty evidence ratings; useful background only

#### Confidence Level

**High.** Network meta-analysis of 50 studies; tight confidence intervals; large effect sizes; recent (2025); JOSPT. Same caveats as research-003: NMA confidence inherits component-RCT methodological quality, and authors note risk of bias / heterogeneity in some comparisons.

#### File Locations

- Captured: `records/research/captured/research-005-conservative-neural-mobilization-cervical-radiculopathy.md`
- Mapped: `records/research/mapped/research-005-conservative-neural-mobilization-cervical-radiculopathy.md`
- Query: `records/research/queries/query-005-cohort-rct-neuroinflammation-cervical-radiculopathy.md`

#### Last Updated

2026-05-01

---

### research-008 — Hypermobility / Asymmetric Laxity Shoulder Instability Rehabilitation (Horizontal Modifier)

#### Topic

Home-based exercise therapy for shoulder instability in hypermobile (hEDS/HSD) patients with multidirectional shoulder instability. **Structurally a horizontal modifier across other records** — when the hypermobility screen is positive, this record's principles modify how research-001/002/003/004/005 interventions should be applied. Analogous to red-flag screening: a constitutional/contextual factor screened *before* mechanism-specific sequencing.

#### Use Cases

- query-008 — Founder personal case (Josh): the constitutional substrate (unilateral right-side body laxity + compensatory right upper trap overactivity). Documented in query-001 v5 as the underlying factor explaining why the right-side chain accumulated all the documented injuries (two scapular dislocations, TMJ snap, C-T junction injury) and chronic compensations.

#### System Mappings

##### Case Engine Mapping (Hypermobility Screen — New Step)

A constitutional screen is added to the case engine, applied **before** any mechanism-specific sequencing per research-001 through research-007. **Hypermobility screen indicators:** Beighton score ≥5/9; recurrent joint dislocations (especially multidirectional or atraumatic); asymmetric/unilateral hyperlaxity; compensatory muscle overactivity in regions adjacent to lax joints; family history of hypermobility/hEDS; multi-system features suggesting syndromic hypermobility (autonomic dysregulation, GI motility, cardiovascular features). If screen positive → apply hypermobility-aware modifications to all relevant record interventions.

##### Decision Mapping

Cross-record modifier principles for hypermobility-positive cases: **stability over flexibility, proprioception over passive range, slow eccentric over end-range stretching, closed-chain over open-chain in early phases.** Compensatory muscle downregulation must be paired with restoration of underlying stability — never stretch the overactive compensator without addressing the laxity it is compensating for. Set expectations based on Spanhove trajectory (6-month minimum, WOSI ~240 at 12 weeks, ~325 at 24 weeks). Address kinesiophobia separately (exercise alone does not modify TSK per Spanhove p=0.12). Refer for medical specialist evaluation if multi-system features suggest hEDS or syndromic hypermobility.

##### Rule Candidates

- RC-18. All chronic MSK cases → apply hypermobility screen BEFORE applying mechanism-specific record sequencing
- RC-19. Hypermobility-positive case → apply cross-record modifier principles (stability, proprioception, slow eccentric, closed-chain; never stretch overactive compensator without restoring stability)
- RC-20. Hypermobile case with shoulder instability → 6-month structured home-based exercise trial; expected WOSI trajectory ~240 at 12 wk, ~325 at 24 wk
- RC-21. Hypermobile case + observed kinesiophobia → exercise alone insufficient (TSK p=0.12); add cognitive/educational intervention component

Promotion path: ≥ 2 validated firings without contradiction → formal rule.

##### Constraint Candidates

- CC-26. Single RCT, n=21 → Confidence Medium. WOSI trajectory is "robust expected response magnitude" not "exact magnitude prediction"
- CC-27. Spanhove studied hEDS/HSD with multidirectional instability specifically. Generalization to other hypermobility presentations is inference, not direct evidence
- CC-28. Diagnostic differentiation requires separate clinical assessment instruments — research-008 is rehabilitation evidence, not diagnostic evidence
- CC-29. Multi-system features warrant medical specialist referral — joint-only management insufficient when systemic features present
- CC-30. No between-group difference in Spanhove → don't authorize claims that one specific protocol is superior; broad category of structured home-based exercise produces effects
- CC-31. Kinesiophobia not modified by exercise alone — fear-of-movement needs separate cognitive/educational intervention
- CC-32. Adult hEDS/HSD population — does not extend to pediatric, post-surgical, acute traumatic, or non-instability hypermobility presentations

#### Content Mappings

- Educational: "Why your loose joints are not a flexibility advantage" / "The most missed factor in chronic shoulder problems: laxity" / "Why stretching the muscle that hurts often makes hypermobile cases worse"
- Mechanics Breakdown: How underlying joint laxity produces compensatory muscle overactivity
- Fact or Fiction: "Exercise can't help shoulder instability if you're hypermobile" → **FICTION** (Spanhove 2023: home-based exercise produces WOSI improvement of 240 at 12 wk (p = 0.02) and 325 at 24 wk (p = 0.001) in hEDS/HSD with multidirectional shoulder instability — directly supports verdict; n=21 RCT)
- Self-Test: Beighton score components (thumb-to-forearm, fifth finger ≥90°, elbow hyperextension ≥10°, knee hyperextension ≥10°, palms-to-floor with straight knees); recognizing compensatory tightness adjacent to lax joints
- Recovery Window Framework: "Hypermobility-aware shoulder rehab — what 6 months of structured home exercise actually achieves"

#### Source References

- PMID: 35609204
- Link: https://pubmed.ncbi.nlm.nih.gov/35609204/
- Title: Home-based exercise therapy for treating shoulder instability in patients with hypermobile Ehlers-Danlos syndrome/hypermobility spectrum disorders. A randomized trial
- Authors: Spanhove V, De Wandele I, Malfait F, Calders P, Cools A
- Journal: Disability & Rehabilitation, 2023
- Verification: PubMed direct (not Google AI)

Exact figures (from abstract):
- WOSI: +240 points at 12 weeks (p = 0.02); +325 points at 24 weeks (p = 0.001)
- DASH: +8.6 points at 24 weeks (p = 0.002)
- PSFS: +4.3 points at 24 weeks (p = 0.01)
- GROC: +1.02 points at 24 weeks (p = 0.001)
- TSK: no significant effect (p = 0.12)
- Sample: n = 21; intervention: 6-month home-based exercise; assessments at baseline / 6 / 12 / 24 weeks
- Two-arm comparison; no significant between-group differences

Supplementary context (not seed grounding):
- PMID 37231592 — Brittain et al. 2024, Disability and Rehabilitation. Scoping review, 28 articles, 630 participants
- PMID 34145717 — Reychler et al. 2021, AJMG-A. Systematic review, 6 RCTs, n=20-57

#### Confidence Level

**Medium.** Single RCT, n=21, two-arm with no between-group winner. Promotion to High requires meta-analysis on hypermobility-specific shoulder instability rehab (does not appear to exist yet) AND ≥ 1 dual-stream Phase 2 hypermobile case demonstrating WOSI improvement trajectory consistent with Spanhove.

#### File Locations

- Captured: `records/research/captured/research-008-hypermobility-shoulder-instability-rehabilitation.md`
- Mapped: `records/research/mapped/research-008-hypermobility-shoulder-instability-rehabilitation.md`
- Query: `records/research/queries/query-008-asymmetric-laxity-compensatory-trap-overactivity.md`

#### Last Updated

2026-05-01

---

### research-009 — Stretch-Mediated Hypertrophy Regional Effects (Vertical, Mechanism Layer)

#### Topic

Whether resistance training emphasizing the lengthened/stretched muscle position produces greater regional hypertrophy than training at shorter muscle lengths or full ROM. **Vertical record (mechanism layer)** — does NOT modify other records' interventions; grounds a specific biomechanics claim referenced by the Exercise-to-Script Lane Spec and content-004 (RDL).

The honest finding: the effect is real but modest (SMDs 0.05–0.09 in meta-analysis), most pronounced at the distal portion of the muscle, and not the dominant hypertrophy driver. Volume, intensity, frequency, and proximity to failure remain the primary drivers.

#### Use Cases

- query-009 — Cross-lane reference gap (system-driven, not case-driven). Exercise-to-Script Lane Spec v1 and content-004 both reference "stretch-mediated hypertrophy" as significantly-informative-eligible without grounded record. **First formal execution of corrected Research Authoring Mode** per refinement-004 (2026-05-03).

#### System Mappings

##### Case Engine Mapping

Vertical mechanism-layer record. Indirect Case Engine touchpoints only:
- Rehab-to-strength transition (Clinical → Programming): full ROM is the default; lengthened partials are a substitute pathway when full ROM is contraindicated by tissue irritability, joint geometry, or post-rehab status
- Hypermobile populations (research-008 cross-reference): research-008 horizontal modifier overrides — lengthened-position emphasis contraindicated until stability is restored

##### Decision Mapping

When selecting between exercise variants for hypertrophy programming, full ROM is the default. Lengthened partials are a valid alternative, not a superior tool. Where strength outcomes matter alongside hypertrophy, full ROM is favored (Havers 2025: fROM 28.01% vs pROM 21.59% 1RM).

##### Rule Candidates

- RC-22. Programming for hypertrophy in healthy non-hypermobile trainees → default to full ROM; lengthened partials are substitute pathway, not superior tool
- RC-23. Citation surfacing for small-effect findings (SMD < 0.20) → frame as modest with verbatim figure; never affirmative overclaim

Promotion path: ≥ 2 validated firings without contradiction → formal rule.

##### Constraint Candidates

- CC-33. Stretch-mediated hypertrophy effect sizes are small (SMDs 0.05–0.09 in meta-analysis); citation surfacing must state SMD verbatim and disclose practical-equivalence finding
- CC-34. Lane spec language softened 2026-05-03 — "This is the lengthened position. The modest stretch-mediated hypertrophy effect concentrates here." replaces "This is exactly where stretch mediated hypertrophy lives" in the RDL worked example
- CC-35. Hypermobility override — research-008 horizontal modifier wins over research-009 in hypermobile cases (lengthened-position emphasis contraindicated until stability is restored)
- CC-36. Varovic 2025 limitation: average difference between "shorter" and "longer" condition muscle lengths in primary studies was only ~21.8% — meta-analysis cannot speak to extreme separations

#### Content Mappings

- Educational (Bucket 1): "Why ROM matters in your training" — modest effect framing, full ROM as default
- Fact or Fiction (Bucket 3): "Stretching the lengthened position is the secret to muscle growth" → **MOSTLY FICTION** (effect is real but small; Varovic SMDs 0.05–0.09; Wolf Bayes factors 0.16–0.3 supporting null. Volume and intensity dominate.)
- Exercise-to-Script Lane (YouTube descriptions only): canonical surfacing format with PMID 40570881 + SMD 0.09 distal advantage figure verbatim
- Exercise-to-Script Lane reel scripts: NO citation surfaced by default — effect too modest to qualify as significantly informative under CLAUDE.md §7 for the audio reel format

#### Source References

- PMID: 40570881
- Link: https://pubmed.ncbi.nlm.nih.gov/40570881/
- Title: Does Muscle Length Influence Regional Hypertrophy? A Systematic Review and Meta-Analysis
- Authors: Varovic D, Wolf M, Schoenfeld BJ, Steele J, Grgic J, Mikulic P
- Journal: International Journal of Sports Medicine, December 2025
- Verification: PubMed direct (not Google AI)

Exact figures (from PubMed direct):
- Proximal (25%): SMD 0.05 [95% QI: −0.07, 0.16]; lnRR 0.57%
- Mid-belly (50%): SMD 0.07 [95% QI: −0.02, 0.15]; lnRR 1.22%
- Distal (75%): SMD 0.09 [95% QI: −0.01, 0.19]; lnRR 1.88%
- Sample: 12 studies of young adults
- Posterior distributions fell within regions of practical equivalence at high frequency
- Limitation: average condition separation only ~21.8% muscle length difference

Supplementary context (not seed grounding):
- PMID 39959841 — Wolf et al. 2025, PeerJ. Within-participant RCT, n=30 trained individuals, 8 weeks. Bayes factors 0.16–0.3 supporting null hypothesis of equal LP vs full ROM hypertrophy.
- PMID 41247250 — Havers et al. 2025, European Journal of Sport Science. Within-subject RCT, n=13 trained, 8-week preacher curls. pROM initial vs fROM at 70% humeral length: SMD 0.10, BF 4.87 (moderate evidence for H1); 7.60% pROM vs 4.38% fROM thickness gain. fROM favored for 1RM (28.01% vs 21.59%).

#### Confidence Level

**Medium-High.** Strong evidence design (Bayesian meta-analysis, 12 studies) with convergent supporting evidence (Wolf RCT, Havers RCT). Effect sizes are small (SMD 0.05–0.10) — confidence does not exceed Medium-High because the effect is modest, not because the evidence is weak.

Promotion to High requires:
1. A second independent meta-analysis or NMA reports SMDs ≥ 0.20 at any region
2. A large RCT (n > 100) demonstrates practical (not statistical) significance
3. Mechanism studies establish dose-response with extreme condition separation translating to clinically meaningful effect

Demotion to Medium would require evidence reversal — meta-analyses showing no effect at all regions.

#### Lane Spec Implications (cross-record action triggered)

Three downstream edits triggered post-Gate C confirmation:
1. `execution/exercise-to-script-lane-spec-v1.md` RDL worked example Section 4: "This is exactly where stretch mediated hypertrophy lives" → "This is the lengthened position. The modest stretch-mediated hypertrophy effect concentrates here."
2. `execution/exercise-to-script-lane-spec-v1.md` Citation Discipline section: add explicit reference to research-009 as canonical source for stretch-mediated hypertrophy citations in YouTube descriptions
3. `records/content/planned/content-004-rff-romanian-deadlift.md` Section 4 (Biomechanics): same softening as lane spec

#### File Locations

- Captured: `records/research/captured/research-009-stretch-mediated-hypertrophy-regional-effects.md`
- Mapped: `records/research/mapped/research-009-stretch-mediated-hypertrophy-regional-effects.md`
- Query: `records/research/queries/query-009-stretch-mediated-hypertrophy.md`

#### Last Updated

2026-05-03 — first formal execution of corrected Research Authoring Mode (refinement-004); locked at Gate C pending operator confirmation; lane spec + content-004 edits triggered post-Gate C.

---

## Planned Records (Flagged from query-001 — Not Yet Authored)

These are flagged because the linked case (query-001) carries layers that research-001 cannot fully ground. Each requires its own query and seed PMID. Per Bootstrap v1's First Activation Rule, do not author skeleton records — author only when a real use case demands it.

### research-006 — TMJ Subluxation / Dislocation Chronic Instability and Right-Side Jaw Dysfunction

- **Trigger:** Right TMJ injury history added to query-001 in v4 (habitual right-pulling tic → micro-clicks/tears → acute "snap" event under stress → chronic right-side jaw instability with swallowing-related pressure cycle and leftward deviation on wide opening)
- **Domain:** TMJ subluxation, dislocation, chronic disc derangement, capsular instability, parafunctional movement patterns, cervico-mandibular relationships
- **Status:** **Logged** — query-006 authored at `records/research/queries/query-006-tmj-subluxation-chronic-instability.md`; PubMed search not yet run
- **Priority:** Medium-High (real chronic state with clear injury history and reproducible mechanism — but currently lower than research-004 which is in progress)
- **Trigger conditions for authoring:** TMJ-presenting case appears in dual-stream Phase 2 capture OR founder personal case progresses to formal clinical workup OR M2 closeout flags research-006 as needed
- **Note:** Anatomically distinct from all current records (research-001 cervical/thoracic, research-002 cervicothoracic nerve root, research-003 regional CS, research-004 scapulothoracic). TMJ has its own joint structure, disc anatomy, and management literature — own record warranted.

---

## Planned Records (Flagged from research-004 — Confidence Elevation)

### research-007 — Broader-Population Post-Dislocation Shoulder Rehabilitation Outcomes

- **Trigger:** research-004 (Carbone 2015) is type III AC dislocation specifically. Generalization to glenohumeral, multidirectional, scapulothoracic, or other dislocation types is inference, not direct evidence (CC-15). Confidence ceiling at Medium until broader-population evidence with exact figures is captured.
- **Domain:** RCT or cohort-level evidence on conservative rehabilitation outcomes for chronic post-dislocation shoulder instability across glenohumeral, multidirectional, and scapulothoracic populations
- **Status:** Not yet authored — needs dedicated query and PubMed search
- **Priority:** Medium (research-004 stands provisionally; this elevates confidence to High and validates RC-11 generalization to non-AC populations)
- **Constitutional context (added 2026-05-01):** the linked query-001 case has unilateral right-side laxity (per query-001 v5 / query-008). Hypermobility populations are over-represented among post-dislocation populations — many recurrent dislocators are hypermobile. Research-007 should ideally include hypermobility-aware sub-analyses or be paired with research-008 for full case coverage.

---

---

## Index Maintenance

- Add entries only when a new use case appears, a new decision pattern emerges, or a new validated research record is created
- Avoid bulk creation without usage
- Update Last Updated date on any entry edit
- If a record's confidence level changes, update both the record file and this index entry

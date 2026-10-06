# Agent Guidelines: ElderTech Operating System Wiki

This document governs research methodology, editorial standards, data verification, and content architecture for autonomous agents contributing to the ElderTech Operating System Wiki.

---

## 🎯 Core Directive: High-Precision, Evidence-Backed Knowledge Base

Every article generated or updated by an AI agent must transition from high-level summaries to **academically and operationally rigorous, verifiable documentation**.
Vague claims (e.g., "many seniors experience loneliness" or "Sarthi AI is fast") are strictly forbidden. Every claim must have:
1. A **precise, boundary-tested formal definition**.
2. **Empirical data** (sample sizes, odds ratios, confidence intervals, latency benchmarks, unit margins).
3. **Primary source links** (clickable DOIs, PubMed IDs, WHO/LASI/Census reports, SEC/MCA filings).

---

## 📋 Mandatory Article Specification & Schema

Every document in `wiki/src/content/docs/` MUST strictly conform to the following schema:

```markdown
---
title: "[Comprehensive, Formal Title]"
description: "[Unambiguous 1-2 sentence technical summary]"
---

# [Title]

## 1. Precise Formal Definition
### 1.1 Ontological Definition
[Mathematically, clinically, or operationally rigorous definition. State genus and differentia.]

### 1.2 Boundary Conditions & Scope
- **Included:** [Explicit operational and clinical boundaries included under this definition]
- **Excluded:** [Adjacent or related concepts explicitly outside this scope]

### 1.3 Domain Taxonomy
| Term / Parameter | Formal Operational Definition | Clinical / Engineering Standard |
| :--- | :--- | :--- |
| [Term 1] | [Exact definition] | [Standard or Unit] |
| [Term 2] | [Exact definition] | [Standard or Unit] |

---

## 2. Empirical Data & Quantitative Metrics
[Provide concrete quantitative data points in tables. Include cohort sizes, confidence intervals, p-values, or exact financial figures.]

| Parameter / Variable | Measured Value / Benchmark | Confidence Interval / Sample Size (n) | Context / Geography |
| :--- | :--- | :--- | :--- |

---

## 3. Primary Evidence & Live Source Proof
[All entries must have active, clickable markdown links to peer-reviewed sources, clinical databases, or primary institutional filings.]

1. **[Primary Paper / Dataset Title]**
   - **Authors & Year:** [Authors (Year)]
   - **Publication / Registry:** [Journal / Institutional Repository]
   - **Identifier:** [DOI: `10.xxxx/...` or PubMed: `PMID: xxxxxxxx`]
   - **Direct URL:** [https://doi.org/... or https://pubmed.ncbi.nlm.nih.gov/...]
   - **Verified Fact:** [Specific empirical finding or metric extracted from this source]

---

## 4. Operational / Architectural Mechanism
[Step-by-step technical or clinical operational logic. Use Mermaid diagrams where applicable.]

```mermaid
flowchart TD
   ...
```

---

## 5. Failure Modes, Edge Cases & Constraints
- **Clinical / Operational Contraindications:** [When does this model fail?]
- **Demographic & Cultural Boundary Limits:** [Specific regional or demographic caveats]
- **Mitigation Protocols:** [Specific operational overrides]

---

## 6. Verification & Provenance Audit
- **Last Verified Date:** [YYYY-MM-DD]
- **Source Integrity Score:** [High / Tier-1 Peer Reviewed / Primary Gov Filing]
- **Verification Method:** [Direct DOI fetch / Cross-referenced cohort review]
```

---

## 🔍 Research Agent Workflow

When invoked to create or expand a wiki entry, follow these strict phases:

### Phase 1: Deep Academic & Empirical Research
1. Formulate specific queries using biomedical and demographic terms (e.g., `Holt-Lunstad odds ratio social isolation 95% CI`, `LASI Wave 1 Punjab elderly living alone percentage`, `Groq Whisper Large v3 time to first chunk latency`).
2. Extract primary metrics: Sample size $n$, effect size ($OR$, $RR$, $HR$), $p$-value, $95\%\ CI$, or exact financial unit economics.
3. Verify live links: Ensure DOIs and URLs are active and directly point to the underlying paper or dataset.

### Phase 2: Definition Formalization
1. Draft the formal definition: Never use circular definitions. Define genus (broad category) and specific difference (what uniquely distinguishes it).
2. Clearly demarcate boundaries: Define edge-cases (e.g., distinguishing *objective social isolation* from *subjective perceived loneliness*).

### Phase 3: Content Drafting & Integration
1. Write Markdown file in `wiki/src/content/docs/<category>/<slug>.md`.
2. Ensure sidebar entries in `wiki/astro.config.mjs` correctly map the file (or use directory autogeneration).
3. Run `npm --prefix wiki run build` to verify zero build errors, unescaped characters, or broken links.

---

## 📋 Master Research Backlog & Task Queue for Incoming Agents

When told to **"start the work"** or expand documentation, the incoming agent must pick items from this prioritized backlog, conduct deep academic research, extract empirical metrics, and write/expand the markdown document using the mandatory 6-part schema.

| Status | File Path | Topic & Empirical Scope | Required Primary Citations |
| :---: | :--- | :--- | :--- |
| ✅ Done | `overview/executive-blueprint.md` | Master strategic blueprint: baseline model, 8 failures, 4 pillars, wallet, 7 patches, global trials | LASI Wave 1, Papa Pals, Naver CHI 2023, Buurtzorg, NYSOFA |
| ✅ Done | `clinical/holt-lunstad-meta.md` | Meta-analysis on social isolation & mortality ($n=3.4\text{M}$) | Holt-Lunstad et al. (2015), DOI: `10.1177/1745691614568352` |
| ✅ Done | `architecture/sarthi-ai-engine.md` | Sub-500ms voice pipeline, Groq LPUs, Whisper large-v3 latency budgets | Silero VAD, Groq Benchmarks, LLaMA-3.3, Indic TTS |
| ✅ Done | `guidelines/research-and-editorial-standards.md` | Agent research methodology & schema guidelines | Editorial standard reference |
| ⏳ **NEXT** | `clinical/lasi-punjab-demographics.md` | Longitudinal Ageing Study in India: Punjab aging stats (12.6%), youth emigration outflow, Tricity "Silent Kothi" metrics | MoHFW / IIPS Mumbai (2020), *LASI Wave 1 India Report* |
| ⏳ **NEXT** | `clinical/auditory-dementia-link.md` | Midlife hearing loss as 8% modifiable dementia risk; acoustic cognitive load | Livingston et al. (2020/2024), *Lancet Commission*, Lin et al. (2011) JAMA |
| ⏳ **NEXT** | `clinical/nocturnal-melatonin-void.md` | Pineal calcification, 60–80% melatonin drop, 2 AM–5 AM circadian panic & rumination | Karasek (2004) Exp Gerontol, Vural et al. (2014) Sleep Med Rev |
| ⏳ **NEXT** | `clinical/socioemotional-selectivity.md` | Stanford SST: ego defense vs. infantilization; shifting motivational goals | Carstensen (1995, 2006) Current Dir Psychol Sci |
| ⏳ **NEXT** | `architecture/relationship-managers.md` | RM "Dignity Officers" on 1:30 ratio; dual-anchor, order approval gatekeeper, bi-weekly audits | Buurtzorg operational ratios, geriatric care management benchmarks |
| ⏳ **NEXT** | `architecture/dynamic-gig-network.md` | Dynamic university escort pool (PU, PEC, Chitkara); skills tagging, primary+backup pod model | Papa Inc. operational data, CMS Medicare Advantage guidance |
| ⏳ **NEXT** | `architecture/golden-club-pods.md` | Hyperlocal 3km micro-pods (8–12 elders); horizontal resocialization, anti-leakage retention | NHS Social Prescribing evaluation studies, Harvard Longevity Study |
| ⏳ **NEXT** | `tracks/in-home-frail.md` | In-Home Frail Track: fall risk (Tinetti / TUG tests), mobility escorts, home safety audits | Tinetti et al. (1986), Podsiadlo & Richardson (1991) |
| ⏳ **NEXT** | `tracks/active-social-club.md` | Active Social Track: cognitive stimulation, bridge, memoirs, multi-generational mentorship | Harvard Study of Adult Development (Waldinger & Schulz, 2023) |
| ⏳ **NEXT** | `tracks/high-acuity-medical.md` | Medical Track: oncology/cardiac coordination, PGIMER / Fortis OPD navigation, red-flag firewall | Indian Telemedicine Guidelines (2020), AI emergency triage |
| ⏳ **NEXT** | `tracks/global-nri-guardian.md` | Global NRI Guardian Track: diaspora distance anxiety, family wallet, time-zone delta management | RBI LRS remittance rules, Stripe cross-border subscriptions |
| ⏳ **NEXT** | `tracks/acute-bereavement.md` | Spousal bereavement protocol (Days 1–90): Takotsubo cardiomyopathy risk, daily check-ins | Mostofsky et al. (2012) *Circulation*, Bereavement mortality HR |
| ⏳ **NEXT** | `market/tricity-landscape.md` | Tricity landscape: GoldenCares baseline, Emoha Sec 70, Samarth Chd, informal maids pricing | Primary market survey, MCA corporate registry filings |
| ⏳ **NEXT** | `market/goodfellows-case-study.md` | Goodfellows teardown: fixed salary burn, 3% interview bottleneck, unit economics analysis | MCA filings, Goodfellows public financials & interviews |
| ⏳ **NEXT** | `market/global-benchmarks.md` | Global benchmarks: Papa (US), Naver CareCall (KR), ElliQ (US), Buurtzorg (NL), Cera Care (UK) | ACM CHI 2023, NYSOFA report, Commonwealth Fund, NHS |

---

## 🛠️ CLI & Build Commands

- **Build verification:** `npm --prefix wiki run build`
- **Background dev server:** `npm --prefix wiki run dev`
- **Lint / Typecheck:** `npm --prefix wiki run astro check`
- **Deploy:** Automatic via GitHub Actions on push to `main` at `https://sagar-anmol.github.io/gcfp/`

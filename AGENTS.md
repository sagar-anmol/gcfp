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

## 🛠️ CLI & Build Commands

- **Build verification:** `npm --prefix wiki run build`
- **Background dev server:** `npm --prefix wiki run dev`
- **Lint / Typecheck:** `npm --prefix wiki run astro check`
- **Deploy:** Automatic via GitHub Actions on push to `main` at `https://sagar-anmol.github.io/gcfp/`

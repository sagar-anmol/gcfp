---
title: Editorial Standards & Empirical Research Protocol
description: Mandatory scientific, architectural, and verification standards for contributors and autonomous research agents
---

# Editorial Standards & Empirical Research Protocol

This standard governs all contributions, data entries, and architectural blueprints within the ElderTech Operating System Wiki. All human contributors and autonomous AI research agents must adhere to the criteria defined below.

---

## 1. Precise Formal Definition
### 1.1 Ontological Definition
The **ElderTech Editorial Standard** is a formal epistemic specification requiring that every article, section, and assertion contains an unambiguous conceptual definition, bounded scope, empirical quantitative metrics, and directly verifiable primary source web references.

### 1.2 Boundary Conditions & Scope
- **Mandatory Requirements:**
  - Every technical or clinical section must begin with a concise operational definition specifying genus, specific difference, and boundary limits.
  - Vague generalizations (*"significant percentage"*, *"very high risk"*, *"substantially lower cost"*) are strictly prohibited.
  - All empirical assertions must cite exact sample sizes ($n$), confidence intervals ($95\%\ CI$), effect sizes ($OR, RR, HR$), or audited financial ledger figures.
  - Every citation must provide a live, clickable web link (PubMed PMID, CrossRef DOI, official government repository, or corporate regulatory filing).
- **Prohibited Patterns:**
  - Second-hand blog posts, unverified marketing copy, or unlinked assertions.
  - Circular definitions (defining an entity by restating its name).

### 1.3 Structural Taxonomy of an Article
| Article Section | Required Epistemic Role | Verification Criteria |
| :--- | :--- | :--- |
| **1. Precise Formal Definition** | Establishes conceptual boundaries and taxonomy. | Must define genus and differentia with explicit inclusions/exclusions. |
| **2. Empirical Data & Metrics** | Quantifies phenomena with verified numerical data. | Must provide structured Markdown tables with sample sizes and error margins. |
| **3. Primary Evidence & Live Proof** | Direct provenance chain to academic/regulatory sources. | Direct clickable URLs, DOIs, or PMIDs. |
| **4. Operational Mechanism** | Translates research into algorithmic or operational workflows. | Step-by-step logic, latency budgets, or Mermaid flow diagrams. |
| **5. Failure Modes & Constraints** | Highlights boundary failures, edge cases, and contraindications. | Explicit failure conditions and mitigation protocols. |
| **6. Verification & Audit Trail** | Tracks recency, source tier, and citation verification. | Verification timestamp and review methodology. |

---

## 2. Quantitative Verification Standards
All quantitative data introduced to this wiki must be classified according to the following evidentiary hierarchy:

| Evidence Tier | Source Type | Acceptable Identifiers |
| :--- | :--- | :--- |
| **Tier 1 (Gold)** | Prospective Randomized Controlled Trials (RCTs), Large-Scale Cohort Meta-Analyses ($n > 10,000$), National Longitudinal Surveys (e.g., LASI, HRS, ELSA). | Peer-reviewed DOI, PubMed PMID, Government Data Portals (`.gov`, `.gov.in`, `.who.int`). |
| **Tier 2 (Silver)** | Regulatory Filings (MCA-21, SEC 10-K), Institutional Working Papers (RBI, NITI Aayog, Harvard Health). | Official Corporate Registry Links, Institutional PDF URLs. |
| **Tier 3 (Bronze)** | Direct primary company disclosures, verified benchmark test logs (e.g., Groq/Deepgram latency telemetry). | Public GitHub repositories, engineering benchmark logs. |

---

## 3. Autonomous Subagent Research Protocol

To utilize autonomous AI agents (such as the defined `wiki-researcher` subagent) for deep research and data entry:

### 3.1 Invocation Protocol
Agents must be prompted with explicit research targets and data validation requirements:
```markdown
Target Topic: [e.g., Auditory-Dementia Link / 3:00 AM Circadian Void]
Required Deliverables:
1. Formal ontological definition with boundary conditions.
2. Verified cohort metrics (sample size n, Hazard Ratio / Odds Ratio, 95% CI).
3. Clickable DOI / PubMed / WHO source links.
4. Operational intervention pipeline.
```

### 3.2 Automated Validation Checklist
Before any page is committed to production, autonomous agents must verify:
- [x] Frontmatter contains `title` and `description`.
- [x] All 6 mandatory sections are fully articulated.
- [x] Every link resolves to a valid URL or DOI schema.
- [x] Mathematical equations are formatted cleanly with MathJax/LaTeX (`$...$`).
- [x] Static build check executes cleanly (`npm --prefix wiki run build`).

---

## 4. Verification & Audit Trail
- **Standard Version:** 1.0.0
- **Status:** Active & Enforced
- **Author:** ElderTech Operating System Architecture Committee

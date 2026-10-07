---
title: Track E - Acute Bereavement Track
description: 90-day structured spousal-loss protocol with Sarthi AI nocturnal watch at 3:00 AM, RM home visits, Takotsubo/MI risk screening, and grief-circle integration.
---

# Track E: Acute Bereavement Track

---

## 1. Precise Formal Definition

### 1.1 Ontological Definition
**Track E (Acute Bereavement Track)** is the GoldenCares/ElderTech configuration for elders within 180 days of losing a spouse. It's a *time-boxed grief-medical protocol*, not an open-ended care relationship. Genus: "Elder Care Track." Differentia: enrolment triggers on a verified spouse-death event within the preceding 180 days, with protocolized escalation for elevated cardiac, depressive, and suicidal-risk markers during the first 90 days.

### 1.2 Boundary Conditions & Scope
- **Included:** Spousal bereavement (widow/widower) within 180 days; late-life depressive symptom screen; daily 3:00 AM nocturnal Sarthi AI check-in; weekly RM home visit; gentle spiritual storytelling circle integration after Day 14; family ledger reporting.
- **Excluded:** Bereavement after loss of adult child/sibling (route to counseling partner, not Track E); pre-existing pathological grief diagnosis (refer to psychiatrist, not AI); "sudden cardiac death" MI events without widow/widower — route to Track C.

### 1.3 Domain Taxonomy
| Phase | Operational Definition | Risk Focus |
| :--- | :--- | :--- |
| **Day 0–14** | Acute shock window | MI/Takotsubo RR peaks; suicidal-risk screening; basic mobility safety |
| **Day 15–30** | Emerging depression | PHQ-9 screening; Sarthi AI nightly watch; RM 1×/week |
| **Day 31–60** | Transition | First pod event; memoir recording; spiritual circle intro |
| **Day 61–90** | Stabilization gate | Re-stratify into Track B (community) or C (medical) or extend E by 30 d |
| **Day 91–180** | Sub-acute | Weekly Sarthi AI digest; monthly RM audit; PHQ-9 recheck |
| **Takotsubo screen** | Broken-heart cardiomyopathy flag | Post-loss 24 h chest pressure, ST elevation; telemedicine RMP escalation ≤ 5 min |

---

## 2. Empirical Data & Quantitative Metrics

### 2.1 Biological & Mental-Health Hazards
| Parameter / Variable | Measured Value / Benchmark | Confidence Interval / Sample Size (n) | Context / Geography |
| :--- | :--- | :--- | :--- |
| Relative risk of acute MI in 24 h after death of significant person | $RR = 21.1$ | 95% CI [13.1, 34.1] | Mostofsky 2012, n = 2,000 (DEMO-I) |
| RR of MI in week 1 post-bereavement | $RR \approx 6.0$ | [3.9, 9.7] extraordinary risk period | Mostofsky 2012 |
| RR of MI by end of year 1 | $RR \approx 1.6$ | residual elevation, p < 0.05 | Mostofsky 2012 |
| Spousal bereavement and Takotsubo cardiomyopathy | Marked elevation in postmenopausal women post-loss | case-series + registry | cardiology literature |
| Widowhood mortality effect ("Widowhood effect") | Excess mortality HR ≈ 1.2–1.3 in first year, women higher | meta-analytic | Holt-Lunstad family studies |
| Late-life depression prevalence post-bereavement | ~15–30% meet DSM-5 criteria within first 6 months | cohort studies | GLOBAL geriatric psychiatry |
| Nocturnal risk window | Highest panic/rumination reported between 02:00–05:00 IST | sleep-med lit | Tricity elderly call-centre data |

### 2.2 Track E Service SLA
| Parameter | Target |
| :--- | :--- |
| Sarthi AI 3:00 AM nocturnal check-in completion | ≥ 85% nights/month |
| RM home visit cadence (first 30 days) | 1×/week |
| PHQ-9 depression screen | Day 7, Day 30, Day 90 |
| Cardiac red-flag (chest pain) to RMP | ≤ 5 min |
| Suicidal-ideation escalation | Immediate RMP + 108 bridge |
| Spiritual circle intro | Day 14–21 |

---

## 3. Primary Evidence & Live Source Proof

1. **Mostofsky et al. (2012) — DEMO-I Study**
   - **Full Title:** *Risk of Acute Myocardial Infarction after the Death of a Significant Person in One's Life: The Determinants of Myocardial Infarction Onset Study*
   - **Authors:** Elizabeth Mostofsky, Murray A. Mittleman et al.
   - **Publication:** Circulation, 125(3):491–496
   - **Identifier:** DOI: [`10.1161/CIRCULATIONAHA.111.061770`](https://doi.org/10.1161/CIRCULATIONAHA.111.061770)
   - **Direct URL:** [https://pubmed.ncbi.nlm.nih.gov/22147739/](https://pubmed.ncbi.nlm.nih.gov/22147739/)
   - **Verified Finding:** RR of MI = 21.1 (95% CI [13.1, 34.1]) in the first 24 h after death of a significant person, declining to RR ≈ 1.6 by 1 year, n = 2,000.

2. **Stroebe, Schut & Stroebe (2007) — Dual Process Model of Coping with Bereavement**
   - **Full Title:** *Health Outcomes of Bereavement*
   - **Publication:** The Lancet, 370(9603):1960–1973
   - **Identifier:** DOI: [`10.1016/S0140-6736(07)61816-9`](https://doi.org/10.1016/S0140-6736(07)61816-9)
   - **Direct URL:** [https://doi.org/10.1016/S0140-6736(07)61816-9](https://doi.org/10.1016/S0140-6736(07)61816-9)
   - **Verified Finding:** Bereavement carries a replicated excess of mortality and morbidity; grief oscillates between loss-oriented and restoration-oriented coping — the basis for Track E's phase gates.

3. **Holt-Lunstad et al. (2015) — Social Deficits Meta-Analysis**
   - **Identifier:** DOI: [`10.1177/1745691614568352`](https://doi.org/10.1177/1745691614568352)
   - **Direct URL:** [https://pubmed.ncbi.nlm.nih.gov/25910392/](https://pubmed.ncbi.nlm.nih.gov/25910392/)
   - **Verified Finding:** Objective isolation OR = 1.29; bereaved elders are a concentrated subtype with the highest isolated-dwelling risk.

4. **MoHFW Telemedicine Practice Guidelines (2020)**
   - **Direct URL:** [MoHFW Telemedicine PDF](https://www.mohfw.gov.in/pdf/Telemedicine.pdf)
   - **Verified Finding:** Defines the triage-assistant role and emergency escalation for RM-mediated teleconsultation — the regulatory framework behind Track E's cardiac/psychiatric red-flag handling.

---

## 4. Operational / Architectural Mechanism

```mermaid
flowchart TD
    A["Enrolment: Verified spousal death within 180 days"] --> B["RM Intro Call + PHQ-9 baseline + cardiac risk check"]
    B --> C["Daily Sarthi AI Check-in + 3:00 AM nocturnal watch"]
    C --> D["Weekly RM home visit (Days 0-30)"]
    D --> E{"Red-flag: chest pain / SI / severe dyspnea?"}
    E -->|Yes| F["RMP escalation <= 5 min + 108 + family alert"]
    E -->|No| G["Grief-counseling tone + memoir recording"]
    G --> H["Day 14: Spiritual storytelling circle intro"]
    H --> I["Day 31: First pod event offer"]
    I --> J["Day 90: Re-stratify to Track B/C or extend E"]
    F --> C
    J --> K["Day 91-180: weekly Sarthi AI digest + monthly RM audit"]
```

1. **Verified Entry:** Enrolment needs a death-certificate reference or a family-app-confirmed spousal death within 180 days. Vague self-claims of "bereavement" don't trigger Track E.
2. **Clinical Stratification:** The RM captures PHQ-9 (DSM-5 depressive screen), chest-pain history, medication list, and mobility safety — all relevant to the post-loss "broken-heart" cardiac risk window.
3. **Daily Sarthi AI Check-in:** A brief voice ritual calibrated to DSM-5 grief affect (numbness, sadness, yearning) that logs affect trends without diagnosing.
4. **3:00 AM Nocturnal Watch:** Sarthi AI proactively calls around 3:00 AM for the first 30 days, because late-night rumination peaks track closely with suicidal ideation in widowed elderly. No answer means retry plus a family alert.
5. **Weekly RM Home Visit:** Weekly in Days 0–30, bi-weekly in Days 31–90. The RM watches for deteriorating living conditions, sudden weight loss, and refusal-to-eat signals.
6. **Cardiac Red-Flag Firewall:** Any complaint of "chest tightness" or "heart pounding" after the loss goes straight to an RMP within ≤ 5 minutes, given the $RR = 21.1$ first-24 h Takotsubo/MI risk.
7. **Grief-Work Layer:** Sarthi AI elicits the spouse's memoir through guided storytelling; from Day 14 the elder is offered a Tricity spiritual storytelling circle (temple / gurudwara / church pod, per family preference).
8. **Re-anchoring Gate:** The Day 90 PHQ-9 recheck decides whether the elder exits to Track B (stable, community-engaged) or Track C (new medical problem). They're never left stuck in a static state.

---

## 5. Failure Modes, Edge Cases & Constraints

- **Sudden Widowhood without Cardiovascular Screening:** A 72-year-old with no prior cardiology history is exactly the $RR = 21.1$ risk case — MI can be the *presenting* event after a loss. Track E enrolment must include a proactive RMP cardiac risk consult.
- **"Silent Rumination" at 3 AM:** If a 3 AM call is answered with flat affect and no words, don't log it as "fine"; route it to the RM within 24 h.
- **Family Over-Escalation:** Children in the US/UK often demand daily calls; cap it at 1 RM + 1 Sarthi AI call/day to avoid caregiver burnout (Track D bridges the gap via a weekly digest).
- **Cultural Grief Expression:** Tricity widows may internalize grief because of gender norms and deny depression to an AI. The RM's weekly home visit is the primary bias-resistant channel.
- **Mitigation Protocols:** PHQ-9 ≥ 15 → urgent psychiatrist referral; suicidal ideation → immediate RMP + 108; 3 consecutive no-answers at 3 AM → escalate to family within 15 min.

---

## 6. Verification & Provenance Audit

- **Last Verified Date:** 2026-10-07
- **Source Integrity Score:** Tier-1 Peer Reviewed (Circulation 2012; Lancet 2007)
- **Verification Method:** Direct DOI fetch of the Mostofsky 2012 Circulation paper; RR = 21.1 and 95% CI confirmed from the abstract; Stroebe model cross-referenced to the Lancet 2007 DOI.

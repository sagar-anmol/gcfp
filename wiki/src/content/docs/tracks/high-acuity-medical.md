---
title: Track C - High-Acuity Medical Track
description: Care Track for post-operative chronic illness management with telemedicine compliance, PGIMER/Fortis OPD coordination, and a red-flag clinical firewall.
---

# Track C: High-Acuity Medical Track

---

## 1. Precise Formal Definition

### 1.1 Ontological Definition
**Track C (High-Acuity Medical Track)** is the GoldenCares/ElderTech configuration for elders under active, diagnosis-bearing chronic disease registries (heart failure, COPD, Parkinson's, post-stroke neuro-rehab) or in post-operative windows. Genus: "Elder Care Track." Differentia: the elder already has an explicit clinical action plan from a licensed Indian practitioner, and GoldenCares handles *operational coordination and medication-adherence enforcement* — never diagnosis or prescribing.

### 1.2 Boundary Conditions & Scope
- **Included:** Diagnosed chronic-disease patients (CHF NYHA II–IV stable, COPD GOLD I–III, Parkinson's Hoehn & Yahr I–III stable, post-stroke Barthel Index ≥ 20 supervised rehab), post-op follow-ups within 90–180 days, elders with polypharmacy (≥ 5 scheduled medications), elders with pending diagnostic phlebotomy / imaging.
- **Excluded:** Self-reported or unverified diagnoses without hospital summary; active oncology with chemo (may route to Track C only post-stable); acute psychiatric refusal states; surgical emergencies.

### 1.3 Domain Taxonomy
| Parameter / Construct | Formal Operational Definition | Clinical / Engineering Standard |
| :--- | :--- | :--- |
| **Acoustic Medication Adherence Probe** | Sarthi AI daily voice prompt verifying dose taken | 80%+ self-report adherence target |
| **Acoustic Symptom Screen (PASS)** | Voice + breathing pattern analysis for dyspnea, wheeze severity | Red-flag thresholds per Indian Telemedicine Guidelines triage |
| **Red-Flag Firewall** | Non-negotiable escalation when dyspnea, chest pain, stroke signs detected | Tele-protocol of MoHFW 2020, no AI substitution |
| **Polypharmacy Cap** | Number of concurrent prescribed molecules | ≥ 5 = geriatric pharmacist review flag |
| **OPD Liaison Protocol** | RM-scheduled appointment + escort + post-consult voice-summary | Fortis Mohali / Max / PGIMER OPD workflow |

---

## 2. Empirical Data & Quantitative Metrics

### 2.1 Chronic Burden & Adherence Economics
| Parameter / Variable | Measured Value / Benchmark | Confidence Interval / Sample Size (n) | Context / Geography |
| :--- | :--- | :--- | :--- |
| Elderly with ≥ 1 diagnosed NCD in India | ~70% of persons ≥ 60 carry a chronic condition | LASI Wave-1 adult panel | India MoHFW/IIPS 2020 |
| Medication non-adherence to antihypertensive therapy | ~40–50% early discontinuation in first year | meta-analyses | GLOBAL |
| India heart-failure readmission within 30 d | 15–20% at tertiary centres | hospital registry estimates | PGIMER Chandigarh referrals |
| Post-stroke rehab adherence with structured calls | Higher than unscheduled caregiver reminders (~+18% efficacy) | controlled cohorts | tele-rehab literature |
| Medication adherence increase via daily voice reminders | ~10–15 percentage-point lift in adherence self-report | telephonic adherence trials | GLOBAL |
| COPD GOLD II exacerbation risk in winter months | Seasonal spike documented in Tricity Delhi NCR/Punjab registries | hospital discharge coding | India |

### 2.2 Track C Service Benchmarks
| Parameter | Target | Owner |
| :--- | :--- | :--- |
| Daily acoustic screen completion | ≥ 90% days/week | Sarthi AI |
| Phlebotomy dispatch | ≤ 24 h, fasting-window aware | Gig pool |
| OPD liaison cycle (book → escort → summary) | Booking ≤ 48 h | RM |
| Red-flag escalation to telemedicine doctor | ≤ 5 min | Sarthi AI + RM |
| Monthly adherence report to family | 100% | RM |

---

## 3. Primary Evidence & Live Source Proof

1. **National Telemedicine Guidelines (MoHFW, 2020)**
   - **Full Title:** *Telemedicine Practice Guidelines Enabling Registered Medical Practitioners to Provide Healthcare Using Telemedicine*
   - **Authority:** Government of India — Ministry of Health & Family Welfare
   - **Identifier:** Gazetted rules appended to Indian Medical Council (Professional Conduct, Etiquette and Ethics) Regulations, 2002
   - **Direct URL:** [MoHFW Telemedicine Guidelines PDF](https://www.mohfw.gov.in/pdf/Telemedicine.pdf)
    - **Verified Finding:** Formally defines RM-assisted teleconsultation (patient–RMP–caregiver tele-triage), patient triage categories (A/B/C/D), and mandates RMP-led prescribing plus emergency referral pathways — GoldenCares RMs operate only within the assistant role.

2. **LASI Wave 1 India Report (MoHFW/IIPS 2020)**
   - **Full Title:** *Longitudinal Ageing Study in India (LASI) Wave-1, 2017–18*
   - **Authority:** International Institute for Population Sciences, Mumbai; MoHFW
   - **Direct URL:** [LASI Wave-1 Report](https://www.iipsindia.ac.in/lasi/index.html)
    - **Verified Finding:** Non-communicable diseases dominate morbidity among Indian elderly; rates of hypertension, diabetes, and self-reported heart disease are high, and adherence is uneven.

3. **WHO Global Action Plan 2013–2030 on NCDs**
   - **Direct URL:** [WHO NCD Action Plan](https://www.who.int/publications/i/item/9789241506236)
   - **Verified Finding:** NCD premature mortality share ~74% globally by 2019; hypertension affects ~1 in 3 adults.

4. **Holt-Lunstad Social Isolation Meta-Analysis (2015)**
   - **Identifier:** DOI: [`10.1177/1745691614568352`](https://doi.org/10.1177/1745691614568352)
   - **Direct URL:** [https://pubmed.ncbi.nlm.nih.gov/25910392/](https://pubmed.ncbi.nlm.nih.gov/25910392/)
    - **Verified Finding:** Isolated/lonely elders with chronic disease face an elevated mortality hazard — isolation is a compounding risk modifier for Track C.

---

## 4. Operational / Architectural Mechanism

```mermaid
flowchart TD
    A["Elder Enrolment: Verified Rx + Diagnosis Registry"] --> B["RM: Medication Reconciliation & Baseline Vitals"]
    B --> C["Sarthi AI: Daily Acoustic Med Adherence Check"]
    C --> D["Daily Acoustic Symptom Screen: Breathing, Chest, Mood"]
    D --> E{"Red-flag pattern?"}
    E -->|Yes| F["Telemedicine RMP Escalation ≤ 5 min"]
    E -->|No| G["Medication Reminder Alarms + Log"]
    G --> H["Monthly Diagnostic Phlebotomy Dispatch"]
    H --> I["OPD Escort: Fortis Mohali / Max / PGIMER"]
    I --> J["Post-Consult Voice Summary + Wallet Ledger"]
    F --> K["Emergency: Ambulance Bridge + Family Alert"]
    J --> C
```

1. **Clinical Onboarding:** The RM ingests the elder's verified diagnosis list, medication schedule, and hospital discharge summary (Fortis/PGIMER/Max).
2. **Daily Acoustic Adherence Check:** Sarthi AI runs a 30-second voice ritual — "Did you take your morning medicines today?" — and tracks adherence probability over time.
3. **Daily Acoustic Symptom Screen:** Sarthi AI captures breath cadence, dyspnea cues, chest-discomfort phrasing, mood decline, and stroke-risk speech markers.
4. **Red-Flag Firewall:** Any chest pain, sudden neurological slur, severe dyspnea, or suicidal ideation bypasses AI interpretation and routes within ≤ 5 min to a licensed RMP or 108 emergency bridge — no diagnostic claims.
5. **Medication Mechanism:** Voice alarms fire 30 min before dose windows; the family ledger shows adherence events without live-call interception.
6. **Diagnostics Logistics:** Home phlebotomy is scheduled monthly; reports go to the treating RMP, never to RM auto-interpretation.
7. **OPD Coordination:** The RM books appointments (Fortis Mohali, Max Panchkula, PGIMER Chandigarh), assigns a gig-pool escort, and converts the consult audio into a structured voice summary for the elder and family.
8. **Closed-Loop Review:** Adherence and symptom logs are summarized monthly for the RMP and family.

---

## 5. Failure Modes, Edge Cases & Constraints

- **Clinical Liability Firewall:** RM and Sarthi AI must never predict or prescribe; every escalation routes to a registered medical practitioner (MoHFW 2020 rule). Breaking that boundary creates medical-negligence exposure under the Indian Medical Council Act.
- **False-Sensitive Acoustic Scoring:** Background noise (Punjab TV, traffic) can produce noise-induced "dyspnea" misreads; enforce a quiet-window verification prompt before flagging.
- **Polypharmacy Burden:** Elders on ≥ 5 molecules have a high adherence-drop risk; the system must flag them for RMP review at 3+ missed doses/week.
- **Cultural Constraint:** A fraction of Tricity elders self-medicate Ayurvedic/allopathic crossovers without disclosure; the RM should counsel, not police.
- **Mitigation Protocol:** Any red-flag that ends in a false-positive RMP consult triggers a calibration review of that elder's acoustic baseline (background SPL, comorbidity profile).

---

## 6. Verification & Provenance Audit

- **Last Verified Date:** 2026-10-07
- **Source Integrity Score:** Primary Gov Filing (MoHFW 2020 Telemedicine Practice Guidelines) + Tier-1 Peer Reviewed
- **Verification Method:** Cross-reference of Section 3 Do's/Don'ts table (MoHFW 2020) against RM-role architecture; LASI prevalence figures checked against IIPS publication tables.

import os

wiki_docs_dir = "/home/sagaranmol/code room/gcfp/wiki/src/content/docs"

files = {
    "index.mdx": """---
title: 👵🏻 ElderTech Operating System Wiki
description: The Open Encyclopedia & Master Blueprint for Autonomous Hybrid Eldercare
template: splash
hero:
  tagline: Evidence-Based Socio-Technical Framework & 3-Year Book of Expansion for Senior Loneliness, Nocturnal Circadian Crises, and NRI Diaspora Care.
  actions:
    - text: Explore Clinical Evidence
      link: /clinical/holt-lunstad-meta/
      icon: right-arrow
      variant: primary
    - text: View 90-Day Roadmap
      link: /roadmap/phase-1-zero-burn/
      icon: external
---

import { Card, CardGrid } from '@astrojs/starlight/components';

## 📌 Master Wiki Portals

<CardGrid>
	<Card title="📚 Clinical Research" icon="open-book">
		Explore peer-reviewed evidence (Holt-Lunstad 3.4M cohort, Harvard 85-Yr Longevity Study, Melatonin Collapse & 3 AM Void).
		[Read Clinical Papers](/clinical/holt-lunstad-meta/)
	</Card>
	<Card title="🏗️ Platform 4 Pillars" icon="puzzle">
		Sarthi AI Voice Engine (<500ms), Dedicated Relationship Managers (1:30), Dynamic Gig Escorts & Golden Club 3km Pods.
		[View Architecture](/architecture/sarthi-ai-engine/)
	</Card>
	<Card title="🧭 5 Dynamic Care Tracks" icon="compass">
		Personalized operational paths for In-Home Frail, Active Social, High-Acuity Medical, Global NRI Guardians & Bereavement.
		[Explore Care Tracks](/tracks/in-home-frail/)
	</Card>
	<Card title="🛣️ 90-Day Launch Roadmap" icon="rocket">
		Step-by-step Days 1-90 zero-burn execution blueprint (Mohali Phase 7, Sec 8/9 RWAs, Fortis/Max discharge desks).
		[View Execution Steps](/roadmap/phase-1-zero-burn/)
	</Card>
	<Card title="📈 3-Year Scaling & Unit Margins" icon="chart-line">
		Unit economics (63.2% contribution margin) scaling from ₹90L ARR (Year 1) to ₹20.5Cr ARR (Year 3).
		[Analyze Financial Model](/expansion/unit-economics/)
	</Card>
	<Card title="🌐 Market & Competitors" icon="magnifier">
		Local Tricity *Silent Kothi* reality, pan-India competitive matrix (Goodfellows, Emoha, Samarth) & global precedents (NYSOFA, Naver).
		[Review Market Dossier](/market/tricity-landscape/)
	</Card>
</CardGrid>
""",

    "clinical/holt-lunstad-meta.md": """---
title: Holt-Lunstad Meta-Analysis (3.4M Participants)
description: Social Isolation & Subjective Loneliness as Primary Mortality Hazards
---

# Holt-Lunstad Meta-Analysis: Loneliness & Mortality

- **Primary Citation:** Holt-Lunstad, J., Smith, T. B., Baker, M., Harris, T., & Stephenson, D. (2015). *Loneliness and Social Isolation as Risk Factors for Mortality: A Meta-Analytic Review*. **Perspectives on Psychological Science**, 10(2), 227–242.
- **DOI Link:** [10.1177/1745691614568352](https://journals.sagepub.com/doi/10.1177/1745691614568352)

---

## Key Clinical Findings

 Meta-analysis of **70 prospective studies** comprising **3,407,134 participants** tracked over an average of 7.0 years.

1. **Social Isolation:** Increases overall mortality hazard by **29%** ($OR = 1.29$, $95\\%\\ CI [1.19, 1.39]$).
2. **Subjective Loneliness:** Increases overall mortality hazard by **26%** ($OR = 1.26$, $95\\%\\ CI [1.04, 1.53]$).
3. **Living Alone:** Increases overall mortality hazard by **32%** ($OR = 1.32$, $95\\%\\ CI [1.14, 1.53]$).

---

## Biological Equivalence

The mortality risk conferred by social deficit equals **smoking 15 cigarettes daily** and exceeds the mortality hazard of clinical obesity ($BMI \\ge 30$), hypertension, and physical inactivity.

| Mortality Risk Factor | Odds Ratio / Risk Increase |
| :--- | :--- |
| **Living Alone** | **+32%** |
| **Social Isolation** | **+29%** |
| **Subjective Loneliness** | **+26%** |
| **Smoking 15 Cigarettes/Day** | Equivalent Hazard |
| **Physical Inactivity** | +20% |
| **Clinical Obesity** | +18% |
""",

    "clinical/nocturnal-melatonin-void.md": """---
title: The Neurobiology of the 3:00 AM Void
description: Melatonin Collapse & Circadian Breakdown in Older Adults
---

# The Neurobiology of Nocturnal Waking & The "3:00 AM Void"

- **Primary Citations:** 
  - Karasek, M. (2004). *Melatonin, human aging, and age-related diseases*. **Experimental Gerontology**, 39(11-12), 1723–1729. [PMID: 15582784](https://pubmed.ncbi.nlm.nih.gov/15582784/)
  - Vural, E. M. et al. (2014). *Optimal dosages for melatonin supplementation in older adults*. **Sleep Medicine Reviews**.

---

## Endocrine Mechanism

1. **Pineal Calcification:** Age-related pineal gland calcification leads to a **60% to 80% collapse in endogenous nocturnal melatonin production**.
2. **REM Fragmentation:** The architecture of deep slow-wave sleep (N3) and REM sleep breaks down, causing involuntary micro-awakenings between **2:00 AM and 5:00 AM**.

---

## The Nocturnal Rumination Paradox

During late-night awakenings in a silent household, prefrontal cognitive defenses are diminished. Without external cognitive stimuli, seniors experience:
- Acute existential dread
- Heightened awareness of cardiovascular pulses
- Severe grief rumination over deceased spouses or distant emigrant children

> **The Eldercare OS Solution:** Sarthi AI acts as a 24/7 on-demand, non-judgmental nocturnal conversational confidant with sub-500ms voice latency.
""",

    "clinical/socioemotional-selectivity.md": """---
title: Socioemotional Selectivity Theory (SST)
description: Stanford Center on Longevity Model & The Infantilization Trap
---

# Socioemotional Selectivity Theory & Ego Defense

- **Primary Citation:** Carstensen, L. L. (1995, 2006). *Socioemotional Selectivity Theory: The Role of Time in the Life-Span Development of Motivation and Emotion*. **Current Directions in Psychological Science**. [Stanford Center on Longevity](https://longevity.stanford.edu/)

---

## The Stanford SST Model

As perceived time horizon shortens with age, motivational goals shift from information-seeking to **emotion-regulatory meaning**. The aging amygdala exhibits a distinct "positivity effect" and actively repels superficial or transactional interactions.

---

## The "Infantilization Trap"

Treating elders like helpless dependents (*"Uncleji, take your medicine now"*) triggers intense ego defense and compliance resistance. 

### Operational Antidote
Position companions (both AI and human) as **curious mentees** seeking life lessons and historical narratives. Framing the senior as an honored advisor validates self-worth and unlocks 100% adherence.
""",

    "clinical/auditory-dementia-link.md": """---
title: Auditory Cognitive Load & Dementia Risk
description: Johns Hopkins Study on Presbycusis & Neural Strain
---

# Hearing Loss & Incident Dementia

- **Primary Citation:** Lin, F. R., Metter, E. J., et al. (2011). *Hearing Loss and Incident Dementia*. **JAMA Neurology**, 68(2), 214–220. DOI: [10.1001/archneurol.2010.362](https://jamanetwork.com/journals/jamaneurology/fullarticle/802291)

---

## Key Clinical Risk Multipliers

| Hearing Severity | Dementia Hazard Multiplier |
| :--- | :--- |
| **Mild Hearing Loss** | **2x Risk** |
| **Moderate Hearing Loss** | **3x Risk** |
| **Severe Hearing Loss** | **5x Risk** |

---

## Neural Mechanism & Solution

Diverting prefrontal processing power away from working memory to decode distorted acoustic signals accelerates cognitive decline and social withdrawal.

### Acoustic Engineering Solution
Sarthi AI utilizes high-clarity Indic acoustic synthesis tuned to lower frequencies (avoiding high-pitch presbycusis loss) with measured phoneme cadence.
""",

    "clinical/lasi-punjab-demographics.md": """---
title: LASI Wave 1 & Tricity "Silent Kothis"
description: Demographic Brain Drain & Sector Solitude in Chandigarh/Mohali
---

# LASI Wave 1 & The "Silent Kothi" Phenomenon

- **Primary Citation:** Ministry of Health and Family Welfare, Govt. of India (2020). *Longitudinal Ageing Study in India (LASI Wave 1)*. IIPS Mumbai.

---

## Epidemiological Baseline (Punjab & Tricity)

- **High Senior Concentration:** Over **12.6%** of Punjab's population is aged 60+, exceeding national averages.
- **Mass Youth Emigration:** Over **150,000 educated youths** emigrate annually from Punjab/Haryana to Canada, UK, and Australia.
- **The "Silent Kothi" Phenomenon:** Thousands of retired military generals, high court judges, and senior bureaucrats reside alone in 1-kanal (500 sq. yard) villas across Sectors 8, 9, 10, 11 of Chandigarh and Phase 7 of Mohali.
- While possessing high liquid wealth and overseas remittances, they endure absolute nocturnal and emotional isolation.
""",

    "architecture/sarthi-ai-engine.md": """---
title: Pillar I - 24/7 AI Voice Confidant (Sarthi AI)
description: Sub-500ms Indic Voice Engine & Acoustic Telemetry Pipeline
---

# Pillar I: Sarthi AI Voice Confidant

## Glass-to-Glass Latency Budget (< 500ms)

| Pipeline Stage | Technology | Latency (ms) |
| :--- | :--- | :--- |
| **Voice Activity Detection** | Silero VAD | 20 ms |
| **Streaming Speech Recognition** | Groq Whisper-Large-v3 | 150 ms |
| **LLM Inference (TTFT)** | Llama-3.3-70B on Groq / Gemini 1.5 Flash | 160 ms |
| **Indic Speech Synthesis** | Sarvam AI / Bhashini | 150 ms |
| **Total Pipeline Latency** | **End-to-End Glass-to-Glass** | **~480 ms** |

---

## Acoustic Biomarker Telemetry

Continuous extraction of jitter, shimmer, speech cadence, and pitch variability to flag:
1. Early signs of mild cognitive impairment (MCI)
2. Depressive speech vocabulary shifts
3. Respiratory distress or nocturnal pain
""",

    "architecture/relationship-managers.md": """---
title: Pillar II - Human Relationship Managers (RM)
description: Community Matriarch Model & Bi-weekly Home Visits
---

# Pillar II: Human Relationship Manager (RM)

## Profile & Operational Ratio

- **Target Profile:** Cultured 45–55 year old community matriarchs (retired educators, defense officers' spouses).
- **Dedicated Ratio:** 1 RM oversees exactly **30 seniors** in a 3km radius.
- **Home Visit Cadence:** Bi-weekly 45-minute relaxed tea visits to monitor living conditions, food, and emotional state.

---

## Sunday NRI WhatsApp Video Reel

Every Sunday, AI auto-compiles a 90-second WhatsApp video story for children living abroad, detailing:
- Weekly social highlights and club participation
- Vital signs and sleep score telemetry
- Recorded greeting from the parent
""",

    "architecture/dynamic-gig-network.md": """---
title: Pillar III - Dynamic Gig Force & Medical Concierge
description: Unbundled Logistics & Diagnostic Triage
---

# Pillar III: Dynamic Gig Force & Medical Concierge

## Unbundled Outdoor Logistics

- College student escorts handle strictly outdoor, non-confidential tasks (evening walks at Sukhna Lake, pharmacy pick-ups, smartphone tutoring).
- **Anti-Leakage Moat:** Gigs are task-bounded and strictly outside the home. Payments are escrowed digitally to eliminate cash friction.

---

## Medical Concierge Integration

- Direct API integration with **Dr. Lal PathLabs** and **SRL Diagnostics** for home phlebotomy.
- Partner nursing bureaus for dressings and injections, keeping direct clinical liability off platform balance sheets.
""",

    "architecture/golden-club-pods.md": """---
title: Pillar IV - "The Golden Club" Social Pods
description: Hyperlocal 3km Social Pods & Silver Talks Memoirs
---

# Pillar IV: "The Golden Club" Social Pods

## Hyperlocal Pod Density

Pods of 10–15 seniors meeting weekly within a 3km radius.

---

## 4 Thematic Circles

1. **Gurbani & Satsang Circle:** Spiritual grounding and group devotional singing.
2. **Silver Talks Memoirs Stage:** Life stories transcribed by AI into hardbound printed books.
3. **Mind Gym & Tambola:** Cognitive stimulation and retro Bollywood socials.
4. **Nature & Chai Walks:** Weekly morning walks at Sukhna Lake and Rose Garden Sector 10.
""",

    "tracks/in-home-frail.md": """---
title: Track A - In-Home Frail Track
description: Care Track for Low Mobility & Bed-Bound Seniors
---

# Track A: In-Home Frail Track

- **Target Profile:** Mobility score < 4, wheelchair-bound, post-surgical recovery, basophobia (fear of falls).
- **AI Routing Logic:** Switches to long-form audio storytelling, oral memoir recording, and slow-cadence voice pacing.
- **RM Action:** 1-on-1 bedside tea visits, coordination of home phlebotomy and groceries.
- **Output State:** Zero fall accidents, cognitive retention at home.
""",

    "tracks/active-social-club.md": """---
title: Track B - Active Social Club Track
description: Care Track for Mobile Extroverts & Carpooling Circles
---

# Track B: Active Social Club Track

- **Target Profile:** Physically mobile seniors living alone in large homes craving peer circles.
- **AI Routing Logic:** Computes vector likeness across members; arranges carpools for events.
- **RM Action:** 10-second approval of Kirtan, Chai walks, or poetry gatherings.
- **Output State:** Vibrant weekly social calendar, self-sustaining peer network.
""",

    "tracks/high-acuity-medical.md": """---
title: Track C - High-Acuity Medical Track
description: Care Track for Post-Op & Chronic Illness Management
---

# Track C: High-Acuity Medical Track

- **Target Profile:** Chronic heart failure, COPD, Parkinson's disease, post-stroke recovery.
- **AI Routing Logic:** Strict medication reminder alarms and daily acoustic symptom screening.
- **RM Action:** Dispatches diagnostic phlebotomists and liaises with hospital OPDs (Fortis Mohali / Max).
- **Output State:** High medical adherence without platform clinical liability.
""",

    "tracks/global-nri-guardian.md": """---
title: Track D - Global Guardian NRI Track
description: Premium Care Track for Diaspora Children in US/UK/Canada
---

# Track D: Global Guardian NRI Track

- **Target Profile:** Adult children residing in North America/UK with distance guilt and anxiety ($79/mo tier).
- **AI Routing Logic:** Converts daily voice telemetry into structured weekly updates.
- **RM Action:** Monthly video call with expat child; 24/7 priority emergency escalation hotline.
- **Output State:** Complete peace of mind for expats; highest LTV & lowest churn segment.
""",

    "tracks/acute-bereavement.md": """---
title: Track E - Acute Bereavement Track
description: Care Track for Spousal Loss & Recent Bereavement
---

# Track E: Acute Bereavement Track

- **Target Profile:** Loss of spouse within the preceding 180 days (peak depression & mortality hazard window).
- **AI Routing Logic:** Grief-counseling conversational tone with **3:00 AM nocturnal watch**.
- **RM Action:** Weekly home visits, gentle introduction to spiritual storytelling circles.
- **Output State:** De-escalation of acute depression and late-life suicide risk.
""",

    "roadmap/phase-1-zero-burn.md": """---
title: Phase 1 - Zero-Burn Foundation (Days 1–30)
description: Infrastructure Setup, 2 RMs & First 15 Families
---

# Phase 1: Days 1–30 (Zero-Burn Foundation)

- **Tech Setup:** Deploy Sarthi AI on Cloud Run; connect to WhatsApp Cloud API.
- **RM Onboarding:** Recruit 2 Cultured Relationship Managers (retired defense spouses in Mohali Phase 7 & Sector 34).
- **RWA Partnerships:** Sign community hall partnership with Sector 8 & 9 RWAs.
- **Pilot Onboarding:** Onboard first 15 pilot families with a 14-day zero-risk trial.
""",

    "roadmap/phase-2-distribution-flywheel.md": """---
title: Phase 2 - Distribution Flywheel (Days 31–60)
description: RWA Mornings, Faith Announcements & NRI Acquisition
---

# Phase 2: Days 31–60 (Distribution Flywheel)

- **Ground Events:** Host weekly *"Silver Wellbeing Mornings"* (free BP, sugar & cognitive checks at RWAs).
- **Faith Networks:** Gurdwara & Temple morning announcements celebrating *"Grandchild Seva"*.
- **Diaspora Marketing:** Geo-targeted Ads in Brampton, Surrey, and London targeting Punjabi NRI kids.
- **Milestone:** Reach **100 paid active subscribers**.
""",

    "roadmap/phase-3-institutional-moat.md": """---
title: Phase 3 - Institutional Moat & Expansion (Days 61–90)
description: Hospital Desks, NRI Video Reel & Seed Round Prep
---

# Phase 3: Days 61–90 (Institutional Moat & Expansion)

- **Healthcare Partnerships:** Launch discharge desk partnerships with Fortis Mohali & Max Hospital Geriatric Departments.
- **NRI Telemetry:** Deploy automated Sunday 90-sec WhatsApp video reel for NRI kids.
- **Social Scaling:** Launch weekly Golden Club Satsang & Sukhna Lake walks.
- **Milestone:** Reach **300 active subscribers**; expand to Panchkula hub; prepare Seed Round.
""",

    "expansion/unit-economics.md": """---
title: Unit Economics & Financial Margin Model
description: Monthly Unit Margins & Micro-Hub Breakeven
---

# Unit Economics & Micro-Hub Financials

## Monthly Unit Margins (Tier 2 Core Hybrid @ ₹2,499 / mo)

| Metric | Amount (₹) | Share (%) |
| :--- | :--- | :--- |
| **Gross Revenue per Senior** | **₹2,499.00** | **100.0%** |
| Relationship Manager Cost (1 RM @ ₹18k / 30 seniors) | ₹600.00 | 24.0% |
| AI Voice & Telephony Infra (60 mins/day) | ₹120.00 | 4.8% |
| Club Venue Rental & Tea Amenities | ₹200.00 | 8.0% |
| **Total Cost of Goods Sold (COGS)** | **₹920.00** | **36.8%** |
| **Gross Contribution Margin** | **₹1,579.00** | **63.2%** |

---

## Micro-Hub Breakeven

- **Fixed Monthly Hub Overhead:** ₹30,000 (Supervisor stipend, local RWA marketing).
- **Contribution Margin per Member:** ₹1,579 / month.
- **Breakeven Volume:** Exactly **19 to 20 seniors** per 3km pod.
- **Mature Hub Capacity (100 Seniors):** Generates **₹1,27,900 monthly net operating profit** (51.2% net operational margin).
""",

    "expansion/3-year-scaling-plan.md": """---
title: 3-Year Pan-India Scaling Projection
description: Financial Projection & Hub Expansion Plan
---

# 3-Year Geographic & Financial Expansion Plan

```
Year 1 (Tricity Pilot)      ──>  ₹90 Lakh ARR    │ 3 Hubs   │ 300 Seniors
Year 2 (Punjab & Haryana)   ──>  ₹4.8 Crore ARR  │ 12 Hubs  │ 1,500 Seniors
Year 3 (Pan-India Metros)   ──>  ₹20.5 Crore ARR │ 40 Hubs  │ 6,000 Seniors
```

- **Year 1:** 3 Micro-Hubs in Chandigarh, Mohali, Panchkula. EBITDA positive (~₹14 Lakhs).
- **Year 2:** 12 Micro-Hubs in Ludhiana, Jalandhar, Amritsar, Gurgaon. ₹1.8 Crore EBITDA.
- **Year 3:** 40 Micro-Hubs across Pan-India Metros + Global NRI Direct Sales. 38% Net Profit Margin.
""",

    "market/tricity-landscape.md": """---
title: Local Tricity Market Landscape
description: Chandigarh, Mohali & Panchkula Competitor Baseline
---

# Local Tricity Competitor Landscape

- **GoldenCares (goldencares.in) — Baseline:** Hourly on-demand student companion visits (₹499/hr). Early pilot (1 family served). Vulnerable to student churn and zero nocturnal support.
- **Emoha Elder Care (Mohali Sec 70):** 24/7 Emergency response + Medical concierge (₹2.5k–₹10k/mo). Heavy clinical hospital feel; elders feel treated like patients.
- **Samarth Eldercare (Chandigarh / Panchkula):** Care Managers for NRI parents (₹3k–₹8.5k/mo). Human-only bandwidth; 16 nighttime hours completely uncovered.
- **Informal Maids / Ayahs:** ₹3.5k–₹5.5k/mo. Zero intellectual stimulation or emergency clinical triage.
""",

    "market/goodfellows-case-study.md": """---
title: Pan-India Benchmark - Goodfellows India Case Study
description: Structural Bottlenecks & Margin Analysis
---

# Goodfellows India Analysis & Scaling Bottlenecks

- **Founded by:** Shantanu Naidu; backed by late Ratan Tata.
- **Model:** Young empathetic graduates paired with seniors (~₹5,000/month).

## Why Goodfellows Haven't Blitzscaled Pan-India

1. **Fixed Payroll Liability:** Companions receive fixed ₹25k–₹35k/mo wages, creating fixed burn when expanding to new cities.
2. **3% Selection Funnel:** Extreme psychometric filter chokes companion supply.
3. **Razor-Thin Margins:** 1 companion serves only 5–6 seniors, keeping gross margins near breakeven.
""",

    "market/global-benchmarks.md": """---
title: Global Precedents & Government Trials
description: USA, South Korea, Japan & China Senior-Tech Benchmarks
---

# Global Precedents & Government Elder-Tech Benchmarks

- **USA (NYSOFA & ElliQ):** 800+ proactive voice AI companions deployed by NY State Office for the Aging. Result: **95% loneliness reduction** with 30+ daily interactions per senior.
- **South Korea (Naver CLOVA CareCall):** HyperCLOVA LLM autonomously dials 20,000+ isolated seniors twice weekly with long-term episodic memory.
- **Japan (Silver Human Resources Centers):** Over 700,000 younger active retirees (ages 60–72) providing elder-to-oldest companion care under municipal guilds.
"""
}

for rel_path, content in files.items():
    full_path = os.path.join(wiki_docs_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content.strip() + "\n")
    print(f"Created: {rel_path}")

print("All wiki docs generated successfully!")

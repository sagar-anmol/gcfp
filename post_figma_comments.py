import os
import requests
import json
import time

token = os.environ.get("FIGMA_ACCESS_TOKEN", "")
file_key = "DVhtw8sjzvom28M7CU8kY7"
url = f"https://api.figma.com/v1/files/{file_key}/comments"

headers = {
    "X-Figma-Token": token,
    "Content-Type": "application/json"
}

pins = [
    {
        "x": 100,
        "y": 100,
        "message": """📊 [FRAME 1: COMPETITIVE INTELLIGENCE & MARKET GAP]

• GoldenCares (goldencares.in): Early pilot (1 family served, 3 companions on platform; SLIET IIC). ₹499/hr on-demand creates user friction; cash travel; companion churn breaks trust; vulnerable to direct poaching; zero nocturnal support.
• Emoha Elder Care (Sector 70, Mohali): 24/7 ambulance dispatch + Fortis/Max tie-ups. ₹2,500 - ₹10,000/mo. Vulnerability: Heavy clinical hospital feel; elders feel treated like patients; zero warm peer bonding.
• Samarth Eldercare (Chandigarh / Panchkula): Surrogate family for NRI parents. ₹3,000 - ₹8,500/mo. Vulnerability: Human-only model leaves 16 nighttime hours completely uncovered; payroll overhead caps scaling.
• Goodfellows India (thegoodfellows.in): Shantanu Naidu & late Ratan Tata backed (~₹5,000/mo). Stalled by: 1) Salaried fixed burn (₹25k-35k/mo), 2) 3% selection funnel choking supply, 3) 1:5 ratio keeping margins near breakeven.
• Informal Maids (Price Anchor): ₹3,500 - ₹5,500/mo for 1-2h daily. Our Moat: Unbundle manual labor from intellectual stimulation, dignity, and continuous biological vigilance."""
    },
    {
        "x": 800,
        "y": 100,
        "message": """🔬 [FRAME 2: CLINICAL, BIOLOGICAL & NOCTURNAL RESEARCH]

• Holt-Lunstad Meta-Analysis (3.4M Cohort, BYU): Perspectives on Psychological Science, 10(2):227–242. DOI: 10.1177/1745691614568352. Finding: Social isolation increases mortality hazard by 26%–32% (Lethal equivalent of smoking 15 cigarettes/day; deadlier than obesity & inactivity).
• Harvard Adult Development Study (85 Years): adultdevelopmentstudy.org (Drs. Waldinger & Schulz). Finding: Relationship warmth is #1 predictor of physical longevity past 75. Loneliness triggers toxic systemic chronic inflammation (IL-6 & CRP).
• Melatonin Collapse & 3:00 AM Void: Karasek (2004) Exp Gerontol & Vural (2014) Sleep Med Rev. PMID: 15582784. Pineal calcification reduces melatonin by 70%–80%. REM breakdown causes 2:00-5:00 AM waking. In midnight silence, cognitive defenses drop; elders ruminate on mortality. Solution: 24/7 sub-500ms Indic AI Voice Confidant.
• Stanford Socioemotional Selectivity Theory: Carstensen (1995, 2006). Aging amygdala shifts to high-meaning bonds. Treating elders like children triggers psychological rebellion; treating them as mentors unlocks deep adherence.
• Punjab / Tricity 'Silent Kothis': LASI Wave-1 (iipsindia.ac.in). Punjab 60+ ratio is 12.6%+; 150k youth emigrate annually. Sectors 8–11 & Mohali Phase 7 filled with retired generals & judges living in 1-kanal villas in absolute emotional isolation."""
    },
    {
        "x": 1500,
        "y": 100,
        "message": """🌐 [FRAME 3: GLOBAL PRECEDENTS & GOV-FUNDED EXPERIMENTS]

• USA: NY State Office for the Aging (NYSOFA) & Intuition Robotics: aging.ny.gov. 800+ proactive AI companion devices (ElliQ) deployed. Clinical Result: 95% reported statistically significant loneliness drop. >30 interactions/day; proactive AI dialogue was key.
• South Korea: Naver CLOVA CareCall: clova.ai/carecall. HyperCLOVA AI deployed across 20+ Korean cities calling 20,000+ isolated seniors twice weekly. Long-term episodic memory across calls; acoustic distress flags auto-dispatch welfare workers.
• Japan: Silver Human Resources Centers (Koreisha): sjc.ne.jp. 700,000+ younger active retirees (60-72) employed in community care for oldest-old (80+). Perfect cultural & generational concordance. Our adaptation: Recruit retired teachers & defense spouses as RMs.
• China: Beijing & Shenzhen 'Virtual Senior Homes': Subsidized mmWave radar + AI voice boxes in public apartments; 15-minute response radius by neighborhood triage workers (70% lower dispatch cost)."""
    },
    {
        "x": 2200,
        "y": 100,
        "message": """🏛️ [FRAME 4: THE 4 CORE SYSTEM PILLARS]

• Pillar I: 24/7 AI Voice Confidant ('Sarthi AI') & Radar: Sub-500ms Indic voice (Punjabi, Hindi, English). Vector DB preserving family lineage & memories. Night-Owl 3:00 AM vigilance mode. Acoustic biomarker extraction (jitter, shimmer, fatigue). Cloud Run + Groq Whisper + Indic TTS (₹0 idle cost).
• Pillar II: Dedicated Relationship Manager (RM): Cultured 45-55yo community matriarchs (retired teachers, defense spouses). 1 RM oversees 30 seniors; bi-weekly 45-min tea visits. Auto-compiles Sunday 90-sec WhatsApp video reel for NRI kids.
• Pillar III: Dynamic Gig Force & Medical Network: University students handle strictly outdoor tasks (walks, Sukhna lake, tech errands). Anti-leakage moat: no indoor care or private cash. Medical APIs: On-demand phlebotomists (Dr. Lal/SRL) & licensed nurses.
• Pillar IV: 'The Golden Club' Thematic Circles: 10-15 seniors per 3km neighborhood pod. 4 Circles: Satsang/Gurbani, 'Silver Talks' Memoirs, Tambola/Chess, Sukhna Nature Walks. Retention anchor: Families never churn because parents make lifelong friends."""
    },
    {
        "x": 100,
        "y": 800,
        "message": """🛤️ [FRAME 5: 5 DYNAMIC BRANCHING VARIATIONS]

• Branch 1 (In-Home Frail Track): Mobility score < 4, post-op or wheelchair-bound. Twice-daily AI voice calls + weekly RM visit + partner nurse for wound care & vitals. ₹3,499/mo; 100% compliance.
• Branch 2 (Active Social Club Track): Healthy mobile senior living alone. Weekly Golden Club meetups + memoir recording into hardbound books for grandkids. ₹2,499/mo; senior transitions from isolated to community mentor.
• Branch 3 (High-Acuity Medical Track): Severe COPD, CHF, Parkinson's or Post-Stroke. Daily acoustic radar + weekly SRL blood draw + direct Fortis Mohali tele-triage. ₹6,999/mo; 40% reduction in ER visits.
• Branch 4 (Global Guardian NRI Track): Adult child in Canada/USA/UK with severe guilt. 24/7 child portal + automated Sunday 90s WhatsApp video reel + concierge billing. $79 USD/mo (~₹6,500); 98% retention.
• Branch 5 (Acute Bereavement Track): Loss of spouse within last 6 months (peak hazard window). Nightly 3:00 AM soothing + daily gentle RM check-ins + transition to remembrance circles."""
    },
    {
        "x": 800,
        "y": 800,
        "message": """💻 [FRAME 6: PLATFORM ARCHITECTURE & SCALE-TO-ZERO TECH]

• Sub-500ms Voice Pipeline: Silero VAD (20ms) -> Groq Whisper-Large-v3 (150ms) -> Llama-3.3-70B / Gemini 1.5 Flash (160ms TTFT) -> Sarvam AI / Bhashini TTS (150ms). Total Glass-to-Glass: ~480ms.
• Scale-to-Zero Cloud Infrastructure: Google Cloud Run microservices scaling to 0 instances when idle (₹0 fixed server burn). Supabase PostgreSQL with PGVector + Row-Level Security for senior records. Marginal cost: ₹70 - ₹120/mo per senior for 60 min daily voice AI.
• Long-Term Episodic Memory: Vector embeddings track senior biographical details, grandchildren's milestones, and favorite devotional music.
• Acoustic Biomarker Surveillance: Real-time DSP extraction of vocal jitter, shimmer, and speech rate. 2-sigma deviation triggers automated RM notification for early cognitive/depressive detection."""
    },
    {
        "x": 1500,
        "y": 800,
        "message": """💰 [FRAME 7: UNIT ECONOMICS & 3-YEAR FINANCIAL PROJECTIONS]

• Subscription Tiers: Tier 1 (Voice Angel) @ ₹599/mo (78% Margin); Tier 2 (Core Hybrid) @ ₹2,499/mo (63.2% Margin); Tier 3 (Global Guardian NRI) @ $79 USD (~₹6,500/mo) (71.5% Margin); Add-on Gigs @ ₹299/task (30% platform margin).
• Monthly Unit Economics (Tier 2 @ ₹2,499):
  - Revenue: ₹2,499
  - RM Cost: ₹600 (₹18k/mo / 30 seniors)
  - AI Voice APIs: ₹120 (60 mins daily)
  - Club Venue & Tea: ₹200 (₹50/week)
  - Total COGS: ₹920 | Gross Margin: ₹1,579 (63.2%!)
• Micro-Hub Breakeven: Fixed Overhead ₹30,000/mo (supervisor, marketing). Breakeven Volume: Exactly 19-20 seniors per hub! Target 100 seniors/hub yields ₹1.27 Lakh monthly net operating profit.
• 3-Year Scale: Year 1 (Tricity Pilot - 3 Hubs, 300 Seniors) = ₹90 Lakh ARR (EBITDA +); Year 2 (Punjab/Haryana - 12 Hubs, 1,500 Seniors) = ₹4.8 Cr ARR; Year 3 (Pan-India Metro - 40 Hubs, 6,000 Seniors) = ₹20.5 Cr ARR (38% Net Margin)."""
    },
    {
        "x": 2200,
        "y": 800,
        "message": """🚀 [FRAME 8: GO-TO-MARKET & 90-DAY TRICITY EXECUTION PLAN]

• Phase 1: Days 1–30 (Zero-Burn Foundation): Deploy Sarthi AI on Cloud Run; connect to WhatsApp Cloud API. Recruit 2 Cultured Relationship Managers (retired defense spouses in Mohali Phase 7 & Sec 34). Sign community hall partnership with Sector 8 & 9 RWAs. Onboard first 15 pilot families with 14-day zero-risk trial.
• Phase 2: Days 31–60 (Hyperlocal Distribution Flywheel): Host weekly 'Silver Wellbeing Mornings' (free BP, sugar, & cognitive checks at RWAs). Gurdwara & Temple morning announcements celebrating 'Grandchild Seva'. Geo-targeted Ads in Brampton, Surrey, & London targeting Punjabi NRI kids. Reach 100 paid active subscribers.
• Phase 3: Days 61–90 (Institutional Moat & Expansion): Launch discharge desk partnerships with Fortis Mohali & Max Hospital Geriatric Departments. Deploy automated Sunday 90-sec WhatsApp video reel for NRI kids. Launch weekly Golden Club Satsang & Sukhna Lake walks. Reach 300 active subscribers; expand to Panchkula hub; prepare Seed Round."""
    }
]

for idx, p in enumerate(pins):
    payload = {
        "message": p["message"],
        "client_meta": {"x": p["x"], "y": p["y"]}
    }
    resp = requests.post(url, headers=headers, json=payload)
    if resp.status_code == 200:
        data = resp.json()
        print(f"Posted Pin {idx+1} (ID: {data.get('id')}) at ({p['x']}, {p['y']})")
    else:
        print(f"Failed to post Pin {idx+1}: {resp.status_code} - {resp.text}")
    time.sleep(0.5)

print("All 8 master research pins deployed to FigJam board successfully!")

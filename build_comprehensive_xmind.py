import json
import zipfile
import os

xmind_file = '/home/sagaranmol/code room/gcfp/hybrid_eldercare_master.xmind'

def make_topic(title, children=None, note=None, href=None, labels=None):
    t = {
        "id": os.urandom(8).hex(),
        "title": title
    }
    if note:
        t["notes"] = {"plain": {"content": note}}
    if href:
        t["href"] = href
    if labels:
        t["labels"] = labels
    if children:
        t["children"] = {"attached": children}
    return t

# 1. Competitive Intelligence
comp_children = [
    make_topic("Local Tricity Landscape", [
        make_topic("GoldenCares (goldencares.in)", [
            make_topic("Model: ₹499/hr on-demand college student visits", labels=["Hourly On-Demand"]),
            make_topic("Incubation: SLIET IIC; Early pilot (1 family served, 3 companions on platform)", labels=["Pilot Stage"]),
            make_topic("Fatal Vulnerabilities: Pay-per-hour disincentivizes regular use; travel paid in cash; student turnover breaks trust; zero nocturnal support", labels=["High Friction"])
        ], href="https://goldencares.in"),
        make_topic("Emoha Elder Care (Mohali Hub - Sector 70)", [
            make_topic("Model: 24/7 Emergency response + Medical concierge + Social engagement", labels=["Clinical"]),
            make_topic("Pricing: ₹2,500/mo (Essential) to ₹10,000/mo (Empower/Complete)", labels=["High Cost"]),
            make_topic("Vulnerability: Heavy clinical/hospital atmosphere; elders feel treated like patients; zero warm peer companionship", labels=["Defensive"])
        ], href="https://emoha.com"),
        make_topic("Samarth Eldercare (Chandigarh / Panchkula)", [
            make_topic("Model: Dedicated Care Managers acting as surrogate children for NRI parents", labels=["Concierge"]),
            make_topic("Pricing: ₹3,000 – ₹8,500/month (billed quarterly/annually)", labels=["Premium"]),
            make_topic("Vulnerability: Human-only bandwidth limits scaling; 16 nighttime hours completely uncovered", labels=["Nocturnal Gap"])
        ], href="https://samarth.community"),
        make_topic("Informal Domestic Maids / Ayahs (Price Anchor)", [
            make_topic("Cost: ₹3,500 – ₹5,500/month for daily 1-2 hours presence", labels=["Price Anchor"]),
            make_topic("Family Psychology: Children mentally anchor eldercare costs against domestic maids", labels=["Consumer Bias"]),
            make_topic("Our Moat: Unbundle manual labor from intellectual stimulation, dignity, and biological vigilance", labels=["Differentiator"])
        ])
    ]),
    make_topic("Pan-India Benchmark: Goodfellows India", [
        make_topic("Model: 'Grandkids on Demand' (~₹5,000/month) founded by Shantanu Naidu, backed by late Ratan Tata", href="https://thegoodfellows.in"),
        make_topic("Scaling Bottleneck 1: Salaried Fixed Burn (Companions paid fixed ₹25k-35k wages, creating high payroll liabilities)", labels=["Fixed Burn"]),
        make_topic("Scaling Bottleneck 2: 3% Psychometric Filter (Extreme selection funnel chokes companion supply)", labels=["Supply Choke"]),
        make_topic("Scaling Bottleneck 3: Low Margins (1:5 companion ratio caps unit profitability)", labels=["Margin Cap"])
    ])
]

# 2. Clinical Research
clinical_children = [
    make_topic("Holt-Lunstad Meta-Analysis (3.4 Million Participants)", [
        make_topic("Citation: Holt-Lunstad et al. (2015). 'Loneliness and Social Isolation as Risk Factors for Mortality: A Meta-Analytic Review.' Perspectives on Psychological Science, 10(2):227–242.", href="https://journals.sagepub.com/doi/10.1177/1745691614568352"),
        make_topic("Core Finding: Social isolation increases mortality risk by 26% to 32%, equal to smoking 15 cigarettes/day", labels=["Mortality Proof"]),
        make_topic("Comparative Hazard: Greater mortality threat than clinical obesity, physical inactivity, or air pollution", labels=["Lethal Risk"])
    ]),
    make_topic("Harvard Study of Adult Development (85 Years)", [
        make_topic("Citation: Waldinger, R. J., & Schulz, M. S. (2023). 'The Good Life: Lessons from the World's Longest Scientific Study of Happiness.' Harvard Adult Development Study.", href="https://www.adultdevelopmentstudy.org/"),
        make_topic("Core Finding: Relationship warmth is the single strongest predictor of biological longevity, cardiovascular health, and cognitive retention past 75", labels=["Longevity"]),
        make_topic("Mechanism: Chronic loneliness triggers toxic sustained systemic inflammation (Interleukin-6 & C-reactive protein)", labels=["Inflammation"])
    ]),
    make_topic("Melatonin Collapse & The 3:00 AM Void", [
        make_topic("Citation: Karasek M. (2004). 'Melatonin, human aging, and age-related diseases.' Exp Gerontol. & Vural et al. (2014). Sleep Med Rev.", href="https://pubmed.ncbi.nlm.nih.gov/15582784/"),
        make_topic("Neurobiology: Pineal gland calcification reduces melatonin production by 70%–80% in older adults", labels=["Endocrine"]),
        make_topic("The Nocturnal Void: REM sleep fragmentation leads to involuntary waking at 2:00–5:00 AM", labels=["Circadian"]),
        make_topic("Rumination Paradox: In midnight stillness, psychological defenses collapse, triggering severe existential dread and acute mortality rumination", labels=["Crisis Point"]),
        make_topic("Our Solution: 24/7 sub-500ms Indic AI Voice Confidant on continuous nocturnal vigilance", labels=["AI Intervention"])
    ]),
    make_topic("Socioemotional Selectivity Theory (SST)", [
        make_topic("Citation: Carstensen, L. L. (1995, 2006). 'Socioemotional Selectivity Theory.' Stanford Center on Longevity, Current Directions in Psychological Science.", href="https://longevity.stanford.edu/"),
        make_topic("Psychological Principle: Aging amygdala prioritizes emotionally meaningful relationships over transactional contacts", labels=["Stanford Aging"]),
        make_topic("The Infantilization Trap: Treating elders like children triggers psychological rebellion; positioning youth as mentees seeking elder wisdom unlocks deep compliance", labels=["Dignity Anchor"])
    ]),
    make_topic("Auditory Load & Dementia Risk", [
        make_topic("Citation: Lin, F. R. et al. (2011, 2013). 'Hearing Loss and Incident Dementia.' JAMA Neurology, 68(2):214–220.", href="https://jamanetwork.com/journals/jamaneurology/fullarticle/802291"),
        make_topic("Finding: Mild to moderate age-related hearing loss multiplies dementia risk up to 5-fold due to cognitive overload and social withdrawal", labels=["Cognitive Load"]),
        make_topic("Our Tech: Ultra-clear Indic voice acoustic synthesis with customizable frequencies and speech cadence", labels=["Acoustic Tuning"])
    ]),
    make_topic("Longitudinal Ageing Study in India (LASI Wave 1)", [
        make_topic("Citation: Ministry of Health and Family Welfare, Govt. of India (2020). 'LASI Wave 1 National Report.' IIPS Mumbai.", href="https://www.iipsindia.ac.in/content/lasi-wave-i"),
        make_topic("Punjab Demographics: 12.6%+ population aged 60+; over 150,000 youths emigrate to Canada/UK annually", labels=["Brain Drain"]),
        make_topic("The 'Silent Kothi' Reality: Thousands of retired generals, judges, and civil servants in Sectors 8–11 living in 1-kanal villas with high capital wealth but absolute emotional abandonment", labels=["Tricity Reality"])
    ])
]

# 3. Global Precedents
global_children = [
    make_topic("USA: New York State Office for the Aging (NYSOFA)", [
        make_topic("Program: 800+ AI robotic companions (ElliQ) deployed across New York state elderly households", href="https://aging.ny.gov/news/nysofa-announces-preliminary-results-pilot-program-using-ai-companion-technology"),
        make_topic("Empirical Outcome: 95% of seniors reported statistically significant loneliness reduction; over 30 interactions per day", labels=["95% Success"]),
        make_topic("Key Finding: Proactive AI conversation (agent initiating dialogue based on circadian habits) drove 80%+ of engagement", labels=["Proactivity"])
    ]),
    make_topic("South Korea: Naver CLOVA CareCall", [
        make_topic("Program: HyperCLOVA conversational AI telephone calls across 20+ Korean municipalities (Seoul, Busan, Daegu)", href="https://clova.ai/carecall"),
        make_topic("Scale: Over 20,000 isolated seniors receiving bi-weekly AI voice health check-ins", labels=["20,000+ Scale"]),
        make_topic("Episodic Memory: Tracks previous conversations, meals, sleep, and emotional tone across months with 90% senior satisfaction", labels=["Long-Term Graph"]),
        make_topic("Triage Integration: Acoustic distress flags immediately dispatch municipal social welfare officers", labels=["Triage"])
    ]),
    make_topic("Japan: Silver Human Resources Centers (Koreisha)", [
        make_topic("Program: 700,000+ younger active retirees (ages 60–72) employed in community care for oldest-old seniors (80+)", href="https://www.sjc.ne.jp/"),
        make_topic("Sociological Success: Shared cultural vernacular, shared nostalgic references, and zero generational disconnect", labels=["Cultural Match"]),
        make_topic("Our Adaptation: Recruiting 45–55yo cultured community matriarchs (retired teachers, defense spouses) as Relationship Managers", labels=["RM Recruitment"])
    ]),
    make_topic("China: Beijing 'Virtual Senior Homes'", [
        make_topic("Program: Beijing & Shenzhen smart-radar infrastructure + AI voice box in public housing", labels=["Smart Radar"]),
        make_topic("Triage: 15-minute response radius by neighborhood triage workers", labels=["15-Min SLA"]),
        make_topic("Insight: Proves that high-density cluster pods lower emergency dispatch costs by 70%", labels=["Density Efficiency"])
    ])
]

# 4. The 4 Core System Pillars
pillars_children = [
    make_topic("Pillar I: 24/7 AI Voice Confidant ('Sarthi AI')", [
        make_topic("Indic Conversational Engine: Sub-500ms glass-to-glass latency in Punjabi, Hindi, and English code-switching", labels=["Sub-500ms"]),
        make_topic("Episodic Senior Graph Memory: Vector DB preserving childhood memoirs, family lineage, grandchild exam dates, favorite Gurbani shabads", labels=["Long-Term Memory"]),
        make_topic("Night-Owl Vigilance Mode: Autonomous 3:00 AM check-in when senior's circadian pattern shows waking or distress", labels=["3 AM Void"]),
        make_topic("Acoustic Biomarker Radar: Speech signal processing extracting jitter, shimmer, formant dispersion, and pause elongation to detect early cognitive decline & depression", labels=["Biomarkers"])
    ]),
    make_topic("Pillar II: Dedicated Relationship Manager (RM)", [
        make_topic("Recruitment Persona: Cultured 45–55yo community matriarchs (retired teachers, military spouses, bank managers)", labels=["Trust Anchor"]),
        make_topic("Capacity & Cadence: 1 RM oversees 30 seniors; conducts bi-weekly 45-minute in-person tea visits", labels=["1:30 Ratio"]),
        make_topic("Weekly NRI Video Reel: AI auto-edits a 90-second Sunday WhatsApp video digest showing senior smiling, activities, vitals, and highlights", labels=["NRI Delight"]),
        make_topic("Role: Trust gatekeeper, family advisor, and escalation point for medical anomalies", labels=["Gatekeeper"])
    ]),
    make_topic("Pillar III: Dynamic Gig & Medical Network", [
        make_topic("Unbundled Gig Companions: University students dispatched strictly for outdoor tasks (walks, Sukhna lake, tech assistance)", labels=["Outdoor Only"]),
        make_topic("Anti-Leakage Moat: Students never handle household health administration or private cash; paid digitally per verified task", labels=["Anti-Disintermediation"]),
        make_topic("Integrated Medical Concierge: On-demand phlebotomists (Dr. Lal PathLabs, SRL Diagnostics) and certified home nursing bureaus on API trigger", labels=["Medical APIs"])
    ]),
    make_topic("Pillar IV: 'The Golden Club' Thematic Social Pods", [
        make_topic("Micro-Cluster Architecture: 10–15 seniors grouped per 3km neighborhood pod", labels=["Hyperlocal"]),
        make_topic("Circle 1: Gurbani & Satsang Circle (Spiritual connection, hymn sharing, temple visits)", labels=["Spiritual"]),
        make_topic("Circle 2: 'Silver Talks' Oral Memoirs (AI records senior life stories, transcribed and printed into hardbound legacy books for grandchildren)", labels=["Legacy"]),
        make_topic("Circle 3: Games & Mind Gym (Tambola, chess, bridge, memory stimulation)", labels=["Cognitive"]),
        make_topic("Circle 4: Nature & Movement (Morning walks at Sukhna Lake, Sector 10 Rose Garden)", labels=["Physical"])
    ])
]

# 5. Dynamic Branching Pathways
branching_children = [
    make_topic("Branch 1: In-Home Frail Track", [
        make_topic("Clinical Trigger: Mobility score < 4, post-operative, or wheelchair-bound", labels=["Trigger"]),
        make_topic("Service Delivery: Daily AI voice check-in (15 min morning/night) + weekly RM visit + partner nurse home visits", labels=["Protocol"]),
        make_topic("Pricing: ₹3,499 / month", labels=["Pricing"]),
        make_topic("Outcome: 100% medication compliance, zero bed sores, elimination of daytime isolation", labels=["Output"])
    ]),
    make_topic("Branch 2: Active Social Club Track", [
        make_topic("Clinical Trigger: High mobility, cognitively sharp, living in an empty villa", labels=["Trigger"]),
        make_topic("Service Delivery: Weekly Golden Club meetups, memoir recording, community mentorship roles", labels=["Protocol"]),
        make_topic("Pricing: ₹2,499 / month", labels=["Pricing"]),
        make_topic("Outcome: Shift from passive aging to active community elder with high self-esteem", labels=["Output"])
    ]),
    make_topic("Branch 3: High-Acuity Medical Track", [
        make_topic("Clinical Trigger: Chronic COPD, congestive heart failure, Parkinson's, post-stroke", labels=["Trigger"]),
        make_topic("Service Delivery: Daily acoustic biometric surveillance + weekly SRL blood sample collection + direct Fortis/Max Mohali tele-triage", labels=["Protocol"]),
        make_topic("Pricing: ₹6,999 / month", labels=["Pricing"]),
        make_topic("Outcome: 40% reduction in emergency room admissions through early biomarker detection", labels=["Output"])
    ]),
    make_topic("Branch 4: Global Guardian NRI Track", [
        make_topic("Family Trigger: Adult children residing in Canada, USA, UK, or UAE with chronic guilt/worry", labels=["Trigger"]),
        make_topic("Service Delivery: 24/7 child portal, automated Sunday WhatsApp video reels, proactive RM crisis liaison", labels=["Protocol"]),
        make_topic("Pricing: $79 USD (~₹6,500) / month via Stripe auto-debit", labels=["Pricing"]),
        make_topic("Outcome: Complete peace of mind for diaspora children; 98% annual customer retention", labels=["Output"])
    ]),
    make_topic("Branch 5: Acute Bereavement Track", [
        make_topic("Clinical Trigger: Loss of spouse within the preceding 6 months (peak depression/mortality hazard window)", labels=["Trigger"]),
        make_topic("Service Delivery: Nightly 3:00 AM AI voice soothing, daily gentle RM phone touchpoint, gradual transition to bereavement storytelling", labels=["Protocol"]),
        make_topic("Outcome: De-escalation of acute suicide/depression ideation during the critical 180-day window", labels=["Output"])
    ])
]

# 6. Technical Architecture
tech_children = [
    make_topic("Sub-500ms Indic Voice Stack", [
        make_topic("VAD Layer: Silero VAD (Voice Activity Detection, 20ms frame evaluation)", labels=["VAD"]),
        make_topic("ASR Layer: Groq Whisper-Large-v3 (150ms transcription latency with Punjabi code-switching)", labels=["ASR"]),
        make_topic("Intelligence Layer: Llama-3.3-70B on Groq / Gemini 1.5 Flash (sub-200ms TTFT)", labels=["LLM"]),
        make_topic("TTS Layer: Sarvam AI / Bhashini / ElevenLabs streaming audio buffer chunks (150ms)", labels=["TTS"]),
        make_topic("Glass-to-Glass Total Latency: 480ms (achieving human-like conversational fluidity and natural interruption handling)", labels=["480ms SLA"])
    ]),
    make_topic("Scale-to-Zero Serverless Infrastructure", [
        make_topic("Compute: Google Cloud Run microservices scaling down to 0 instances during idle hours (₹0 fixed server burn)", labels=["Scale-to-Zero"]),
        make_topic("Database: Supabase PostgreSQL with PGVector + Row Level Security for senior medical telemetry", labels=["Database"]),
        make_topic("Marginal Cost per Senior: ₹70 – ₹120 / month for 60 minutes of daily voice AI interactions", labels=["Unit Cost"])
    ]),
    make_topic("Acoustic Biomarker Surveillance", [
        make_topic("Features: Real-time feature extraction of jitter, shimmer, harmonic-to-noise ratio, speech rate, and pause duration", labels=["DSP"]),
        make_topic("Clinical Thresholds: 2-sigma deviation from baseline triggers automated push notification to Relationship Manager dashboard", labels=["Telemetry"])
    ])
]

# 7. Unit Economics & Financial Projections
fin_children = [
    make_topic("Subscription Tier Economics", [
        make_topic("Tier 1 (Digital Voice Angel): ₹599/mo (AI Voice Confidant + 3 AM Vigilance) | 78% Gross Margin", labels=["₹599"]),
        make_topic("Tier 2 (Core Hybrid Companion): ₹2,499/mo (AI + Bi-weekly RM Visits + The Golden Club) | 63.2% Gross Margin", labels=["₹2,499"]),
        make_topic("Tier 3 (Global Guardian NRI): $79 USD (~₹6,500/mo) (AI + RM + Sunday Video Reel + Lab Concierge) | 71.5% Gross Margin", labels=["$79 USD"]),
        make_topic("Add-On Gigs: ₹299 per task (₹210 to student gig worker, ₹89 platform margin)", labels=["Marketplace"])
    ]),
    make_topic("Monthly Unit Economics (Tier 2 @ ₹2,499)", [
        make_topic("Revenue per Senior: ₹2,499", labels=["Revenue"]),
        make_topic("Relationship Manager Allocation: ₹600 (RM paid ₹18,000/mo for 30 seniors)", labels=["RM Cost"]),
        make_topic("AI Voice & Telephony APIs: ₹120 (60 mins daily usage)", labels=["Tech Cost"]),
        make_topic("Thematic Club Venue & Tea: ₹200 (₹50/week at local community hall)", labels=["Club Cost"]),
        make_topic("Total COGS: ₹920 | Gross Profit: ₹1,579 per senior per month (63.2% Gross Margin)", labels=["63.2% Margin"])
    ]),
    make_topic("Micro-Hub Breakeven Dynamics", [
        make_topic("Fixed Hub Overhead: ₹30,000 / month (Local supervisor, marketing, contingency)", labels=["Overhead"]),
        make_topic("Contribution Margin per Senior: ₹1,579 / month", labels=["Margin"]),
        make_topic("Breakeven Senior Count: Exactly 19–20 seniors per neighborhood cluster", labels=["Breakeven: 19"]),
        make_topic("Target Capacity: 100 seniors per hub yields ₹1.27 Lakh monthly net operating profit", labels=["Hub Profit"])
    ]),
    make_topic("3-Year Pan-India Financial Trajectory", [
        make_topic("Year 1 (Tricity Pilot - 3 Hubs): 300 Active Seniors | ₹90 Lakh ARR | EBITDA Positive", labels=["Year 1: ₹90L"]),
        make_topic("Year 2 (Punjab & Haryana - 12 Hubs): 1,500 Active Seniors | ₹4.8 Crore ARR | ₹1.8 Crore EBITDA", labels=["Year 2: ₹4.8Cr"]),
        make_topic("Year 3 (Pan-India Metro - 40 Hubs): 6,000 Active Seniors | ₹20.5 Crore ARR | 38% Net Profit Margin", labels=["Year 3: ₹20.5Cr"])
    ])
]

# 8. 90-Day Execution Plan
gtm_children = [
    make_topic("Phase 1: Zero-Burn Foundation (Days 1–30)", [
        make_topic("Deploy Sarthi AI on Cloud Run; connect to WhatsApp Cloud API gateway", labels=["Tech"]),
        make_topic("Recruit 2 Cultured Relationship Managers (retired defense spouses in Mohali Phase 7 & Sector 34)", labels=["Hiring"]),
        make_topic("Sign community hall partnership with Sector 8 & 9 Resident Welfare Associations (RWAs)", labels=["Partnerships"]),
        make_topic("Onboard first 15 pilot families with 14-day zero-risk trial", labels=["Milestone: 15"])
    ]),
    make_topic("Phase 2: Hyperlocal Distribution Flywheel (Days 31–60)", [
        make_topic("Host weekly 'Silver Wellbeing Mornings' (free blood pressure, blood sugar & cognitive checks)", labels=["RWA Activations"]),
        make_topic("Gurdwara & Temple morning announcements celebrating 'Grandchild Seva'", labels=["Community Trust"]),
        make_topic("Digital Geo-targeted Social Ads in Brampton, Surrey, & London targeting Punjabi NRI children", labels=["NRI CAC"]),
        make_topic("Reach 100 paid active subscribers across Chandigarh and Mohali", labels=["Milestone: 100"])
    ]),
    make_topic("Phase 3: Institutional Moat & Expansion (Days 61–90)", [
        make_topic("Establish discharge desk partnerships with Fortis Mohali & Max Hospital Geriatric Departments", labels=["Hospitals"]),
        make_topic("Deploy automated 'Sunday 90-Second WhatsApp Reel' for NRI family delight", labels=["Retention"]),
        make_topic("Launch weekly 'The Golden Club' Satsang and nature walks at Sukhna Lake", labels=["Club Launch"]),
        make_topic("Achieve 300 active subscribers; expand to Panchkula hub; prepare institutional Seed Round", labels=["Milestone: 300"])
    ])
]

root_topic = make_topic("Autonomous Hybrid Eldercare Operating System (Master Research & Execution Blueprint)", [
    make_topic("1. Competitive Intelligence & Market Gap", comp_children, labels=["Market"]),
    make_topic("2. Clinical, Biological & Nocturnal Loneliness Research", clinical_children, labels=["Science"]),
    make_topic("3. Global Precedents & State-Sponsored AI Eldercare", global_children, labels=["Global Precedents"]),
    make_topic("4. The 4 Core Platform Pillars", pillars_children, labels=["Architecture"]),
    make_topic("5. 5 Dynamic Branching Pathways & Clinical Decision Trees", branching_children, labels=["Branching"]),
    make_topic("6. Technical Architecture & Scale-to-Zero Cloud Infrastructure", tech_children, labels=["Tech Stack"]),
    make_topic("7. Financial Model, Unit Economics & 3-Year Projections", fin_children, labels=["Financials"]),
    make_topic("8. 90-Day Hyperlocal Go-to-Market Execution Plan", gtm_children, labels=["GTM Blueprint"])
])

content_json = [{
    "id": "master-sheet-1",
    "title": "Autonomous Eldercare Master OS",
    "rootTopic": root_topic,
    "theme": {
        "id": "modern-dark",
        "palette": ["#EF4444", "#F59E0B", "#10B981", "#06B6D4", "#6366F1", "#EC4899"]
    }
}]

metadata_json = {
    "creator": {"name": "Antigravity Research Engine", "version": "2.0"},
    "created": 1727310000000
}

manifest_json = {
    "file-entries": {
        "content.json": {},
        "metadata.json": {}
    }
}

with zipfile.ZipFile(xmind_file, 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr('content.json', json.dumps(content_json, indent=2))
    z.writestr('metadata.json', json.dumps(metadata_json, indent=2))
    z.writestr('manifest.json', json.dumps(manifest_json, indent=2))

print(f"Master Xmind archive built successfully at {xmind_file} (Size: {os.path.getsize(xmind_file)} bytes)")

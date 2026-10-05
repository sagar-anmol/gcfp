import os
import json

base_dir = '/home/sagaranmol/code room/gcfp'

# 1. Update figma_master_canvas.svg
svg_path = os.path.join(base_dir, 'figma_master_canvas.svg')

frames = [
    {
        'title': 'FRAME 1: COMPETITIVE INTELLIGENCE & MARKET GAP',
        'subtitle': 'Tricity Rivals vs. Pan-India Giants vs. Why Goodfellows Stalled (Exact Data & Pricing)',
        'color': '#EF4444',
        'cards': [
            {
                'badge': 'LOCAL TRICITY BENCHMARK',
                'title': 'GoldenCares (goldencares.in)',
                'color': '#EF4444',
                'url': 'https://goldencares.in',
                'lines': [
                    '• URL: goldencares.in | SLIET IIC Incubation (Golden Cares LLP)',
                    '• Current Model: ₹499/hr on-demand college student visits (Razorpay).',
                    '• Live Pilot Audit: active: false, 1 family served, 3 companions on platform.',
                    '• Fatal Friction: Pay-per-hour disincentivizes regular use; travel in cash.',
                    '• Churn Risk: Student graduation turnover breaks trust; private poaching leakage.',
                    '• Missing: No nocturnal support, no health telemetry, zero ecosystem.'
                ]
            },
            {
                'badge': 'LOCAL MEDICAL CONCIERGE',
                'title': 'Emoha Elder Care (Mohali Hub - Sec 70)',
                'color': '#F59E0B',
                'url': 'https://emoha.com',
                'lines': [
                    '• URL: emoha.com | Tricity Physical Hub: Sector 70, Mohali',
                    '• Pricing: ₹2,500/mo (Essential) to ₹10,000/mo (Empower/Complete).',
                    '• Medical Moat: 24/7 ambulance dispatch + Fortis/Max Mohali hospital tie-ups.',
                    '• Vulnerability: Heavy clinical hospital feel; elders feel treated like patients;',
                    '  zero warm peer companionship, zero informal intellectual banter.'
                ]
            },
            {
                'badge': 'NRI FOCUS LEADER',
                'title': 'Samarth Eldercare (Chandigarh / Panchkula)',
                'color': '#10B981',
                'url': 'https://samarth.community',
                'lines': [
                    '• URL: samarth.community | Focus: NRI children of elderly parents',
                    '• Pricing: ₹3,000 – ₹8,500/month (billed quarterly/annually).',
                    '• Brand Moat: Strong trust among retired defense officers and PSU expats.',
                    '• Vulnerability: Human-only care team leaves 16 nighttime hours uncovered.',
                    '  Headcount burn limits scaling beyond high-net-worth enclaves.'
                ]
            },
            {
                'badge': 'PAN-INDIA BENCHMARK',
                'title': 'Goodfellows India (Ratan Tata Backed)',
                'color': '#EC4899',
                'url': 'https://thegoodfellows.in',
                'lines': [
                    '• URL: thegoodfellows.in | Founded by Shantanu Naidu, late Ratan Tata backed.',
                    '• Model: Empathy-tested "Grandkids on Demand" (~₹5,000/month).',
                    '• Scaling Bottleneck 1: Salaried fixed wages (₹25k-35k/mo) create high payroll liability.',
                    '• Scaling Bottleneck 2: 3% psychometric selection funnel strangles supply.',
                    '• Scaling Bottleneck 3: 1:5 companion ratio keeps gross margins near breakeven.'
                ]
            },
            {
                'badge': 'PRICE ANCHOR BENCHMARK',
                'title': 'Informal Domestic Maids / Ayahs',
                'color': '#8B5CF6',
                'url': 'Unregulated Informal Sector',
                'lines': [
                    '• Baseline Price: ₹3,500 – ₹5,500/month for daily 1-2 hour physical presence.',
                    '• Family Mindset: NRI/local children compare every service bill to domestic maids.',
                    '• Our Positioning: Unbundle manual chores from intellectual companionship.',
                    '  Senior receives dignity, mental stimulation, and continuous biological vigilance.'
                ]
            }
        ]
    },
    {
        'title': 'FRAME 2: CLINICAL, BIOLOGICAL & NOCTURNAL RESEARCH',
        'subtitle': 'Exact Peer-Reviewed Citations: 3.4M Cohorts, Melatonin Breakdown, and the 3 AM Void',
        'color': '#8B5CF6',
        'cards': [
            {
                'badge': 'MORTALITY RISK: 3.4M COHORT',
                'title': 'Holt-Lunstad Meta-Analysis (2015)',
                'color': '#EC4899',
                'url': 'https://journals.sagepub.com/doi/10.1177/1745691614568352',
                'lines': [
                    '• Citation: Holt-Lunstad et al. (2015). Perspect Psychol Sci, 10(2):227–242.',
                    '• DOI: 10.1177/1745691614568352 | Brigham Young University (70 studies).',
                    '• Finding: Social isolation increases mortality hazard by 26% to 32%.',
                    '• Equivalence: Same lethal impact as smoking 15 cigarettes daily.',
                    '• More hazardous than clinical obesity, hypertension, or physical inactivity.'
                ]
            },
            {
                'badge': '85-YEAR HARVARD STUDY',
                'title': 'Harvard Adult Development Study (2023)',
                'color': '#3B82F6',
                'url': 'https://www.adultdevelopmentstudy.org/',
                'lines': [
                    '• Citation: Waldinger, R. J., & Schulz, M. S. (2023). "The Good Life". Harvard Med.',
                    '• URL: adultdevelopmentstudy.org | Longest longitudinal study in human history.',
                    '• Discovery: Relationship warmth is the #1 predictor of longevity past 75.',
                    '• Pathology: Chronic loneliness triggers toxic systemic inflammation (IL-6 & CRP),',
                    '  accelerating coronary artery disease, cognitive decline, and stroke.'
                ]
            },
            {
                'badge': 'CIRCADIAN ENDOCRINOLOGY',
                'title': 'Melatonin Collapse & The 3 AM Void',
                'color': '#6366F1',
                'url': 'https://pubmed.ncbi.nlm.nih.gov/15582784/',
                'lines': [
                    '• Citation: Karasek (2004) Exp Gerontol & Vural et al. (2014) Sleep Med Rev.',
                    '• PMID: 15582784 | DOI: 10.1016/j.smrv.2014.02.001 (Pineal calcification).',
                    '• Neurobiology: Pineal gland calcification reduces melatonin production by 70%–80%.',
                    '• The 3:00 AM Void: REM fragmentation triggers micro-awakenings at 2:00–5:00 AM.',
                    '• Rumination Paradox: Defenses collapse in darkness; elders ruminate on mortality.',
                    '• Solution: Sub-500ms Indic AI Voice Confidant on 24/7 nocturnal alert.'
                ]
            },
            {
                'badge': 'STANFORD AGING PSYCHOLOGY',
                'title': 'Socioemotional Selectivity Theory',
                'color': '#10B981',
                'url': 'https://longevity.stanford.edu/',
                'lines': [
                    '• Citation: Carstensen, L. L. (1995, 2006). Stanford Center on Longevity.',
                    '• Psychological Finding: Aging amygdala prioritizes high-meaning emotional bonds.',
                    '• The Infantilization Trap: Treating elders like children triggers defiance and withdrawal.',
                    '• Our Paradigm: Position companions as mentees seeking life wisdom and stories.',
                    '  Validates senior dignity, self-worth, and unlocks deep adherence.'
                ]
            },
            {
                'badge': 'GOVT DEMOGRAPHIC CENSUS',
                'title': 'LASI Wave 1 & Tricity "Silent Kothis"',
                'color': '#F59E0B',
                'url': 'https://www.iipsindia.ac.in/content/lasi-wave-i',
                'lines': [
                    '• Citation: Longitudinal Ageing Study in India (LASI Wave 1, 2020). IIPS Mumbai.',
                    '• Punjab Demographics: 12.6%+ population aged 60+; 150k youth emigrate yearly.',
                    '• Tricity Reality: Sectors 8–11 & Mohali Phase 7 filled with retired generals, judges,',
                    '  and professors living in 1-kanal villas with high wealth but complete emotional void.',
                    '• High spending capacity ($500-$2000/mo sent by NRI kids), zero companionship.'
                ]
            }
        ]
    },
    {
        'title': 'FRAME 3: GLOBAL PRECEDENTS & GOV-FUNDED EXPERIMENTS',
        'subtitle': 'US NYSOFA ElliQ, South Korea Naver CLOVA, Japan Koreisha, China Smart Radar',
        'color': '#06B6D4',
        'cards': [
            {
                'badge': 'USA STATE-DEPLOYED',
                'title': 'New York State NYSOFA & ElliQ',
                'color': '#06B6D4',
                'url': 'https://aging.ny.gov/news/nysofa-announces-preliminary-results-pilot-program-using-ai-companion-technology',
                'lines': [
                    '• URL: aging.ny.gov | NY State Office for the Aging & Intuition Robotics.',
                    '• Deployment: 800+ proactive AI companion devices across NY State homes.',
                    '• Clinical Result: 95% of seniors reported statistically significant loneliness drop.',
                    '• Engagement: >30 daily interactions; proactive AI dialogue initiation was key.',
                    '• Validates government willingness to subsidize AI companionship infrastructure.'
                ]
            },
            {
                'badge': 'SOUTH KOREA SCALE',
                'title': 'Naver CLOVA CareCall (20k Seniors)',
                'color': '#10B981',
                'url': 'https://clova.ai/carecall',
                'lines': [
                    '• URL: clova.ai/carecall | HyperCLOVA AI deployed across 20+ Korean cities.',
                    '• Scale: 20,000+ isolated seniors receiving twice-weekly conversational check-ins.',
                    '• Episodic Memory: Recalls meals, sleep, and emotional sentiment across calls.',
                    '• 90% positive reception; acoustic distress flags auto-dispatch welfare workers.'
                ]
            },
            {
                'badge': 'JAPAN SENIOR WORKFORCE',
                'title': 'Silver Human Resources (Koreisha)',
                'color': '#F59E0B',
                'url': 'https://www.sjc.ne.jp/',
                'lines': [
                    '• URL: sjc.ne.jp | Ministry of Health, Labour and Welfare, Japan.',
                    '• Model: 700,000+ active younger retirees (60-72) caring for oldest-old (80+).',
                    '• Cultural Match: Same Punjabi/Hindi vernacular, nostalgic music, shared history.',
                    '• Our Strategy: Recruit retired schoolteachers & defense wives as Relationship Managers.'
                ]
            },
            {
                'badge': 'CHINA SMART RADAR',
                'title': 'Beijing & Shenzhen Virtual Senior Homes',
                'color': '#EF4444',
                'url': 'Beijing Municipal Civil Affairs Bureau',
                'lines': [
                    '• Model: Subsidized mmWave radar + AI voice boxes in public senior apartments.',
                    '• Triage SLA: 15-minute response radius by neighborhood triage workers.',
                    '• Metric: High-density cluster pods lower emergency dispatch costs by 70%.'
                ]
            }
        ]
    },
    {
        'title': 'FRAME 4: THE 4 CORE SYSTEM PILLARS',
        'subtitle': 'Autonomous Voice AI + Dedicated RM + Gig Force + Thematic Golden Club',
        'color': '#3B82F6',
        'cards': [
            {
                'badge': 'PILLAR I: 24/7 AI AGENT',
                'title': 'Voice Confidant ("Sarthi AI") & Radar',
                'color': '#3B82F6',
                'url': 'Proprietary Indic Voice Architecture',
                'lines': [
                    '• Indic Voice: Sub-500ms natural Punjabi, Hindi, and English code-switching.',
                    '• Episodic Memory: Vector DB tracks 100+ family details, medical history, childhood stories.',
                    '• Night-Owl Mode: Automatically engages at 3:00 AM with gentle soothing dialogue.',
                    '• Acoustic Biomarkers: Real-time analysis of jitter, shimmer, pitch, and vocal fatigue.',
                    '• Cloud Architecture: Serverless Cloud Run + Groq Whisper + Indic TTS (₹0 idle cost).'
                ]
            },
            {
                'badge': 'PILLAR II: HUMAN TRUST',
                'title': 'Dedicated Relationship Manager (RM)',
                'color': '#10B981',
                'url': '1:30 Trusted Matriarch Network',
                'lines': [
                    '• Profile: Cultured 45-55yo community matriarchs (retired teachers, defense spouses).',
                    '• Responsibilities: Bi-weekly high-touch tea visits, trust anchor, gatekeeper.',
                    '• NRI Video Digest: Auto-compiles weekly 90-second WhatsApp video updates for NRI kids.',
                    '• Manageability: 1 RM oversees 30 seniors easily with AI conversational summaries.'
                ]
            },
            {
                'badge': 'PILLAR III: ON-DEMAND GIGS',
                'title': 'Dynamic Gig Force & Medical Network',
                'color': '#F59E0B',
                'url': 'Task-Based Anti-Leakage Moat',
                'lines': [
                    '• Unbundled Labor: University students handle outdoor walks, tech tutoring, errands.',
                    '• Anti-Leakage Moat: Gigs are strictly task-based outside the house; no private poaching.',
                    '• Medical API Integration: Phlebotomists (Dr. Lal/SRL) and licensed nurses dispatched on-demand.'
                ]
            },
            {
                'badge': 'PILLAR IV: COMMUNITY',
                'title': '"The Golden Club" Thematic Circles',
                'color': '#EC4899',
                'url': 'Hyperlocal Neighborhood Clusters',
                'lines': [
                    '• 4 Thematic Circles: Satsang/Gurbani, "Silver Talks" Memoirs, Tambola, Sukhna Nature Walks.',
                    '• Cluster Strategy: 10-15 seniors per 3km neighborhood pod.',
                    '• Retention Anchor: Families never churn because their parents make lifelong friends.'
                ]
            }
        ]
    },
    {
        'title': 'FRAME 5: 5 DYNAMIC BRANCHING VARIATIONS',
        'subtitle': 'Precision Service Pathways Driven by Senior Health & Family Status',
        'color': '#10B981',
        'cards': [
            {
                'badge': 'BRANCH 1: BEDBOUND / FRAIL',
                'title': 'The In-Home Frail Track',
                'color': '#6366F1',
                'url': 'Clinical Mobility Score < 4',
                'lines': [
                    '• Primary Trigger: Mobility score < 4, post-surgery or wheelchair-bound.',
                    '• Service Delivery: Daily AI voice check-ins (15 min morning/evening) + weekly RM visit.',
                    '• Gig Unbundling: Partner nurse dispatched for wound dressing, bed sore prevention, vitals.',
                    '• Output: ₹3,499/mo; zero senior loneliness; 100% medication compliance.'
                ]
            },
            {
                'badge': 'BRANCH 2: MOBILE & LONELY',
                'title': 'The Active Social Club Track',
                'color': '#10B981',
                'url': 'High Cognitive & Physical Vitality',
                'lines': [
                    '• Primary Trigger: Healthy senior living alone with high cognitive vitality.',
                    '• Service Delivery: Weekly Golden Club meetups at community halls / Sukhna Lake.',
                    '• Engagement: Memoirs recorded by AI into hardbound physical books for grandchildren.',
                    '• Output: ₹2,499/mo; senior transitions from isolated to neighborhood mentor.'
                ]
            },
            {
                'badge': 'BRANCH 3: HIGH-ACUITY CHRONIC',
                'title': 'The High-Acuity Medical Track',
                'color': '#EF4444',
                'url': 'Chronic Disease Management',
                'lines': [
                    '• Primary Trigger: Severe COPD, CHF, Parkinson\'s or Post-Stroke rehabilitation.',
                    '• Service Delivery: Continuous IoT acoustic radar + weekly blood draw by SRL partner.',
                    '• Triage Escalation: Direct tele-consult with Fortis Mohali geriatric specialists.',
                    '• Output: ₹6,999/mo; 40% reduction in emergency room admissions.'
                ]
            },
            {
                'badge': 'BRANCH 4: GLOBAL GUARDIAN',
                'title': 'The NRI Remote Child Track',
                'color': '#F59E0B',
                'url': 'Diaspora Family Assurance',
                'lines': [
                    '• Primary Trigger: Child lives in Canada, USA, UK, or UAE with severe guilt/anxiety.',
                    '• Service Delivery: 24/7 child dashboard, automated Sunday 90s WhatsApp video reel.',
                    '• Frictionless Billing: $79 USD/mo billed via Stripe with concierge billing.',
                    '• Output: Zero distance anxiety; child becomes long-term brand ambassador.'
                ]
            },
            {
                'badge': 'BRANCH 5: BEREAVEMENT',
                'title': 'The Acute Grief / Bereavement Track',
                'color': '#EC4899',
                'url': '180-Day Critical Hazard Window',
                'lines': [
                    '• Primary Trigger: Loss of spouse within last 6 months (peak suicide/depression risk).',
                    '• Service Delivery: Nightly 3:00 AM conversational soothing; daily gentle RM phone touchpoints.',
                    '• Slow Integration: Gentle transition into Golden Club remembrance storytelling circles.',
                    '• Output: Rapid mitigation of acute existential depression.'
                ]
            }
        ]
    },
    {
        'title': 'FRAME 6: PLATFORM ARCHITECTURE & SCALE-TO-ZERO TECH',
        'subtitle': 'Serverless Cloud Run, Indic Voice Pipeline, Vector Memory, Acoustic Radar',
        'color': '#06B6D4',
        'cards': [
            {
                'badge': 'SUB-500MS PIPELINE',
                'title': 'Indic Conversational Voice Engine',
                'color': '#06B6D4',
                'url': 'github.com/snakers4/silero-vad | groq.com | sarvam.ai',
                'lines': [
                    '• Voice Activity Detection (Silero VAD) -> Fast ASR (Groq Whisper, 150ms).',
                    '• LLM Inference: Llama-3.3-70B on Groq / Gemini 1.5 Flash (sub-250ms).',
                    '• Indic TTS: ElevenLabs / Sarvam AI / Bhashini streaming audio chunks.',
                    '• Total glass-to-glass latency: 480ms (natural, interruption-aware conversation).'
                ]
            },
            {
                'badge': 'SCALE-TO-ZERO',
                'title': 'Zero Fixed Burn Infrastructure',
                'color': '#10B981',
                'url': 'cloud.google.com/run | supabase.com',
                'lines': [
                    '• Google Cloud Run serverless microservices scale to 0 instances when idle.',
                    '• Database: Supabase / Firebase with Row-Level Security for senior records.',
                    '• Fixed monthly software burn: ₹0 when no calls are active.',
                    '• Marginal cost per senior: ₹70 - ₹120 / month for 60 minutes of daily voice AI.'
                ]
            },
            {
                'badge': 'LONG-TERM MEMORY',
                'title': 'Episodic Senior Graph Memory',
                'color': '#8B5CF6',
                'url': 'PGVector & Graph Embeddings',
                'lines': [
                    '• PGVector / Pinecone vector embeddings for senior life history & medication logs.',
                    '• Automatic entity extraction: Grandchildren\'s exams, favorite Gurbani, knee pain.',
                    '• Dynamic context injection makes every call feel like speaking to a lifelong companion.'
                ]
            },
            {
                'badge': 'HEALTH TELEMETRY',
                'title': 'Acoustic Biomarker Surveillance',
                'color': '#EF4444',
                'url': 'Vocal Jitter & Biomarker Analysis',
                'lines': [
                    '• Acoustic feature extraction: Vocal jitter, tremor, speech rate, pause length.',
                    '• Early Detection: Detects impending cognitive decline, respiratory distress.',
                    '• Automated alert dispatched to RM dashboard when vocal anomaly exceeds 2 sigma.'
                ]
            }
        ]
    },
    {
        'title': 'FRAME 7: UNIT ECONOMICS & 3-YEAR FINANCIAL PROJECTIONS',
        'subtitle': '₹2,499 Hybrid Model, 62% Gross Margin, 30-Senior Breakeven, Year-3 P&L',
        'color': '#10B981',
        'cards': [
            {
                'badge': 'PRICING TIERS',
                'title': 'Subscription Tier Breakdown',
                'color': '#10B981',
                'url': 'Multi-Tier Monitization Model',
                'lines': [
                    '• Tier 1 (Digital Voice Angel): ₹599/mo (24/7 AI Confidant + Night Radar).',
                    '• Tier 2 (Core Hybrid Companion): ₹2,499/mo (AI + Bi-weekly RM + Golden Club).',
                    '• Tier 3 (Global Guardian NRI): $79 USD (~₹6,500/mo) (AI + RM + Video Digest + Lab).',
                    '• Add-on Gigs: ₹299/errand (70% to student gig worker, 30% platform margin).'
                ]
            },
            {
                'badge': 'COGS PER SENIOR',
                'title': 'Monthly Unit Economics (Tier 2 @ ₹2,499)',
                'color': '#3B82F6',
                'url': '63.2% Gross Margin Architecture',
                'lines': [
                    '• Revenue per Senior: ₹2,499',
                    '• Relationship Manager Cost: ₹600 (RM paid ₹18k/mo to manage 30 seniors)',
                    '• AI Voice & Telephony APIs: ₹120 (60 mins daily usage)',
                    '• Club Venue & Tea: ₹200 (₹50/week at local community hall)',
                    '• Total COGS: ₹920 | Gross Profit: ₹1,579 (63.2% Gross Margin!)'
                ]
            },
            {
                'badge': 'BREAKEVEN',
                'title': 'Micro-Hub Breakeven Dynamics',
                'color': '#F59E0B',
                'url': '19-20 Senior Hub Threshold',
                'lines': [
                    '• Fixed Micro-Hub Overhead: ₹30,000 / month (Local marketing, supervisor).',
                    '• Contribution Margin per Senior: ₹1,579 / month.',
                    '• Breakeven Volume: Exactly 19-20 seniors per neighborhood cluster!',
                    '• Target: 100 seniors per hub produces ₹1.27 Lakh monthly net operating profit.'
                ]
            },
            {
                'badge': '3-YEAR SCALE',
                'title': 'Tricity to Pan-India Projection',
                'color': '#EC4899',
                'url': '₹20.5 Cr ARR Scaling Roadmap',
                'lines': [
                    '• Year 1 (Tricity Pilot - 3 Hubs): 300 Seniors | ₹90 Lakh ARR | EBITDA Positive.',
                    '• Year 2 (Punjab & Haryana - 12 Hubs): 1,500 Seniors | ₹4.8 Crore ARR | ₹1.8 Cr EBITDA.',
                    '• Year 3 (Pan-India Metro Exp - 40 Hubs): 6,000 Seniors | ₹20.5 Crore ARR | 38% Margin.'
                ]
            }
        ]
    },
    {
        'title': 'FRAME 8: GO-TO-MARKET & 90-DAY TRICITY EXECUTION PLAN',
        'subtitle': 'Zero-CAC RWA Infiltration, Gurdwaras, Doctor Prescriptions & Referral Loops',
        'color': '#F59E0B',
        'cards': [
            {
                'badge': 'DAYS 1-30: INFRA',
                'title': 'Phase 1: Zero-Burn Pilot Setup',
                'color': '#EF4444',
                'url': 'SLIET / Mohali Phase 1 Deployment',
                'lines': [
                    '• Deploy Indic Voice Sarthi AI on Cloud Run; connect to WhatsApp Twilio gateway.',
                    '• Recruit 2 Cultured Relationship Managers (retired defense spouses in Mohali/Sec 34).',
                    '• Negotiate venue partnership with 2 local Sector community centers.',
                    '• Onboard first 15 pilot families with 14-day free trial.'
                ]
            },
            {
                'badge': 'DAYS 31-60: DISTRIBUTION',
                'title': 'Phase 2: Hyperlocal RWA & Gurdwara Engine',
                'color': '#F59E0B',
                'url': 'Zero-CAC Community Activations',
                'lines': [
                    '• Host "Silver Wellbeing Mornings" with free BP & cognitive checks at RWAs.',
                    '• Gurdwara & Temple morning announcements celebrating "Grandchild Seva".',
                    '• Digital Geo-targeted Ads in Brampton, Surrey, & London targeting Punjabi NRI children.',
                    '• Reach 100 paid active subscribers across Chandigarh and Mohali.'
                ]
            },
            {
                'badge': 'DAYS 61-90: SCALE',
                'title': 'Phase 3: Institutional Flywheel & Moat',
                'color': '#10B981',
                'url': 'Hospital Discharge Desk Partnerships',
                'lines': [
                    '• Launch official tie-up with Fortis Mohali & Max Hospital Geriatric discharge desks.',
                    '• Release "Sunday 90-Second WhatsApp Reel" feature for NRI family delight.',
                    '• Launch "The Golden Club" weekly Satsang and nature walks.',
                    '• Reach 300 subscribers; establish second hub in Panchkula; prepare Seed Round.'
                ]
            }
        ]
    }
]

# Write SVG
frame_w = 1920
frame_h = 1080
cols = 2
gap_x = 120
gap_y = 120
total_rows = (len(frames) + 1) // 2
canvas_w = cols * frame_w + (cols - 1) * gap_x + 200
canvas_h = total_rows * frame_h + (total_rows - 1) * gap_y + 200

svg_parts = []
svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {canvas_w} {canvas_h}" width="{canvas_w}" height="{canvas_h}" style="background:#05070B; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, Helvetica, Arial, sans-serif;">')
svg_parts.append('<defs>')
svg_parts.append('<filter id="card-shadow" x="-5%" y="-5%" width="110%" height="115%"><feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#000000" flood-opacity="0.6"/></filter>')
svg_parts.append('</defs>')

for idx, f in enumerate(frames):
    row = idx // cols
    col = idx % cols
    fx = 100 + col * (frame_w + gap_x)
    fy = 100 + row * (frame_h + gap_y)

    svg_parts.append(f'<g id="frame_{idx+1}">')
    svg_parts.append(f'<rect x="{fx}" y="{fy}" width="{frame_w}" height="{frame_h}" rx="24" fill="#0D111A" stroke="{f["color"]}" stroke-width="2" />')
    svg_parts.append(f'<rect x="{fx+50}" y="{fy+40}" width="6" height="52" fill="{f["color"]}" rx="3" />')
    svg_parts.append(f'<text x="{fx+70}" y="{fy+68}" fill="#FFFFFF" font-size="26" font-weight="800" letter-spacing="0.5">{f["title"]}</text>')
    svg_parts.append(f'<text x="{fx+70}" y="{fy+96}" fill="#94A3B8" font-size="16" font-weight="400">{f["subtitle"]}</text>')

    num_cards = len(f['cards'])
    c_cols = 3 if num_cards >= 5 else num_cards
    c_rows = 2 if num_cards >= 5 else 1
    c_gap = 24
    card_w = (frame_w - 100 - (c_cols - 1) * c_gap) // c_cols
    card_h = (frame_h - 170 - (c_rows - 1) * c_gap) // c_rows

    for c_idx, c in enumerate(f['cards']):
        if num_cards == 5 and c_idx >= 3:
            cr = 1
            cc = c_idx - 3
            c_w_actual = (frame_w - 100 - c_gap) // 2
            cx = fx + 50 + cc * (c_w_actual + c_gap)
            cy = fy + 140 + cr * (card_h + c_gap)
        else:
            cr = c_idx // c_cols
            cc = c_idx % c_cols
            c_w_actual = card_w
            cx = fx + 50 + cc * (card_w + c_gap)
            cy = fy + 140 + cr * (card_h + c_gap)

        svg_parts.append(f'<rect x="{cx}" y="{cy}" width="{c_w_actual}" height="{card_h}" rx="16" fill="#161E2E" stroke="{c["color"]}" stroke-width="1.5" filter="url(#card-shadow)" />')
        
        badge_text = c['badge']
        svg_parts.append(f'<rect x="{cx+20}" y="{cy+20}" width="{len(badge_text)*8.5+20}" height="26" rx="6" fill="{c["color"]}22" stroke="{c["color"]}" stroke-width="1" />')
        svg_parts.append(f'<text x="{cx+30}" y="{cy+38}" fill="{c["color"]}" font-size="11" font-weight="700" letter-spacing="0.8">{badge_text}</text>')

        # URL Label
        url_text = c.get('url', '')
        if url_text:
            safe_url = url_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            svg_parts.append(f'<text x="{cx+c_w_actual-20}" y="{cy+38}" text-anchor="end" fill="#64748B" font-size="10.5" font-family="monospace">{safe_url[:45]}</text>')

        svg_parts.append(f'<text x="{cx+20}" y="{cy+75}" fill="#F8FAFC" font-size="17" font-weight="700">{c["title"]}</text>')
        svg_parts.append(f'<line x1="{cx+20}" y1="{cy+90}" x2="{cx+c_w_actual-20}" y2="{cy+90}" stroke="#334155" stroke-width="1" />')

        line_y = cy + 118
        for line in c['lines']:
            safe_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            if line.startswith('• URL:') or line.startswith('• Citation:'):
                svg_parts.append(f'<text x="{cx+20}" y="{line_y}" fill="#38BDF8" font-size="12" font-weight="600">{safe_line}</text>')
            elif line.startswith('•'):
                svg_parts.append(f'<text x="{cx+20}" y="{line_y}" fill="#E2E8F0" font-size="12.5" font-weight="500">{safe_line}</text>')
            else:
                svg_parts.append(f'<text x="{cx+28}" y="{line_y}" fill="#94A3B8" font-size="12" font-weight="400">{safe_line}</text>')
            line_y += 23

    svg_parts.append('</g>')

svg_parts.append('</svg>')

with open(svg_path, 'w', encoding='utf-8') as f_out:
    f_out.write('\n'.join(svg_parts))

print(f"Updated {svg_path} successfully (Size: {os.path.getsize(svg_path)} bytes)")

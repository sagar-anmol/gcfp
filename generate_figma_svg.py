import os

svg_path = '/home/sagaranmol/code room/gcfp/figma_master_canvas.svg'

frames = [
    {
        'title': 'FRAME 1: COMPETITIVE INTELLIGENCE & MARKET GAP',
        'subtitle': 'Tricity Local Rivals vs. Pan-India Giants vs. Why Goodfellows Stalled',
        'color': '#EF4444',
        'cards': [
            {
                'badge': 'LOCAL TRICITY BENCHMARK',
                'title': 'GoldenCares (goldencares.in)',
                'color': '#EF4444',
                'lines': [
                    '• Current Model: ₹499/hr on-demand student companion visits.',
                    '• Stage: Early pilot incubated at SLIET IIC; 1 family served, 3 companions.',
                    '• Fatal Friction: Pay-per-hour discourages regular usage; travel in cash.',
                    '• Churn Risk: Students graduate/quit; family leaks directly to student.',
                    '• Missing: No nocturnal support, no health telemetry, zero ecosystem.'
                ]
            },
            {
                'badge': 'LOCAL MEDICAL CONCIERGE',
                'title': 'Emoha Elder Care (Mohali Hub - Sec 70)',
                'color': '#F59E0B',
                'lines': [
                    '• Model: 24/7 Emergency ambulance dispatch + hospital coordination.',
                    '• Pricing: ₹2,500/mo (Essential) to ₹10,000/mo (Empower/Complete).',
                    '• Moat: Established medical partnerships across Fortis & Max Mohali.',
                    '• Vulnerability: Heavy clinical hospital feel; elders feel sick and guarded;',
                    '  zero warm peer friendship or intellectual stimulation.'
                ]
            },
            {
                'badge': 'NRI FOCUS LEADER',
                'title': 'Samarth Eldercare (Chandigarh / Panchkula)',
                'color': '#10B981',
                'lines': [
                    '• Model: Dedicated Care Managers acting as surrogate family for NRIs.',
                    '• Pricing: ₹3,000 - ₹8,500/month (billed quarterly/annually).',
                    '• Brand: Strong trust among retired defense officers and PSU expats.',
                    '• Vulnerability: Human-only model leaves 16 nighttime hours uncovered.',
                    '  Scale is strictly limited by care-manager headcount burn.'
                ]
            },
            {
                'badge': 'PAN-INDIA BENCHMARK',
                'title': 'Goodfellows India (Ratan Tata Backed)',
                'color': '#EC4899',
                'lines': [
                    '• Model: Empathy-tested "Grandkids on Demand" (~₹5,000/month).',
                    '• The Scaling Bottlenecks:',
                    '  1. Salaried Fixed Burn: ₹25k-35k/mo fixed salaries create high burn.',
                    '  2. 3% Psychometric Funnel: Ultra-stringent filter strangles supply.',
                    '  3. Low Gross Margins: 1:5 ratio caps financial scalability.'
                ]
            },
            {
                'badge': 'INFORMAL BENCHMARK',
                'title': 'Domestic Maids / Ayahs (Price Anchor)',
                'color': '#8B5CF6',
                'lines': [
                    '• Pricing: ₹3,500 - ₹5,500/month for daily 1-2 hour physical presence.',
                    '• Family Mindset: NRI/local children compare every bill to maids.',
                    '• Our Positioning: Unbundle manual labor from intellectual companionship.',
                    '  Elders receive dignity, mental stimulation, and biological vigilance.'
                ]
            }
        ]
    },
    {
        'title': 'FRAME 2: CLINICAL, BIOLOGICAL & NOCTURNAL RESEARCH',
        'subtitle': 'Academic Proof: 3.4M Cohorts, Melatonin Collapse, and the 3:00 AM Void',
        'color': '#8B5CF6',
        'cards': [
            {
                'badge': 'MORTALITY METRICS',
                'title': 'Holt-Lunstad Meta-Analysis (3.4M Cohort)',
                'color': '#EC4899',
                'lines': [
                    '• Brigham Young Univ, Perspectives on Psychological Science.',
                    '• Finding: Social isolation increases mortality hazard by 26% to 32%.',
                    '• Biological Impact: Lethal equivalent of smoking 15 cigarettes daily.',
                    '• Worse than obesity, high blood pressure, and chronic inactivity.'
                ]
            },
            {
                'badge': '85-YEAR STUDY',
                'title': 'Harvard Adult Development Study',
                'color': '#3B82F6',
                'lines': [
                    '• Longest longitudinal study on human flourishing (Waldinger & Schulz).',
                    '• Discovery: Warmth of relationships is the #1 predictor of physical',
                    '  longevity, vascular health, and memory retention past age 75.',
                    '• Loneliness triggers toxic systemic chronic inflammation (IL-6 & CRP).'
                ]
            },
            {
                'badge': 'CIRCADIAN SCIENCE',
                'title': 'Melatonin Collapse & 3:00 AM Loneliness',
                'color': '#6366F1',
                'lines': [
                    '• Sleep Medicine Reviews: Pineal calcification reduces melatonin by 70%.',
                    '• Result: Circadian sleep architecture breaks into 3:00 AM micro-waking.',
                    '• The Nocturnal Void: Elders wake up in silence, fearing sudden death.',
                    '• The Solution: Sub-500ms Indic AI Voice Confidant available 24/7/365.'
                ]
            },
            {
                'badge': 'BEHAVIORAL PSYCH',
                'title': 'Socioemotional Selectivity & Dignity',
                'color': '#10B981',
                'lines': [
                    '• Stanford Aging Center (Prof. Laura Carstensen): Amygdala shifts to meaning.',
                    '• The Rebellion: Treating elders like children triggers fierce defiance.',
                    '• The Solution: Position companions as mentees seeking life guidance.',
                    '• Elders feel respected, useful, and emotionally validated.'
                ]
            },
            {
                'badge': 'REGIONAL DEMOGRAPHICS',
                'title': 'Punjab / Tricity "Silent Kothis" Reality',
                'color': '#F59E0B',
                'lines': [
                    '• LASI Wave-1: Punjab elder ratio 12.6%+; 150k youth emigrate yearly.',
                    '• Tricity Reality: Sectors 8-11 & Mohali Phase 7 filled with retired officers,',
                    '  judges, and professors living in 1-kanal villas in complete solitude.',
                    '• High spending power ($500-$2000/mo sent by NRI kids), zero companionship.'
                ]
            }
        ]
    },
    {
        'title': 'FRAME 3: GLOBAL PRECEDENTS & GOV-FUNDED EXPERIMENTS',
        'subtitle': 'US NYSOFA, South Korea Care-Call, Japan Silver Human Resources, China AI Lab',
        'color': '#06B6D4',
        'cards': [
            {
                'badge': 'USA STATE-BACKED',
                'title': 'ElliQ (New York State NYSOFA Deployment)',
                'color': '#06B6D4',
                'lines': [
                    '• NY State Office for the Aging deployed 800+ AI robotic companions.',
                    '• Clinical Results: 95% reported measurable reduction in loneliness.',
                    '• Key Insight: Proactive AI conversation (initiating dialogue) was critical.',
                    '• Validates government willingness to subsidize AI companionship.'
                ]
            },
            {
                'badge': 'SOUTH KOREA SCALE',
                'title': 'Naver CLOVA CareCall (Municipal Scale)',
                'color': '#10B981',
                'lines': [
                    '• HyperCLOVA AI calls 20,000+ isolated seniors twice weekly.',
                    '• Senses appetite, sleep, and emotional distress via natural voice.',
                    '• Integrates long-term episodic memory across calls with 90% positive score.',
                    '• Triggers municipal welfare worker visits when acoustic distress is flagged.'
                ]
            },
            {
                'badge': 'JAPAN SENIOR WORKFORCE',
                'title': 'Silver Human Resources Centers (Koreisha)',
                'color': '#F59E0B',
                'lines': [
                    '• 700,000+ active younger retirees (60-72) employed to assist seniors (80+).',
                    '• Solves the generation gap: Same cultural vernacular, songs, and history.',
                    '• Our Strategy: Recruit retired teachers & defense wives as Relationship Managers.'
                ]
            },
            {
                'badge': 'CHINA / BEIJING',
                'title': 'Beijing "Virtual Senior Homes" & AI Lab',
                'color': '#EF4444',
                'lines': [
                    '• Beijing & Shenzhen government subsidize smart home radar + AI voice boxes.',
                    '• 15-minute response radius by neighborhood triage workers.',
                    '• Venture funding boom in domestic AI eldercare assistants.'
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
                'lines': [
                    '• Indic Voice: Sub-500ms natural Punjabi, Hindi, and English code-switching.',
                    '• Episodic Memory: Vector DB tracks 100+ family details, medical history.',
                    '• Night-Owl Mode: Automatically engages at 3:00 AM with gentle dialogue.',
                    '• Acoustic Biomarkers: Real-time analysis of jitter, shimmer, and vocal fatigue.',
                    '• Cloud Architecture: Serverless Cloud Run + Groq Whisper + Indic TTS (₹0 idle).'
                ]
            },
            {
                'badge': 'PILLAR II: HUMAN TRUST',
                'title': 'Dedicated Relationship Manager (RM)',
                'color': '#10B981',
                'lines': [
                    '• Profile: Cultured 45-55yo community matriarchs (teachers, defense spouses).',
                    '• Responsibilities: Bi-weekly high-touch tea visits, trust anchor, gatekeeper.',
                    '• NRI Video Digest: Auto-compiles weekly 90-sec WhatsApp video reels for NRI kids.',
                    '• Manageability: 1 RM oversees 30 seniors easily with AI conversational summaries.'
                ]
            },
            {
                'badge': 'PILLAR III: ON-DEMAND GIGS',
                'title': 'Dynamic Gig Force & Medical Network',
                'color': '#F59E0B',
                'lines': [
                    '• Unbundled Labor: University students handle outdoor walks, errands, tech tutor.',
                    '• Anti-Leakage Moat: Gigs are strictly task-based outside house; no private poaching.',
                    '• Medical API Integration: Phlebotomists (Dr. Lal/SRL) and nurses dispatched on-demand.'
                ]
            },
            {
                'badge': 'PILLAR IV: COMMUNITY',
                'title': '"The Golden Club" Thematic Circles',
                'color': '#EC4899',
                'lines': [
                    '• 4 Thematic Circles: Satsang/Gurbani, "Silver Talks" Memoirs, Tambola, Nature Walks.',
                    '• Cluster Strategy: 10-15 seniors per 3km neighborhood pod.',
                    '• Retention Anchor: Families never churn because parents make lifelong friends.'
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
                'lines': [
                    '• Primary Trigger: Mobility score < 4, post-surgery or wheelchair-bound.',
                    '• Service Delivery: Daily AI voice check-ins (15 min) + weekly RM visit.',
                    '• Gig Unbundling: Partner nurse dispatched for wound dressing, bed sore care.',
                    '• Output: ₹3,499/mo; zero senior loneliness; 100% medication compliance.'
                ]
            },
            {
                'badge': 'BRANCH 2: MOBILE & LONELY',
                'title': 'The Active Social Club Track',
                'color': '#10B981',
                'lines': [
                    '• Primary Trigger: Healthy senior living alone with high cognitive vitality.',
                    '• Service Delivery: Weekly Golden Club meetups at community halls / Sukhna Lake.',
                    '• Engagement: Memoirs recorded by AI into hardbound physical books for family.',
                    '• Output: ₹2,499/mo; senior transitions from isolated to neighborhood mentor.'
                ]
            },
            {
                'badge': 'BRANCH 3: HIGH-ACUITY CHRONIC',
                'title': 'The High-Acuity Medical Track',
                'color': '#EF4444',
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
                'lines': [
                    '• Primary Trigger: Loss of spouse within last 6 months (peak depression risk).',
                    '• Service Delivery: Nightly 3:00 AM conversational soothing; daily gentle RM calls.',
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

# SVG Layout
frame_w = 1920
frame_h = 1080
cols = 2
gap_x = 120
gap_y = 120

total_cols = 2
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

    svg_parts.append(f'<!-- FRAME {idx+1}: {f["title"]} -->')
    svg_parts.append(f'<g id="frame_{idx+1}">')
    svg_parts.append(f'<rect x="{fx}" y="{fy}" width="{frame_w}" height="{frame_h}" rx="24" fill="#0D111A" stroke="{f["color"]}" stroke-width="2" />')
    
    # Title Banner
    svg_parts.append(f'<rect x="{fx+50}" y="{fy+40}" width="6" height="52" fill="{f["color"]}" rx="3" />')
    svg_parts.append(f'<text x="{fx+70}" y="{fy+68}" fill="#FFFFFF" font-size="26" font-weight="800" letter-spacing="0.5">{f["title"]}</text>')
    svg_parts.append(f'<text x="{fx+70}" y="{fy+96}" fill="#94A3B8" font-size="16" font-weight="400">{f["subtitle"]}</text>')

    num_cards = len(f['cards'])
    if num_cards <= 4:
        c_cols = num_cards
        c_rows = 1
    elif num_cards == 5:
        c_cols = 3
        c_rows = 2
    else:
        c_cols = 3
        c_rows = 2

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

        # Card rect
        svg_parts.append(f'<rect x="{cx}" y="{cy}" width="{c_w_actual}" height="{card_h}" rx="16" fill="#161E2E" stroke="{c["color"]}" stroke-width="1.5" filter="url(#card-shadow)" />')
        
        # Badge
        badge_text = c['badge']
        svg_parts.append(f'<rect x="{cx+20}" y="{cy+20}" width="{len(badge_text)*8.5+20}" height="26" rx="6" fill="{c["color"]}22" stroke="{c["color"]}" stroke-width="1" />')
        svg_parts.append(f'<text x="{cx+30}" y="{cy+38}" fill="{c["color"]}" font-size="11" font-weight="700" letter-spacing="0.8">{badge_text}</text>')

        # Title
        svg_parts.append(f'<text x="{cx+20}" y="{cy+75}" fill="#F8FAFC" font-size="18" font-weight="700">{c["title"]}</text>')
        svg_parts.append(f'<line x1="{cx+20}" y1="{cy+90}" x2="{cx+c_w_actual-20}" y2="{cy+90}" stroke="#334155" stroke-width="1" />')

        # Lines
        line_y = cy + 120
        for line in c['lines']:
            safe_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            if line.startswith('•'):
                svg_parts.append(f'<text x="{cx+20}" y="{line_y}" fill="#E2E8F0" font-size="13" font-weight="500">{safe_line}</text>')
            elif line.startswith('  1.') or line.startswith('  2.') or line.startswith('  3.'):
                svg_parts.append(f'<text x="{cx+26}" y="{line_y}" fill="#CBD5E1" font-size="12.5" font-weight="500">{safe_line}</text>')
            else:
                svg_parts.append(f'<text x="{cx+28}" y="{line_y}" fill="#94A3B8" font-size="12.5" font-weight="400">{safe_line}</text>')
            line_y += 24

    svg_parts.append('</g>')

svg_parts.append('</svg>')

with open(svg_path, 'w', encoding='utf-8') as f_out:
    f_out.write('\n'.join(svg_parts))

print(f'Successfully generated {svg_path} with size {os.path.getsize(svg_path)} bytes')

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

remaining_pins = [
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

print("Waiting 10 seconds for rate limit to reset...")
time.sleep(10)

for idx, p in enumerate(remaining_pins):
    payload = {
        "message": p["message"],
        "client_meta": {"x": p["x"], "y": p["y"]}
    }
    for attempt in range(3):
        resp = requests.post(url, headers=headers, json=payload)
        if resp.status_code == 200:
            data = resp.json()
            print(f"Posted Pin {idx+6} (ID: {data.get('id')}) at ({p['x']}, {p['y']})")
            break
        elif resp.status_code == 429:
            print(f"Rate limited on Pin {idx+6}, sleeping 8s before retry...")
            time.sleep(8)
        else:
            print(f"Error posting Pin {idx+6}: {resp.status_code} - {resp.text}")
            break
    time.sleep(3)

print("All remaining pins deployed!")

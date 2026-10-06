import os
import subprocess

html_deck = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>ElderTech Operating System — Executive Presentation Deck</title>
<style>
  @page {
    size: 297mm 167.06mm; /* Exact 16:9 Landscape A4 Ratio */
    margin: 0;
  }

  * {
    box-sizing: border-box;
  }

  body {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    background: #0f172a;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  /* Slide Canvas */
  .slide {
    width: 297mm;
    height: 167.06mm;
    padding: 14mm 16mm 10mm 16mm;
    background: #ffffff;
    position: relative;
    page-break-after: always;
    break-after: page;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  /* Slide Header */
  .slide-header {
    margin-bottom: 10px;
    border-bottom: 1.5px solid #e2e8f0;
    padding-bottom: 6px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }
  .header-left {
    display: flex;
    flex-direction: column;
  }
  .slide-tag {
    font-size: 7.5pt;
    font-weight: 700;
    color: #0284c7;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 2px;
  }
  .slide-title {
    font-size: 17pt;
    font-weight: 800;
    color: #0f172a;
    margin: 0;
    line-height: 1.15;
  }
  .slide-subtitle {
    font-size: 8.5pt;
    color: #64748b;
    margin: 2px 0 0 0;
  }
  .slide-badge-top {
    font-size: 7.5pt;
    font-weight: 600;
    background: #f1f5f9;
    color: #475569;
    padding: 3px 8px;
    border-radius: 4px;
    border: 1px solid #cbd5e1;
  }

  /* Slide Body */
  .slide-body {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }

  /* Slide Footer */
  .slide-footer {
    height: 16px;
    margin-top: auto;
    border-top: 1px solid #f1f5f9;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 7pt;
    color: #94a3b8;
  }

  /* Layout Grids */
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    height: 100%;
  }
  .grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 10px;
    height: 100%;
  }
  .grid-4 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 10px;
    height: 100%;
  }
  .grid-2x4 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    gap: 8px;
    height: 100%;
  }

  /* Card Styles */
  .card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 9px 11px;
    display: flex;
    flex-direction: column;
  }
  .card-danger {
    background: #fffafa;
    border-color: #fecaca;
    border-left: 3.5px solid #ef4444;
  }
  .card-primary {
    background: #f0f9ff;
    border-color: #bae6fd;
    border-left: 3.5px solid #0284c7;
  }
  .card-success {
    background: #f0fdf4;
    border-color: #bbf7d0;
    border-left: 3.5px solid #10b981;
  }
  .card-amber {
    background: #fffbeb;
    border-color: #fde68a;
    border-left: 3.5px solid #f59e0b;
  }

  .card-title {
    font-size: 9pt;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 5px;
  }
  .card-title-red { color: #b91c1c; }
  .card-title-blue { color: #0369a1; }
  .card-title-green { color: #15803d; }

  .card-text {
    font-size: 7.6pt;
    line-height: 1.38;
    color: #334155;
    margin: 0;
  }

  .metric-box {
    display: flex;
    flex-direction: column;
    margin: 4px 0;
  }
  .metric-val {
    font-size: 18pt;
    font-weight: 800;
    color: #0f172a;
    line-height: 1;
  }
  .metric-label {
    font-size: 7pt;
    font-weight: 600;
    color: #64748b;
    text-transform: uppercase;
  }

  /* Tables in PPT */
  table.ppt-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.5pt;
    margin: 4px 0;
  }
  table.ppt-table th {
    background: #f1f5f9;
    color: #0f172a;
    font-weight: 700;
    padding: 5px 7px;
    border: 1px solid #cbd5e1;
    text-align: left;
  }
  table.ppt-table td {
    padding: 5px 7px;
    border: 1px solid #cbd5e1;
    vertical-align: top;
    line-height: 1.35;
  }
  table.ppt-table tr:nth-child(even) td {
    background: #f8fafc;
  }

  /* Pills & Badges */
  .pill {
    display: inline-block;
    padding: 1px 6px;
    border-radius: 999px;
    font-size: 6.8pt;
    font-weight: 700;
    text-transform: uppercase;
  }
  .pill-red { background: #fee2e2; color: #991b1b; }
  .pill-green { background: #dcfce7; color: #166534; }
  .pill-blue { background: #e0f2fe; color: #075985; }

  /* Flow Diagram */
  .flow-diagram {
    background: #0f172a;
    color: #e2e8f0;
    border-radius: 6px;
    padding: 10px 14px;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 7.2pt;
    line-height: 1.35;
    white-space: pre;
    overflow: hidden;
  }

  /* Cover Slide Special Styling */
  .cover-slide {
    background: radial-gradient(circle at 80% 20%, #1e293b 0%, #0f172a 100%);
    color: #ffffff;
    justify-content: center;
    padding: 24mm 24mm;
  }
  .cover-pill {
    background: rgba(2, 132, 199, 0.2);
    border: 1px solid #0284c7;
    color: #38bdf8;
    font-size: 8pt;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 999px;
    width: fit-content;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 16px;
  }
  .cover-h1 {
    font-size: 32pt;
    font-weight: 800;
    color: #ffffff;
    margin: 0 0 10px 0;
    line-height: 1.1;
    letter-spacing: -0.02em;
  }
  .cover-sub {
    font-size: 13pt;
    color: #94a3b8;
    max-width: 820px;
    line-height: 1.45;
    margin-bottom: 24px;
  }
  .cover-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-top: 12px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 16px;
  }
  .cover-stat-label {
    font-size: 7.5pt;
    color: #64748b;
    text-transform: uppercase;
    font-weight: 600;
  }
  .cover-stat-val {
    font-size: 10.5pt;
    color: #e2e8f0;
    font-weight: 700;
    margin-top: 2px;
  }
</style>
</head>
<body>

<!-- ================= SLIDE 1: COVER ================= -->
<div class="slide cover-slide">
  <div class="cover-pill">Strategic Presentation Deck • October 2026</div>
  <h1 class="cover-h1">ElderTech Operating System</h1>
  <div class="cover-sub">
    An Autonomous Hybrid Platform for Solitary Seniors, Nocturnal Circadian Crises, and Global NRI Diaspora Care.
  </div>

  <div class="cover-grid">
    <div>
      <div class="cover-stat-label">Origin & Incubation</div>
      <div class="cover-stat-val">SLIET IIC / Tricity Pilot</div>
    </div>
    <div>
      <div class="cover-stat-label">Target Geography</div>
      <div class="cover-stat-val">Chandigarh "Silent Kothis" & Diaspora</div>
    </div>
    <div>
      <div class="cover-stat-label">Core Architecture</div>
      <div class="cover-stat-val">4-Pillar Hybrid Autonomous OS</div>
    </div>
    <div>
      <div class="cover-stat-label">Status</div>
      <div class="cover-stat-val">Verified v2.4 Master Specification</div>
    </div>
  </div>
</div>

<!-- ================= SLIDE 2: CURRENT BASELINE ================= -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <div class="slide-tag">Part 1 • Baseline Model</div>
      <h2 class="slide-title">What We Are Doing Today: The GoldenCares Baseline</h2>
      <div class="slide-subtitle">Early proof-of-concept operating in the Chandigarh–Mohali–Panchkula corridor</div>
    </div>
    <div class="slide-badge-top">Current Footprint</div>
  </div>

  <div class="slide-body">
    <div class="grid-3" style="height: auto; margin-bottom: 10px;">
      <div class="card card-primary">
        <div class="card-title card-title-blue">🎓 Student Companionship</div>
        <p class="card-text">
          On-demand pairing of university students (Panjab Univ, PEC, Chitkara) with solitary elders for daytime conversations, smartphone tech tutorials, and park walks.
        </p>
      </div>
      <div class="card card-primary">
        <div class="card-title card-title-blue">⏱️ Hourly Pay-Per-Use</div>
        <p class="card-text">
          Billed at <strong>₹499 per hour</strong> on-demand. Students receive a per-session stipend; local auto/fuel travel across Tricity sectors is reimbursed separately.
        </p>
      </div>
      <div class="card card-primary">
        <div class="card-title card-title-blue">📍 Tricity Footprint</div>
        <p class="card-text">
          Active pilot testing with early test households in Mohali Phase 7 and Chandigarh Sectors 8/9/10/11, establishing validated initial consumer demand.
        </p>
      </div>
    </div>

    <div class="card" style="background: #f8fafc; border: 1px solid #cbd5e1; flex: 1;">
      <div class="card-title" style="font-size: 8.8pt;">🏛️ The Demographic Reality: Tricity's "Silent Kothi" Crisis</div>
      <table class="ppt-table">
        <thead>
          <tr>
            <th style="width: 25%;">Demographic Metric</th>
            <th style="width: 25%;">Observed Benchmark</th>
            <th style="width: 50%;">Socio-Economic & Clinical Ground Reality</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Aging Index</strong></td>
            <td><strong>12.6%</strong> aged 60+ in Punjab</td>
            <td>Significantly exceeds the national average (Ministry of Health / LASI Wave 1).</td>
          </tr>
          <tr>
            <td><strong>Youth Emigration Drain</strong></td>
            <td><strong>150,000+</strong> youth / year</td>
            <td>Massive brain drain to Canada, UK, and Australia leaving aging parents isolated.</td>
          </tr>
          <tr>
            <td><strong>"Silent Kothi" Phenomenon</strong></td>
            <td>Sectors 8–11 (Chd), Phase 7 (Mohali)</td>
            <td>Retired generals, high court judges, bureaucrats alone in 1-kanal villas with liquid wealth but absolute emotional solitude.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="slide-footer">
    <span>ElderTech Operating System • Confidential Deck</span>
    <span>Slide 02</span>
  </div>
</div>

<!-- ================= SLIDE 3: THE 8 CORE PROBLEMS ================= -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <div class="slide-tag">Part 2 • Diagnosis & Failures</div>
      <h2 class="slide-title">The 8 Fatal Loopholes in the Current Baseline Model</h2>
      <div class="slide-subtitle">Why on-demand student matching fails at scale in real-world eldercare</div>
    </div>
    <div class="slide-badge-top" style="color: #b91c1c; border-color: #fca5a5; background: #fef2f2;">8 Critical Failure Modes</div>
  </div>

  <div class="slide-body">
    <div class="grid-2x4">
      <div class="card card-danger">
        <div class="card-title card-title-red">1. The Nocturnal Void</div>
        <p class="card-text">Companions leave at 6 PM. Melatonin collapses 60–80%, causing awakenings at 2–5 AM with severe existential dread and panic.</p>
      </div>
      <div class="card card-danger">
        <div class="card-title card-title-red">2. Cash Disintermediation</div>
        <p class="card-text">By visit #3, families exchange numbers with students and pay ₹300/hr directly in cash, bypassing the platform and killing LTV.</p>
      </div>
      <div class="card card-danger">
        <div class="card-title card-title-red">3. Pay-Per-Use Friction</div>
        <p class="card-text">₹499/hr forces a purchase decision every session. Frugal elders delay booking: <em>"Let's save money today"</em>, killing habitual retention.</p>
      </div>
      <div class="card card-danger">
        <div class="card-title card-title-red">4. Student Churn Cycle</div>
        <p class="card-text">Semester exams, internships, and holidays pull students away every 4 months. Seniors feel abandoned and reject new strangers.</p>
      </div>
      <div class="card card-danger">
        <div class="card-title card-title-red">5. Infantilization Trap</div>
        <p class="card-text">Positioning care as "babysitting lonely elders" triggers intense ego defense from proud retired officers and judges.</p>
      </div>
      <div class="card card-danger">
        <div class="card-title card-title-red">6. Broken Margins</div>
        <p class="card-text">At ₹499/hr, student pay (₹300) + commute costs (₹120) leave &lt;₹80 gross margin, incapable of absorbing ₹3k customer acquisition costs.</p>
      </div>
      <div class="card card-danger">
        <div class="card-title card-title-red">7. Zero NRI Telemetry</div>
        <p class="card-text">NRI children paying from Toronto receive casual WhatsApp texts instead of objective clinical vitals and cognitive trends.</p>
      </div>
      <div class="card card-danger">
        <div class="card-title card-title-red">8. Emergency Liability</div>
        <p class="card-text">Untrained students lack Basic Life Support (BLS) training during acute falls, TIAs, or cardiac events, exposing platform to liability.</p>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span>ElderTech Operating System • Confidential Deck</span>
    <span>Slide 03</span>
  </div>
</div>

<!-- ================= SLIDE 4: THE 4-PILLAR SOLUTION ================= -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <div class="slide-tag">Part 3 • The Solution</div>
      <h2 class="slide-title">The Solution: 4-Pillar Autonomous Hybrid Operating System</h2>
      <div class="slide-subtitle">Neither pure human nor pure AI — an intelligent hybrid socio-technical stack</div>
    </div>
    <div class="slide-badge-top" style="color: #0369a1; border-color: #bae6fd; background: #f0f9ff;">Defensible Architecture</div>
  </div>

  <div class="slide-body">
    <div class="grid-4">
      <div class="card card-primary">
        <div class="card-title card-title-blue">🧠 Pillar 1: Sarthi AI</div>
        <div class="metric-box">
          <span class="metric-val" style="color: #0284c7;">&lt;500ms</span>
          <span class="metric-label">Voice Pipeline Latency</span>
        </div>
        <p class="card-text">
          • 24/7 vernacular voice agent (Hindi/Punjabi)<br>
          • Proactive check-ins during 2–5 AM insomnia<br>
          • Passive vocal biomarker surveillance (tremors, word recall latency)
        </p>
      </div>

      <div class="card card-success">
        <div class="card-title card-title-green">🛡️ Pillar 2: Dignity RM</div>
        <div class="metric-box">
          <span class="metric-val" style="color: #10b981;">1:30</span>
          <span class="metric-label">Fixed Elder Ratio</span>
        </div>
        <p class="card-text">
          • Permanent, salaried geriatric care manager<br>
          • Dual-facing: elders locally + NRI kids abroad<br>
          • Gatekeeper: approves all AI orders<br>
          • Bi-weekly in-person clinical audits
        </p>
      </div>

      <div class="card card-primary">
        <div class="card-title card-title-blue">🚶 Pillar 3: Youth Escorts</div>
        <div class="metric-box">
          <span class="metric-val" style="color: #0284c7;">Mentee</span>
          <span class="metric-label">Relationship Framing</span>
        </div>
        <p class="card-text">
          • Vetted students (PU, PEC, Chitkara)<br>
          • Framed as mentees seeking life wisdom<br>
          • Reverses infantilization ego defense<br>
          • Hospital queues (PGIMER/Fortis), walks
        </p>
      </div>

      <div class="card card-amber">
        <div class="card-title" style="color: #b45309;">🏘️ Pillar 4: Golden Club</div>
        <div class="metric-box">
          <span class="metric-val" style="color: #f59e0b;">3 km</span>
          <span class="metric-label">Micro-Pod Radius</span>
        </div>
        <p class="card-text">
          • Hyperlocal clusters of 8–12 active elders<br>
          • Weekly bridge, book clubs, garden tea<br>
          • Fosters mutual horizontal peer support<br>
          • Prevents platform disintermediation
        </p>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span>ElderTech Operating System • Confidential Deck</span>
    <span>Slide 04</span>
  </div>
</div>

<!-- ================= SLIDE 5: GATEKEEPER & WORKERS POOL ================= -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <div class="slide-tag">Part 4 • Operational Mechanics</div>
      <h2 class="slide-title">Dynamic Workers Pool & The RM Approval Firewall</h2>
      <div class="slide-subtitle">Zero idle payroll combined with human-in-the-loop safety verification</div>
    </div>
    <div class="slide-badge-top">Human-in-the-Loop</div>
  </div>

  <div class="slide-body">
    <div class="grid-2">
      <div class="flow-diagram">
┌────────────────────────────────────────────────────────┐
│               THE REAL-TIME DISPATCH FLOW              │
├────────────────────────────────────────────────────────┤
│ 1. 👵 Senior Speaks to Sarthi AI at Bedside            │
│    "Mainu knee pain ho rahi hai, spray bhej do te      │
│     PGIMER OPD lai companion book karo"                │
│                         ▼                              │
│ 2. 🧠 Sarthi AI Generates Pending Action Item          │
│    • Flags: ₹450 Volini spray + 3hr OPD Companion      │
│                         ▼                              │
│ 3. 🛡️ RM Reviews & Authorizes in Console               │
│    • Checks clinical validity & elder safety           │
│    • Prevents fraud, scams, or dementia mis-orders     │
│                         ▼                              │
│ 4. 🚶 Dynamic Escort Dispatched from Pool              │
│    • Health-tagged student matched for PGIMER          │
│    • Debits pre-funded Family Digital Wallet           │
└────────────────────────────────────────────────────────┘
      </div>

      <div style="display: flex; flex-direction: column; gap: 8px;">
        <div class="card card-primary" style="flex: 1;">
          <div class="card-title card-title-blue">⚡ Dynamic Workers Pool: Just-In-Time Supply</div>
          <p class="card-text">
            • <strong>Zero Fixed Salary Burn:</strong> Avoids Goodfellows' mistake of paying fixed salaries to idle companions. Students and escorts sit in an on-demand, skills-tagged pool.<br>
            • <strong>Specialized Dispatch:</strong> Hospital queues at PGIMER $\to$ Health escorts; Tech tutor / Chess $\to$ Engineering mentees; Mobility errands $\to$ Mobility assistants.
          </p>
        </div>

        <div class="card card-success" style="flex: 1;">
          <div class="card-title card-title-green">🛡️ The RM Approval Firewall: Fraud & Liability Shield</div>
          <p class="card-text">
            • <strong>The Threat:</strong> Direct AI purchases expose elders to predatory scams, mistaken orders, and adverse drug reactions.<br>
            • <strong>The Gatekeeper:</strong> The RM approves every financial debit and service dispatch, protecting both elder dignity and platform liability.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span>ElderTech Operating System • Confidential Deck</span>
    <span>Slide 05</span>
  </div>
</div>

<!-- ================= SLIDE 6: DUAL-BUCKET FAMILY WALLET ================= -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <div class="slide-tag">Part 5 • Financial Architecture</div>
      <h2 class="slide-title">The Dual-Bucket Family Wallet & Modular Add-Ons</h2>
      <div class="slide-subtitle">Stopping platform cash leakage while preserving elder financial dignity</div>
    </div>
    <div class="slide-badge-top" style="color: #15803d; border-color: #bbf7d0; background: #f0fdf4;">Fintech Moat</div>
  </div>

  <div class="slide-body">
    <div class="grid-2" style="margin-bottom: 8px;">
      <div class="card card-primary">
        <div class="card-title card-title-blue">📊 Bucket A: Health & Core Care Wallet</div>
        <p class="card-text">
          • <strong>Funded & Monitored by NRI Child:</strong> Maintained via Stripe in USD/CAD/GBP or domestic auto-debit.<br>
          • <strong>Itemized Transparency:</strong> Covers RM visits, prescription medicine refills, routine lab blood draws, and clinical escorts.<br>
          • <strong>Full Telemetry:</strong> Receipts and medical compliance logs shared directly with children.
        </p>
      </div>

      <div class="card card-success">
        <div class="card-title card-title-green">👑 Bucket B: Dignity Freedom Float (Private)</div>
        <p class="card-text">
          • <strong>Autonomous Senior Spending:</strong> Fixed monthly pool (₹5,000/mo) pre-authorized for tea companions, nursery visits, and hobbies.<br>
          • <strong>Zero Child Surveillance:</strong> Child has <strong>no veto or line-item visibility</strong>, ending the humiliation of adult children questioning elder spending.<br>
          • <strong>Preserves Autonomy:</strong> Seniors feel respected, not policed.
        </p>
      </div>
    </div>

    <div class="card" style="background: #f8fafc; border: 1px solid #cbd5e1; flex: 1;">
      <div class="card-title" style="font-size: 8.8pt;">📦 Modular Add-On Marketplace (Recurring & On-Demand)</div>
      <table class="ppt-table">
        <thead>
          <tr>
            <th style="width: 25%;">Add-On Category</th>
            <th style="width: 35%;">Service Scope</th>
            <th style="width: 40%;">Operational Delivery Mechanism</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Monthly Chronic Care</strong></td>
            <td>Cardio & Diabetes management: home blood draws, teleconsult, pill-box audits</td>
            <td>Contracted via Tier-1 B2B APIs (Dr. Lal PathLabs, Max Labs) with verified SLAs.</td>
          </tr>
          <tr>
            <td><strong>In-Home Physiotherapy</strong></td>
            <td>2x weekly geriatric mobility therapy & fall prevention</td>
            <td>Vetted freelance physiotherapists verified and monitored by the RM.</td>
          </tr>
          <tr>
            <td><strong>Hospital OPD Navigation</strong></td>
            <td>Half-day companion escort at PGIMER Chandigarh or Fortis Mohali</td>
            <td>Health-tagged youth escort manages registration, queues, and pharmacy collection.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="slide-footer">
    <span>ElderTech Operating System • Confidential Deck</span>
    <span>Slide 06</span>
  </div>
</div>

<!-- ================= SLIDE 7: STRESS-TESTING & 7 PATCHES ================= -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <div class="slide-tag">Part 6 • Operational Resilience</div>
      <h2 class="slide-title">System Stress-Testing: The 7 Loopholes & Patches</h2>
      <div class="slide-subtitle">Pre-empting operational bottlenecks, legal liabilities, and cross-border frictions</div>
    </div>
    <div class="slide-badge-top">Institutional Rigor</div>
  </div>

  <div class="slide-body">
    <table class="ppt-table" style="font-size: 7.2pt;">
      <thead>
        <tr>
          <th style="width: 4%;">#</th>
          <th style="width: 22%;">Identified Loophole</th>
          <th style="width: 34%;">Operational Failure Mode</th>
          <th style="width: 40%;">Architectural Patch</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>1</strong></td>
          <td><strong>RM Overload Bottleneck</strong></td>
          <td>1:30 ratio = 60 home visits/mo. Commute + 30 NRI WhatsApp chats burns out RMs in 90 days.</td>
          <td><span class="pill pill-green">Geographic Micro-Zoning</span> RMs restricted to tight sector zone (Chd Sec 1–15 only). Ratio capped at 1:20 for high-acuity tiers.</td>
        </tr>
        <tr>
          <td><strong>2</strong></td>
          <td><strong>Order Approval Latency</strong></td>
          <td>If RM is driving, urgent AI requests (taxi, pain spray) sit unread for 3 hours, frustrating elders.</td>
          <td><span class="pill pill-green">Tiered Approval Thresholds</span> Orders &lt;₹500 and emergency SOS auto-dispatch instantly. RM review reserved for &gt;₹1,000.</td>
        </tr>
        <tr>
          <td><strong>3</strong></td>
          <td><strong>Dynamic Pool "Stranger Danger"</strong></td>
          <td>Sending different students every week creates theft paranoia; elders refuse to open doors.</td>
          <td><span class="pill pill-green">Primary + Backup Pod (2:1)</span> Assign each senior a dedicated 2-person pod. Dynamic pooling applies only to outdoor errands.</td>
        </tr>
        <tr>
          <td><strong>4</strong></td>
          <td><strong>Family Wallet Dignity Clash</strong></td>
          <td>NRI child inspects every rupee; questions dad's spending on snacks, humiliating the proud senior.</td>
          <td><span class="pill pill-green">Freedom Float Partition</span> Split wallet into monitored "Health Core" and private "Freedom Float" (₹5,000/mo) with zero child surveillance.</td>
        </tr>
        <tr>
          <td><strong>5</strong></td>
          <td><strong>AI Misdiagnosis Liability</strong></td>
          <td>Elder slurs or uses dialect (<em>"chhati ch jalan"</em>). AI recommends antacids for acute heart attack.</td>
          <td><span class="pill pill-red">Hardcoded Red-Flag Firewall</span> Chest pain, numbness, or dyspnea locks commercial ordering and triggers instant hospital/RM SOS.</td>
        </tr>
        <tr>
          <td><strong>6</strong></td>
          <td><strong>NRI Time-Zone Delta</strong></td>
          <td>Tricity 1 PM crisis is 12:30 AM in California. Child is asleep; delayed approvals stall medical care.</td>
          <td><span class="pill pill-blue">Emergency Power of Attorney</span> Onboarding contract pre-authorizes $250–$500 emergency spend threshold for immediate clinical triage.</td>
        </tr>
        <tr>
          <td><strong>7</strong></td>
          <td><strong>Add-on Vendor No-Shows</strong></td>
          <td>Outsourced phlebotomists arrive 2 hours late. Fasting diabetic elder suffers; platform takes blame.</td>
          <td><span class="pill pill-blue">Institutional B2B SLAs</span> Direct API contracts with certified chains (Max Healthcare, Dr. Lal PathLabs) with strict financial penalty clauses.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="slide-footer">
    <span>ElderTech Operating System • Confidential Deck</span>
    <span>Slide 07</span>
  </div>
</div>

<!-- ================= SLIDE 8: GLOBAL PRECEDENTS & EVIDENCE ================= -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <div class="slide-tag">Part 7 • Global Validation</div>
      <h2 class="slide-title">Global Precedents: Proven in Parts Across the World</h2>
      <div class="slide-subtitle">Evidence-based validation from peer-reviewed trials and government initiatives</div>
    </div>
    <div class="slide-badge-top" style="color: #0369a1; border-color: #bae6fd; background: #f0f9ff;">Peer-Reviewed Data</div>
  </div>

  <div class="slide-body">
    <div class="grid-4" style="margin-bottom: 8px;">
      <div class="card card-primary">
        <div class="card-title card-title-blue">🇺🇸 USA: Papa Pals</div>
        <div class="metric-box">
          <span class="metric-val" style="color: #0284c7;">-33%</span>
          <span class="metric-label">ER Admissions</span>
        </div>
        <p class="card-text">
          Dynamic student companionship funded via Medicare Advantage plans across 50 US states. Proven model for non-medical social support.
        </p>
      </div>

      <div class="card card-primary">
        <div class="card-title card-title-blue">🇰🇷 S. Korea: Naver CareCall</div>
        <div class="metric-box">
          <span class="metric-val" style="color: #0284c7;">20,000+</span>
          <span class="metric-label">Elders Called</span>
        </div>
        <p class="card-text">
          Gov-funded telephony AI check-in across 20+ Korean cities (HyperCLOVA LLM). 90%+ retention; automated welfare alerts (ACM CHI 2023).
        </p>
      </div>

      <div class="card card-primary">
        <div class="card-title card-title-blue">🇺🇸 USA: NYSOFA & ElliQ</div>
        <div class="metric-box">
          <span class="metric-val" style="color: #0284c7;">95%</span>
          <span class="metric-label">Loneliness Drop</span>
        </div>
        <p class="card-text">
          NY State Government purchased proactive voice AI companions for 800+ seniors. 30+ daily interactions; 80% proactive AI prompts.
        </p>
      </div>

      <div class="card card-success">
        <div class="card-title card-title-green">🇳🇱 Netherlands: Buurtzorg</div>
        <div class="metric-box">
          <span class="metric-val" style="color: #10b981;">-30%</span>
          <span class="metric-label">ER Visits</span>
        </div>
        <p class="card-text">
          Decentralized 3km neighborhood nursing pods (our RM layer). 8% overhead vs. 25% industry average; #1 Dutch employer 5 times.
        </p>
      </div>
    </div>

    <div class="card" style="background: #f8fafc; border: 1px solid #cbd5e1; flex: 1;">
      <div class="card-title" style="font-size: 8.5pt;">📺 Empathetic Video Proof & Clinical Studies</div>
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; font-size: 7.5pt; color: #334155;">
        <div>
          <strong>• South Korea: Naver CLOVA CareCall in Action:</strong> Real Korean seniors talking to the AI telephony agent like family, with local welfare officers intervening in emergencies. (YouTube: <code>NAVER CLOVA Official Showcase</code>).
        </div>
        <div>
          <strong>• New York State: Meet Lucinda (69, New York) & ElliQ:</strong> Moving documentary where Lucinda describes through tears how proactive voice companion ended her nocturnal panic and gave her back joy. (YouTube: <code>Meet Lucinda, 69, from New York ElliQ</code>).
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span>ElderTech Operating System • Confidential Deck</span>
    <span>Slide 08</span>
  </div>
</div>

<!-- ================= SLIDE 9: SUMMARY & MOAT ================= -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <div class="slide-tag">Summary & Strategic Moat</div>
      <h2 class="slide-title">Summary: The 3-Way Lock-in & Anti-Leakage Moat</h2>
      <div class="slide-subtitle">Why the hybrid operating system cannot be bypassed by clients or workers</div>
    </div>
    <div class="slide-badge-top" style="color: #15803d; border-color: #bbf7d0; background: #f0fdf4;">The Moat</div>
  </div>

  <div class="slide-body">
    <div class="grid-3" style="height: 100%;">
      <div class="card card-primary">
        <div class="card-title card-title-blue">1. Clinical & Nocturnal Lock-In</div>
        <p class="card-text" style="font-size: 8pt; line-height: 1.45;">
          • An informal student or maid leaves at 6:00 PM.<br>
          • Only Sarthi AI provides the <strong>2:00 AM – 5:00 AM nocturnal shield</strong>, monitoring sleep disturbances and speech biomarkers.<br>
          • The family cannot cancel without losing 24/7 emergency telemetry and nighttime security.
        </p>
      </div>

      <div class="card card-success">
        <div class="card-title card-title-green">2. The RM Trust & Safety Lock-In</div>
        <p class="card-text" style="font-size: 8pt; line-height: 1.45;">
          • The student is merely an outdoor escort; the <strong>RM is the clinical and emotional guardian</strong>.<br>
          • The RM manages hospital emergency triage, medicine reconciliation, and weekly diaspora video digests.<br>
          • Disintermediating the student cash-in-hand forfeits the RM safety umbrella and family wallet.
        </p>
      </div>

      <div class="card card-amber">
        <div class="card-title" style="color: #b45309;">3. Hyperlocal Pod Social Lock-In</div>
        <p class="card-text" style="font-size: 8pt; line-height: 1.45;">
          • An elder’s active social life is rooted in the <strong>Golden Club 3km Pod</strong> (bridge tournaments, poetry sessions, peer friends).<br>
          • A family cannot take the 12-person neighborhood club private.<br>
          • Social network effects generate organic RWA word-of-mouth with near-zero CAC.
        </p>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span>ElderTech Operating System • Confidential Deck</span>
    <span>Slide 09</span>
  </div>
</div>

</body>
</html>
"""

html_deck_path = "/home/sagaranmol/code room/gcfp/eldertech_presentation_deck.html"
pdf_deck_path = "/home/sagaranmol/code room/gcfp/eldertech_presentation_deck.pdf"

with open(html_deck_path, "w", encoding="utf-8") as f:
    f.write(html_deck)

print(f"Generated PPT-style HTML at: {html_deck_path}")

cmd = [
    "google-chrome",
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_deck_path}",
    html_deck_path
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome stdout:", res.stdout)
print("Chrome stderr:", res.stderr)

if os.path.exists(pdf_deck_path):
    size = os.path.getsize(pdf_deck_path)
    print(f"SUCCESS: Generated 16:9 Landscape PPT-Style PDF at {pdf_deck_path} ({size} bytes)")
else:
    print("FAILED to generate PDF")

---
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

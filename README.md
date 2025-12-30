# Crisis at CyberCorp 🛡️

**Role:** Chief Information Security Officer (CISO)  
**Mission:** Protect CyberCorp from a multi-stage cyber attack.

## Overview
"Crisis at CyberCorp" is an educational simulation game designed to teach:
- **Phishing Analysis:** Identifying spear-phishing and social engineering.
- **Incident Response:** Analyzing server logs to distinguish between benign traffic and data exfiltration.
- **Ethical Strategy:** Making high-stakes decisions under pressure (Ransomware negotiation).

## Features
- 📧 **Level 1:** Analyze 10 realistic emails. Can you spot the traps?
- 📜 **Level 2:** Forensic log analysis. Find "Patient Zero".
- ⚖️ **Level 3:** The Boardroom. Handle a ransomware ultimatum.
- 📝 **Auto-Grading:** Generates a detailed CISO Report at the end of the session.

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/zytang/CyberCorp-Game.git
   cd CyberCorp-Game
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## Deployment
This app is ready for [Streamlit Community Cloud](https://streamlit.io/cloud).
1. Fork/Clone this repo.
2. Connect your GitHub account to Streamlit Cloud.
3. Select `app.py` as the entry point.

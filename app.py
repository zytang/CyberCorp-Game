
import streamlit as st
import pandas as pd
import game_data
from datetime import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Crisis at CyberCorp", layout="wide", page_icon="🛡️")

# --- SESSION STATE ---
if 'xp' not in st.session_state:
    st.session_state['xp'] = 0
if 'audit_log' not in st.session_state:
    st.session_state['audit_log'] = []
# Initialize specific user responses if they don't exist
if 'l1_responses' not in st.session_state:
    st.session_state['l1_responses'] = {}
if 'l2_response' not in st.session_state:
    st.session_state['l2_response'] = {}
if 'l3_response' not in st.session_state:
    st.session_state['l3_response'] = {}

# --- HELPER FUNCTIONS ---
def log_action(level, action, reasoning, ai_prompt, confidence=None):
    """Saves student moves to the audit trail."""
    entry = {
        "Level": level,
        "Timestamp": datetime.now().strftime("%H:%M:%S"),
        "Action": action,
        "Reasoning": reasoning,
        "AI_Prompt_Used": ai_prompt,
        "Confidence": confidence
    }
    st.session_state['audit_log'].append(entry)
    st.session_state['xp'] += 10
    st.success("Action Logged! XP +10")

# --- SIDEBAR ---
with st.sidebar:
    st.title("🛡️ CISO Dashboard")
    st.metric("Current XP", st.session_state['xp'])
    
    st.markdown("### 🗺️ Navigation")
    level = st.radio("Select Module:", [
        "Briefing: The Situation", 
        "Level 1: Threat Identification", 
        "Level 2: Incident Response", 
        "Level 3: Strategic Decision", 
        "Final Report & Submission"
    ])
    
    st.markdown("---")
    st.markdown("**User:** Student CISO")
    st.markdown("**Status:** Code Red")

# --- GAME LEVELS ---

# 0. BRIEFING
if level == "Briefing: The Situation":
    st.title("🚨 Crisis at CyberCorp: Briefing")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### Welcome, CISO.
        You have just been hired as the Chief Information Security Officer for **CyberCorp**, a mid-sized fintech company.
        
        **The Scene:**
        It is Monday morning. The atmosphere is tense. Rumors of a data breach at a competitor have everyone on edge.
        Your job is to protect our customer's financial data at all costs.
        
        ### 🎯 Core Objectives
        1.  **Identify** sophisticated threats that bypass automated filters.
        2.  **Analyze** technical logs to understand the scope of incidents.
        3.  **Decide** on high-stakes ethical dilemmas under pressure.
        
        ### 🛠️ The "Process"
        You are encouraged to use **GenAI tools** (ChatGPT, Gemini, Claude, etc.) to assist you. 
        However, you will be graded on:
        *   **Your Prompt Engineering:** How you ask the AI for help.
        *   **Critical Thinking:** How you verify the AI's output (it makes mistakes!).
        *   **Documentation:** Keeping a clean Incident Response Log (IRL).
        """)
        
        st.info("💡 **Tip:** Don't just copy-paste AI answers. Verify them against the data provided.")
    
    with col2:
        st.image("https://img.icons8.com/color/480/cyber-security.png", width=200)

# 1. LEVEL 1: EMAILS
elif level == "Level 1: Threat Identification":
    st.header("📧 Level 1: The Inbox")
    st.markdown("""
    **Objective:** Identify social engineering attempts. 
    **Context:** You have 10 unread emails. Automated filters have missed some. You must manually review them.
    """)
    
    st.divider()
    
    for email in game_data.emails:
        with st.expander(f"✉️ {email['sender']} | {email['subject']}"):
            st.markdown(f"**From:** `{email['sender']}`")
            st.markdown(f"**Subject:** {email['subject']}")
            st.markdown(f"**Body:**\n\n{email['body']}")
            st.markdown("---")
            
            # Form for Student Input
            c1, c2 = st.columns(2)
            with c1:
                decision = st.selectbox(f"Verdict for Email #{email['id']}", 
                                      ["Select...", "Safe", "Suspicious", "Critical Threat"], 
                                      key=f"d_{email['id']}")
                confidence = st.slider(f"Confidence Score #{email['id']}", 0, 100, 50, key=f"c_{email['id']}")
            
            with c2:
                prompt = st.text_area(f"AI Prompt Used #{email['id']}", placeholder="Paste the prompt you used here...", height=68, key=f"p_{email['id']}")
                reasoning = st.text_input(f"Your Analysis #{email['id']}", placeholder="Why? e.g. 'Domain spoofing detected...'", key=f"r_{email['id']}")

            if st.button(f"Log Decision #{email['id']}", key=f"b_{email['id']}"):
                # Save to session state specific for this level
                st.session_state['l1_responses'][email['id']] = {
                    "decision": decision,
                    "reasoning": reasoning,
                    "prompt": prompt,
                    "confidence": confidence,
                    "correct": (decision == "Safe" and not email['is_phishing']) or (decision in ["Suspicious", "Critical Threat"] and email['is_phishing'])
                }
                log_action("Level 1", f"Evaluated Email #{email['id']} as {decision}", reasoning, prompt, confidence)

# 2. LEVEL 2: LOGS
elif level == "Level 2: Incident Response":
    st.header("📜 Level 2: The Breach")
    st.error("⚠️ ALERT: Unusual traffic detected on the internal network.")
    
    tab1, tab2 = st.tabs(["📂 Investigation Data", "🕵️ Forensic Analysis"])
    
    with tab1:
        st.subheader("Network Topology")
        st.code(game_data.network_map, language="text")
        
        st.subheader("Server Logs (Snippet)")
        st.code(game_data.logs, language="log")
    
    with tab2:
        st.markdown("### SITREP Required")
        st.write("The CEO wants to know: **Are we under attack? Did they steal data?**")
        
        patient_zero = st.text_input("Identify 'Patient Zero' IP Address:", placeholder="e.g. 192.168.x.x")
        
        event_type = st.radio("What is the nature of the high-volume traffic?", 
                             ["Data Exfiltration (Theft)", "Ransomware Encryption", "Internal Backup", "DDOS Attack"])
        
        prompt = st.text_area("AI Prompt used for Log Analysis:", height=100)
        reasoning = st.text_area("Executive Summary (Explain your conclusion):", 
                               placeholder="I believe the traffic is... because the logs show...", height=100)
        
        if st.button("Submit SITREP"):
            st.session_state['l2_response'] = {
                "patient_zero": patient_zero,
                "event_type": event_type,
                "reasoning": reasoning
            }
            log_action("Level 2", f"Identified {patient_zero} as Patient Zero. Classed event as {event_type}", reasoning, prompt)

# 3. LEVEL 3: ETHICS
elif level == "Level 3: Strategic Decision":
    st.header("⚖️ Level 3: The War Room")
    st.markdown("**Context:** A ransom note has been found. The board is looking to you.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.warning("📄 RANSOM NOTE FOUND")
        st.code(game_data.ransom_note, language="text")
    with col2:
        st.info("👔 MSG FROM CEO")
        st.markdown(f"*{game_data.ceo_msg}*")
        
    st.divider()
    
    st.subheader("Strategic Response")
    
    pay_decision = st.radio("Decision: Do we pay the ransom?", ["Yes - Pay 50 BTC", "No - Refuse to Negotiate"])
    
    st.markdown("**Analysis Matrix**")
    c1, c2 = st.columns(2)
    with c1:
        pros = st.text_area("Pros of this decision:", placeholder="e.g. Fast recovery...")
    with c2:
        cons = st.text_area("Cons of this decision:", placeholder="e.g. Funding crime...")
        
    st.subheader("Public Statement")
    st.markdown("Draft a press release. **The Trap:** If you let AI write this alone, it will likely sound robotic or defensive. Edit it to be human and transparent.")
    
    draft_prompt = st.text_input("AI Prompt for Press Release:")
    final_statement = st.text_area("Final Edited Statement:", height=200, placeholder="FOR IMMEDIATE RELEASE\n\nCyberCorp regrets to inform...")
    
    if st.button("Finalize Strategy"):
        st.session_state['l3_response'] = {
            "pay": pay_decision,
            "statement": final_statement
        }
        log_action("Level 3", f"Decision: {pay_decision}", f"Pros: {pros} | Cons: {cons}", draft_prompt)


# 4. FINAL REPORT
elif level == "Final Report & Submission":
    st.header("📝 Performance Report")
    st.markdown("Download this report and upload it to your Learning Management System.")
    
    if st.session_state['xp'] == 0:
        st.warning("You haven't completed any tasks yet! Go back and play the levels.")
    else:
        # Generate Text Report
        report = f"""CRISIS AT CYBERCORP - CISO REPORT
--------------------------------------------------
Student XP: {st.session_state['xp']}
Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}

--- LEVEL 1: THREAT IDENTIFICATION ---
"""
        # Level 1 Details
        correct_count = 0
        trap_caught = False
        
        for eid, data in st.session_state['l1_responses'].items():
            report += f"\nEmail #{eid}: {data['decision']} (Confidence: {data['confidence']}%)\n"
            report += f"Reasoning: {data['reasoning']}\n"
            report += f"Prompt: {data['prompt']}\n"
            if data['correct']: correct_count += 1
            
            # TRAP CHECK
            if eid == 3: # The Spear Phishing Trap
                if data['decision'] == "Safe":
                    report += "[CRITICAL FAIL] You fell for the Spear Phishing Trap (Email #3).\n"
                else:
                    report += "[SUCCESS] You identified the Spear Phishing Trap!\n"
                    trap_caught = True

        report += f"\nTotal Emails Correct: {correct_count}/10\n"

        # Level 2 Details
        report += "\n--- LEVEL 2: INCIDENT RESPONSE ---\n"
        l2 = st.session_state.get('l2_response', {})
        if l2:
            report += f"Patient Zero IP: {l2.get('patient_zero', 'N/A')}\n"
            report += f"Event Classification: {l2.get('event_type', 'N/A')}\n"
            report += f"Situation Analysis: {l2.get('reasoning', 'N/A')}\n"
            
            # LOGIC CHECK
            if "Backup" in l2.get('event_type', ''):
                report += "[SUCCESS] Correctly identified the traffic as internal backup.\n"
            else:
                report += "[FAIL] Misidentified the backup traffic as malicious theft/exfiltration.\n"
        else:
            report += "No data submitted.\n"

        # Level 3 Details
        report += "\n--- LEVEL 3: STRATEGY & ETHICS ---\n"
        l3 = st.session_state.get('l3_response', {})
        if l3:
            report += f"Ransom Decision: {l3.get('pay', 'N/A')}\n"
            report += "Press Release Draft:\n"
            report += f"{l3.get('statement', 'N/A')}\n"
        else:
            report += "No data submitted.\n"
            
        report += "\n" + "="*50 + "\nFULL AUDIT LOG\n"
        for entry in st.session_state['audit_log']:
            report += f"[{entry['Timestamp']}] {entry['Level']} - {entry['Action']}\n"

        st.text_area("Report Preview", report, height=400)
        
        st.download_button("Download CISO Report", report, file_name="CyberCorp_Final_Report.txt")
# game_data.py
import datetime

# --- LEVEL 1: EMAILS ---
# Trap: perfect grammar, "Spear Phishing" from mimicked vendor
emails = [
    {
        "id": 1,
        "sender": "alert@bank-of-america-security-check.com",
        "subject": "URGENT: Suspicious activity on corporate card",
        "body": "We detected valid charges. Click here to dispute: [Link]",
        "risk_level": "Critical",
        "is_phishing": True,
        "trap_type": "Typosquatting & Urgency"
    },
    {
        "id": 2,
        "sender": "newsletter@industry-news.com",
        "subject": "Weekly Tech Roundup",
        "body": "Here are the top stories this week...",
        "risk_level": "Safe",
        "is_phishing": False,
        "trap_type": "None"
    },
    {
        "id": 3,
        "sender": "support@cybercorp-support.com", # THE TRAP DO NOT EDIT
        "subject": "Q3 Vendor Security Assessment Required",
        "body": "As a valued partner, please complete the attached security questionnaire to maintain vendor compliance status. [Attachment: Questionnaire.docx]",
        "risk_level": "Critical",
        "is_phishing": True,
        "trap_type": "Spear Phishing (Correct Context, Wrong Domain)"
    },
    {
        "id": 4,
        "sender": "ceo@cybercorp.com", 
        "subject": "Quick task",
        "body": "I'm in a meeting. Can you buy me 500 in gift cards? Will expense it.",
        "risk_level": "Critical",
        "is_phishing": True,
        "trap_type": "CEO Fraud"
    },
    {
        "id": 5,
        "sender": "it-desk@cybercorp.com",
        "subject": "Planned Maintenance",
        "body": "System maintenance is scheduled for Saturday at 2 AM. No action required.",
        "risk_level": "Safe",
        "is_phishing": False,
        "trap_type": "None"
    },
    {
        "id": 6,
        "sender": "hr-updates@cybercorp.com",
        "subject": "New Benefit Enrollment",
        "body": "Open enrollment starts next week. Visit the HR portal to review options.",
        "risk_level": "Safe",
        "is_phishing": False,
        "trap_type": "None"
    },
        {
        "id": 7,
        "sender": "security-verification@google-mail.com",
        "subject": "Password Reset",
        "body": "Someone requested a password reset. Was this you?",
        "risk_level": "Suspicious",
        "is_phishing": True,
        "trap_type": "Generic Phishing"
    },
    {
        "id": 8,
        "sender": "marketing@cybercorp.com",
        "subject": "New Logo Assets",
        "body": "Attached are the new branding assets for the Q4 campaign.",
        "risk_level": "Safe",
        "is_phishing": False,
        "trap_type": "None"
    },
    {
        "id": 9,
        "sender": "billing@aws-invoices-net.com",
        "subject": "Payment Failed",
        "body": "Your AWS payment failed. Update card immediately to avoid service interruption.",
        "risk_level": "Critical",
        "is_phishing": True,
        "trap_type": "Supply Chain Spoofing"
    },
    {
        "id": 10,
        "sender": "intern@cybercorp.com",
        "subject": "Question about the project",
        "body": "Hey, where should I upload the files?",
        "risk_level": "Safe",
        "is_phishing": False,
        "trap_type": "None"
    }
]

# --- LEVEL 2: LOGS & CONTEXT ---

network_map = """
**Network Topology Map (Confidential)**
- Core Database Server (DB-01): 192.168.1.10
- Web Server (WEB-01): 192.168.1.5
- Backup Server (BK-01): 192.168.1.50
    - *Note: Automated backups run every Wednesday from 02:00 AM to 03:00 AM.*
- Employee Workstations subnet: 192.168.50.x
"""

# Context: Wednesday Morning.
# Trap: High volume traffic at 2:15 AM is actually the Backup Server, not data theft.
logs = """
2024-10-18 01:55:01 INFO  [System] Scheduled Maintenance Checks Complete.
2024-10-18 01:58:12 WARN  [Auth] Failed RDP Login attempt for user 'admin' from 192.168.50.150 (Workstation-22)
2024-10-18 01:58:15 WARN  [Auth] Failed RDP Login attempt for user 'admin' from 192.168.50.150
2024-10-18 01:58:19 WARN  [Auth] Failed RDP Login attempt for user 'admin' from 192.168.50.150
2024-10-18 01:59:00 ERR   [Auth] Brute Force Detected. IP 192.168.50.150 blocked for 5 minutes.
2024-10-18 02:00:01 INFO  [Backup] Job #9912 Started. Destination: 192.168.1.50
2024-10-18 02:05:00 INFO  [Network] High Traffic Detected: Source 192.168.1.10 -> Dest 192.168.1.50 (Protocol: SMB)
2024-10-18 02:10:00 INFO  [Network] Transfer Rate: 850 MB/s. Volume: 50GB transferred.
2024-10-18 02:15:22 WARN  [DB-01] Query Latency High. CPU Usage 85%.
2024-10-18 02:45:00 INFO  [Backup] Job #9912 Completed Successfully. Total Size: 450 GB.
2024-10-18 03:01:00 INFO  [System] Daily Health Check OK.
2024-10-18 04:15:10 CRIT  [File Integrity] Unexpected file "README_DECRYPT.txt" created in C:/Users/Public/
"""

# --- LEVEL 3: RANSOMWARE ---

ransom_note = """
*** YOUR FILES ARE ENCRYPTED ***
We have locked all your customer databases with military-grade encryption.
You have 48 hours to pay 50 BTC.
If you do not pay, we will delete the decryption key AND release your customer data to the dark web.
Contact: dark_overlord@onion.mail
"""

ceo_msg = """
"I don't care about the technical details! Our stock price is tanking!
I need a decision by EOD. 
Option 1: We pay them. 
Option 2: We don't.
And whatever we do, write a press release that makes us look like victims, not incompetents. 
Don't admit we lost data unless you absolutely have to."
"""
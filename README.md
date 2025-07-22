# Secure Input Monitoring Tool (Python)

A lightweight, ethically-designed keylogger built in Python for educational use, red team simulation, and behavioral analysis training. This project demonstrates how keystroke monitoring can be implemented securely and analyzed to extract meaningful insights.

---

## Features

-  Logs all keystrokes with timestamps
-  Detects and labels special keys (e.g., [ENTER], [SPACE], [ESC])
-  Optional email alerting after a defined number of keystrokes (Gmail App Password compatible)
-  Clean exit with [ESC] key
-  Includes behavioral analysis script for parsing logs, detecting sensitive phrases, and measuring typing speed

---

##  Technologies

- Python 3.13+
- `pynput` (for keypress monitoring)
- `smtplib` (for email sending)
- Standard Python libraries (`datetime`, `logging`, etc.)

---

##  Setup

1. Clone the repo:
```bash
git clone https://github.com/rnz2004/python-keylogger.git
cd python-keylogger
```

2. Install dependencies:
```bash
python -m pip install -r requirements.txt
```

3. Run the keylogger:
```bash
python enhanced_keylogger.py
```

Logs will be saved to `logs/keylog.txt`. Press `[ESC]` to stop the logger.

---

## Enable Email Reporting (Optional)

1. Open `enhanced_keylogger.py`
2. Set `EMAIL_REPORT = True`
3. Update the `EMAIL_CONFIG` section with:
   - Your Gmail address
   - A 16-character App Password from [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

---

##  Log Behavior Analysis

This project includes `analyze_logs.py`, a companion script to analyze your keylog data:

### Features:
- Detects sensitive phrases like `password`, `login`, `admin`
- Calculates average typing speed (in seconds)
- Displays total keystrokes captured

### Run It:

```bash
python analyze_logs.py
```

### Example Output:

```
Keylog Analysis Summary
------------------------------
Total keystrokes captured: 103
Average typing delay (sec): 0.81
Suspicious keywords detected: ['login', 'admin']
```

---

## Sample Log Snippet

```
2025-07-22 13:41:03 - u
2025-07-22 13:41:04 - s
2025-07-22 13:41:04 - e
2025-07-22 13:41:05 - r
2025-07-22 13:41:06 - [SPACE]
2025-07-22 13:41:07 - l
2025-07-22 13:41:08 - o
2025-07-22 13:41:08 - g
2025-07-22 13:41:09 - i
2025-07-22 13:41:09 - n
2025-07-22 13:41:11 - [ENTER]
```

> This sequence could suggest a login attempt and can be used to simulate red team activity or train SOC analysts in behavioral detection techniques.

---

## Legal & Ethical Disclaimer

> This tool is for **educational purposes only**. Do **not** use this on systems you do not own or without explicit permission. Unauthorized use may be illegal and unethical.

---

## Author

**Raif Zaman**  
[GitHub](https://github.com/rnz2004) • [LinkedIn](https://www.linkedin.com/in/raif-zaman)

---

## 📄 License

MIT License

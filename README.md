# 🛡️ SOC Log Analyzer

A Python-based Command Line Interface (CLI) tool that analyzes security log files and generates a detailed scan report.

This project was built as part of my cybersecurity learning journey to practice Python scripting, Regular Expressions, file handling, and terminal-based application development.

---

## ✨ Features

- 📂 Read security log files
- 📊 Count:
  - Total Lines
  - Total Words
  - Total Characters
- 📈 Analyze log entries:
  - INFO
  - WARNING
  - ERROR
- 📧 Extract Email Addresses
- 🌐 Extract IPv4 Addresses
- 📁 Display File Size
- 📅 Show Scan Date & Time
- 💾 Save generated reports
- 🎨 Colored terminal output
- ⏳ Animated loading screens
- ⚠ Error handling for missing files

---

## 🛠 Technologies Used

- Python 3
- Regular Expressions (re)
- os Module
- datetime Module
- ANSI Terminal Colors

---

## 📸 Example Output

```text
==============================
      SOC LOG ANALYZER
==============================

Initializing..........
Loading Modules..........
Preparing Scanner..........

Ready!

Opening Log File..........
Reading File..........
Analyzing..........

File Loaded Successfully!

==============================
      FILE STATISTICS
==============================

File Name         : server.log
File Size         : 520 Bytes
Total Lines       : 18
Total Words       : 145
Total Characters  : 932

INFO Entries      : 12
WARNING Entries   : 3
ERROR Entries     : 2

Emails Found      : 4
IP Addresses      : 6

Scan Date         : 12-07-2026
Scan Time         : 22:15:48
```

---

## 📂 Project Structure

```
soc-log-analyzer/
│
├── main.py
├── sample.log
├── README.md
└── report.txt
```

---

## 🚀 Future Improvements

- Progress Bar
- Spinner Animation
- Duplicate IP Detection
- Duplicate Email Detection
- Hash Detection
- CSV Report Export
- JSON Report Export
- Better Log Parsing
- Menu-Based Interface

---

## 🎯 Learning Outcomes

This project helped me practice:

- Python Programming
- File Handling
- Exception Handling
- Regular Expressions
- CLI Development
- Report Generation
- Terminal Animations
- Basic Security Log Analysis

---

## 👨‍💻 Author

**Yuvraj Singh**

Cybersecurity Student | Python Learner | Aspiring Ethical Hacker

---

⭐ If you found this project useful, consider giving it a star.

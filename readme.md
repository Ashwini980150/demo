# 🎓 Student Resource Sharing Platform

A modern, interactive web application built with **Streamlit** to help college students easily upload, search, download study materials, explore learning resources, and view college announcements.

---

## ✨ Features

- **👤 Student Profile**: Personalize your session by entering your name and selecting your current academic semester.
- **📚 Study Materials**:
  - **Subject Filtering**: Browse materials by subject (Python, Data Structures, Mathematics, Computer Science, etc.).
  - **PDF Upload**: Upload course materials and PDF notes directly to the platform.
  - **Search**: Fast file search functionality to find relevant study guides.
  - **Download**: One-click PDF download for all available materials.
- **🔗 Useful Resources**: Quick access to official documentation, coding practice platforms (LeetCode, HackerRank, GeeksforGeeks), and curated learning materials.
- **📢 Announcements**: Stay updated with important college notices, hackathon alerts, and updates.
- **🎮 Additional Utilities**: Includes utility scripts like `project1.py` (a word-guessing game) and `test/calculator.py`.

---

## 🛠️ Tech Stack

- **Frontend & Backend Framework**: [Streamlit](https://streamlit.io/)
- **Programming Language**: Python 3.x
- **Storage**: Local filesystem storage (`materials/` folder for PDF files)

---

## 📁 Project Structure

```text
.
├── app.py               # Main Streamlit application
├── materials/           # Storage directory for uploaded PDF study materials
├── announcements.json   # College announcements data
├── project1.py          # Terminal-based fruit word guessing game
├── test/
│   └── calculator.py    # Console calculator script
├── .gitignore           # Git ignore file
└── README.md            # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have **Python 3.8+** installed on your system.

### 1. Installation

Clone this repository or download the project files, then install the required dependencies:

```bash
pip install streamlit
```

### 2. Running the Application

Launch the Streamlit app by running:

```bash
streamlit run app.py
```

The web application will automatically open in your default browser at `http://localhost:8501`.

---

## 📝 License

This project is open-source and available for educational and student use.

# 📄 Resume Scanner System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red?style=for-the-badge&logo=streamlit&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-blueviolet?style=for-the-badge&logo=apache&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-Text_Processing-009900?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/sohail189/resume-scanner-system-?style=for-the-badge)

**An AI-powered Resume Scanner that reads PDF, DOCX, and TXT resumes, processes them with NLP, and predicts the candidate's job category using Machine Learning.**

[🚀 Run Locally](#-installation) · [🔍 How It Works](#-how-it-works) · [📊 Features](#-features) · [🐛 Report Bug](https://github.com/sohail189/resume-scanner-system-/issues)

</div>

---

## 📝 Description

The **Resume Scanner System** is an AI-powered hiring assistant built with **Streamlit** and **NLP**. It allows users to upload a resume in any common format — **PDF, DOCX, or TXT** — and automatically:

1. **Extracts** the raw text from the document
2. **Cleans** and preprocesses it using NLP techniques
3. **Vectorises** the text using a trained **TF-IDF** model
4. **Predicts** the candidate's **job category** using a trained **ML classifier**

> 💡 **Real-World Use Case:** HR teams and recruiters can use this tool to automatically screen and categorise hundreds of resumes — saving hours of manual work and reducing hiring bias.

---

## ✨ Features

- 📤 **Multi-Format Upload** — Supports **PDF**, **DOCX**, and **TXT** resume formats
- 🧹 **Automatic Text Cleaning** — Removes noise, special characters, and stopwords via NLP
- 🔢 **TF-IDF Vectorisation** — Converts resume text into numerical features for the ML model
- 🎯 **Job Category Prediction** — Predicts the most suitable job role/category for the resume
- 🏷️ **Label Encoding** — Decodes numeric predictions back to human-readable job categories
- 🖥️ **Clean Streamlit UI** — Simple, fast, and beginner-friendly web interface
- 💾 **Pre-trained Models** — Uses saved `tfidf.pkl` and `encoder.pkl` for instant inference
- 📊 **Resume Dataset** — Trained on `UpdatedResumeDataSet.csv` with multiple job categories

---

## 🔍 How It Works

```
Upload Resume (PDF / DOCX / TXT)
         ↓
   Extract Raw Text
   (PyPDF2 / python-docx)
         ↓
   Clean & Preprocess Text
   (NLTK — remove stopwords,
    punctuation, URLs, numbers)
         ↓
   TF-IDF Vectorisation
   (tfidf.pkl — same vectorizer
    used during training)
         ↓
   ML Model Prediction
   (model.pkl — trained classifier)
         ↓
   Label Decode
   (encoder.pkl → category name)
         ↓
   Display Job Category Result 🎯
```

---

## 🛠️ Technologies Used

| Category | Technology | Purpose |
|---|---|---|
| **UI Framework** | Streamlit | Web interface |
| **Text Extraction** | PyPDF2 | Extract text from PDF |
| **Text Extraction** | python-docx | Extract text from DOCX |
| **NLP Preprocessing** | NLTK | Tokenisation, stopword removal, cleaning |
| **Feature Engineering** | TF-IDF (scikit-learn) | Convert text to numerical vectors |
| **ML Classification** | scikit-learn | Predict job category |
| **Label Encoding** | scikit-learn LabelEncoder | Decode prediction to category name |
| **Data Handling** | Pandas, NumPy | Dataset processing |
| **Language** | Python 3.12 | 100% Python |

---

## 📁 Repository Structure

```
resume-scanner-system-/
│
├── app.py                      ← Main Streamlit application
├── UpdatedResumeDataSet.csv    ← Training dataset (resumes + categories)
│
├── 🤖 Saved Models
│   ├── tfidf.pkl               ← Trained TF-IDF vectorizer
│   └── encoder.pkl             ← Trained Label Encoder
│
├── requirements.txt            ← Python dependencies
└── README.md                   ← Project documentation
```

---

## 🗂️ Dataset

**File:** `UpdatedResumeDataSet.csv`

The dataset contains resumes labelled with their corresponding job categories. Sample categories include:

| Job Category Examples |
|---|
| Data Science |
| Web Designing |
| Mechanical Engineer |
| Sales |
| HR |
| Advocate |
| Arts |
| Fitness |
| Java Developer |
| Business Analyst |
| SAP Developer |
| Automation Testing |
| ETL Developer |
| Operations Manager |
| Python Developer |
| DevOps Engineer |
| Network Security Engineer |
| PMO |
| Database Administrator |
| Hadoop |
| DotNet Developer |
| Blockchain |
| Testing |

---

## 📦 Installation

### Step 1 — Clone the Repository

```bash
git clone https://github.com/sohail189/resume-scanner-system-.git
cd resume-scanner-system-
```

### Step 2 — Create Virtual Environment

```bash
# Anaconda (recommended)
conda create -n resume-scanner python=3.12
conda activate resume-scanner

# Standard venv
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Download NLTK Data (first time only)

```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

### Step 5 — Run the App

```bash
streamlit run app.py
```

App opens at **http://localhost:8501** 🎉

---

## 🚀 Usage

### Scanning a Resume

1. Open the app in your browser at `http://localhost:8501`
2. Click **Browse files** or drag-and-drop your resume
3. Supported formats: **PDF**, **DOCX**, **TXT**
4. Click **Scan Resume** or wait for automatic processing
5. View the predicted **Job Category** result instantly

### Expected Output

```
✅ Resume uploaded successfully!

📄 Extracted Text Preview:
"Experienced Python developer with 3 years of expertise in
Django, Flask, REST APIs, and PostgreSQL..."

🎯 Predicted Job Category:  Python Developer
```

---

## ⚙️ Requirements

```txt
streamlit
scikit-learn
nltk
python-docx
PyPDF2
pandas
numpy
```

Install all:
```bash
pip install -r requirements.txt
```

---

## 🖥️ Demo

> 💡 *Add screenshots of your app here by uploading images to the repo*

```markdown
![Upload Screen](screenshots/upload_screen.png)
![Prediction Result](screenshots/prediction_result.png)
![Text Extraction](screenshots/text_extraction.png)
```

---

## 🔧 Troubleshooting

| Problem | Solution |
|---|---|
| `ModuleNotFoundError: nltk` | Run `pip install nltk` |
| `LookupError: stopwords` | Run `nltk.download('stopwords')` in Python |
| `FileNotFoundError: tfidf.pkl` | Make sure all `.pkl` files are in the same folder as `app.py` |
| PDF text not extracted | Ensure the PDF has selectable text (not a scanned image) |
| DOCX not supported error | Run `pip install python-docx` |
| `streamlit: command not found` | Run `pip install streamlit` |
| Wrong category predicted | The model is trained on English resumes — ensure resume is in English |

---

## 🤝 Contributing

Contributions are welcome!

1. **Fork** the repository
2. **Create** a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit** your changes:
   ```bash
   git commit -m "Add: description of your change"
   ```
4. **Push** and open a **Pull Request**

### 💡 Ideas for Contribution

- [ ] Add support for scanned PDF (OCR using Tesseract)
- [ ] Add skill extraction (Python, SQL, Machine Learning, etc.)
- [ ] Add resume scoring / match percentage against a job description
- [ ] Add ATS (Applicant Tracking System) compatibility check
- [ ] Add support for more job categories
- [ ] Deploy to Streamlit Community Cloud
- [ ] Add multi-resume batch upload and comparison
- [ ] Add downloadable PDF report of the scan result

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute with attribution.

---

## 📬 Contact

**Muhammad Sohail**
*Data Scientist | NLP Engineer | ML Developer*

[![GitHub](https://img.shields.io/badge/GitHub-sohail189-181717?style=flat-square&logo=github)](https://github.com/sohail189)
[![Email](https://img.shields.io/badge/Email-sm7933294@gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:sm7933294@gmail.com)

🔗 **Project Link:** [https://github.com/sohail189/resume-scanner-system-](https://github.com/sohail189/resume-scanner-system-)

---

<div align="center">

Built with ❤️ using NLP, Machine Learning & Python

⭐ **Found this useful? Give it a star!** ⭐

</div>

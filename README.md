# Resume Scanner System  

## 🌈 Resume Category Prediction App  

A **data-powered, ML-driven Resume Scanner** built with **Streamlit**. Upload your resume in **PDF, DOCX, or TXT** format, and the system will **extract, clean, and predict your career category** using Natural Language Processing (NLP) and Machine Learning.  

✨ More than a simple scanner — this is an **AI-powered hiring assistant** designed for clarity, precision, and inclusivity.  


## ⇨ Features  
• Upload & Extract → Supports **PDF, DOCX, and TXT** formats  
• NLP Magic → Cleans and processes text automatically  
• Smart Predictions → Predicts **job category** using trained ML models  
• Elegant Web UI → Built with **Streamlit**  
• Inclusive & Unique → Designed for flexibility across career paths  


## ⇨ Project Structure  



resume-scanner-system/
│
├── app.py → Streamlit application
├── model (1).pkl → Trained ML model
├── tfidf.pkl → TF-IDF vectorizer
├── encoder.pkl → Label encoder
├── requirements.txt → Dependencies
└── README.md → Documentation



## ⇨ Installation  

⮕ Clone the repository:  
```bash
git clone https://github.com/your-username/resume-scanner-system.git
cd resume-scanner-system


⮕ Create a virtual environment:

python -m venv venv
source venv/bin/activate   # Linux/Mac  
venv\Scripts\activate      # Windows  


⮕ Install dependencies:

pip install -r requirements.txt

⇨ Run the App
streamlit run app.py


⮕ Open in your browser:
http://localhost:8501

⇨ Dependencies

• streamlit
• scikit-learn
• nltk
• python-docx
• PyPDF2
• pandas
• numpy

⇨ Demo Preview

Here’s how the app works:

Upload a resume (PDF, DOCX, or TXT)

The system extracts and cleans text → NLP preprocessing

The trained ML model predicts the job role category

Result is displayed in the web app 🎯

⇨ Why This Project?

Resumes are more than text — they’re career stories.
This project uses machine learning to decode, categorize, and highlight talent with transparency and fairness.

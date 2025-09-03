import streamlit as st 
import re 
import pickle
import nltk 

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

#loading models 
model = pickle.load(open(r"C:\Users\Sohail\Desktop\ai travel planner\machine learning\resume project\model (1).pkl", "rb"))
tfidf = pickle.load(open(r"C:\Users\Sohail\Desktop\ai travel planner\machine learning\resume project\tfidf.pkl", "rb"))

#web app
def main():   # FIXED (added colon)
    st.title('RESUME SCANNER SYSTEM')
    uploaded_file = st.file_uploader('Upload Resume', type=['txt','pdf'])  # FIXED (file_Uploader → file_uploader, Uploaded_file → uploaded_file)
    if uploaded_file is not None:
        try:
            resume_bytes = uploaded_file.read()
            resume_text = resume_bytes.decode('utf-8')
        except Exception as e:
            st.error(f"Error reading file: {str(e)}")

# you need to install all these in your terminal
# pip install streamlit
# pip install scikit-learn
# pip install python-docx
# pip install PyPDF2

import docx  # Extract text from Word file
import PyPDF2  # Extract text from PDF

# Load pre-trained model and TF-IDF vectorizer (ensure these are saved earlier)
le = pickle.load(open('encoder.pkl', 'rb'))  # Example file name, adjust as needed

# Function to clean resume text
def cleanResume(txt):
    cleanText = re.sub('http\S+\s', ' ', txt)
    cleanText = re.sub('RT|cc', ' ', cleanText)
    cleanText = re.sub('#\S+\s', ' ', cleanText)
    cleanText = re.sub('@\S+', '  ', cleanText)
    cleanText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)
    cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText)
    cleanText = re.sub('\s+', ' ', cleanText)
    return cleanText

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to extract text from DOCX
def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text

# Function to extract text from TXT with explicit encoding handling
def extract_text_from_txt(file):
    try:
        text = file.read().decode('utf-8')
    except UnicodeDecodeError:
        text = file.read().decode('latin-1')
    return text

# Function to handle file upload and extraction
def handle_file_upload(uploaded_file):
    file_extension = uploaded_file.name.split('.')[-1].lower()
    if file_extension == 'pdf':
        text = extract_text_from_pdf(uploaded_file)
    elif file_extension == 'docx':
        text = extract_text_from_docx(uploaded_file)
    elif file_extension == 'txt':
        text = extract_text_from_txt(uploaded_file)
    else:
        raise ValueError("Unsupported file type. Please upload a PDF, DOCX, or TXT file.")
    return text

# Function to predict the category of a resume
def pred(input_resume):
    cleaned_text = cleanResume(input_resume)
    vectorized_text = tfidf.transform([cleaned_text])
    vectorized_text = vectorized_text.toarray()
    predicted_category = model.predict(vectorized_text)   # FIXED (svc_model → model)
    predicted_category_name = le.inverse_transform(predicted_category)
    return predicted_category_name[0]

# Streamlit app layout
def main():   # FIXED (second main kept same name, Python allows redefinition but this overwrites first)
    st.set_page_config(page_title="Resume Category Prediction", page_icon="📄", layout="wide")

    st.title("Resume Category Prediction App")
    st.markdown("Upload a resume in PDF, TXT, or DOCX format and get the predicted job category.")

    uploaded_file = st.file_uploader("Upload a Resume", type=["pdf", "docx", "txt"])  # FIXED (file_Uploader → file_uploader)

    if uploaded_file is not None:
        try:
            resume_text = handle_file_upload(uploaded_file)
            st.write("Successfully extracted the text from the uploaded resume.")

            if st.checkbox("Show extracted text", False):
                st.text_area("Extracted Resume Text", resume_text, height=300)

            st.subheader("Predicted Category")
            category = pred(resume_text)
            st.write(f"The predicted category of the uploaded resume is: **{category}**")

        except Exception as e:
            st.error(f"Error processing the file: {str(e)}")

if __name__ == "__main__":
    main()

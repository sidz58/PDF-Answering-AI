from transformers import pipeline
import PyPDF2
import re
import numpy
   
def cache_model():
    return pipeline("question-answering", model="test-squad-trained-fullData")

def clean_text(full_file_path):

    pdf_file = open(full_file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    
    for page in pdf_reader.pages:
        text += page.extract_text()
    pdf_file.close()

    # Remove unwanted characters
    text = text.replace('\n', ' ').replace('\xa0', ' ').replace('\uf0b7', ' ').replace('\uf0a7', ' ')
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)
    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    # TRIAL: Remove punctutations
    text = text.replace(',', '').replace(';', '').replace('!', '').replace(':', '').replace('.', '')
    # TRIAL: Remove 'and'
    text = text.replace('and', ' ').strip()



    return text


# filename will come from our uploaded files. qa_model will come from the cache
def getPrediction(question_string, filename, qa_model):
    
    pdf_path = 'static/' + filename # to input the file path to PyPDF2
    # Extracting text and cleaning it
    cleaned_text = clean_text(pdf_path)

    # getting the answer string from the model
    answer = qa_model(question = question_string, context = cleaned_text)['answer']

    return answer




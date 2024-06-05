import fitz  # PyMuPDF
import docx
import os

# Directory containing the documents
doc_dir = r'C:\Users\Elena\Documents\GitHub\Imigration_project_new_res\prepering_data\Infoormation_for_clean'

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function to extract text from DOCX
def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

# Extract text from all files in the directory
def extract_all_text(directory):
    all_text = {}
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            file_path = os.path.join(directory, filename)
            all_text[filename] = extract_text_from_pdf(file_path)
        elif filename.endswith(".docx"):
            file_path = os.path.join(directory, filename)
            all_text[filename] = extract_text_from_docx(file_path)
    return all_text

# Extract text from the documents
extracted_text = extract_all_text(doc_dir)

# Save the extracted text to a JSON file for further processing
import json
with open('extracted_text.json', 'w') as f:
    json.dump(extracted_text, f, indent=4)

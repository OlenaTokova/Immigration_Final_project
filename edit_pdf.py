import os
from flask import Blueprint, render_template, request, jsonify, send_from_directory
import logging

edit_pdf_app = Blueprint('edit_pdf_app', __name__)

@edit_pdf_app.route('/applications')
def applications():
    pdf_path = 'C:/Users/Elena/Documents/GitHub/Imigration_project_new_res/Addition_information'
    pdf_files = [f for f in os.listdir(pdf_path) if f.endswith('.pdf')]
    logging.debug(f'PDF files found: {pdf_files}')
    return render_template('applications.html', pdf_files=pdf_files, pdf_path=pdf_path)

@edit_pdf_app.route('/view-pdf/<filename>')
def view_pdf(filename):
    logging.debug(f'Viewing PDF: {filename}')
    return send_from_directory('C:/Users/Elena/Documents/GitHub/Imigration_project_new_res/Addition_information', filename)

@edit_pdf_app.route('/edit-pdf/<filename>')
def edit_pdf(filename):
    logging.debug(f'Editing PDF: {filename}')
    return render_template('edit_pdf.html', filename=filename)

@edit_pdf_app.route('/save-pdf', methods=['POST'])
def save_pdf():
    data = request.json
    file_name = data['fileName']
    pdf_data = data['pdfData']
    save_path = os.path.join('C:/Users/Elena/Documents/GitHub/Imigration_project_new_res/pdf_Application', file_name)
    logging.debug(f'Saving PDF: {file_name} at {save_path}')

    with open(save_path, 'wb') as f:
        f.write(bytes.fromhex(pdf_data))
    
    return jsonify({"message": "PDF saved successfully!"})

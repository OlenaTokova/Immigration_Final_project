import os
from flask import Flask, render_template, request, jsonify, send_from_directory, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import logging
import speech_recognition as sr
from pydub import AudioSegment
from forms import ClientForm
from models import db, Client
import openai
from translator import transcribe_audio, translate_text
import requests

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/voice-recorder')
def voice_recorder():
    return render_template('voice_to_text.html')

@app.route('/visa')
def visa():
    return render_template('visa.html')

@app.route('/visa/immigrant')
def immigrant_visas():
    return render_template('immigrant_visas.html')

@app.route('/visa/non-immigrant')
def non_immigrant_visas():
    return render_template('non_immigrant_visas.html')

@app.route('/client-info', methods=['GET', 'POST'])
def client_info():
    form = ClientForm()
    if form.validate_on_submit():
        client = Client(
            full_name=form.full_name.data,
            alien_registration_number=form.alien_registration_number.data,
            uscis_online_account_number=form.uscis_online_account_number.data,
            date_of_birth=form.date_of_birth.data.strftime('%m/%d/%Y'),
            country_of_birth=form.country_of_birth.data,
            country_of_citizenship=form.country_of_citizenship.data,
            ssn=form.ssn.data,
            gender=form.gender.data,
            marital_status=form.marital_status.data,
            spouse_full_name=form.spouse_full_name.data,
            marriage_date=form.marriage_date.data,
            number_of_children=form.number_of_children.data,
            children_names_dobs=form.children_names_dobs.data,
            physical_address=form.physical_address.data,
            mailing_address=form.mailing_address.data,
            telephone_number=form.telephone_number.data,
            email_address=form.email_address.data,
            residential_history=form.residential_history.data,
            employment_status=form.employment_status.data,
            current_employer_name_address=form.current_employer_name_address.data,
            job_title=form.job_title.data,
            start_date_current_job=form.start_date_current_job.data,
            employment_history=form.employment_history.data,
            previous_us_visas=form.previous_us_visas.data,
            previous_us_entries=form.previous_us_entries.data,
            deportation_history=form.deportation_history.data,
            criminal_history=form.criminal_history.data,
            political_social_orgs=form.political_social_orgs.data,
            languages_spoken=form.languages_spoken.data,
            emergency_contact=form.emergency_contact.data,
            other_citizenship=form.other_citizenship.data,
            travel_purpose=form.travel_purpose.data,
            countries_to_visit=form.countries_to_visit.data,
            length_of_trip=form.length_of_trip.data,
            intended_departure_date=form.intended_departure_date.data,
            travel_document_type=form.travel_document_type.data,
            summary=form.summary.data,
        )
        db.session.add(client)
        db.session.commit()
        pdf_file = create_pdf(client)
        flash('Client information has been saved!', 'success')
        return send_from_directory(directory='client_applications', path=pdf_file, as_attachment=True)
    return render_template('client.html', form=form)

@app.route('/applications')
def applications():
    pdf_path = 'C:/Users/Elena/Documents/GitHub/Imigration_project_new_res/Addition_information'
    pdf_files = [f for f in os.listdir(pdf_path) if f.endswith('.pdf')]
    app.logger.debug(f'PDF files found: {pdf_files}')
    return render_template('applications.html', pdf_files=pdf_files, pdf_path=pdf_path)

@app.route('/view-pdf/<filename>')
def view_pdf(filename):
    app.logger.debug(f'Viewing PDF: {filename}')
    return send_from_directory('C:/Users/Elena/Documents/GitHub/Imigration_project_new_res/Addition_information', filename)

@app.route('/edit-pdf/<filename>')
def edit_pdf(filename):
    app.logger.debug(f'Editing PDF: {filename}')
    return render_template('edit_pdf.html', filename=filename)

@app.route('/save-pdf', methods=['POST'])
def save_pdf():
    data = request.json
    file_name = data['fileName']
    pdf_data = data['pdfData']
    save_path = os.path.join('C:/Users/Elena/Documents/GitHub/Imigration_project_new_res/pdf_Application', file_name)
    app.logger.debug(f'Saving PDF: {file_name} at {save_path}')

    with open(save_path, 'wb') as f:
        f.write(bytes.fromhex(pdf_data))
    
    return jsonify({"message": "PDF saved successfully!"})



@app.route('/online-helper', methods=['GET', 'POST'])
def online_helper():
    if request.method == 'POST':
        user_info = request.form['user_info']
        response = requests.post('http://localhost:5000/get-advice', json={'user_info': user_info})
        
        if response.status_code == 200:
            try:
                response_data = response.json()
                advice = response_data.get('advice', 'No advice available')
            except requests.exceptions.JSONDecodeError as e:
                advice = f"Error decoding response: {str(e)}"
        else:
            advice = f"Error: Received status code {response.status_code}"
        
        return render_template('online_helper_result.html', advice=advice)
    return render_template('online_helper.html')

def create_pdf(client):
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas

    pdf_file = os.path.join('client_applications', f'{client.full_name.replace(" ", "_")}.pdf')
    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.drawString(100, 750, f"Full Name: {client.full_name}")
    c.drawString(100, 735, f"Alien Registration Number: {client.alien_registration_number}")
    c.drawString(100, 720, f"USCIS Online Account Number: {client.uscis_online_account_number}")
    c.drawString(100, 705, f"Date of Birth: {client.date_of_birth}")
    c.drawString(100, 690, f"Country of Birth: {client.country_of_birth}")
    c.drawString(100, 675, f"Country of Citizenship: {client.country_of_citizenship}")
    c.drawString(100, 660, f"U.S. Social Security Number: {client.ssn}")
    c.drawString(100, 645, f"Gender: {client.gender}")
    c.drawString(100, 630, f"Marital Status: {client.marital_status}")
    c.drawString(100, 615, f"Number of Children: {client.number_of_children}")
    children_list = eval(client.children_names_dobs) if client.children_names_dobs else []
    for i, child in enumerate(children_list):
        c.drawString(100, 600 - i * 15, f"Child {i+1} - Name: {child['first_name']} {child['last_name']}, Date of Birth: {child['date_of_birth']}")
    c.drawString(100, 540, f"Current Physical Address: {client.physical_address}")
    c.drawString(100, 525, f"Mailing Address: {client.mailing_address}")
    c.drawString(100, 510, f"Telephone Number: {client.telephone_number}")
    c.drawString(100, 495, f"Email Address: {client.email_address}")
    c.drawString(100, 480, f"Residential History: {client.residential_history}")
    c.drawString(100, 465, f"Employment Status: {client.employment_status}")
    c.drawString(100, 450, f"Current Employer Name and Address: {client.current_employer_name_address}")
    c.drawString(100, 435, f"Job Title: {client.job_title}")
    c.drawString(100, 420, f"Start Date of Current Job: {client.start_date_current_job}")
    c.drawString(100, 405, f"Employment History: {client.employment_history}")
    c.drawString(100, 390, f"Previous U.S. Visas: {client.previous_us_visas}")
    c.drawString(100, 375, f"Previous U.S. Entries: {client.previous_us_entries}")
    c.drawString(100, 360, f"Deportation History: {client.deportation_history}")
    c.drawString(100, 345, f"Criminal History: {client.criminal_history}")
    c.drawString(100, 330, f"Political or Social Organizations: {client.political_social_orgs}")
    c.drawString(100, 315, f"Languages Spoken: {client.languages_spoken}")
    c.drawString(100, 300, f"Emergency Contact: {client.emergency_contact}")
    c.drawString(100, 285, f"Other Countries of Citizenship: {client.other_citizenship}")
    c.drawString(100, 270, f"Purpose of Travel: {client.travel_purpose}")
    c.drawString(100, 255, f"Countries to Visit: {client.countries_to_visit}")
    c.drawString(100, 240, f"Expected Length of Trip: {client.length_of_trip}")
    c.drawString(100, 225, f"Date of Intended Departure: {client.intended_departure_date}")
    c.drawString(100, 210, f"Travel Document Type: {client.travel_document_type}")
    c.drawString(100, 195, f"Summary: {client.summary}")
    c.save()
    return pdf_file

@app.route('/transcribe', methods=['POST'])
def transcribe_audio_route():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file"}), 400

    audio_file = request.files['audio']
    recognizer = sr.Recognizer()

    try:
        # Convert audio file to WAV format
        audio = AudioSegment.from_file(audio_file)
        audio.export("temp.wav", format="wav")

        # Read the WAV file with speech_recognition
        with sr.AudioFile("temp.wav") as source:
            audio_data = recognizer.record(source)
            transcription = recognizer.recognize_google(audio_data, language="auto")
            return jsonify({"transcription": transcription})
    except sr.UnknownValueError:
        return jsonify({"error": "Could not understand audio"}), 400
    except sr.RequestError as e:
        return jsonify({"error": f"Could not request results from Google Speech Recognition service; {e}"}), 500

@app.route('/translate', methods=['POST'])
def translate_text_route():
    data = request.json
    text = data.get('text')
    target_language = data.get('target_language')

    if not text or not target_language:
        return jsonify({"error": "Text and target language are required."}), 400

    try:
        translation = translate_text(text, target_language)
        return jsonify({"translation": translation})
    except Exception as e:
        logging.error(f"Error translating text: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/get-advice', methods=['POST'])
def get_advice():
    user_info = request.json.get('user_info')
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Replace with your fine-tuned model ID
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_info}
            ],
            max_tokens=150
        )
        
        advice = response.choices[0].message['content'].strip()
        return jsonify({'advice': advice})
    
    except openai.error.OpenAIError as e:
        logging.error(f"OpenAI API error: {e}")
        return jsonify({'error': str(e)}), 500
    
    except Exception as e:
        logging.error(f"General error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)

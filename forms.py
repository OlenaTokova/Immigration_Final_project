from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SubmitField, SelectField, IntegerField, FieldList, FormField
from wtforms.validators import DataRequired, InputRequired
import pycountry

# Utility function to generate a list of countries
def get_country_list():
    return [(country.name, country.name) for country in pycountry.countries]

class ChildForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    date_of_birth = DateField('Date of Birth (mm/dd/yyyy)', format='%m/%d/%Y', validators=[DataRequired()])

class ClientForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    alien_registration_number = StringField('Alien Registration Number')
    uscis_online_account_number = StringField('USCIS Online Account Number')
    date_of_birth = DateField('Date of Birth (mm/dd/yyyy)', format='%m/%d/%Y', validators=[DataRequired()])
    country_of_birth = SelectField('Country of Birth', choices=get_country_list(), validators=[DataRequired()])
    country_of_citizenship = SelectField('Country of Citizenship', choices=get_country_list(), validators=[DataRequired()])
    ssn = StringField('U.S. Social Security Number')
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], validators=[DataRequired()])
    marital_status = SelectField('Marital Status', choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')], validators=[DataRequired()])
    number_of_children = IntegerField('Number of Children', validators=[InputRequired()])
    children = FieldList(FormField(ChildForm), min_entries=0)
    physical_address = TextAreaField('Current Physical Address', validators=[DataRequired()])
    mailing_address = TextAreaField('Mailing Address')
    telephone_number = StringField('Telephone Number')
    email_address = StringField('Email Address')
    residential_history = TextAreaField('Residential History')
    employment_status = StringField('Employment Status')
    current_employer_name_address = TextAreaField('Current Employer Name and Address')
    job_title = StringField('Job Title')
    start_date_current_job = StringField('Start Date of Current Job')
    employment_history = TextAreaField('Employment History')
    previous_us_visas = TextAreaField('Previous U.S. Visas')
    previous_us_entries = TextAreaField('Previous U.S. Entries')
    deportation_history = TextAreaField('Deportation History')
    criminal_history = TextAreaField('Criminal History')
    political_social_orgs = TextAreaField('Political or Social Organizations')
    languages_spoken = StringField('Languages Spoken', validators=[DataRequired()])
    emergency_contact = TextAreaField('Emergency Contact')
    other_citizenship = TextAreaField('Other Countries of Citizenship')
    travel_purpose = TextAreaField('Purpose of Travel')
    countries_to_visit = TextAreaField('Countries to Visit')
    length_of_trip = TextAreaField('Expected Length of Trip')
    intended_departure_date = StringField('Date of Intended Departure')
    travel_document_type = StringField('Travel Document Type')
    summary = TextAreaField('Summary')
    submit = SubmitField('Submit')

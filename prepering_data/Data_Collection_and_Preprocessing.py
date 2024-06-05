import json
import re

# Load your data (this example assumes you have a list of documents)
documents = ["Visitor_Visa.docx"]

# Function to clean and preprocess text
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'\n+', ' ', text)  # Remove new lines
    return text

# Example of extracted and cleaned text from Visitor_Visa.docx
extracted_data = {
    "Visa Type": "Visitor Visa",
    "Description": clean_text("Generally a citizen of a foreign country who wishes to enter the United States must first obtain a visa either a nonimmigrant visa for a temporary stay or an immigrant visa for permanent residence. Visitor visas are nonimmigrant visas for persons who want to enter the United States temporarily for business (visa category B-1) for tourism (visa category B-2) or for a combination of both purposes (B-1/B-2)."),
    "Permitted Activities": clean_text("Consult with business associates, Attend a scientific educational professional or business convention or conference, Settle an estate, Negotiate a contract."),
    "Not Permitted Activities": clean_text("Study, Employment, Paid performances or any professional performance before a paying audience, Arrival as a crewmember on a ship or aircraft, Work as foreign press in radio film print journalism or other information media, Permanent residence in the United States."),
    "Application Process": clean_text("Complete the Online Visa Application, Form DS-160, print the application form confirmation page to bring to your interview, upload your photo, schedule an interview.")
}

# Save the extracted data to a JSON file for training
with open('visa_data.json', 'w') as outfile:
    json.dump(extracted_data, outfile, indent=4)

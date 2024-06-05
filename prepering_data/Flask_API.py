from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = 'YOUR_API_KEY'


def rule_based_advice(user_info):
    if "student" in user_info.lower() and "visa" in user_info.lower():
        return "You might be eligible for an F-1 Student Visa."
    elif "work" in user_info.lower() and "visa" in user_info.lower():
        return "You might be eligible for an H-1B Work Visa."
    else:
        return "Please provide more details about your situation."

@app.route('/get-advice', methods=['POST'])
def get_advice():
    user_info = request.json.get('user_info')
    advice = rule_based_advice(user_info)

    if advice == "Please provide more details about your situation.":
        response = openai.Completion.create(
            model="fine_tuned_model_id",
            prompt=user_info,
            max_tokens=150
        )
        advice = response.choices[0].text.strip()
    
    return jsonify({'advice': advice})

if __name__ == '__main__':
    app.run(debug=True)

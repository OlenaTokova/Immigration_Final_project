def rule_based_advice(user_info):
    if "student" in user_info.lower() and "visa" in user_info.lower():
        return "You might be eligible for an F-1 Student Visa."
    elif "work" in user_info.lower() and "visa" in user_info.lower():
        return "You might be eligible for an H-1B Work Visa."
    else:
        return "Please provide more details about your situation."

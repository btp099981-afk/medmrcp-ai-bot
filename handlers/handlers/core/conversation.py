
patient_answers = {
    "name": "My name is Ahmed.",
    "age": "I am 55 years old.",
    "symptom": "I have chest pain.",
    "location": "The pain is in the center of my chest.",
    "onset": "It started 2 hours ago.",
    "character": "It feels like pressure.",
    "radiation": "It goes to my left arm.",
    "associated": "I have sweating and shortness of breath."
}


def get_patient_response(question):

    question = question.lower()

    if "name" in question:
        return patient_answers["name"]

    elif "age" in question:
        return patient_answers["age"]

    elif "pain" in question or "symptom" in question:
        return patient_answers["symptom"]

    elif "where" in question or "location" in question:
        return patient_answers["location"]

    elif "when" in question or "start" in question:
        return patient_answers["onset"]

    elif "feel" in question or "character" in question:
        return patient_answers["character"]

    elif "radiat" in question or "spread" in question:
        return patient_answers["radiation"]

    elif "associated" in question or "other" in question:
        return patient_answers["associated"]

    else:
        return "I am not sure. Could you ask another question?"

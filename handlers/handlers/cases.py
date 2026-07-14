
from modules.internal_medicine.cardiovascular.history_cases import chest_pain_case


def get_chest_pain_case():

    return (
        f"🧑 Patient: {chest_pain_case['patient']['name']}\n"
        f"Age: {chest_pain_case['patient']['age']}\n\n"
        f"Chief complaint:\n"
        f"{chest_pain_case['complaint']}\n\n"
        "Start taking the history."
    )

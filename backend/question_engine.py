from typing import Dict, List


QUESTIONS = [
    {
        "key": "city",
        "question": "Aap kis city mein building banana chahte hain?",
        "type": "text",
        "required": True,
    },
    {
        "key": "building_type",
        "question": "Building residential house, bungalow, commercial plaza ya apartment hai?",
        "type": "text",
        "required": True,
    },
    {
        "key": "plot_width",
        "question": "Plot ki width kitni hai?",
        "type": "number",
        "required": True,
    },
    {
        "key": "plot_length",
        "question": "Plot ki length/depth kitni hai?",
        "type": "number",
        "required": True,
    },
    {
        "key": "floors",
        "question": "Aap kitne floors banana chahte hain?",
        "type": "number",
        "required": False,
    },
    {
        "key": "bedrooms",
        "question": "Kitne bedrooms chahiye?",
        "type": "number",
        "required": False,
    },
    {
        "key": "bathrooms",
        "question": "Kitne bathrooms chahiye?",
        "type": "number",
        "required": False,
    },
    {
        "key": "car_parking",
        "question": "Kitni cars ki parking chahiye?",
        "type": "number",
        "required": False,
    },
    {
        "key": "special_requirements",
        "question": "Koi special requirement hai? Misal ke taur par lawn, servant room, office ya separate entrance.",
        "type": "text",
        "required": False,
    },
]


def get_next_question(answers: Dict) -> Dict:
    """
    Return the first unanswered required question.
    """

    for question in QUESTIONS:
        key = question["key"]

        if question["required"] and not answers.get(key):
            return question

    # After required information is collected,
    # ask optional questions one by one.
    for question in QUESTIONS:
        key = question["key"]

        if not answers.get(key):
            return question

    return {
        "key": None,
        "question": "Basic requirements complete.",
        "type": "complete",
        "required": False,
    }


def get_all_questions() -> List[Dict]:
    return QUESTIONS

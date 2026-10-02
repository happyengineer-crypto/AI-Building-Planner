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
        "question": "Building type kya hai? Residential house, bungalow, commercial plaza ya apartment?",
        "type": "text",
        "required": True,
    },
    {
        "key": "floors",
        "question": "Aap kitne floors banana chahte hain?",
        "type": "number",
        "required": True,
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
        "key": "kitchen",
        "question": "Kitni kitchens chahiye?",
        "type": "number",
        "required": False,
    },
    {
        "key": "servant_room",
        "question": "Kya servant room chahiye?",
        "type": "text",
        "required": False,
    },
    {
        "key": "special_requirements",
        "question": "Koi special requirement hai? Misal ke taur par lawn, office, separate entrance ya store room.",
        "type": "text",
        "required": False,
    },
]


def get_next_question(answers: Dict) -> Dict:
    """
    Return the first unanswered required question.
    After required questions are completed,
    return optional questions one by one.
    """

    # First ask required questions
    for question in QUESTIONS:
        key = question["key"]

        if question["required"] and not answers.get(key):
            return question

    # Then ask optional questions
    for question in QUESTIONS:
        key = question["key"]

        if not answers.get(key):
            return question

    # All questions completed
    return {
        "key": None,
        "question": "Basic building requirements complete.",
        "type": "complete",
        "required": False,
    }


def get_all_questions() -> List[Dict]:
    return QUESTIONS

import difflib

# Hardcoded dataset of questions and answers
FAQ_DATA = [
    {
        "question": "What does the eligibility verification agent (EVA) do?",
        "answer": "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
    },
    {
        "question": "What does the claims processing agent (CAM) do?",
        "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
    },
    {
        "question": "How does the payment posting agent (PHIL) work?",
        "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
    }
]

GENERIC_RESPONSE = "I'm not sure about that, but I'll find out for you!"

def support_response(user_question):
    questions = [item['question'] for item in FAQ_DATA]
    match = difflib.get_close_matches(user_question, questions, n=1, cutoff=0.4)
    if match:
        for item in FAQ_DATA:
            if item['question'] == match[0]:
                return item['answer']
    return GENERIC_RESPONSE

def chat():
    print("Welcome to Thoughtful AI Support. Ask me a question (type 'exit' to quit).")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = support_response(user_input)
        print(f"AI: {response}")

if __name__ == "__main__":
    chat()

quiz = [
    {
        "question": "What is the capital of Nigeria?",
        "options": ["A. Abuja", "B. Lagos", "C. Port Harcourt", "D. Kano"],
        "answer": "A"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 7"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
        "answer": "C"
    }
]

score = 0

def run_quiz():
    global score

    for q in quiz:
        print("\n" + q["question"])
        for options in q["options"]:
            print(options)
        
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong. The correct answer was {q['answer']}.")
    
    print(f"\n Your final score is {score} / {len(quiz)}")


run_quiz()
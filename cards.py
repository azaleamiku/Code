questions = [
    ["What is the capital of France?", "Paris"],
    ["What is 5 + 7?", "12"],
    ["Who created Python?", "Guido"]
]

score = 0  # Total score

for question in questions:
    print(question[0])
    answer = input("Answer: ")

    if answer.strip().lower() == question[1].lower():
        print("Correct")
        score += 1
    else:
        print("Wrong")

print("Your score is:", score, "out of", len(questions))

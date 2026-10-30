# Case Study 10: Examination Question Analysis

answer_key = ["A", "B", "C", "D", "A"]

students = [
    ["A", "B", "C", "D", "A"],
    ["A", "C", "C", "D", "B"],
    ["B", "B", "C", "A", "A"]
]

question_count = len(answer_key)

correct_counts = [0] * question_count

for i in range(len(students)):

    correct = 0

    for j in range(question_count):

        if students[i][j] == answer_key[j]:

            correct = correct + 1

            correct_counts[j] = correct_counts[j] + 1

    incorrect = question_count - correct

    print("Student:", i + 1)

    print("Correct Answers:", correct)

    print("Incorrect Answers:", incorrect)

    print()

for j in range(question_count):

    success_rate = correct_counts[j] / len(students) * 100

    print("Question:", j + 1)

    print("Success Rate:", round(success_rate, 2), "%")

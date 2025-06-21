def get_student_dictionary():
    student_dict = {}
    
    while True:
        student_name = str(input("Enter student name or press the enter key to terminate: "))
        if student_name == "":
            break
        if not student_name.replace(" ", "").isalpha():
            print("Name must contain only letters!")
            continue

        student_score = int(input("Enter student score in range (1 - 10): "))
        if student_score not in range(1, 11):
            print("Score must be between 1 and 10!")
            continue

        if student_name in student_dict:
            student_dict[student_name] += (student_score,)
        else:
            student_dict[student_name] = (student_score, )
        
        print(student_dict)

    return student_dict

# Get student data
student_summary = get_student_dictionary()

print("\nSummary:\n")

# Display student results
for key, value in sorted(student_summary.items()):
    total = sum(value)
    count = len(value)
    average = total / count

    print(f"The student {key} has scores: {value}")
    print(f"{key}'s total score is: {total}")
    print(f"{key}'s average score is: {average:.2f}\n")

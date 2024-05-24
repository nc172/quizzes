import test3_quuestion_format

questions, answers = test3_quuestion_format.read_question("test3_q_f_demo.txt")
answer_key = test3_quuestion_format.read_answer("test3_a_f_demo.txt")
options = "abcd"

print(questions["1"])#print question
print(answers["1"][answer_key["1"]])#print correct statement
print(answer_key["1"])#print the correct letter
print(answers["1"]["a"]) #print option "a" for question 1


print()
print("Test 3 review")
print()
for i in range(1, len(questions) + 1):  # Loop through each question
        print(f"Question {i}: {questions[str(i)]}")
        
        # Print options for each question
        for option in options:
            print(f"{option}. {answers[str(i)][option]}")
        
        # Prompt user for their choice
        print()
        user_ans = input("What is your choice: ").strip().lower()
        print()
        
        
        # Validate user input and provide feedback
        if user_ans in options:
            if user_ans == answer_key[str(i)].lower():
                print("Correct!!!")
            else:
                print("Incorrect!")
                print(f"The correct answer is: {answer_key[str(i)]}. {answers[str(i)][answer_key[str(i)]]}")
                print()
        else:
            print("Invalid option! Please choose a valid option.")
            print()
       
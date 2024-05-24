def read_question(input_filename):
    
    questions = {}
    answers = {}
    temp_question = ""
    with open(input_filename, 'r', encoding='utf-8') as f: 
        for line in f:
            line = line.strip()
            if line:
                #adjust the upper bound if there are more than 300 questions
                if any(line.startswith(str(num)) for num in range(0, 301)):
                    question_number, question_text = line.split('.', 1)
                    question_number = question_number.strip()
                    question_text = question_text.strip()
                    temp_question = question_number
                    answers[temp_question] = {}  # Initialize answers for this question
                    questions[temp_question] = question_text  # Store question text
                elif line.startswith("a.") or line.startswith("b.") or line.startswith("c.") or line.startswith("d."):
                    option, ans = line.split('.', 1)  
                    option = option.strip()
                    ans = ans.strip()
                    answers[temp_question][option] = ans
                
    return questions, answers


def read_answer(filename):
    answers = {}
    with open(filename, 'r', encoding='utf-8-sig') as f:  # Use utf-8-sig encoding
        for line in f:
            line = line.strip()
            if line:
                number, answer = line.split('.', 1)  
                number = number.strip()
                answer = answer.strip()
                answers[number] = answer
    return answers

   
    

if __name__ == "__main__":
    questions, answers = read_question("test3_q_f_demo.txt")
    print(questions["5"])
    print(answers["5"]["a"])
    print(read_answer("test3_q_a_demo.txt"))
    
import tkinter as tk
from tkinter import messagebox
import test3_quuestion_format

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz App")
        self.questions, self.answers, self.answer_key = self.load_questions()
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.current_question = 1

        # Frame to hold all widgets
        self.frame = tk.Frame(master)
        self.frame.pack(expand=True)

        self.question_label = tk.Label(self.frame, text="", wraplength=600, font=("Arial", 28))
        self.question_label.grid(row=0, column=0, columnspan=2, pady=(20, 0))

        self.option_vars = []
        self.option_labels = []
        self.selected_option = tk.StringVar(value="")
        for i, (option, letter) in enumerate(zip("abcd", ["A", "B", "C", "D"])):
            var = tk.StringVar()
            self.option_vars.append(var)
            label = tk.Label(self.frame, text="", font=("Arial", 24))
            self.option_labels.append(label)
            label.grid(row=i+1, column=0, sticky="w", pady=(10, 0))
            tk.Radiobutton(self.frame, text="", variable=self.selected_option, value=option, indicatoron=False, width=10, height=2).grid(row=i+1, column=1, sticky="w", pady=(10, 0))

        self.correct_answer_label = tk.Label(self.frame, text="", font=("Arial", 24))
        self.correct_answer_label.grid(row=len(self.option_vars)+1, column=0, columnspan=2)

        self.submit_button = tk.Button(self.frame, text="Submit", command=self.submit_answer, font=("Arial", 20))
        self.submit_button.grid(row=len(self.option_vars)+2, column=0, columnspan=2, pady=(20, 0))

        self.next_button = tk.Button(self.frame, text="Next", command=self.next_question, state=tk.DISABLED, font=("Arial", 20))
        self.next_button.grid(row=len(self.option_vars)+3, column=0, columnspan=2, pady=(10, 20))

        self.score_label = tk.Label(self.frame, text="Score: Correct: 0, Incorrect: 0", font=("Arial", 18))
        self.score_label.grid(row=len(self.option_vars)+4, column=0, columnspan=2)

        # Center the frame horizontally and vertically
        self.center_window()

    def load_questions(self):
        questions, answers = test3_quuestion_format.read_question("test3_q_f.txt")
        answer_key = test3_quuestion_format.read_answer("test3_a_f.txt")
        
        return questions, answers, answer_key

    def center_window(self):
        self.master.update_idletasks()
        screen_width = 1280
        screen_height = 720
        window_width = self.master.winfo_width()
        window_height = self.master.winfo_height()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.master.geometry(f"1280x720+{x}+{y}")

    def present_question(self):
        self.selected_option.set("")  # Clear the selected option
        question_text = self.questions[str(self.current_question)]
        self.question_label.config(text=f"Question {self.current_question}:\n{question_text}")

        options = ["a", "b", "c", "d"]
        for var, label, option, letter in zip(self.option_vars, self.option_labels, options, ["A", "B", "C", "D"]):
            var.set(option)
            label.config(text=f"{letter}. {self.answers[str(self.current_question)][option]}")

    def submit_answer(self):
        selected_option = self.selected_option.get()

        if not selected_option:
            messagebox.showwarning("Warning", "Please select an option.")
            return

        if selected_option == self.answer_key[str(self.current_question)]:
            self.correct_answers += 1
            self.correct_answer_label.config(text="Correct!", fg="green")
        else:
            self.incorrect_answers += 1
            self.correct_answer_label.config(text=f"Correct answer: {self.answer_key[str(self.current_question)]}", fg="red")

        self.score_label.config(text=f"Score: Correct: {self.correct_answers}, Incorrect: {self.incorrect_answers}")

        self.submit_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.submit_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)
        self.correct_answer_label.config(text="")
        self.current_question += 1
        if self.current_question <= len(self.questions):
            self.present_question()
        else:
            messagebox.showinfo("Quiz Completed", f"Your score: Correct: {self.correct_answers}, Incorrect: {self.incorrect_answers}")
            self.master.destroy()

def main():
    root = tk.Tk()
    root.geometry("1280x720")  # Set initial window size to 1280x720
    app = QuizApp(root)
    app.present_question()
    root.mainloop()

if __name__ == "__main__":
    main()

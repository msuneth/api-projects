from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.title("Quizzler")
        self.score = 0
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        # self.question_text = self.quiz_brain.next_question()
        self.question_text = self.canvas.create_text(150, 125,width=280, text="", font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        #
        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, highlightthickness=0, command=self.right_button_clicked)
        self.right_button.grid(row=2, column=0)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.wrong_button_clicked)
        self.wrong_button.grid(row=2, column=1)
        self.show_next_question()

        self.window.mainloop()

    def right_button_clicked(self):
        status = self.quiz.check_answer("true")
        self.give_feedback(status)

    def wrong_button_clicked(self):
        status = self.quiz.check_answer("false")
        self.give_feedback(status)

    def show_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You have finished the quiz.\n\nFinal Score: {self.score}")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def give_feedback(self,status: bool):
        if status:
            self.canvas.config(bg="green")
            self.score += 1
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.show_next_question)


# #
# # flip_timer = window.after(100, display_random_word)
#
# window.mainloop()

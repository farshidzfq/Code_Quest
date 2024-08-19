import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QFont

class QuizApp(QWidget):
    def __init__(self):
        super().__init__()

        self.correct_answers = 0
        self.incorrect_answers = 0
        
        self.setWindowTitle("بازی کوئیز")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("background-color: #e0f7fa;")
        
        self.questions = [
            {
                "question": "پایتون یک زبان برنامه‌نویسی است که توسط چه کسی ساخته شده است؟",
                "options": ["لینوس توروالدز", "گویدو ون روسم", "یوزف آندرسون"],
                "correct_option": 2
            },
            {
                "question": "کتابخانه معروف پایتون برای محاسبات عددی چیست؟",
                "options": ["Pandas", "NumPy", "Requests"],
                "correct_option": 2
            },
            {
                "question": "کدام نسخه پایتون به عنوان نسخه پایدار و طولانی مدت پشتیبانی می‌شود؟",
                "options": ["Python 2.x", "Python 3.x", "Python 4.x"],
                "correct_option": 2
            },
            {
                "question": "کدام یک از موارد زیر یک زبان اسکریپتی است؟",
                "options": ["Python", "JavaScript", "C++"],
                "correct_option": 1
            },
            {
                "question": "کدام یک از موارد زیر یک کتابخانه پایتون برای یادگیری ماشین است؟",
                "options": ["TensorFlow", "Flask", "Django"],
                "correct_option": 1
            },
            {
                "question": "Pandas برای چه استفاده می‌شود؟",
                "options": ["تحلیل داده", "توسعه وب", "امنیت سایبری"],
                "correct_option": 1
            },
            {
                "question": "Django یک چارچوب برای کدام زبان برنامه‌نویسی است؟",
                "options": ["JavaScript", "Python", "Ruby"],
                "correct_option": 2
            },
            {
                "question": "کدام یک از موارد زیر یک نوع داده در پایتون است؟",
                "options": ["Dictionary", "File", "Image"],
                "correct_option": 1
            },
            {
                "question": "Jupyter Notebook بیشتر برای چه استفاده می‌شود؟",
                "options": ["تحلیل داده", "مدیریت پروژه", "طراحی وب"],
                "correct_option": 1
            },
            {
                "question": "Numpy برای کار با چه نوع داده‌ای استفاده می‌شود؟",
                "options": ["داده‌های عددی", "داده‌های متنی", "داده‌های تصویری"],
                "correct_option": 1
            }
        ]

        self.current_question = 0
        self.score = 0

        self.initUI()

    def initUI(self):
        self.setFont(QFont("Arial", 12))
        
        # Create main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Question label
        self.question_label = QLabel(self.questions[self.current_question]["question"], self)
        self.question_label.setWordWrap(True)
        self.question_label.setStyleSheet("font-weight: bold; font-size: 18px; padding: 20px; border: 2px solid #4CAF50; border-radius: 10px; background-color: #ffffff;")
        main_layout.addWidget(self.question_label)

        # Radio buttons for options
        self.option_buttons = []
        self.option_vars = []
        options_layout = QVBoxLayout()
        for i, option in enumerate(self.questions[self.current_question]["options"]):
            rb = QRadioButton(option, self)
            rb.setStyleSheet("margin: 10px; padding: 10px; font-size: 16px; border: 1px solid #4CAF50; border-radius: 5px;")
            self.option_buttons.append(rb)
            self.option_vars.append(rb)
            options_layout.addWidget(rb)
        main_layout.addLayout(options_layout)
        
        # Feedback labels and submit button layout
        bottom_layout = QHBoxLayout()
        
        # Feedback labels
        self.feedback_label = QLabel(f"درست: {self.correct_answers} نادرست: {self.incorrect_answers}", self)
        self.feedback_label.setStyleSheet("font-size: 16px; padding: 10px;")
        bottom_layout.addWidget(self.feedback_label)
        
        # Submit button
        self.submit_button = QPushButton("ارسال", self)
        self.submit_button.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 15px;
            border-radius: 10px;
            border: none;
        """)
        self.submit_button.clicked.connect(self.check_answer)
        bottom_layout.addWidget(self.submit_button)
        
        main_layout.addLayout(bottom_layout)

    def check_answer(self):
        selected_option = None
        for i, rb in enumerate(self.option_vars):
            if rb.isChecked():
                selected_option = i + 1
        
        if selected_option == self.questions[self.current_question]["correct_option"]:
            self.score += 1
            self.correct_answers += 1
        else:
            self.incorrect_answers += 1
        
        self.current_question += 1
        
        if self.current_question < len(self.questions):
            self.load_next_question()
        else:
            self.show_final_score()

    def load_next_question(self):
        self.question_label.setText(self.questions[self.current_question]["question"])
        
        for i, rb in enumerate(self.option_vars):
            rb.setText(self.questions[self.current_question]["options"][i])
            rb.setChecked(False)

        # Update feedback label
        self.feedback_label.setText(f"درست: {self.correct_answers} نادرست: {self.incorrect_answers}")

    def show_final_score(self):
        QMessageBox.information(self, "نتیجه نهایی", f"امتیاز نهایی شما: {self.score}/{len(self.questions)}\nپاسخ‌های درست: {self.correct_answers}\nپاسخ‌های نادرست: {self.incorrect_answers}")
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    quiz = QuizApp()
    quiz.show()
    sys.exit(app.exec_())

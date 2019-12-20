class Quiz:
    def __init__(self, name):
        self.name = name
        self.students = list()
        self.questions = list()
        self.quiz_scoreboard = dict()
        self.submission_type = dict()

    def add_student(self, student):
        """Add student and initialize the score board."""
        if student:
            if isinstance(student, list):
                self.students.extend(student)
                for stud in student:
                    self.quiz_scoreboard[stud.uid] = 0.00
                    self.submission_type[stud.uid] = None
            else:
                self.students.append(student)
                self.quiz_scoreboard[student.uid] = 0.00
                self.submission_type[student.uid] = None

    def student_eligible(self, student_id):
        is_eligible = False
        stud = None
        for student in self.students:
            if student.uid == student_id:
                is_eligible = True
                stud = student
                break
        return is_eligible, stud

    def get_student_score(self, student):
        if student:
            return self.quiz_scoreboard.get(student.uid, 0.00)
        return None

    def get_student_submission(self, student):
        if student:
            return self.submission_type.get(student.uid, None)
        return None

    def add_student_sub_type(self, student, sub_type):
        if student:
            self.submission_type[student.uid] = sub_type

    def add_student_score(self, student, score):
        if student:
            self.quiz_scoreboard[student.uid] += score

    def add_question(self, question):
        self.questions.append(question)

    def get_questions(self):
        return self.questions

    def get_question(self, question_id):
        ques = None
        for question in self.questions:
            if question.question_id == question_id:
                ques = question
                break
        return ques

    def answer_question(self, student_id, question_id, option_id):
        """Answer the question and update the scoreboard.
        student must be in the list of students.
        """
        ques = self.get_question(question_id)
        is_student_eligible, student = self.student_eligible(student_id)
        if ques and is_student_eligible:
            if ques.get_right_answer() and option_id == ques.get_right_answer().option_id:
                self.add_student_score(student, 1)

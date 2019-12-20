import uuid


class ClassRoom:
    def __init__(self, name):
        """Construct a classroom object and immediately assign a teacher"""
        self.class_id = uuid.uuid4()
        self.name = name
        self.students = list()
        self.quizzes = list()

    def get_students(self):
        return self.students

    def get_quizzes(self):
        return self.quizzes

    def add_quiz(self, quiz):
        self.quizzes.append(quiz)

    def add_student(self, student):
        self.students.append(student)

    def get_student_cumulative_score(self, student_id):
        score = 0
        for quiz in self.quizzes:
            score += quiz.get_student_score(student_id)
        return score

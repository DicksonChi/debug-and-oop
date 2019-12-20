import uuid
from constants import STUDENT, TEACHER


class Person(object):
    """Create the person class.
       This can be either a teacher or a student.
    """
    def __init__(self, name, person_type=None):
        self.name = name
        self.uid = uuid.uuid4()  # just to give a unique identifier
        self.person_type = person_type

    def is_student(self):
        """Check if the object is a student."""
        return self.person_type == STUDENT

    def is_teacher(self):
        """Check if the object is a student."""
        return self.person_type == TEACHER


class Teacher (Person):
    """Inherit the person class"""

    def __init__(self, name, person_type=TEACHER):
        super(Teacher, self).__init__(name, person_type)
        self.classrooms = list()

    def add_class(self, classroom):
        if classroom:
            self.classrooms.append(classroom)

    def is_my_class(self, classroom_id):
        is_classroom = False
        for classroom in self.classrooms:
            if classroom.class_id == classroom_id:
                is_classroom = True
                break
        return is_classroom

    def is_my_student(self, student_id):
        is_student = False
        for classroom in self.classrooms:
            for student in classroom.students:
                if student_id == student.uid:
                    is_student = True
                    break
            if is_student:
                break
        return is_student

    def set_and_assign_quiz(self, classroom, quiz, student):
        if self.is_my_class(classroom.class_id):
            quiz.add_student(student)
            classroom.add_quiz(quiz)

    def get_student_score_all_classes(self, student_id):
        student_score = 0.00
        for classroom in self.classrooms:
            student_score += classroom.get_student_cumulative_score(student_id)
        return student_score


class Student (Person):
    """Inherit the person class"""

    def __init__(self, name, person_type=STUDENT):
        super(Student, self).__init__(name, person_type)

    def answer_quiz(self, quiz, question_id, option_id):
        if quiz:
            quiz.answer_question(self.uid, question_id, option_id)

    def join_class(self, classroom):
        if classroom:
            classroom.add_student(self)

    def submit_quiz(self, quiz, sub_type=None):
        if quiz:
            quiz.add_student_sub_type(self, sub_type)




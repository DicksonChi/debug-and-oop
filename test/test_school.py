from unittest import TestCase
from classRoom import ClassRoom
from person import Teacher, Student
from question import Question
from quiz import Quiz
from option import Option
from constants import PARTIAL_SUBMISSION, FULL_SUBMISSION


class TestSchool(TestCase):

    def setUp(self):
        # test teachers
        self.teacher1 = Teacher("Test Teacher 1")
        self.teacher2 = Teacher("Test Teacher 2")

        # create test class
        self.classroom1 = ClassRoom("Test Classroom 1")
        self.classroom2 = ClassRoom("Test Classroom 2")

        # test student
        self.student1 = Student("Test Student 1")
        self.student2 = Student("Test Student 2")
        self.student3 = Student("Test Student 3")

    def test_teacher_add_class(self):
        self.assertEqual(len(self.teacher1.classrooms), 0)
        self.assertEqual(len(self.teacher2.classrooms), 0)

        # add the classes to teacher
        self.teacher1.add_class(self.classroom1)
        self.teacher2.add_class(self.classroom2)

        self.assertEqual(len(self.teacher1.classrooms), 1)
        self.assertEqual(len(self.teacher2.classrooms), 1)
        self.assertTrue(self.teacher1.is_my_class(self.classroom1.class_id))
        self.assertFalse(self.teacher1.is_my_class(self.classroom2.class_id))
        self.assertTrue(self.teacher2.is_my_class(self.classroom2.class_id))
        self.assertFalse(self.teacher2.is_my_class(self.classroom1.class_id))

    def test_student_join_class(self):
        self.assertEqual(len(self.classroom1.students), 0)
        self.assertEqual(len(self.classroom2.students), 0)

        # student joining classes
        self.student1.join_class(self.classroom1)
        self.student2.join_class(self.classroom1)
        self.student1.join_class(self.classroom2)
        self.student2.join_class(self.classroom2)
        self.student3.join_class(self.classroom2)

        self.assertEqual(len(self.classroom1.students), 2)
        self.assertEqual(len(self.classroom2.students), 3)

        self.assertEqual(self.student3.name, self.classroom2.students[2].name)

    def test_is_my_student(self):
        self.teacher1.add_class(self.classroom1)
        self.teacher2.add_class(self.classroom2)

        self.student1.join_class(self.classroom1)
        self.student2.join_class(self.classroom1)
        self.student1.join_class(self.classroom2)
        self.student2.join_class(self.classroom2)
        self.student3.join_class(self.classroom2)

        self.assertTrue(self.teacher2.is_my_student(self.student1.uid))
        self.assertFalse(self.teacher1.is_my_student(self.student3.uid))


class TestQuizOperations(TestCase):
    def setUp(self):
        # test teachers
        self.teacher1 = Teacher("Test Teacher 1")
        self.teacher2 = Teacher("Test Teacher 2")

        # create test class
        self.classroom1 = ClassRoom("Test Classroom 1")
        self.classroom2 = ClassRoom("Test Classroom 2")

        self.teacher1.add_class(self.classroom1)
        self.teacher2.add_class(self.classroom2)

        # test student
        self.student1 = Student("Test Student 1")
        self.student2 = Student("Test Student 2")
        self.student3 = Student("Test Student 3")

        self.student1.join_class(self.classroom1)
        self.student2.join_class(self.classroom1)
        self.student1.join_class(self.classroom2)
        self.student2.join_class(self.classroom2)
        self.student3.join_class(self.classroom2)

        self.quiz1 = Quiz("Test Quiz")
        question1 = Question(name="test question 1", content="Who is the best Dev you know?")
        option1 = Option("A", content="Dickson")
        option2 = Option("B", content="Nobody")
        question1.add_option(option1)
        question1.add_option(option2)

        question1.choose_right_answer(option1.option_id)

        question2 = Question(name="test question 2", content="Will I be a great addition to FineTune?")
        option1 = Option("A", content="Yes :)")
        option2 = Option("B", content="Yes :)")
        question2.add_option(option1)
        question2.add_option(option2)
        question2.choose_right_answer(option2.option_id)

        self.quiz1.add_question(question1)
        self.quiz1.add_question(question2)

    def test_set_assign_quiz(self):
        self.assertEqual(len(self.quiz1.students), 0)
        students = list()
        students.append(self.student1)
        students.append(self.student2)
        self.teacher1.set_and_assign_quiz(self.classroom1, quiz=self.quiz1, student=students)
        self.assertEqual(len(self.quiz1.students), 2)

    def test_student_answer_question(self):
        # assign students to the quiz
        students = list()
        students.append(self.student1)
        students.append(self.student2)
        self.teacher1.set_and_assign_quiz(self.classroom1, quiz=self.quiz1, student=students)
        # students answer question
        # wrong answer
        self.student1.answer_quiz(self.quiz1, self.quiz1.questions[0].question_id,
                                  self.quiz1.questions[0].options[1].option_id)
        self.student1.submit_quiz(self.quiz1, PARTIAL_SUBMISSION)
        student_quiz_score = self.quiz1.get_student_score(self.student1)

        self.assertEqual(student_quiz_score, 0.00)
        self.assertEqual(self.quiz1.get_student_submission(self.student1), PARTIAL_SUBMISSION)

        # right answer
        self.student1.answer_quiz(self.quiz1, self.quiz1.questions[0].question_id,
                                  self.quiz1.questions[0].options[0].option_id)
        student_quiz_score = self.quiz1.get_student_score(self.student1)
        self.student1.submit_quiz(self.quiz1, FULL_SUBMISSION)
        self.assertEqual(student_quiz_score, 1.00)
        self.assertEqual(self.quiz1.get_student_submission(self.student1), FULL_SUBMISSION)

        # test the get cumulative for a semester by teacher
        student1_cum_score = self.teacher1.get_student_score_all_classes(self.student1)
        student3_cum_score = self.teacher1.get_student_score_all_classes(self.student3)
        self.assertEqual(student1_cum_score, 1.00)
        self.assertEqual(student3_cum_score, 0.00)

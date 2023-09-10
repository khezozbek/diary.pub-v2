from .models import CustomUser, Teacher, Group, Student
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import override_settings
from .signals import create_students
User = get_user_model()


@override_settings(RESTRICT_SIGNALS=True)
class StudentModelTestCase(TestCase):
    def setUp(self):
        with create_students.suppress_signals():
            self.user = CustomUser.objects.create(username='testuser', password='testpassword', first_name='John', last_name='Doe', type='Student')
            self.student = Student.objects.create(user=self.user, level='Beginner')


class TeacherModelTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='testuser', password='testpassword')
        self.teacher = Teacher.objects.create(user=self.user, department='Math')

    def test_teacher_creation(self):
        teacher = Teacher.objects.get(user=self.user)
        self.assertEqual(teacher.user, self.user)
        self.assertEqual(teacher.department, 'Math')

    def test_teacher_groups(self):
        teacher = Teacher.objects.get(user=self.user)
        group1 = Group.objects.create(name='Group 1')
        group2 = Group.objects.create(name='Group 2')
        teacher.groups.add(group1, group2)
        self.assertEqual(teacher.groups.count(), 2)
        self.assertIn(group1, teacher.groups.all())
        self.assertIn(group2, teacher.groups.all())



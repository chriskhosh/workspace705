import datetime
from django.test import TestCase
from .models import resume, education, experience

class ResumeTestCases(TestCase):
    def setUp(self):
        today = datetime.datetime.today()
        resume1 = resume.objects.create(
            first_name='Jon',
            last_name='Shallow'
        )
        experience1 = experience.objects.create(
            full_name=resume1,
            title='Instructor',
            location='UNH Manchester',
            start_date=today,
            end_date=today,
            description='hello from Jon'
        )
        education1 = education.objects.create(
            full_name=resume1,
            institution_name='UNH Manchester',
            degree='Bachelors',
            major='Computer Science',
            gpa=4.0
        )
    def test_instances(self):
        resume1 = resume.objects.first()
        self.assertIsInstance(resume1, resume)
        education1 = education.objects.first()
        self.assertIsInstance(education1, education)
        experience1 = experience.objects.first()
        self.assertIsInstance(experience1, experience)

    def test_get_full_name(self):
        resume1 = resume.objects.first()
        actual = resume1.get_full_name()
        expected = "Jon Shallow"
        self.assertEqual(actual, expected)

    def test_get_last_name_first_name(self):
        resume1 = resume.objects.first()
        actual = resume1.get_last_name_first_name()
        expected = "Shallow, Jon"
        self.assertEqual(actual, expected)

    def test_get_experience(self):
        resume1 = resume.objects.first()
        actual = list(resume1.get_experience())
        expected = list(resume1.experience_set.all())
        self.assertEqual(actual, expected)

    def test_get_education(self):
        resume1 = resume.objects.first()
        actual = list(resume1.get_education())
        expected = list(resume1.education_set.all())
        self.assertEqual(actual, expected)

from django.test import TestCase
import tempfile
from my_works.models import Work, WorkFile, WorkShot


class MyWorkTestCase(TestCase):
    def setUp(self):
        self.work = Work.objects.create(title="Test_work_name1",
                                        description="Test description",
                                        main_photo=tempfile.NamedTemporaryFile(suffix=".jpg").name,
                                        url="test_work_name1",
                                        draft=False)

        self.work_file = WorkFile.objects.create(title="Test_work_name2",
                                                description="Test description",
                                                file=tempfile.NamedTemporaryFile(suffix=".jpg").name,
                                                work=self.work,
                                                )
        self.work_shot = WorkShot.objects.create(title="Test_work_name3",
                                                description="Test description",
                                                image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
                                                work=self.work,
                                                )

    def test_my_works_was_correctly_built(self):
        """Testing My_Works-Model Object"""
        work_test = Work.objects.get(title="Test_work_name1")
        work_file_test = WorkFile.objects.get(pk=1)
        work_shot_test = WorkShot.objects.get(pk=1)
        self.assertEqual(work_file_test.work, work_test)
        self.assertEqual(work_shot_test.work, work_test)

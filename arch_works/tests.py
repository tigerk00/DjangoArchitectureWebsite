from django.test import TestCase
import tempfile
from arch_works.models import Architecture, Architector, Style


class ArchitectureTestCase(TestCase):
    def setUp(self):
        self.architect = Architector.objects.create(name="Test_architect_name1",
                                                    description="Test description",
                                                    image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
                                                    country="Ukraine",
                                                    date_of_birth=1960,
                                                    date_of_death=1980,
                                                    url="test_name1",
                                                    draft=False
                                                    )
        self.style = Style.objects.create( name="Test_style_name2",
                                           description="Test description",
                                           image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
                                           url="test_title2",
                                           draft=False
                                           )

        self.arch = Architecture.objects.create(title="Test_title",
                                                description="Test description",
                                                main_photo=tempfile.NamedTemporaryFile(suffix=".jpg").name,
                                                year=2021,
                                                country="Ukraine",
                                                budget=1000000,
                                                url="test_title",
                                                draft=False
                                                )

        self.arch.architectors.add(self.architect)
        self.arch.styles.add(self.style)

    def test_architecture_was_correctly_built(self):
        """Testing Architecture-Model Object"""
        architecture_test = Architecture.objects.get(url="test_title")
        self.assertEqual(architecture_test.year, 2021)
        self.assertEqual(architecture_test.architectors.all()[0].country, 'Ukraine')
        self.assertEqual(architecture_test.styles.all()[0].name, 'Test_style_name2')
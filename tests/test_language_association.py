from unittest import TestCase
from srccat.language_association import LanguageAssociation


class TestLanguageAssociation(TestCase):


    def setUp(self):
        self.subject = LanguageAssociation()

    def test__call__when_extension_exists(self):
        assert self.subject(".py") == "Python"




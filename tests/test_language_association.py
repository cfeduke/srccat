from unittest import TestCase
from srccat.language_association import LanguageAssociation, DEFAULT_LANGUAGE


class TestLanguageAssociation(TestCase):


    def setUp(self):
        self.subject = LanguageAssociation()

    def test__call__when_extension_exists(self):
        assert self.subject(".py") == "Python"

    def test__call__when_extension_does_not_exist_returns_text_only(self):
        assert self.subject(".nonexistent-ext") == DEFAULT_LANGUAGE




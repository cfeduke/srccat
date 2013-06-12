from unittest import TestCase
from srccat.language_association import LanguageAssociation, DEFAULT_LANGUAGE


class TestLanguageAssociation(TestCase):

    def setUp(self):
        self.subject = LanguageAssociation()

    def test__call__when_extension_exists(self):
        assert self.subject("file.py") == "Python"

    def test__call__when_extension_does_not_exist_returns_text_only(self):
        assert self.subject("file.nonexistent-ext") == DEFAULT_LANGUAGE

    def test__call__when_filename_is_extension(self):
        assert self.subject("gvimrc") == "VimL"

    def test__call__when_extension_only(self):
        assert self.subject(".vimrc") == "VimL"

    def test__call__when_extension_only_2(self):
        assert self.subject(".rb") == "Ruby"




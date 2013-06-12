from extension_language_index import EXTENSION_LANGUAGE_INDEX
import os.path

DEFAULT_LANGUAGE = "Text only"


class LanguageAssociation:
    def __init__(self):
        pass

    def __call__(self, filename):
        filename, ext = os.path.splitext(filename)
        ext = ext or filename
        if ext not in EXTENSION_LANGUAGE_INDEX.keys():
            return DEFAULT_LANGUAGE

        return EXTENSION_LANGUAGE_INDEX[ext]

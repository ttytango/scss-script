# class Functions:
"""
This is written for python 3.8.x rather than for python 3.9 Python 3.9's now contains a built-in PEP 616 method
to remove prefix and suffixes Python 3.9 will not work with windows 7 or earlier however, so I have stuck to
regular expressions for the time being. https://www.python.org/dev/peps/pep-0616/
:rtype: object
"""


def endswith(self, suffix):
    pass


def startswith(self, prefix):
    pass


def remove_affix(word, prefix="_", suffix=".scss"):
    if word.startswith(prefix) and word.endswith(suffix):
        return word[len(prefix):-len(suffix)]

    return word






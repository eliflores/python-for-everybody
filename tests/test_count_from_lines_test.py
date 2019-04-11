import os

from unittest import TestCase

from exercises.count_from_lines import words_in_file


class TestCountFromLines(TestCase):

    def setUp(self) -> None:
        file_name = os.path.join(os.path.dirname(__file__), "mbox_test.txt")
        self.file = open(file_name)

    def test_words_are_counted(self):
        words = words_in_file(self.file)
        self.assertEqual(len(words), 10)

    def test_only_words_used_after_From_are_counted(self):
        words = words_in_file(self.file)
        self.assertListEqual([
            "zqian@umich.edu",
            "rjlowe@iupui.edu",
            "zqian@umich.edu",
            "rjlowe@iupui.edu",
            "cwen@iupui.edu",
            "cwen@iupui.edu",
            "gsilver@umich.edu",
            "gsilver@umich.edu",
            "zqian@umich.edu",
            "gsilver@umich.edu",
        ], words)

    def tearDown(self) -> None:
        self.file.close()

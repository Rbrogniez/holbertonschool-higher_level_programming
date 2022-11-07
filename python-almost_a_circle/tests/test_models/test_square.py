#!/usr/bin/python3
"Unit tests for Rectangle class"
import unittest
from unittest import mock
import io
from models.square import Square


class TestSquare(unittest.TestCase):
    """Testing Square"""

    def test_instance(self):
        """test input size correct standard """

        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

        with self.assertRaises(TypeError):
            Square(5, "1")

        with self.assertRaises(TypeError):
            Square()

        with self.assertRaises(TypeError):
            Square("1")

        with self.assertRaises(ValueError):
            Square(-5, 3, 4)

        with self.assertRaises(TypeError):
            Square(1, 2, "3")

        with self.assertRaises(ValueError):
            Square(1, -2)

        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_case_normal(self):
        """Test of Square(1, 2, 3, 4) exists"""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_area(self):
        """testing area"""
        s = Square(5)
        self.assertEqual(s.area(), 25)

        s = Square(1, 2)
        self.assertEqual(s.area(), 1)

    def test_display(self):
        """test display()"""
        s = Square(5)
        with mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            s.display()

        assert mock_stdout.getvalue() == "#####\n#####\n#####\n#####\n#####\n"

        s = Square(1, 2)
        with mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            s.display()

        assert mock_stdout.getvalue() == "  #\n"

    def test_string(self):
        """Test str"""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.__str__(), '[Square] (4) 2/3 - 1')

    def test_update(self):
        """test update()"""
        s1 = Square(2)
        s1.update(10)
        self.assertEqual(s1.id, 10)
        s1.update(size=1, id=89, x=2)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.x, 2)

    def test_to_dictionary(self):
        """
        Test of to_dictionary() in Square exists
        """
        dict = {'id': 7, 'size': 10, 'x': 9, 'y': 8}
        s = Square(10, 9, 8, 7)
        self.a#!/usr/bin/python3
""" Doc """
import os, sys
import subprocess


def run_command(cmd):
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return "{}{}".format(output, error)


def run_unittest():
    nb_tests = 0
    is_success = False
    try:
        res = run_command("python3 -m unittest discover tests")
        for line in res.split("\\n"):
            if "Ran " in line:
                nb_tests = int(res.split("Ran ")[-1].split(" tests")[0])
            if nb_tests > 0 and "OK" in line:
                is_success = True
    except:
        nb_tests = 0
        is_success = False
    return nb_tests, is_success


# validate tests are passing by default
nb_tests, passing = run_unittest()

if nb_tests <= 0:
    print("No test found")
    exit(1)
if not passing:
    print("Regular tests are not passing")
    exit(1)

file_path_to_update = "models/base.py"
file_path_updated = "models/tmp_base.py"
if not os.path.exists(file_path_to_update):
    print("{} not found".format(file_path_to_update))
    exit(1)

try:
    # Move file
    if os.path.exists(file_path_updated):
        os.remove(file_path_updated)
    os.rename(file_path_to_update, file_path_updated)

    # update file
    new_content = """#!/usr/bin/python3
\"\"\" Random documentation \"\"\"
from models.tmp_base import Base


class Base(Base):
    \"\"\" Random documentation \"\"\"

    def __init__(self, id=None):
        \"\"\" Random documentation \"\"\"
        if id is None:
            self.id = 89
        else:
            super().__init__(id)
"""

    with open(file_path_to_update, "w") as file:
        file.write(new_content)

    # run tests
    nb_tests, passing = run_unittest()
    if nb_tests <= 0:
        print("No test found")
    if passing:
        print("No test found for this case")
except:
    print("An error occured... {}".format(sys.exc_info()[0]))

# rollback file
if os.path.exists(file_path_updated):
    if os.path.exists(file_path_to_update):
        os.remove(file_path_to_update)
    os.rename(file_path_updated, file_path_to_update)

print("OK", end="")
ssertEqual(dict, s.to_dictionary())


if __name__ == "__main__":
    unittest.main()

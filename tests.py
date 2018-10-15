import unittest
from cruiseshIP import validate_ip, notify_change
from unittest.mock import patch
import os


class TestCruiseship(unittest.TestCase):

    @patch('cruiseshIP.urlopen')
    def test_no_file(self, urlopen):
        filename = 'nonexistent.txt'
        fakeip = b'1.1.1.1/n'
        urlopen.return_value.read.return_value = fakeip
        validate_ip(filename)
        with open(filename) as newFile:
            self.assertEqual(
                newFile.readline().split()[0],
                fakeip.decode('utf-8').rstrip())
        os.remove(filename)
        
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()

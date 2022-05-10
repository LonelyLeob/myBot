import unittest
from db import get_auth, get_user

#Admin entry in DB
us_db_id = '738071641'
us_db_pwd = 'rXdqPXHW'

class Test_DB(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_auth(self):
        """Auth user testing"""
        expected = True

        self.assertEqual(get_auth(us_id=us_db_id, msg=us_db_pwd), expected)

    def test_get_user(self):
        expected = (738071641, 'guybtw', 'rXdqPXHW', '2022-05-09 19:23:23.588512', 1, 'Гость', 79113473655, None)

        self.assertEqual(get_user(us_id=us_db_id), expected)

unittest.main()
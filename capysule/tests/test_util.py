import unittest


class TestUtil(unittest.TestCase):

    def test_split_full_name(self):
        from capysule.util import split_full_name
        self.assertEquals(
            split_full_name('Frodo Baggins'),
            ('Frodo', 'Baggins')
        )
        self.assertEquals(
            split_full_name('Frodo L. Baggins'),
            ('Frodo L.', 'Baggins')
        )
        self.assertEquals(
            split_full_name('Gandalf'),
            ('Gandalf', None)
        )
        self.assertEquals(
            split_full_name(''),
            None
        )
        self.assertEquals(
            split_full_name(' '),
            None
        )

import unittest
from cref.sequence import fragment


class SequenceTestCase(unittest.TestCase):

    def test_fragment(self):
        sequence = 'ABCDEFGHIJKLM'
        fragments = list(fragment(sequence, 1))
        self.assertEqual(len(fragments), len(sequence))
        self.assertEqual(fragments[0], 'A')
        self.assertEqual(fragments[-1], 'M')

        fragments = list(fragment('ABCDEFGHIJKLM', 5))
        self.assertEqual(len(fragments), 9)
        self.assertEqual(fragments[0], 'ABCDE')
        self.assertEqual(fragments[-1], 'IJKLM')

        fragments = list(fragment('ABCDEFGHIJKLM', 9))
        self.assertEqual(len(fragments), 5)
        self.assertEqual(fragments[0], 'ABCDEFGHI')
        self.assertEqual(fragments[-1], 'EFGHIJKLM')

    def test_fragment_empty(self):
        with self.assertRaisesRegex(ValueError, 'Cannot create fragments'):
            list(fragment(''))
        with self.assertRaisesRegex(ValueError, 'Cannot create fragments'):
            list(fragment('ABCDEFGHIJKLM', 0))

    def test_fragment_size_overflow(self):
        with self.assertRaisesRegex(ValueError, 'Cannot create fragments'):
            list(fragment('ABCDEFGHIJKLM', 20))

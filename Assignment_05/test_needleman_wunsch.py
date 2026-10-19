import unittest

from needleman_wunsch import needleman_wunsch


class TestNeedlemanWunsch(unittest.TestCase):
    def test_match_and_gap(self):
        self.assertEqual(needleman_wunsch('AC', 'AC'), (2, 'AC', 'AC'))
        self.assertEqual(needleman_wunsch('AC', 'A'), (-1, 'AC', 'A-'))

    def test_alignment_keeps_both_sequences(self):
        score, first, second = needleman_wunsch('GATTACA', 'GCATGCU')
        self.assertEqual(first.replace('-', ''), 'GATTACA')
        self.assertEqual(second.replace('-', ''), 'GCATGCU')
        self.assertEqual(len(first), len(second))
        self.assertEqual(score, sum(1 if a == b else -2 if '-' in (a, b) else -1
                                    for a, b in zip(first, second)))


if __name__ == '__main__':
    unittest.main()

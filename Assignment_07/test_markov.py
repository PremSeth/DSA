import unittest
from pathlib import Path

from markov_text_analysis_and_generation import following, generate, make_model


class TestMarkov(unittest.TestCase):
    def test_following_counts(self) -> None:
        model = make_model('Cat sat. Cat slept. Cat sat.')
        self.assertEqual(following(model, 'cat'), {'sat': 2, 'slept': 1})
        self.assertEqual(following(model, 'sat'), {'cat': 1})

    def test_missing_word(self) -> None:
        self.assertEqual(following(make_model('one word'), 'missing'), {})
        self.assertEqual(following(make_model('one word'), 'WORD'), {})

    def test_peter_rabbit(self) -> None:
        text = Path(__file__).with_name('peter_rabbit_gutenberg_14838.txt').read_text(encoding='utf-8')
        model = make_model(text)
        self.assertEqual(following(model, 'peter')['was'], 3)
        self.assertEqual(following(model, 'the')['gate'], 5)

    def test_generate(self) -> None:
        model = make_model('cat sat cat sat')
        self.assertEqual(generate(model, 'cat', 4), 'cat sat cat sat')
        self.assertEqual(generate(model, 'missing', 4), 'missing')
        self.assertEqual(generate(model, 'cat', 0), '')

    def test_generated_words_follow_the_model(self) -> None:
        model = make_model('cat sat cat slept cat ran cat sat')
        words = generate(model, 'cat', 20, seed=2026).split()
        for first, second in zip(words, words[1:]):
            self.assertIn(second, following(model, first))


if __name__ == '__main__':
    unittest.main()

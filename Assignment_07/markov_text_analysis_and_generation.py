import random
import re
import sys
from pathlib import Path

from associative_array import AssociativeArray


def make_model(text: str) -> AssociativeArray:
    """Count which words come after each word."""
    words = re.findall(r"[a-z]+(?:'[a-z]+)?", text.lower())
    model = AssociativeArray(101)
    for word, next_word in zip(words, words[1:]):
        counts = model.get(word)
        if not isinstance(counts, AssociativeArray):
            counts = AssociativeArray(5)
            model.set(word, counts)
        old_count = counts.get(next_word)
        counts.set(next_word, old_count + 1 if isinstance(old_count, int) else 1)
    return model


def following(model: AssociativeArray, word: str) -> dict[str, int]:
    """Get the counts for words that follow this one."""
    counts = model.get(word.lower())
    if not isinstance(counts, AssociativeArray):
        return {}
    return {key: count for key, count in counts.keyValuePairs()
            if isinstance(key, str) and isinstance(count, int)}


def generate(model: AssociativeArray, start: str, length: int, seed: int | None = None) -> str:
    """Make a string by picking likely next words."""
    if length <= 0:
        return ''
    rng = random.Random(seed)
    words = [start.lower()]
    while len(words) < length:
        counts = following(model, words[-1])
        if not counts:
            break
        choices = sorted(counts)
        words.append(rng.choices(choices, weights=[counts[word] for word in choices])[0])
    return ' '.join(words)


if __name__ == '__main__':
    text = Path(__file__).with_name('peter_rabbit_gutenberg_14838.txt').read_text(encoding='utf-8')
    model = make_model(text)
    if len(sys.argv) > 1 and sys.argv[1] == '--generate':
        start = sys.argv[2] if len(sys.argv) > 2 else 'peter'
        length = int(sys.argv[3]) if len(sys.argv) > 3 else 30
        print(generate(model, start, length))
    else:
        for word in sys.argv[1:] or ['peter']:
            print(word, following(model, word))

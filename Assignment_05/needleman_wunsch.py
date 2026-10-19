def needleman_wunsch(first, second, match=1, mismatch=-1, gap=-2):
    """Return the best global alignment and its score."""
    scores = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]
    for i in range(1, len(first) + 1):
        scores[i][0] = i * gap
    for j in range(1, len(second) + 1):
        scores[0][j] = j * gap

    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            diagonal = scores[i - 1][j - 1] + (match if first[i - 1] == second[j - 1] else mismatch)
            scores[i][j] = max(diagonal, scores[i - 1][j] + gap, scores[i][j - 1] + gap)

    aligned_first = []
    aligned_second = []
    i, j = len(first), len(second)
    while i or j:  # Trace back from the best score.
        if i and j and scores[i][j] == scores[i - 1][j - 1] + (
            match if first[i - 1] == second[j - 1] else mismatch
        ):
            aligned_first.append(first[i - 1])
            aligned_second.append(second[j - 1])
            i -= 1
            j -= 1
        elif i and scores[i][j] == scores[i - 1][j] + gap:
            aligned_first.append(first[i - 1])
            aligned_second.append('-')
            i -= 1
        else:
            aligned_first.append('-')
            aligned_second.append(second[j - 1])
            j -= 1

    aligned_first.reverse()
    aligned_second.reverse()
    return scores[-1][-1], ''.join(aligned_first), ''.join(aligned_second)


if __name__ == '__main__':
    from genome import genomeSnippet, testAgainst

    score, snippet, query = needleman_wunsch(genomeSnippet, testAgainst)
    print(f'Score: {score}')
    print(snippet)
    print(query)

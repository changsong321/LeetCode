def rankIndex(values, rank):
    scores = []
    for i in range(len(values)):
        scores.append((sum(values[i]), i))
    scores.sort(reverse=True)
    return scores[rank-1][1]

values = [[79,89,15],[85,89,92],[71,96,88]]
rank = 2
print(rankIndex(values,rank))
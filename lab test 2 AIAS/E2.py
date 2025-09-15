def avg(scores):
    if not scores:
        return "no scores available"
    return sum(scores) / len(scores)

print(avg([90, 80, 100]))
print(avg([]))   
def main():
    items = []
    with open("text.txt", "r") as f:
        for line in f:
            items += line.split()
        word_count(items)


def word_count(items):
    counts = dict()

    for word in items:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    print(counts)
    return counts


main()
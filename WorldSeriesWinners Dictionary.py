def main():
    items = []
    teams_file = open("WorldSeriesWinners.txt", "r")
    lines = teams_file.readlines()
    lines.insert(1, "World Series Not Played")
    lines.insert(91, "World Series Not Played")
    keys = range(106)
    keys = [x + 1903 for x in keys]
    windict = world_series_count(lines)
    # print(lines)
    yeardict = yearly_count(keys, lines)
    print(yeardict)

    year = int(input("Please input a year in the range from 1903 to 2008."))
    if year in yeardict:
        print("In", year, "this team won the World Series:", yeardict[year])
        print(
            "The",
            yeardict[year],
            "have won the World Series this many times:",
            windict[yeardict[year]],
        )
    else:
        print("There was not a World Series played this year.")


def world_series_count(items):
    counts = dict()

    for team in items:
        if team in counts:
            counts[team] += 1
        else:
            counts[team] = 1

    # print(counts)
    return counts


def yearly_count(keys, items):
    counts = {}

    for i in keys:
        for j in items:
            counts[i] = j
            items.remove(j)
            break

    # print(counts)
    return counts


main()
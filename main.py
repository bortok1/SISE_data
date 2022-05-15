import draw


def main():
    data = []

    filepath = "result.txt"
    file = open(filepath, "r")

    for line in file:
        data.append(line.split(' '))

    # 4 - długość znalezionego rozwiązania
    # 5 - liczba stanów odwiedzonych
    # 6 - liczba stanów przetworzonych
    # 7 - maksymalna osiągnięta głębokość rekursji
    # 8 - czas trwania procesu obliczeniowego

    rang = [4, 5, 6, 7, 8]
    for i in rang:
        draw.draw_one(data, i)
        draw.draw_two(data, i)
        draw.draw_three(data, i)
        draw.draw_four(data, i)
    # draw.draw_one(data, 4)


if __name__ == '__main__':
    main()


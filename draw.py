import matplotlib.pyplot as plt


# solution:
# [0] - bfs
#     [0] - 1
#         [0] - sum
#         [1] - count
#     [1] - 2
#     ...
# [1] - dfs
# [2] - astr

def kryterium(the_thing):
    match the_thing:
        case 4:
            return "długość znalezionego rozwiązania"
        case 5:
            return "liczba stanów odwiedzonych"
        case 6:
            return "liczba stanów przetworzonych"
        case 7:
            return "maksymalna osiągnięta głębokość rekursji"
        case 8:
            return "czas trwania procesu obliczeniowego"


def calc_avg_one(data, the_thing):
    solution = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # bfs
                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # dfs
                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]  # astr

    for line in data:
        match line[2]:
            case "bfs":
                solution[0][int(line[0]) - 1][0] += float(line[the_thing])
                solution[0][int(line[0]) - 1][1] += 1
            case "dfs":
                solution[1][int(line[0]) - 1][0] += float(line[the_thing])
                solution[1][int(line[0]) - 1][1] += 1
            case "astr":
                solution[2][int(line[0]) - 1][0] += float(line[the_thing])
                solution[2][int(line[0]) - 1][1] += 1

    avg = []
    for sol in solution:
        for i in range(0, 7):
            avg.append(sol[i][0] / sol[i][1])
    return avg


def draw_one(data: [], the_thing):
    # 4 - długość znalezionego rozwiązania
    # 5 - liczba stanów odwiedzonych
    # 6 - liczba stanów przetworzonych
    # 7 - maksymalna osiągnięta głębokość rekursji
    # 8 - czas trwania procesu obliczeniowego

    avg = calc_avg_one(data, the_thing)

    ax = plt.subplot(111)
    ax.bar(0 + 1 - 0.2, avg[0], width=0.2, color='b', align='center', label='bfs')
    ax.bar(0 + 1, avg[0 + 7], width=0.2, color='g', align='center', label='dfs')
    ax.bar(0 + 1 + 0.2, avg[0 + 14], width=0.2, color='r', align='center', label='astar')
    for j in range(1, int(len(avg) / 3)):
        ax.bar(j + 1 - 0.2, avg[j], width=0.2, color='b', align='center')
        ax.bar(j + 1, avg[j + 7], width=0.2, color='g', align='center')
        ax.bar(j + 1 + 0.2, avg[j + 14], width=0.2, color='r', align='center')

    plt.ylabel(kryterium(the_thing))
    plt.xlabel('Głębokość')
    plt.title('Ogółem')

    ax.legend()

    plt.show()


def calc_avg_two(data, the_thing):
    solution = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # hamm
                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]  # manh

    for line in data:
        match line[3]:
            case "hamm":
                solution[0][int(line[0]) - 1][0] += float(line[the_thing])
                solution[0][int(line[0]) - 1][1] += 1
            case "manh":
                solution[1][int(line[0]) - 1][0] += float(line[the_thing])
                solution[1][int(line[0]) - 1][1] += 1

    avg = []
    for sol in solution:
        for i in range(0, 7):
            avg.append(sol[i][0] / sol[i][1])
    return avg


def draw_two(data: [], the_thing):
    avg = calc_avg_two(data, the_thing)

    ax = plt.subplot(111)
    ax.bar(0 + 1 - 0.2, avg[0], width=0.2, color='b', align='center', label='Hamming')
    ax.bar(0 + 1, avg[0 + 7], width=0.2, color='g', align='center', label='Manhatten')
    for j in range(1, int(len(avg) / 2)):
        ax.bar(j + 1 - 0.2, avg[j], width=0.2, color='b', align='center')
        ax.bar(j + 1, avg[j + 7], width=0.2, color='g', align='center')

    plt.ylabel(kryterium(the_thing))
    plt.xlabel('Głębokość')
    plt.title('A*')

    ax.legend()

    plt.show()


def calc_avg_three_and_four(data, the_thing, isdfs=0):
    solution = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # RDUL
                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # RDLU
                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # DRUL
                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # DRLU
                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # LUDR
                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # LURD
                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # ULDR
                [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]  # ULRD

    if isdfs == 1:
        isdfs = "dfs"
    else:
        isdfs = "bfs"

    for line in data:
        if line[2] == isdfs:
            match line[3]:
                case "rdul":
                    solution[0][int(line[0]) - 1][0] += float(line[the_thing])
                    solution[0][int(line[0]) - 1][1] += 1
                case "rdlu":
                    solution[1][int(line[0]) - 1][0] += float(line[the_thing])
                    solution[1][int(line[0]) - 1][1] += 1
                case "drul":
                    solution[2][int(line[0]) - 1][0] += float(line[the_thing])
                    solution[2][int(line[0]) - 1][1] += 1
                case "drlu":
                    solution[3][int(line[0]) - 1][0] += float(line[the_thing])
                    solution[3][int(line[0]) - 1][1] += 1
                case "ludr":
                    solution[4][int(line[0]) - 1][0] += float(line[the_thing])
                    solution[4][int(line[0]) - 1][1] += 1
                case "lurd":
                    solution[5][int(line[0]) - 1][0] += float(line[the_thing])
                    solution[5][int(line[0]) - 1][1] += 1
                case "uldr":
                    solution[6][int(line[0]) - 1][0] += float(line[the_thing])
                    solution[6][int(line[0]) - 1][1] += 1
                case "ulrd":
                    solution[7][int(line[0]) - 1][0] += float(line[the_thing])
                    solution[7][int(line[0]) - 1][1] += 1

    avg = []
    for sol in solution:
        for i in range(0, 7):
            avg.append(sol[i][0] / sol[i][1])

    return avg


def help_draw_three_four(ax, avg):
    ax.bar(1 - 0.36, avg[0], width=0.12, color='red', align='center', label='RDUL')
    ax.bar(1 - 0.24, avg[7], width=0.12, color='green', align='center', label='RDLU')
    ax.bar(1 - 0.12, avg[14], width=0.12, color='blue', align='center', label='DRUL')
    ax.bar(1, avg[21], width=0.12, color='black', align='center', label='DRLU')
    ax.bar(1 + 0.12, avg[28], width=0.12, color='grey', align='center', label='LUDR')
    ax.bar(1 + 0.24, avg[35], width=0.12, color='pink', align='center', label='LURD')
    ax.bar(1 + 0.36, avg[42], width=0.12, color='yellow', align='center', label='ULDR')
    ax.bar(1 + 0.48, avg[49], width=0.12, color='yellow', align='center', label='ULRD')
    for j in range(1, int(len(avg) / 7) - 1):
        ax.bar(j + 1 - 0.36, avg[j], width=0.12, color='red', align='center')
        ax.bar(j + 1 - 0.24, avg[j + 7], width=0.12, color='green', align='center')
        ax.bar(j + 1 - 0.12, avg[j + 14], width=0.12, color='blue', align='center')
        ax.bar(j + 1, avg[j + 21], width=0.12, color='black', align='center')
        ax.bar(j + 1 + 0.12, avg[j + 28], width=0.12, color='grey', align='center')
        ax.bar(j + 1 + 0.24, avg[j + 35], width=0.12, color='pink', align='center')
        ax.bar(j + 1 + 0.36, avg[j + 42], width=0.12, color='yellow', align='center')
        ax.bar(j + 1 + 0.48, avg[j + 49], width=0.12, color='yellow', align='center')


def draw_three(data: [], the_thing):
    avg = calc_avg_three_and_four(data, the_thing)
    ax = plt.subplot(111)

    help_draw_three_four(ax, avg)

    plt.ylabel(kryterium(the_thing))
    plt.xlabel('Głębokość')
    plt.title('BFS')

    ax.legend()

    plt.show()


def draw_four(data: [], the_thing):
    avg = calc_avg_three_and_four(data, the_thing, 1)
    ax = plt.subplot(111)

    help_draw_three_four(ax, avg)

    plt.ylabel(kryterium(the_thing))
    plt.xlabel('Głębokość')
    plt.title('DFS')

    ax.legend()

    plt.show()

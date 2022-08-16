def m_coloring(w, vcolor, n, i):
    if i == 4:
        print(vcolor)
    else:
        for color in range(n):
            if promissing(w, vcolor, i , color):
                vcolor[i] = color
                m_coloring(w, vcolor, n, i + 1)


def promissing(w, vcolor, i , color):
    j = 0
    for j in range(i):
        if w[i][j] == 1 and color == vcolor[j]:
            return False
    return True


def initial_graph():
    # w = [[0 for i in range(5)] for j in range(5)]
    # w[0][1] = 1
    # w[1][0] = 1
    # w[0][2] = 1
    # w[2][0] = 1
    # w[0][3] = 1
    # w[3][0] = 1
    # w[1][2] = 1
    # w[2][1] = 1
    # w[1][4] = 1
    # w[4][1] = 1
    # w[2][4] = 1
    # w[4][2] = 1
    # w[3][4] = 1
    # w[4][3] = 1
    # w[2][3] = 1
    # w[3][2] = 1
    w = [  # j start from 1
            [0, 1, 1, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 1],
            [1, 0, 1, 0],
        ]
    return w


if __name__ == '__main__':
    n = int(input("Please enter the amount of the color: "))
    w = initial_graph()
    vcolor = [0 for i in range(4)]
    m_coloring(w, vcolor, n, 0)

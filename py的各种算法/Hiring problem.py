import random


def randomize_permute(n, List):
    for i in range(0, n - 1):
        k = random.randrange(i + 1, n)
        List[i], List[k] = List[k], List[i]
    print(List)
    return List


def randomize_hire_assistant(n, c, List):
    List = randomize_permute(n, List)
    return hire_assistant(n, c, List)


def hire_assistant(n, c, List):
    best = 0
    cost = c
    for i in range(n):
        if List[i] > best:
            cost += c
            best = List[i]
    return cost


if __name__ == '__main__':
    List = [3, 1, 4, 5, 2, 8, 55, 17, 16, 100, 19]
    cost = 100
    n = len(List)
    print(randomize_hire_assistant(n, cost, List))

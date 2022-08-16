import math


def interpolation_search(n, s, x):
    low = 0
    high = n - 1
    i = -1
    if s[low] <= x <= s[high]:
        while low <= high and i == -1:
            denominator = s[high] - s[low]
            if denominator == 0:
                mid = low
            else:
                mid = low + math.floor(((x - s[low]) * (high - low)) / denominator)
            if x == s[mid]:
                i = mid
            else:
                if x < s[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
    return i


if __name__ == '__main__':
    s = [1, 4, 25, 47, 53, 66, 233, 234]
    n = len(s)
    x = int(input("Please input the number want to search: "))
    i = interpolation_search(n, s, x)
    if i >= 0:
        print("The index of the number in array is", i)
    else:
        print("Don't find in array")

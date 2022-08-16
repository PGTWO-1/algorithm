class node:
    def __init__(self, key):
        self.key = key
        self.next = None


def make_LinkedList(elements):
    head = node(elements[0])  # key is entered but next is still empty
    ptr = head
    for element in elements[1:]:
        ptr.next = node(element)
        ptr = ptr.next
    return head


def radixsort(masterList, numdigits):
    lists = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # piles
    for i in range(1, numdigits + 1, 1):  # 1<=i<=numdigits
        lists = distribute(masterList, lists, i)
        # print("这是",lists)
        masterList = coalesce(masterList, lists)

        # print("\n")
        p = masterList
        while p is not None:
            if isinstance(p.key,int):
                print(p.key)
            p = p.next
        print("_________________________\n")
    return masterList


def distribute(masterList, lists, i):
    for j in range(0, 10, 1):  # 0<= j <= 9
        lists[j] = node(None)  # Null piles
        # print(lists[j].key)

    p = masterList
    while p is not None:
        if isinstance(p.key,int):
            # j= p.key // (10**i) %10
            j = p.key % (10 ** i) // (10 ** (i - 1))
            # print("j: ", j)
            ptr = lists[j]
            if isinstance(ptr.key,int):
                ptr.key = p.key
                # print("current1: ", ptr.key)
            else:
                while ptr.next is not None:
                    ptr = ptr.next
                ptr.next = node(None)
                ptr = ptr.next
                ptr.key = p.key
                # print("current2: ", ptr.key)
        p = p.next
    return lists


def coalesce(masterList, lists):  # masterList 用来next了，又令了一个head
    headIndex = 0
    for j in range(0, 10, 1):  # 0-9
        if isinstance(lists[j].key,int):
            headIndex = j  # 新数组的head：lists[3]
            break

    masterList = node(None)  # 新地址，相当于清空了原head
    for j in range(headIndex, 10, 1):  # 从3开始，以防有next
        ptr = lists[j]  # used for next lists[j]
        masterList.key = ptr.key
        if j == headIndex:
            head = masterList  # head指向头节点，用于返回
        masterList.next = node(None)
        masterList = masterList.next

        while ptr.next is not None:  # lists[7] 有next
            ptr = ptr.next
            masterList.key = ptr.key
            masterList.next = node(None)
            masterList = masterList.next
    return head

if __name__ == '__main__':

    # masterList is the head
    masterList = make_LinkedList([239, 234, 879, 879, 123, 358, 416, 317, 137, 225])

    numdigits = 3
    masterList = radixsort(masterList, numdigits)

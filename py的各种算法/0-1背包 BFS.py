class item:
    def __init__(self, level, profit, weight):
        self.level = level
        self.profit = profit
        self.weight = weight

    def print_info(self):
        print(self.level, self.profit, self.weight,"\n")


def bound(u, n, v, w, W):
    if u.weight >= W:
        return 0
    else:
        result = u.profit
        j = u.level + 1
        totweight = u.weight
        while j <= n and totweight + w[j] <= W:
            totweight = totweight + w[j]
            result = result + v[j]
            j = j + 1
        k = j
        if k <= n:
            result += (W - totweight) * v[k] / w[k]
        return result


def knapsack_breath(n, v, w, W, Q):
    u = item(0, 0, 0)

    maxprofit = 0
    Q.append(u)
    while Q and u.level<=n  :
        u = Q.pop()
        # u.print_info()
        u_child = item(0, 0, 0)
        u_child.level = u.level + 1
        u_child.weight = u.weight + w[u_child.level]
        u_child.profit = u.profit + v[u_child.level]
        if u_child.weight <= W and u_child.profit > maxprofit:
            maxprofit = u_child.profit
        bound1 = bound(u_child, n, v, w, W)
        if bound1 > maxprofit:
            Q.append(u_child)
            # u_child.print_info()
        v_child=item(u_child.level,u.profit,u.weight)
        # v_child.print_info()
        # u_child.weight = u.weight
        # u_child.profit = u.profit
        bound2=bound(v_child,n,v,w,W)
        if bound2 > maxprofit:
            Q.append(v_child)
        # print("数组")
        # for j in Q:
        #     j.print_info()
        # print("--------------")

    return maxprofit

if __name__ == '__main__':
    Q = []
    v = [0, 40, 30, 50, 10]
    w = [0, 2, 5, 10, 5]
    n = 4
    W = 16
    max_profit= knapsack_breath(n, v, w, W, Q)
    print("Maxprofit is %d\n" %max_profit)


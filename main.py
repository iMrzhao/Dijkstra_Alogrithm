
import numpy as np

class Dijkstra():
    def __init__(self, start):
        self.list_P = []
        self.list_Q = [1, 2, 3, 4, 5, 6, 7]
        self.grah = [[1, [2, 6, 7], [12, 16, 14]],
                     [2, [1, 3, 6], [12, 10, 7]],
                     [3, [2, 4, 5, 6], [10, 3, 5, 6]],
                     [4, [3, 5], [3, 4]],
                     [5, [3, 4, 6, 7], [5, 4, 2, 8]],
                     [6, [1, 2, 3, 5, 7], [16, 7, 6, 2, 9]],
                     [7, [1, 5, 6], [14, 8, 9]]]
        self.start_node = start
        inf = 99999
        self.S = inf * np.ones(7, dtype=int)
        self.S[start - 1] = 0
        self.bro_node = np.zeros(7, dtype=int)
        while start != None:
            start = self.lis_P(start)
        print('各自节点的父节点，从该矩阵可得到从起始点到给定点的最优路径:{}'.format(self.bro_node))
        print('各节点到出发点的距离：{}'.format(self.S))

    def lis_P(self, node):
        self.list_P.append(node)
        return self.re_Q(node)

    def re_Q(self, node):
        # if node in self.list_Q():
        self.list_Q.remove(node)
        if len(self.list_Q) == 0:
            print('寻找最优路径结束')
            return None
        else:
            return self.fin_min(node)

    def fin_min(self, node):
        for _, point in enumerate(self.list_P):
            for pos, min_node in enumerate(self.grah[point -1][1]):
                if self.grah[point - 1][2][pos] + self.S[point - 1] < self.S[min_node - 1]:
                    self.S[min_node - 1] = self.grah[point - 1][2][pos] + self.S[point - 1]
                    self.bro_node[min_node - 1] = point    # 找最短路径的父节点
        self.chang_S = self.S.tolist()
        self.chang_S = [self.chang_S[i] for i in range(0, len(self.S), 1) if (i + 1) not in self.list_P]
        n_node = np.where(self.S == min(self.chang_S))[0]
        if n_node.size > 1:
            for i in range(n_node.size):
                if n_node[i] + 1 not in self.list_P:
                    n_node = n_node[i] + 1
                    break
        else:
            n_node = int(np.where(self.S == min(self.chang_S))[0]) + 1
        return n_node

a = Dijkstra(3)




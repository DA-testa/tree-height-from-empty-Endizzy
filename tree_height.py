# Nikita Smirnovs 221RDB433
import sys
import threading

path = "./test/"

class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.lst = []

    def __repr__(self) -> str:
        return f"key: {self.key} , lst: {self.lst}"


class Tree:
    root = Node

    def __init__(self, n):
        self.n = n
        self.map = [Node(x) for x in range(n)]

    def build_tree(self,childrens, i = 0):
        if childrens[i] == -1: 
            self.root = self.map[i]

        else:
            self.map[childrens[i]].lst.append(self.map[i])
        
        if i < self.n -1:
            self.build_tree(childrens, i+1)

    def get_height(self):
        return self.__get_height(self.root)

    def __get_height(self, node):
        height = 0
        if not node.lst:
            return 1

        for child in node.lst:
            height =  max(height, self.__get_height(child))
        return height+1



def getTest(filename):

    with open(f"{path + filename}")  as test:
        n = int(test.readline())
        nodes = list(map(int, test.readline().split()))

    return n , nodes


def computing(n , nodes):
    tree = Tree(n)
    tree.build_tree(nodes)
    return tree.get_height()


def built(n,nodes):
    map = [Node(x) for x in range(n)]
    i = 0
    for i in range(n):
        if nodes[i] == -1: 
            root = map[i]

        else:
            map[nodes[i]].lst.append(map[i])
        
    def calc(node):
        height = 0
        if not node.lst:
            return 1

        for child in node.lst:
            height =  max(height, calc(child))
        return height + 1

    return calc(root)




def main():
    command = input()
    if command == "I":
        n = int(input("input count: "))
        nodes = list(map(int, input().split()))
        #print(computing(n,nodes))
        print(built(n,nodes))

    elif command == "F":
        filename = input()
        test = getTest(filename)
        n = test[0]
        nodes = test[1]
        #print(computing(n,nodes))
        print(built(n,nodes))



        
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()

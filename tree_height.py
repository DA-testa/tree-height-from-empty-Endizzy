# Nikita Smirnovs 221RDB433
import sys
import threading

def compute_height(n,nodes):
    class Node:
        def __init__(self, key):
            self.key = key
            self.lst = []
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
    if "I" in command:
        n = int(input("input count: "))
        nodes = list(map(int, input().split()))

    elif "F" in command:
        filename = input()
        with open("test/" + filename, 'r')  as test:
            n = int(test.readline())
            nodes = list(map(int, test.readline().split()))
    print(compute_height(n,nodes))

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()

from collections import defaultdict

graph = defaultdict(list)

def addEdge(u , v):
    graph[u].append(v)
    
def dfs(start , goal , depth):
    print(start , end = " ")
    if(start == goal):
        return True
    if(depth <= 0):
        return False
    
    for i in graph[start]:
        if(dfs(i , goal , depth - 1)):
            return True
        
    return False

def dfid(start , goal , maxDepth):
    print("Start state is : " , start , " goal state is : " , goal)
    for i in range(maxDepth):
        print("\nDFID level : " , i+1)
        print("Path traversed is : " , end=" ")
        isPathFound = dfs(start , goal , i)
        if isPathFound:
            break
        
    if isPathFound == True:
        print("\nGoal Node is Found")
    else:
        print("\nGoal node is not Found")
        
addEdge('A', 'B')
addEdge('A', 'C')
addEdge('A', 'D')

addEdge('B', 'E')
addEdge('B', 'F')

addEdge('D', 'G')
addEdge('D', 'H')

addEdge('E', 'I')
addEdge('E', 'J')

addEdge('G', 'K')
addEdge('G', 'L')

dfid('A' , 'L' , 4)
        

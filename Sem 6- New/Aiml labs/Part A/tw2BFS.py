successorList = {'S' : [['A' , 3] , ['B' , 6] , ['C' , 5]] , 'A' : [['E' , 8] , ['D' , 9]] , 'B' : [['G' , 14] , ['F' , 12]] , 'C' : [['H' , 7]] , 'H' : [['J' , 6] , ['I' , 5]] , 'I' : [['M' , 2] ,['L' , 10], ['K' , 1]]}

start = input("Enter the start state : ").upper()
goal = input("Enter the goal state : ").upper()
opened = [[start , 5]]
closed = []
success = True
failure = False
state = failure

def GoalTest(N):
    if N == goal:
        return True
    return False

def MovGen(N):
    NewList = list()
    
    if N in successorList.keys():
        NewList = successorList[N]
    
    return NewList


def Append(l1 , l2):
    newlist = list(l1) + list(l2)
    return newlist

def Sort(l):
    l.sort(key = lambda x : x[1])
    return l


def bestFirstSearch():
    i = 1
    global opened
    global closed
    global state
    while( len(opened) != 0 and state != success):
        print("<<<< {} >>>>".format(i))
        N = opened[0]
        print("N = " , N)
        opened.remove(N)
        
        if GoalTest(N[0]):
            state = True
            closed = Append(closed , [N])
            print("Closed : " , closed)
        else:
            #add closed
            closed = Append(closed , [N])
            print("Closed : " , closed)
            children = MovGen(N[0])
            print("Childrens : " , children)
            #nikalo pahle sab ko
            for n in opened:
                if n in children:
                    children.remove(n)
            for n in closed:
                if n in children:
                    children.remove(n)
            opened = Append(children , opened)
            print("Unsorted open : " , opened)
            opened = Sort(opened)
            print("Sorted open : " , opened)
        i = i + 1
        print()
    return True

bestFirstSearch()

if state == success:
    print("\n\nGoal is found")
    print("Best First Path : " , closed)
else:
    print("Goal is Not Found !!!")
            
            
        
    
    
    
    
    
    
    
    
    
    
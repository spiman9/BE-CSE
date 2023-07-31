
print("OR GATE\n")
def OR():
    w1 , w2 , a , t = 0 , 0 , 0.2 , 0
    X = [[0 , 0] , [0 , 1] , [1 , 0 ] , [1 , 1] ]
    Y = [0 , 1 , 1 , 1]
    
    while True:
        out = []
        count = 0
        
        for i in X:
            step = w1 * i[0] + w2 * i[1]
            
            if(step <= t):
                o = 0
                if o == Y[count]:
                    out.append(o)
                    count = count + 1
                else:
                    w1 = w1 + a * i[0] * 1
                    w2 = w2 + a * i[1] * 1
                    print("Weight changes to : w1 = {} , w2 = {} ".format(round(w1 , 2) , round(w2 , 2)))
            else:
                o = 1
                if o == Y[count]:
                    out.append(o)
                    count += 1
                else:
                    w1 = w1 + a * i[0] * 0
                    w2 = w2 + a * i[1] * 0
                    print("Weight changes to : w1 = {} , w2 = {} ".format(round(w1 , 2) , round(w2 , 2)))
            print(round(w1 , 2) ,round( w2 , 2) , out)
        if out[0 :] == Y[0 : ]:
            print("\nFINAL OUTPUT")
            print("Weight w1 = {} weight w2 = {} and output >>> {}".format(w1 , w2 , out))
            break
    
OR()
    



print("\n\n\n\n\nAND GATE\n")

def AND():
    w1 , w2 , a , t = 0 , 0 , 0.2 , 1
    X = [[0 , 0] , [0 , 1] , [1 , 0 ] , [1 , 1] ]
    Y = [0 , 0, 0 ,1]
    
    while True:
        out = []
        count = 0
        
        for i in X:
            step = w1 * i[0] + w2 * i[1]
            
            if(step <= t):
                o = 0
                if o == Y[count]:
                    out.append(o)
                    count = count + 1
                else:
                    w1 = w1 + a * i[0] * 1
                    w2 = w2 + a * i[1] * 1
                    print("Weight changes to : w1 = {} , w2 = {}\n------------------> ".format(round(w1 , 2) , round(w2 , 2)))
                    
            else:
                o = 1
                if o == Y[count]:
                    out.append(o)
                    count += 1
                else:
                    w1 = w1 + a * i[0] * 0
                    w2 = w2 + a * i[1] * 0
                    print("Weight changes to : w1 = {} , w2 = {} \n------------------>".format(round(w1 , 2) , round(w2 , 2)))
                    
            print(round(w1 , 2) ,round( w2 , 2) , out)
        if out[0 :] == Y[0 : ]:
            print("\nFINAL OUTPUT")
            print("Weight w1 = {} weight w2 = {} and output >>> {}".format(round(w1 , 2) , round(w2 , 2), out))
            break
    
AND()



print("\n\n\n\nNot gate\n")



def NOT():
    X = [ 0 ,1]
    Y = [1 , 0]
    weight =-1
    bias = 1
    out = []
    for i in X:
        j = weight * i + bias
        out.append(j)
    print("Final Weights : ")
    for i in range(len(X)):
        print("Input {} --> Output {}".format(X[i] , out[i]))
        
NOT()
    
    
    
import csv
a = []
with open('enjoysport.csv' , 'r') as f:
    next(f)
    for row in csv.reader(f):
        a.append(row)
        
print("Total number of instances are : " , len(a))
num_attributes = len(a[0]) -1

hypothesis = ['0'] * num_attributes

print("The initial Hypothesis is : " , hypothesis)


for i in range(0 , len(a)):
    if a[i][num_attributes] == "yes":
        print("Instance " , i+1 , " is " , a[i] , " is positively classified")
        for j in range(0 , num_attributes):
            if hypothesis[j] == '0' or a[i][j] == hypothesis[j]:
                hypothesis[j] = a[i][j]
            else:
                hypothesis[j] = '?'
        print("Hypothesis for instance " , i+1 , " is " ,hypothesis)
    else:
        print("Instance " , i+1 , " is " , a[i] , " is negatively classified")
        print("Hypothesis for instance " , i+1 , " is " ,hypothesis)
    print()
    


print("\nThe maximal hypotheis is : " , hypothesis)

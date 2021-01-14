a = int(input())
b = int(input())
i=0
j=0
while i<b:
    while j<a:
        if i==j or i+j==a-1:
            print(end="*")
        else:
            print(end=" ")
        j+=1
    print(end="\n")
    i+=1
    j=0
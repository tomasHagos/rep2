list = [[1,2,3],[2,4],[4,5,5]]

#finding sum 
sum = 0
for i in range(0,len(list)):
    for j in range(0,len(list[i])):
        sum += list[i][j]

print(sum)
print("Hello World")

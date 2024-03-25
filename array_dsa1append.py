import array
arr=array.array('i',[1, 2, 3])
print("New array:", end=" ")
for i in range(0, 3):
    print(arr[i], end=" ")
print("\r")
arr.append(4)
print("The appended array is: ",end="")
for i in range (len(arr)):
    print (arr[i], end=" ")

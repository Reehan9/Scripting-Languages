n = int(input("Enter the size of the list")) # Size of the list
List = [0]*n # Intializing the list
print("Enter the elements") # Entering the elements
for i in range(0,n) : # for loop in range 0 ,n
     List[i] = int(input()) # input of the list
print("\n")
print ("Max value element : ", max(List))  # max element of the list
print ("Min value element : ", min(List)) # min element of the list
print("Enter the value to be appended") # appending the value
List.append(int(input()))  # Appending a list , can use List.insert(pos,value)
print(List[0:len(List)]) # Printing the list

print("Enter the index you want to delete")
d = int(input())
if d>n-1: # if the index is greater than the size of the list
     print("Invalid index")
else:
     del List[d] # Deleting the element of the list
sear = int(input("Enter the element to me searched")) # Searching the element
check = 0 # Intializing the check
for i in range(0,len(List)): # for loop in range 0 ,n
     if List[i]==sear:
          check = 1
          print("Element is present at index" , i) # Printing the index
          break # Breaking the loop
if check==0:
     print("Element not present")



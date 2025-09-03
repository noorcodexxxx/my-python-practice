print("\n For loop  number from 1 to 14") #for loop
for i in range(1,14):
       print(i)

#while loop 
print("While loop number: print number from 1 to 5 ")
number=1
while number>=5:
       number=number+1  
  #nested loop
       print("Nested loop:square pattern")
for i in range(1,6):
    for j in range(i):
      print("*", end=" ")
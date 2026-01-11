num = int(input("n = "))

#While loop
i= 0
while_numbers = []
while i < num:
   i += 1
   while_numbers.append(i)
   
#For loop
for_numbers = []
for p in range (1,num + 1):
    for_numbers.append(p)
    
#even_numbers
even_numbers = []
for p in range (1,num + 1):
   if p % 2 == 0:
     even_numbers.append (p)
     
#Results
print("Results for while loop" , while_numbers)
print("Results for for loop" , for_numbers)
print("Results for even numbers" , even_numbers)
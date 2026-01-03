#Print numbers 1–20 but skip multiples of 5

for i in range(1,21):
    if i % 5!=0: 
        print(i)
#Take input until user enters "exit"

input_user =""
while  input_user != "exit":
    input_user= input('Enter the word : ')
print("exited")

#Check if a number is positive, negative, or zero
number = int(input("Enter the number to check : "))
if number > 0:
    print("Positive number")
elif number < 0 : 
    print("Negative number")
else: 
    print("Zero number")
#Print only even numbers from a list

lists = [1,2,3,4,5,6,7,8,9,10]
for i in lists:
    
    if i %2 == 0:
        print(i , end="")



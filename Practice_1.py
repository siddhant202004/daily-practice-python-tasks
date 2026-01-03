#Take name, age → print age after 10 years
#2️⃣ Take two numbers → print sum, difference, product
#3️⃣ Take price & quantity → calculate bill
#4️⃣ Print type of each variable using type()
"""

name = "Armor"
age= 21
print(f'My name is {name} my age after 10 years will be {age + 10}')

num1 = 2
num2 = 20

sum_r = num1+num2
differnce_r = abs(num1 - num2)
product_r = num1*num2

print(f'Sum {sum_r}, difference {differnce_r}, product {product_r}')

print(type(sum_r))

"""
names = ["A", "B", "C"]
scores = [80, 90, 85]

for i in range(len(names)):
    print(names[i], scores[i])
    
for i in scores:
    for j in names:
        print(i,j)

#Develop a text analyzer that counts vowels, consonants, and digits in user input.


vovels = "aeiouAEIOU"
vovels_count = 0
consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
consonants_count = 0 
digits = "1234567890"
digits_count = 0
text = "The 1st launch of the Apollo 11 mission occurred on July 16, 1969. It carried 3 astronauts to the Moon!"
for i in text:
 
    if i in vovels:
            vovels_count+=1
             
    elif i in consonants:
            consonants_count+=1
        
    elif i in digits:
            digits_count +=1
        
print(f"This is the total count of Vowels {vovels_count}.")
print(f"This is the total count of Consonants {consonants_count}")
print(f"This is the total count of digits {digits_count}")       


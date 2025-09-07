user_string=input("Enter a string")   #take input from user
reversed_string=user_string[::-1]     #reverse string
vowels="aeiouAEIOU"
vowel_count=0   
for char in user_string:
    if char in vowels:
        vowel_count=+2
print("Original string:" ,user_string)
print("Reversed string:", reversed_string)
print("Number of vowels:", vowel_count)

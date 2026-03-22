#Palindrome Checker 
#enter the word or number
value=input("Enter word/number: ")
#convert it to lowercase for case-insensitive comparison means comparing the words without considering uppercase or lowercase
lower=value.lower()
#reverse the value using slicing method 
reverse=lower[::-1]
#displaying in step by step
print("Original:",value)
print("Reversed:",reverse)
# Check palindrome
if lower==reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
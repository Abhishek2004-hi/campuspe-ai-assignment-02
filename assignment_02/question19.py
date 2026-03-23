#Text Analysis Functions 
#it is function to count words
def countwords(text):
    words=text.split()          #split the text into words
    return len(words)             #return the number of words
#the function to count vowels
def countvowels(text):
    vowels="aeiouAEIOU"
    count=0
    for char in text:
        if char in vowels:        #if character is a vowel than it returns to the count 
            count+=1              
    return count
#it is function to count consonants
def countconsonants(text):
    vowels="aeiouAEIOU"
    count=0
    for char in text:
        if char.isalpha() and char not in vowels:
            count+=1            # Count only alphabet consonants
    return count
#the function to reverse text
def reversetext(text):
    return text[::-1]             # Reverse using slicing
#the function to check palindrome
def ispalindrome(text):
    text=text.replace(" ","").lower()
    return text==text[::-1]
#the function to remove vowels
def removevowels(text):
    vowels="aeiouAEIOU"
    result=""
    for char in text:
        if char not in vowels:
            result+=char
    return result
#the function to find longest word
def longestword(text):
    words=text.split()
    longest=""
    for word in words:
        if len(word)>len(longest):
            longest=word
    return longest
#it is the main function to analyze text
def analyze_text(text):
    print("\n===TEXT ANALYSIS===")
    print("Words:",countwords(text))
    print("Vowels:",countvowels(text))
    print("Consonants:",countconsonants(text))
    print("Reversed:",reversetext(text))
    if ispalindrome(text):
        print("Palindrome")
    else:
        print("not a palindrome")
    print("Without vowels:",removevowels(text))
    longest=longestword(text)
    print(f"Longest word:{longest}({len(longest)} letters)")
text=input("Enter text: ")
analyze_text(text)
#String Manipulator
sentence=input("Enter a sentence: ")                                #take input from user
print("\nOriginal:",sentence)                                       #displaying original sentence
print("Characters with spaces:",len(sentence))                      #count the characters with spaces
print("Characters without spaces :",len(sentence.replace(" ", "")))  #count the characters without spaces
words=sentence.split()                                              #count the total words
print("Words:",len(words))                                          
print("UPPERCASE:",sentence.upper())                                #convert it to uppercase 
print("lowercase:",sentence.lower())                                #convert to the lowercase                        
print("Title Case:",sentence.title())                               #convert it to title case
if len(words)>0:                                                    #display first word
    print("First word:",words[0])                                   
    print("Last word:",words[-1])                                   
else:                           
    print("No words entered")
print("Reversed:",sentence[::-1])                                   #reverse the sentence
List_of_Entered_words =[input('Please Enter the first word : ').lower(), 
                        input("Please Enter the second word : ").lower(), 
                        input("Please Enter the third word : ").lower(), 
                        input("Please Enter the fourth word : ").lower(), 
                        input("Please Enter the fifth word : ").lower()]

for each_word in List_of_Entered_words:
    a = ''
    for i in reversed(each_word):
        a = a + i
    if a == each_word:
        print(each_word,' is a palindrome.')
    else:
        print(each_word, "is not a palindrome.")


#"The time complexity of this code is O(Total number of words * Number of Characters in each word) = O(n^2)"
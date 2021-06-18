'''Solution 1 - mine'''


word=input("Please enter a word to check if it is a Palindrome: ")
word=str(word)
reverse=word[::-1]
print("Word reversed:",reverse)
if word == reverse:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")

'''Solution 2'''

# def Palind(word):
#     return word[::] == word[::-1]

# def main():
#     word = str(input("Please enter a string to check for palindrome: "))
#     print(Palind(word))

# if __name__ == '__main__':
#     main()
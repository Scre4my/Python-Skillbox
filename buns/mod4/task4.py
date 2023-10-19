word = input()
letters = list(word)
if letters == letters[::-1]:
    palindrome = ''.join(letters)
    print("Можно составить палиндром:", palindrome)
else:
    print("Из данного слова нельзя составить палиндром.")
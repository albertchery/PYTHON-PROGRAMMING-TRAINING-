#pallindrome
CheckPalindrome=input("Enter the sentence:")
cleaned=""
for ch in CheckPalindrome:
    if ch.isalnum():
        cleaned+=ch.lower()
if cleaned==cleaned[::-1]:
    print("True")
else:
    print("False")
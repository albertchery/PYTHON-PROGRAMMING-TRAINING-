s="{{}}"
stack=[]
for ch in s:
    if ch=='(' or ch== '{' or ch=='[':
        stack.append(ch)
    else:
        if len(stack)==0:
            print(False)
        top=stack.pop()
        if((ch==')'and top!='(')or
           (ch=='}'and top!='}')or
           (ch==']'and top!=']')):
            print(False)
if len(stack)==0:
    print(True)
else:
    print(False)
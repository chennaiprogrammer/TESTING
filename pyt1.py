"""The goal of this exercise is to convert a string to a new string where each character in the new string is 
'(' --> if that character appears only once in the original string, 
  ')'--> if that character appears more than once in the original string.
   Ignore capitalization when determining if a character is a duplicate.

Examples:

"din" => "((("

"recede" => "()()()"
"""
text=input("enter the text:")
#text list
textlist=list(text)
print(textlist)
symlist=[]
for i in textlist:
    reap=textlist.count(i)
    print(reap,i)
    if reap == 1:
        sym="("
        symlist.append(sym)
    else:
        sym=")"
        symlist.append(sym)

print("".join(symlist))




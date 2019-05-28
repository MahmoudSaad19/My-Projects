question_prompts = [
     "What color are apples?\n(a) Red/Green\n(b)Orange",
     "What color are bananas?\n(a) Red/Green\n(b)Yellow",
]

score = 0
answer = input("What color are apples?\n(a) Red/Green\n(b)Orange\n")
if answer =='a':
    score += 1
a=input("What color are bananas?\n(a) Red/Green\n(b)Yellow\n")
if answer =='b':
    score += 1
print("you got",str(score)+"/"+str(2) )

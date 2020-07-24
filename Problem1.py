#Take user input or-
# S=["D,D,U,U,U,U,D,D"]
S= [str(x) for x in input("Please input Gary's Path:").split()] 
count=0

d=0
u=0
if S[0]=="D":
    d+=1
elif S[0]=="U":
    u+=1
if S[-1] == "U":
    u+=1
for i in range(1,len(S)-1):
    if S[i] == "D":
        d += 1  
    if S[i] == "U":
        u+=1
    if d-u == 0 and S[i+1] == "U":
        count +=1

print(count)            
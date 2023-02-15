import random

moje = [1,15,20,34,40]
znalezione=0
iteracja=0
while znalezione!=5:
    znalezione=0
    a = random.randint(0,40)
    b=random.randint(0,40)
    c=random.randint(0,40)
    d=random.randint(0,40)
    e=random.randint(0,40)
    if a in moje:
        znalezione+=1
    if b in moje:
        znalezione+=1
    if c in moje:
        znalezione+=1
    if d in moje:
        znalezione+=1
    if e in moje:
        znalezione+=1
    iteracja+=1

print(iteracja)
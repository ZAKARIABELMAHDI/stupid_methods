import os
with open("links.txt", 'w') as f:
    for i in range(96):
       f.write(f"https://www.editions-hatier.fr/flip/flex/docs/c/9782218988035/9782218988035.pdf_{i}.jpg?d=20211208162615")
       f.write("\n")
    f.close()
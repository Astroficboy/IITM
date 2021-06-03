s = input()
depth = 0
match = True
if s.count("(") == s.count(")"):
    dep = 0
    for i in s:
        if i =="(":
            dep = dep + 1
            if dep > depth:
                depth = dep
        elif i == ")":
            dep = dep - 1
            if dep == -1:
                match = False
                break
        else:
            pass
else:
    match = False

if match == True:
    print(depth)
else:
    print("Not matched")

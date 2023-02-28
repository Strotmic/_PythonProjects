x = ["Hanne", "Tim", "Daria", "Diellon"]
y = ""
for i in x:
    y += i
    if i == "Tim":
        continue
    print(i)

if "Tim" in y:
    print("Sorry tim je hoort er niet bij")

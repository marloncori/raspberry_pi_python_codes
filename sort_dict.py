
x = {1: 20, 3: 40, 4: 30, 2: 10, 0: 5}
print(x)
sorted_x = sorted(x.items(), key=lambda kv: kv[1])
print(sorted_x)
print(x.items())
print(x.values())
print(x.keys())
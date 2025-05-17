x = True
z = not x
print(f"not {x} = {z}\n")

# AND
print("----- AND -----")
x = True; y = True
print(f"{x} and {y} = {x and y}")
x = True; y = False
print(f"{x} and {y} = {x and y}")
x = False; y = True
print(f"{x} and {y} = {x and y}")
x = False; y = False
print(f"{x} and {y} = {x and y}\n")

# OR
print("----- OR -----")
x = True; y = True
print(f"{x} or {y} = {x or y}")
x = True; y = False
print(f"{x} or {y} = {x or y}")
x = False; y = True
print(f"{x} or {y} = {x or y}")
x = False; y = False
print(f"{x} or {y} = {x or y}\n")

# XOR (Exclusive OR) menggunakan operator !=
print("----- XOR -----")
x = True; y = True
print(f"{x} xor {y} = {x != y}")
x = True; y = False
print(f"{x} xor {y} = {x != y}")
x = False; y = True
print(f"{x} xor {y} = {x != y}")
x = False; y = False
print(f"{x} xor {y} = {x != y}")

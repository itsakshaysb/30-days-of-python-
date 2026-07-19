# for _ in range(0,11):
#     print(_)

# for _ in range(10,0,-1):
#     print(_)

# for num in range(8):
#     print(num*"#")

# col=8
# for row in range(8):
#     print("#"*col)


# rows = 4
# cols = 6

# for r in range(rows):
#     for c in range(cols):
#         print("#", end=" ")
#     print() 

digit = 0
for digit in range(101):
    digit+=digit
print(digit)
    

total = 0

for i in range(101):  # Iterates from 0 to 100
    total += i

print("Sum =", total)
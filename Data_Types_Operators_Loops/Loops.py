# 1. For Loop (Ek fixed range ya sequence par loop chalane ke liye)
print("For Loop Example:")
for i in range(5):  # 0 se 4 tak loop chalega
    print(i)

# 2. While Loop (Jab tak condition true rahe, loop chalta rahe)
print("\nWhile Loop Example:")
x = 0
while x < 5:
    print(x)
    x += 1  # Har dafa x ko 1 barhao

# 3. Nested Loop (Loop ke andar loop)
print("\nNested Loop Example:")
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"i={i}, j={j}")

# 4. Loop with else (Jab loop complete ho jaye, else chalega)
print("\nFor Loop with Else:")
for i in range(3):
    print(i)
else:
    print("Loop successfully completed!")

# 5. Break Statement (Loop ko beech me hi rokne ke liye)
print("\nBreak Statement Example:")
for i in range(5):
    if i == 3:
        break  # Jab i == 3 ho, loop ruk jayega
    print(i)

# 6. Continue Statement (Ek iteration skip karne ke liye)
print("\nContinue Statement Example:")
for i in range(5):
    if i == 2:
        continue  # Jab i == 2 ho, isko skip kar do
    print(i)

# 7. Pass Statement (Agar loop me kuch nahi likhna to pass likh sakte ho)
print("\nPass Statement Example:")
for i in range(3):
    pass  # Yeh error nahi dega, bas blank chhodne ke liye

# 8. Infinite Loop (Jab condition hamesha true rahe, yeh rukta nahi)
# print("\nInfinite Loop Example:")
# while True:
#     print("Yeh kabhi nahi rukega, jab tak aap manually na rokein (Ctrl + C)") 
#     break  # Yeh break hata doge to infinite chalega

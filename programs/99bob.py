# 99 Bottles of Beer
# Using loops in Python 3.7.7

x = 99
z = 1
while x > 1:
    y = x - 1
    print(x , "bottles of beer on the wall,", x, "bottles of beer.")
    print("Take one down and pass it around,", y, "bottles of beer on the wall.")
    print()
    x = x - 1

if x == 1:
    print("1 bottle of beer on the wall,", "1 bottle of beer")
    print("Take one down and pass it around, no more bottle of beer on the wall.")

print()
print("No more bottles of beer on the wall, no more bottles of beer")
print("Go to the store and buy some more, 99 bottles of beer on the wall")

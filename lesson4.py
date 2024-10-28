# maths functionality
import math

x = 98
square_root = math.sqrt(x)
print("The root is " ,square_root)

rounded = round(square_root, 3)
print("The rounded root is " ,rounded)


print("--------------")
name = "Gloria Prisca Atieno"
print(len(name))
print(name.upper())
print(name.lower())
print(name.title())
print(name.swapcase())

post = "This thing is so easy and fluent"
new_post = post.replace('fluent', 'flowing')
print(new_post)
"""
try except finally else
"""
print("Division")
m = int(input("enter m: "))
n = int(input("enter n: "))

try:
    x = m / n
    print("{}/{}={}".format(m, n, x))

except Exception as e:
    print(e)

else:
    print("this will execute if there is no error")

finally:
    print("This will always execute")

print("\nMultiplication")

x = m * n

print("{}*{}={}".format(m, n, x))

l1 = [[1,2,3],[4,5,6],[7,8,9]]
# for item in l1:
#     print(item)

# triplets = [(z,y,x) for x in range(1,100) for y in range(1,x) for z in range(1,y) if x*x == z*z + y*y ]
# print(triplets)

# for z in range(1,100):
#     for y in range(1,z):
#         for x in range(1,y):
#             if z*z == x*x + y*y:
#                 print(x,y,z)

print("Division")
n = int(input("enter n: "))
m = int(input("enter m: "))

try:
    x = m / n
    print("{}/{}={}".format(m, n, x))
except Exception as e:
    print(e)


else:
    print("this will execute if there is no error")


finally:
    print("This will always execute")



print("Multiplication")

x = m * n

print("{}*{}={}".format(m,n,x))



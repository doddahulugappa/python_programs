# Enter your code here. Read input from STDIN. Print output to STDOUT

X = int(input())
shoe_available = input().split()
shoe_available = list(map(int, shoe_available))
x = int(input())
total_earned = 0
for i in range(x):
    size, dollor = input().split()
    size = int(size)
    dollor = int(dollor)
    if size in shoe_available:
        total_earned += dollor
        shoe_available.remove(size)

print(total_earned)

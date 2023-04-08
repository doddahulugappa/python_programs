import Monkey


def monkey_f(self):
    print("monkey_f() is being called")


# replacing address of "func" with "monkey_f"
Monkey.A.func = monkey_f
obj = Monkey.A()

# calling function "func" whose address got replaced
# with function "monkey_f()"
obj.func()
Monkey.A().func()

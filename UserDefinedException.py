class SalaryException(Exception):
    pass


def process_salary(name, salary):
    try:
        if salary <= 0:
            raise SalaryException
        print(f"{name} has {salary} Salary")
    except SalaryException:
        print("Invalid Salary")

    else:
        print("Has salary")

    finally:
        print("Everyone should have salary > 0")


process_salary("HULI", 23000)
process_salary("Shree", 0)

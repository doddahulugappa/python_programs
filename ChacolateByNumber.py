def get_gcd(m, n):
    # print(m,n,"*********")
    if m % n == 0:
        return n
    else:
        return get_gcd(n, m % n)


def count_no_chacolate(m, n):
    if m % n == 0:
        return 1

    else:
        gcd = get_gcd(m, n)
        print(f"N {n} / GCD {gcd} = No Of Chacolates {int(n // gcd)} with M {m} steps")
        return n // gcd


print(count_no_chacolate(4, 12))
print(count_no_chacolate(12, 5))
print(count_no_chacolate(12, 3))
print(count_no_chacolate(12, 18))
print(count_no_chacolate(6, 8))
print(count_no_chacolate(6, 3))

# print(get_gcd(12, 8), "GCD")
# print(get_gcd(12, 6), "GCD")
# print(get_gcd(12, 5), "GCD")
# print(get_gcd(12, 9), "GCD")

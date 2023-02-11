"""
Minimum no of consecutive days to cover all unique locations
"""

def vacation(A):
    # Get all unique vacation locations
    v_set = set(A)
    a_l = len(A)

    day_count = 0

    # Maximum days to cover all locations will be the length of the array
    max_day_count = a_l

    for i in range(a_l):
        count = 0
        v_set_copy = v_set.copy()

        # Starting point to find next number of days
        # that covers all unique locations

        for j in range(i, a_l):

            # Remove from set, if the location exists,
            # meaning we have visited the location

            if A[j] in v_set_copy:
                v_set_copy.remove(A[j])
            else:
                pass
            count = count + 1

            # If we have visited all locations,
            # determine the current minimum days needed to visit all and break

            if len(v_set_copy) == 0:
                day_count = min(count, max_day_count)
                max_day_count = day_count
                break

    return day_count


a = [7, 2, 3, 4, 3, 2, 2, 7, 2, 3]
print(vacation(a))

a = [7, 2, 3, 4, 3, 2, 2, 8, 2, 3]
print(vacation(a))

a = [7, 2, 3, 4, 3, 2, 5, 3, 2, 3]
print(vacation(a))

a = [5, 5, 3, 4, 3, 2, 5, 3, 2, 4]
print(vacation(a))

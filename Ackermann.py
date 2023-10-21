def ack2(M, N):
   return (N + 1)   if M == 0 else (
          (N + 2)   if M == 1 else (
          (2*N + 3) if M == 2 else (
          (8*(2**N - 1) + 5) if M == 3 else (
          ack2(M-1, 1) if N == 0 else ack2(M-1, ack2(M, N-1))))))


from collections import deque


def ack_ix(m, n):
    "Paddy3118's iterative with optimisations on m"

    stack = deque([])
    stack.extend([m, n])

    while len(stack) > 1:
        n, m = stack.pop(), stack.pop()

        if m == 0:
            stack.append(n + 1)
        elif m == 1:
            stack.append(n + 2)
        elif m == 2:
            stack.append(2 * n + 3)
        elif m == 3:
            stack.append(2 ** (n + 3) - 3)
        elif n == 0:
            stack.extend([m - 1, 1])
        else:
            stack.extend([m - 1, m, n - 1])

    return stack[0]


# print(ack2(4,3))
print(ack_ix(4,3))
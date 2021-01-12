from collections import Counter


def fib_str(s):
    pass
    # counts = Counter(s)
    # if len(counts) < 3:
    #     return True
    # [x, y, z] = counts.most_common(3)
    # if x[1] == y[1] + z[1]:
    #     return True
    # return False

if __name__ == '__main__':
    vars = list(input().split())

    test_n = int(vars[0])

    index = 1
    while index < len(vars):
        q_type = vars[index]

        if q_type == 'Qi':
            print("INV")
        else:
            n1 = vars[index+1]
            n2 = vars[index+2]
            index += 2
            if q_type == 'Qb':
                print("Qb", n1, n2)
            elif q_type == 'Qr':
                print("Qr", n1, n2)

        index += 1


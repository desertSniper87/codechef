from math import log, log2, floor


# 7 Qb 4 5 Qr 4 5 Qi Qb 4 5 Qr 4 5 Qb 8 7 Qb 8 15
# 5 Qb 90 100 Qb 1 20 Qb 4 1 Qr 74 52 Qb 21 2
# 1 Qb 1 20
def calc_rb(n1, n2):
    def get_lr(n):
        return 2*n, 2*n + 1

    def get_line_position(n, h):
        return n % (2 ** h)

    def get_tree_relative_position(line_position, height):
        return 'left' if line_position < 2**(height-1) else 'right'

    def get_height(n):
        if n == 1:
            return 0
        return floor(log2(n))

    def get_root_at_height(n, height_n, desired_height):
        for _ in range(height_n-desired_height):
            n = n // 2
        return n

    h_n2 = get_height(n2)
    line_position_n2 = get_line_position(n2, h_n2)
    relative_position_n2 = get_tree_relative_position(line_position_n2, h_n2)

    count = {
        'red': 0,
        'black': 0
    }

    if h_n2 % 2 == 0:
        count['black'] += 1
    else:
        count['red'] += 1


    while n1!=n2:
        left_n1, right_n1 = get_lr(n1)
        h_n1 = get_height(n1)

        if h_n1 % 2 == 0:
            count['red'] += 1
        else:
            count['black'] += 1


        if n2 == left_n1 or n2 == right_n1:
            return count
        else:
            n2_parent_at_h = get_root_at_height(n2, h_n2, h_n1+1)

            if h_n2 <= h_n1:
                n1 = n1 // 2
            elif n1 == 1 or get_tree_relative_position(get_line_position(n1, h_n1), h_n1) == relative_position_n2:
                n1 = n2_parent_at_h
            else:
                n1 = n1 // 2

    return count


if __name__ == '__main__':
    vars = list(input().split())

    inverse = False

    test_n = int(vars[0])

    index = 1
    while index < len(vars):
        q_type = vars[index]

        if q_type == 'Qi':
            inverse = not inverse
        else:
            n1 = vars[index+1]
            n2 = vars[index+2]
            index += 2
            count = calc_rb(int(n1), int(n2))
            if q_type == 'Qb':
                if inverse is True:
                    print(count['red'], end=' ')
                else:
                    print(count['black'], end=' ')
            elif q_type == 'Qr':
                if inverse is True:
                    print(count['black'], end=' ')
                else:
                    print(count['red'], end=' ')

        index += 1


from math import log, log2, floor


# 5 Qb 4 5 Qr 4 5 Qi Qb 4 5 Qr 4 5
# 1 Qb 8 7

def calc_rb(n1, n2):


    def get_lr(n):
        return 2*n, 2*n + 1

    def get_line_position(n, h):
        return n % (2 ** h)

    def get_tree_relative_position(line_position, height):
        return 'left' if line_position < height else 'right'

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

    # for i in range(1, 30):
    #     h_n2 = floor(log2(i))
    #     line_position = i % (2 ** h_n2)
    #     print(i, get_tree_line_position(line_position, h_n2))


    while n1!=n2:
        print("LINE:38 -- n1 = " + str(n1))
        left_n1, right_n1 = get_lr(n1)

        if n2 == left_n1 or n2 == right_n1:
            print("DONE")
        else:
            if n1 == 3:
                print()

            h_n1 = get_height(n1)
            n2_parent_at_h = get_root_at_height(n2, h_n2, h_n1+1)

            if h_n2 <= h_n1:
                n1 = n1 // 2
            elif n1 == 1:
                if get_tree_relative_position(n2_parent_at_h, 2) == 'left':
                    n1 = n1 * 2
                else:
                    n1 = (n1 * 2) + 1

                if get_tree_relative_position(get_line_position(n1, h_n1), h_n1) == relative_position_n2:
                    print("LINE:61 -- n1 = " + str(n1))
                else:
                    n1 = n1 // 2
            elif get_tree_relative_position(get_line_position(n1, h_n1), h_n1) == relative_position_n2:
                # WE NEED TO FIND IF SAME SIDE
                pass

            else:
                n1 = n1 // 2


        #
        #
        #
        # if (n2 > n1):
        #     n1 = n1 // 2
            

    # print("LINE:6 -- n1, n2 = " + str(n1, n2))


if __name__ == '__main__':
    vars = list(input().split())

    inverse = False

    test_n = int(vars[0])

    index = 1
    while index < len(vars):
        q_type = vars[index]

        if q_type == 'Qi':
            inverse = True
        else:
            n1 = vars[index+1]
            n2 = vars[index+2]
            index += 2
            calc_rb(int(n1), int(n2))
            # if q_type == 'Qb':
            # elif q_type == 'Qr':
            #     print("Qr", n1, n2)

        index += 1


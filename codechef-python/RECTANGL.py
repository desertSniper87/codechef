from collections import Counter

test_n = int(input())

def main(vars):
    counts = Counter(vars)
    for e in counts:
        if counts[e] == 4:
            return True
        if counts[e] != 2:
            return False

    return True


for _ in range(test_n):
    vars = list(input().split())
    if main(vars):
        print("YES")
    else:
        print("NO")
#
# for _ in range(int(input())):
#     a,b,c,d=map(int,input().split())
#     if a==b and c==d:
#         print('YES')
#     elif a==c and b==d:
#         print('YES')
#     elif a==d and b==c:
#         print('YES')
#     else:
#         print('NO')
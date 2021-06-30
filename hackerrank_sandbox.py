if __name__ == '__main__':
    n = int(input())

post_int_below_n = list(range(0, n))

for pos_int in post_int_below_n:
    print(pos_int ^ 2)

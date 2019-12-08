def valid_pair(num):

    num_list = [int(x) for x in str(num)]
    pairs = [1]
    j = 0

    for i in range(1, len(num_list)):
        if num_list[i] == num_list[i - 1]:
            pairs[j] += 1
        else:
            pairs.append(1)
            j += 1

    if 2 in pairs:
        valid_pair = True
    else:
        valid_pair = False

    return valid_pair


if __name__ == "__main__":

    codes = []

    # we need to go deeper...
    for x0 in range(2, 8):
        for x1 in range(x0, 10):
            for x2 in range(x1, 10):
                for x3 in range(x2, 10):
                    for x4 in range(x3, 10):
                        for x5 in range(x4, 10):
                            tmp = 100000 * x0 + 10000 * x1 + 1000 * x2 + 100 * x3 + 10 * x4 + x5
                            if valid_pair(tmp) and (tmp >= 266666) and (tmp <= 699999):
                                codes.append(tmp)

    print("number of valid codes: %i" % (len(codes)))

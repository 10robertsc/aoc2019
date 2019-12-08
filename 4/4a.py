codes = []

# we need to go deeper...
for x0 in range(2, 8):
    for x1 in range(x0, 10):
        for x2 in range(x1, 10):
            for x3 in range(x2, 10):
                for x4 in range(x3, 10):
                    for x5 in range(x4, 10):
                        if (x0 == x1) or (x1 == x2) or (x2 == x3) or (x3 == x4) or (x4 == x5):
                            codes.append(100000 * x0 + 10000 * x1 + 1000 * x2 + 100 * x3 + 10 * x4 + x5)

codes = codes[codes.index(266666) : codes.index(699999) + 1]
print("number of valid codes: %i" % (len(codes)))

# 1. probability of getting two heads in a row at depth=num_flips
def two_heads_probability(num_flips, flip=2):
    prob = 0

    # case 0: base case, maximum depth
    if flip >= num_flips:
        if flip == num_flips:
            # probability of goal state, HH
            prob += 0.5**flip
        return prob

    # case 1: recursive case, T
    prob += two_heads_probability(num_flips, flip+1)

    # case 2: recursive case, HT
    prob += two_heads_probability(num_flips, flip+2)
    return prob


# 2. expected value of number of flips to get two heads in a row
def expected_value(max_depth=30, num_flips=2):
    prob = 0

    # case 0: base case, exceeded maximum depth
    if num_flips > max_depth:
        return 0

    # case 1: recursive case
    prob += (num_flips * two_heads_probability(num_flips)) + \
        expected_value(max_depth, num_flips+1)

    return prob


# 3. The answer is 6! Run it and see
if __name__ == '__main__':
    print(expected_value())

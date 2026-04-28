import math

# calculate the number of guesses allowed

def calc_guesses(low,high):
    num_range = high - low +1
    max_ram = math.log2(num_range)
    max_uppad = math.ceil(max_ram)
    max_guesses = max_uppad +1
    return max_guesses


# Automated testing is below in the form (test_case, expected_value)
to_test =[
    (1, 10, 5),
    (1, 20, 6),
    (1, 100, 8),
    (1, 1000, 11),
]

# run tests!
for item in to_test:
    # retrieve test case and expeted value
    low_num = item[0]
    high_num = item[1]
    expected = item[2]

    # get actual value (ie: test ticket function)
    actual = calc_guesses(low_num, high_num)

    #compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✔️🖤✔️Passed! Case: {low_num}-{high_num}, expected: {expected}, received: {actual}🖤✔️🖤")
    else:
        print(f"🫤👎🫤 Failed! Case: {low_num}-{high_num}, expected: {expected}, received: {actual} 👎🫤👎")
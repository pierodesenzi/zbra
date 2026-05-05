# Question 1

len_password = 6  # password can only be of length 6

# Part 1

def password_follows_rules_part1(password) -> bool:
    # test whether thee password follows the given rules
    # input: password in int format
    # output: bool -> "are rules being followed?"
    str_password = str(password)

    # 1) needs consecutive repeated numbers
    i = 0
    while i < len_password-1:
        if str_password[i] == str_password[i+1]:
            # found repeated consecutive chars
            break
        i += 1
    else:
        # did not find any repeated consecutive chars
        return False
        
    # 2) digits should be non-decreasing
    i = 0
    while i < len_password - 1:
        if str_password[i] > str_password[i+1]:
            # found decrease
            return False
        i += 1

    # if loop above ended, no decrease was found in the sequence

    return True

def calculate_num_passwords_part1() -> int:
    # output: int -> number of possible passwords within the range
    # password is between 184759 and 856920, assuming inclusive.
    # approach: brute-force over fixed range [184759, 856920] -> O(672,162) ~ O(1) for this input
    return sum(1 for n in range(184759, 856921) if password_follows_rules_part1(n))

print("Part 1 answer:", calculate_num_passwords_part1())  # Answer: 1687


# Part 2

# all rules from part 1 still apply, but the repeated char rule is now more specific.

def password_follows_rules_part2(password) -> bool:
    # test whether thee password follows the given rules
    # input: password in int format
    # output: bool -> "are rules being followed?"
    # new rule: the password needs at least one instance of exactly 2 consecutive repeated numbers - e.g: 445555 is valid, 444555 is not

    str_password = str(password)

    # 1) needs 2, but not 3, consecutive repeated numbers
    i = 0
    while i < len_password-1:
        if str_password[i] == str_password[i+1] and (i == len_password - 2 or str_password[i+2] != str_password[i]):
            # found 2, but not 3, repeated consecutive chars
            break
        i += 1

        while i < len_password and str_password[i] == str_password[i-1]:  # no need to retest with consecutive repeated numbers
            i += 1
    else:
        # did not find any repeated consecutive chars, or any sequence of repeated chars was of at least length 3
        return False
        
    # 2) digits should be non-decreasing
    i = 0
    while i < len_password - 1:
        if str_password[i] > str_password[i+1]:
            # found decrease
            return False
        i += 1

    # if loop above ended, no decrease was found in the sequence

    return True

def calculate_num_passwords_part2() -> int:
    # output: int -> number of possible passwords within the range
    # password is between 184759 and 856920, assuming inclusive.
    # approach: brute-force over fixed range [184759, 856920] -> O(672,162) ~ O(1) for this input
    return sum(1 for n in range(184759, 856921) if password_follows_rules_part2(n))

print("Part 2 answer:", calculate_num_passwords_part2())
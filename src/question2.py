# Question 2

# - Assuming all commands are stored in "commands.txt"
# - If no commands increase the address count, the adress in Cross Street will be 0

def solve_address(file_path):
    def read_file():  # yields line by line
        with open(file_path) as f:
            for line in f:
                yield line.strip()

    gen = read_file()  # use line generator
    counter = 0

    while True:
        line = next(gen, None)
        if line is None:  # stops if no more lines are yielded
            break

        # process command
        if line.startswith("20"):
            counter += int(line[2:])  # increase counter
        elif line.startswith("5"):
            for _ in range(int(line[1:])-1):  # skip number of lines after "5"
                line = next(gen, None)
                if line is None:
                    break
        # if line does not start with 20 or 5, just yield next line

    return counter

if __name__ == "__main__":
    print(f"Final address: {solve_address('commands.txt')} Cross Street")
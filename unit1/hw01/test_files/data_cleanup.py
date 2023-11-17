import sys


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def write_lines(content, filename):
    with open(filename, "w") as file:
        file.writelines(content)


def main(input):
    # read in file
    # read_lines, strip each space and comma
    # re-write to file in this format "{name},{score}"

    lines = read_lines(input)
    csv_lines = [f"{line.strip()}\n" for line in lines]

    write_lines(csv_lines, input)


if __name__ == "__main__":
    main(sys.argv[1])

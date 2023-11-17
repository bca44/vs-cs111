import sys


def is_command(args):
    """Return True if args[1] is valid command"""
    return args[1] in ["-p", "-i", "-h", "-w", "-r"]


def execute_command(args):
    """Execute command specified in argument list."""
    command_func_dict = {
        "-p": print_args,
        "-i": intro_message,
        "-h": help_function,
        "-w": write_file,
        "-r": read_file,
    }
    command_func_dict[args[1]](args)


def print_args(args):
    """Print all command line arguments after '-p'."""
    [print(i) for i in args[2:]]


def intro_message(args):
    """Print 'Hello World'."""
    print("Hello World")


def help_function(args):
    """Print help information."""
    help_message = """Valid flags:\n-p : prints out all the command line arguments after the -p\n\
-i : prints "Hello World"\n-h : prints out a help command"""
    print(help_message)


def write_file(args):
    """Write content to file specified in arguments."""
    if len(args) > 3:
        with open(args[2], "w") as file:
            file.writelines([f"{element}\n" for element in args[3:]])
    else:
        print("No Content Provided")


def read_file(args):
    """Read and print content of file specified in arguments."""
    with open(args[2]) as file:
        for line in file:
            print(line.strip())


if __name__ == "__main__":
    if is_command(sys.argv):
        execute_command(sys.argv)
    else:
        [print(arg) for arg in sys.argv]

import sys
import os
import templates


def check_gitignore_existance(path):
    file_list = os.listdir(path)
    if ".gitignore" in file_list:
        return True
    return False


def create_gitignore(path):
    with open(path + "/.gitignore", "a") as gitignore:
        gitignore.write(templates.main)


def add_program_template(path, program):
    if program in templates.programs:
        with open(path + "/.gitignore", "a") as gitignore:
            gitignore.write("\n\n")
            gitignore.write(templates.programs[program])
    else:
        print("WARNING: " + program + " not yet supported.")


class PathNotFound(Exception):
    pass


class ProgramNotFound(Exception):
    pass


if __name__ == "__main__":
    args_number = len(sys.argv)

    # Remove program name from argv
    sys.argv.pop(0)

    # Search for the provided path and check existance
    if "-h" in sys.argv:
        path = os.getcwd()
        sys.argv.remove("-h")
    else:
        path = sys.argv[0]
        sys.argv.pop(0)
        if not os.path.exists(path):
            msg = "The first argument is not an existing path."
            raise PathNotFound(msg)
        if path.endswith("/"):
            path = path[:-1]

    # Create/improve .gitignore file
    gitignore_exists = check_gitignore_existance(path)
    if gitignore_exists:
        print(
            "WARNING: a .gitignore file already exists.\n\n Content will be appended to the existing file."
        )
    create_gitignore(path)

    # Add templates from provided programs
    for program in sys.argv:
        add_program_template(path, program)

#!/usr/local/anaconda3/bin/python
"""
add-gitignore.py
----------------

Provides fast .gitigore creation and modification for common OS and
programs that generates files that should not be present in version history
(e.g. cache files,...).

Installation and Examples
-------------------------
For details on how to install and use the script on different OSs refer to the
Github page https://github.com/damianolodi/add-gitignore

Notes
-----
If you want to know the working principles for the script and the reason for
some design choice refer to https://damianolodi.com/project/add-gitignore
"""

import sys
import os
import templates


def check_gitignore_existance(path):
    """Check if .gitignore already exists.

    Parameters
    ----------
    path: str
        String containing the path in which the check should be executed.
    
    Returns
    -------
    bool
        True if the .gitignore file already exists. False otherwise.
    """

    file_list = os.listdir(path)
    if ".gitignore" in file_list:
        return True
    return False


def create_gitignore(path):
    """Create the .gitignore file.

    The file is created/opened and the main template is written into the file.

    Parameters
    ----------
    path: str
        String containing the path in which the file should be created.
    """

    with open(path + "/.gitignore", "a") as gitignore:
        gitignore.write(templates.main)


def add_program_template(path, program):
    """Add program templates to the existing gitignore file.

    This function search the provided program inside the 'programs' dictionary
    of the templates.py file. If the program is found, the associated template
    will be appended to the existing .gitignore file. Otherwise, if the program
    is not found, a warning message is printed to the user.

    Parameters
    ----------
    path: str
        String containing the path in which the .gitignore file is present.
    program: str
        String with the name of the program provided by the user in the arguments.

    Returns
    -------
    bool
        Return 1 if the program is not found inside the programs dictionary. Otherwise,
        return 0.
    """

    if program in templates.programs:
        with open(path + "/.gitignore", "a") as gitignore:
            gitignore.write("\n\n")
            gitignore.write(templates.programs[program])
    else:
        return 1
    return 0


class PathNotFound(Exception):
    pass


class ProgramNotFound(Exception):
    pass


if __name__ == "__main__":
    # Remove program name from argv
    sys.argv.pop(0)

    # Search for the provided path and check its existance
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
        error = add_program_template(path, program)
        if error:
            print("WARNING: " + program + " not yet supported.")

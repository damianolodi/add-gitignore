import sys
import os


def copy_main_template(path):
    pass


class PathNotFound(Exception):
    pass


if __name__ == "__main__":
    args_number = len(sys.argv)

    # The first argument should be the path
    path = sys.argv[1]
    if path == "-h":
        path = os.getcwd()
    elif not os.path.exists(sys.argv[1]):
        msg = "The first argument is not an existing path."
        raise PathNotFound(msg)
    else:
        if path.endswith("/"):
            path = path[:-1]

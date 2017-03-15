#!/usr/bin/env python3

import sys
import getopt


def main():
    """
    Get argumentsm and call rebuild or render accordingly.
    """

    arguments = sys.argv[1:]

    if not arguments:
        print("Please run with correct arguments.")
        sys.exit(1)

    try:
        opts, args = getopt.getopt(arguments,"",["rebuild", "render="])
    except getopt.GetoptError:
        print("Please run with correct arguments.")
        sys.exit(1)

    for opt, arg in opts:
        if opt == '--rebuild':
            rebuild()
        elif opt == "--render":
            try:
                cid = int(arg)
            except:
                print("Invalid ID")
                return
            render(cid)


if __name__ == "__main__":

    main()

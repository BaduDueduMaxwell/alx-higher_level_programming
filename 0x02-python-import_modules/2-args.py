#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    if count == 0:
        print("0 argument.")
    elif count == 1:
        print("1 argument.")
    else:
        print(f"{count}", "arguments.")
        for i in range(count):
            sys.argv += i
        print(f"{sys.argv}")

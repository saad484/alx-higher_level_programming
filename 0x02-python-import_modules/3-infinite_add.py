#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    counter = 0
    if len(sys.argv) == 1:
        print(counter)
    else:
        for i in range(1, len(sys.argv)):
            counter += int(sys.argv[i])
print("{}".format(counter))

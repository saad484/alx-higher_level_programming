#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    counter = 0
    for i in range(1, len(sys.argv)):
        counter += int(sys.argv[i])
print("{}".format(counter))

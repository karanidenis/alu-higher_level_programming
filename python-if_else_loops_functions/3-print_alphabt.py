#!/usr/bin/python3
for i in range(97, 113):
    if chr(i) == 'q' or chr(i) == 'e':
        continue
    print("{}".format(chr(i)), end='')

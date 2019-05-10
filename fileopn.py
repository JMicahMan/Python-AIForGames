import fileinput
import sys
import os

f = open(r"C:\Users\s188041\odOrEven\.vscode\morningfileread.txt")
find = ("they know me")
find2 = ("Jason Terry (Brrt, brrt, ooh)")
find3 = ("80 racks in")
find4 = ("Rambo (Extended)")

rep = ("Louisiana")

for line in fileinput.input(f):
    f.write(line.replace(find, rep))
    f.write(line.replace(find2, rep))
    f.write(line.replace(find3, rep))
    f.write(line.replace(find4, rep))

#print(f)
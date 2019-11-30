from random import choice as c

print(open("intro.txt").read())

s = open("stuff.txt").read().splitlines()

for _ in range(3843):
    print(f"\nOn meillä {c(s)}, {c(s)}, {c(s)} ja {c(s)}")
    print(f"On {c(s)}, {c(s)}, {c(s)} ja {c(s)}")

with open("data/Jabberwocky.txt", "r") as jabber:

    #for line in jabber:
    #    print(line.rstrip())

    lines = jabber.readlines()

for l in lines:
    print(l.rstrip())
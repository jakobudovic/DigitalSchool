vprasanja = ["ali imas lijf", "when did minecraft release", "are there points in a circil", "how many", "why"]
ok = [0]
k = 0
p = "pravilno!!!"
p = str(p)
n = "narobe :("
n = str(p)


def pravi(prav):
    global k
    k = k + 1
    for e in vprasanja:
        print(e)
        o = input()
        o = str(o)
        if k == 1:
            print("1")
            if o == "no":
                print("pravilno!!!")

            if o != "no":
                print("narobe :(")
        if k == 2:
            print("2")
            if o == "2011":
                print("pravilno!!!")
            if o != "2011":
                print("narobe :(")
        if k == 3:
            print("3")
            if o == "no":
                print(p)
            if o != "no":
                print(n)

        if k == 4:
            print("4")
            if o == "0":
                print(p)
            if o != "0":
                print(n)

        if k == 5:
            print("5")
            if o == "because":
                print(p)
            if o != "because":
                print(n)

pravi(ok)
# Tail Recursion (Backtracking)---> ehen in a Recursion, first func() calls itself and then job done.

c = 0


def func():
    global c
    if c == 5:
        return
    c += 1
    func()  # first did recursion
    print("Vinit")  # then job done.


func()

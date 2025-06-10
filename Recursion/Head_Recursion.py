# Head Recursion ---> When in a recurion , job done first and then func() called itself.

c = 0


def func():
    global c
    if c == 5:
        return
    print("Vinit")  # this is the job.
    c += 1

    func()  # recursion


func()

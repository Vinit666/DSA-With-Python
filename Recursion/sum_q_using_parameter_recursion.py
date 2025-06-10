# sum of i to n number using parameter recursion-->


def func(sum, i, n):
    if i > n:
        print(f"sum is : {sum}")
        return
    func(sum + i, i + 1, n)


func(0, 3, 5)

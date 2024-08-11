print("Experimental")

list1 = list(range(1,21))

def check_odd(num):
    lst = []
    for i in num:
        if i%2 != 0:
            lst.append(i)
    return lst

print(check_odd(list1))

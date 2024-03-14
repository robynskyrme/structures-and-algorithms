
list = []

def make_list(n):
    for c in range(n,0,-1):
        list.append(c)

# oos = Output Every Step (true/false)
def sort_list_swap(s,oos):
    ordered = False
    c = 0
    while not ordered:
        leftmost_pair_found = False
        print(list)
        ordered = True
        while not leftmost_pair_found:
            if list[c] > list[c+s]:
                ordered = False
                temp = list[c]
                list[c] = list[c+s]
                list[c+s] = temp
                leftmost_pair_found = True


if __name__ == '__main__':
    make_list(5)

    sort_list_swap(1,True)

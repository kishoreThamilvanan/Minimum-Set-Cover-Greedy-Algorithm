from timeit import default_timer as timer

global result
global res_len


def helper(univ, sol_el, rem_set, sol_set):
    return_val = minimum_set_cover(univ, sol_el, rem_set, sol_set, 1)
    return return_val


def minimum_set_cover(univ, sol_el, rem_set, sol_set, depth):
    global result
    global res_len

    if len(rem_set) <= 0:
        return -1

    # if result and (len(rem_set) + len(sol_set)) > len(result):
    #     return

    for i in range(len(rem_set)):

        # optimization Idea: if the length of all the remaining elements in rem_set isnt >= univ.len then break out.

        # if it being the very last set being compared.
        # if depth == 0 and len(rem_set) == 1:
        #     if univ == rem_set:
        #         result = rem_set.pop(0)
        #     break
        # print("Debugging: ", depth, i, sol_set, "__", rem_set)

        if depth == 1:
            sol_set.clear()
            sol_el.clear()

        else:
            # if depth > 1 and i > 0 and res_len != len(result):
            #     print("yeet")
            #     t = sol_set.pop()
            #     rem_set.insert(0, t)
            #
            #     sol_el.clear()
            #     for every_set in sol_set:
            #         for every_el in every_set:
            #             if every_el not in sol_el:
            #                 sol_el.append(every_el)
            #
            #     sol_el.sort()

            # else:
            #     res_len = len(result)

            if i < len(rem_set):
                j = 0
                while j < i:
                    # print("Debugging: ", i, j, rem_set, sol_set)
                    # print(result)
                    rem_set.pop(0)
                    # print("Yeet")
                    j += 1
            else:
                continue

        pop = rem_set.pop(0)
        sol_set.append(pop)

        for e in pop:
            if e not in sol_el:
                sol_el.append(e)
        sol_el.sort()

        # print("--------------------------------->")
        # print(depth, i, sol_set)
        # print(result, len(result))
        # print("--------------------------------->")

        if univ == sol_el:
            if result:
                if len(sol_set) < len(result):
                    result.clear()
                    result = sol_set
            else:
                # setting the result when you encounter a possible solution for the first time.
                result = sol_set
            break
        else:
            minimum_set_cover(univ, sol_el.copy(), rem_set.copy(), sol_set.copy(), depth + 1)

    return result


def get_set_sets(file):
    num_lines = int(file.readline())

    sets = []
    i = 0
    while i < num_lines:
        d = file.readline()
        temp = []
        for k in range(0, len(d) - 1):

            if d[k] is ' ':
                k += 1
            elif (d[k + 1]).isdigit():
                temp.append(int(d[k] + d[k + 1]))

            elif d[k + 1] == '\n' and d[k - 1].isdigit():
                continue

            elif d[k + 1] == '\n' and d[k].isdigit():
                temp.append(int(d[k]))

            elif d[k + 1] != '\n' and not d[k - 1].isdigit():
                temp.append(int(d[k]))

        i += 1
        sets.append(temp)

    return sets


def main():
    global result
    global res_len
    # creating the sets by reading the txt file.
    result = []
    res_len = 0
    res_len = len(result)
    file = open("s-k-20-35.txt", "r")

    # this read the first line for the range of universal set.
    u = file.readline()
    universal_set = list(range(1, int(u) + 1))

    sets = get_set_sets(file)

    # if sets.__contains__([]):
    #     sets.remove([])

    print("Universal Set: ", universal_set)
    print("Sets: ", sets)

    start = timer()
    result = helper(universal_set, [], sets, [])

    print("Global Result: ", result)
    print(len(result))

    # check=[]
    # new_result = result
    # for each in result:
    #     result.remove(each)
    #
    #     for f in result:
    #         for e in f:
    #             if e not in check:
    #                 check.append(e)
    #         check.sort()
    #         if universal_set == check:
    #             new_result = result

    end = timer()

    # print("New Result: ", new_result)
    # print(len(new_result))

    print(end - start)


if __name__ == '__main__':
    main()

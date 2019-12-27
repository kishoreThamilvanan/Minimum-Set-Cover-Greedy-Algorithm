def minimum_set_cover(univ, sol_el, rem_set, sol_set, result):
    if not rem_set:
        return rem_set

    #  if empty universal set.
    if not univ:
        return -1

    # if this is the last remaining subset to check with.
    if sol_el == [] and len(rem_set) == 1:
        if univ == rem_set[0]:
            return sol_set

    else:
        for i in range(len(rem_set)):
            check_set = rem_set.pop(i)

            for e in check_set:
                if e not in sol_el:
                    sol_el.append(e)

            sol_set.append(check_set)
            sol_el.sort()

            if univ == sol_el:
                result.append(sol_set)

            else:
                copy_rem_set = rem_set.copy()
                copy_sol_el = sol_el.copy()
                copy_sol_set = sol_set.copy()
                copy_result = result.copy()

                res1 = minimum_set_cover(univ, copy_sol_el, copy_rem_set, copy_sol_set, copy_result)
                res2 = sol_set

                if res1:
                    if univ == sol_el:
                        # return res2 if len(res1) > len(res2) else res1

                        if len(res1) > len(res2):
                            result.append(res2)
                        else:
                            result.append(res1)

                    else:
                        result.append(res1)

                else:
                    if sol_el == univ:
                        result.append(res2)
                    else:
                        result.append([])

    return result




def longest_consec(strarr, k):
    if strarr == [] or k <= 0 or k > len(strarr):
        return ""

    if k == 1:
        longest = ''
        for x in strarr:
            if len(x) > len(longest):
                longest = x

        return longest

    new_list = []

    for i in range(0, len(strarr)-1):
        new_list.append("".join(strarr[i:k+i]))

    longest = ''
    for x in new_list:
        if len(x) > len(longest):
            longest = x

    return longest


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx",
      "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))
longest_consec([], 3)
longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2)
longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2)
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2)
longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3)
longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15)
longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0)

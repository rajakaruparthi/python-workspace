def read_string(s: str):
    o: str = ""
    count: int = 1

    for i in range(1, len(s)):
        flag = (s[i - 1] == s[i])
        if flag:
            count += 1
        else:
            o = o + str(count) + str(s[i - 1])
            count = 1
    o = o + str(count) + str(s[len(s) - 1])
    return o


class LookAndSay:
    # 1
    # 11
    # 21
    # 1211
    # 111221

    iteration = 5
    inp = "1"
    while iteration > 0:
        inp = read_string(inp)
        print(inp)
        iteration -= 1

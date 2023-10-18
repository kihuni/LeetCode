def longestCommonPrefix(strs):
    if not strs:
        return ""

    # Sort the list of strings
    strs.sort()

    # Take the first and the last strings
    first = strs[0]
    last = strs[-1]

    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1

    return first[:i]


strs1 = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs1))  # Expected output: "fl"

strs2 = ["dog", "racecar", "car"]
print(longestCommonPrefix(strs2))  # Expected output: ""

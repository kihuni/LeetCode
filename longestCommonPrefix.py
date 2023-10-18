# The simplest ways to find the longest common prefix of a list of strings is
# to sort the strings and then compare only the first and the last string
# in the sorted list

def LongestCommonPrefix(strs):
    if not strs:
        return ""
    
    # sort lists strings
    strs.sort() 
    
    # take first and the last strings
    
    first = strs[0]
    last = strs[-1]
    
    i = 0
    while 1 < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
        
    return first[:i]

strs1 = ["flower", "flow", "flight"]
print(LongestCommonPrefix(strs1))  # Expected output: "fl"

strs2 = ["dog", "racecar", "car"]
print(LongestCommonPrefix(strs2))  # Expected output: ""
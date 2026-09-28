def removeDuplicates(s):
    res=""
    for i in s:
        if i not in res:
            res+=i
        else:
            res+='#'
    return res

print(removeDuplicates("aabc"))
            
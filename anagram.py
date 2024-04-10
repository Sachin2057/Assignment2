#Given an array of strings (str), group the anagrams together. You can return the answer in any order.
def string(stringList):
    # temp=list(map(lambda x: "".join(sorted(x)),stringList))
    # print(temp)
    hash_map={}
    for i in range(len(stringList)):
        if("".join(sorted(stringList[i])) in hash_map.keys()):
            hash_map["".join(sorted(stringList[i]))].append(stringList[i])
        else:
             hash_map["".join(sorted(stringList[i]))]=[stringList[i]]
    result=[]
    for i in hash_map.values():
        result.append(i)
    return result
print(string(["ana","aan","man","san","nam","nas","kas"]))
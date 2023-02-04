def findOriginalArray(changed):
    original = []
    if changed[0] *2 not in changed:
        return []
    else:
        original.append(changed[0])
        changed.remove(changed[0])
        changed.remove(changed[changed.index(changed[0]*2)])
        findOriginalArray(changed)

print(findOriginalArray([1,3,4,2,6,8]))

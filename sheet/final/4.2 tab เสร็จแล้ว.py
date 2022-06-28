def keepTab(actions:list):
    dict_of_karma = {}
    for i in actions:
        dict_of_karma[i[0:-2]] = 0
    
    for j in actions:
        if j[-1] == "-":
            dict_of_karma[j[0:-2]] = dict_of_karma[j[0:-2]]-1
        else:
            dict_of_karma[j[0:-2]] = dict_of_karma[j[0:-2]]+1

    return dict_of_karma

example = [
    "Jim++","hong++","June++","John--","hong--","June--",
    "bear++","Jib++","June--","bear--","June++","bear++",
    "hong--","June--","hong++","Jim++","hong++","June++",
    "bear--","bear++","hong--","John--","hong++","Jib--",
    "June++","bear++","hong++","hong--","June++","June--"
]

print(keepTab(example))
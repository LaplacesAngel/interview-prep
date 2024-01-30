dict1  = {
    'A': 1,
    'B': 2,
    'C': {
        'A': 1,
        'B': 2},
    'D': 4
}

dict2  = {
    'A': 1,
    'B': 3,
    'C': {
        'A': 1
     },
    'E': 4
}

Results = {
    'Added': ['E'],
    'Removed': ['D', 'C.B'],
    'Same': ['A', 'C.A'],
    'Modified': ['B']
}

def deep_compare(dicta, dictb):

    results_dict = {}
    Added = []
    Removed = []
    Same = []
    Modified = []

    for key in dicta.keys():
        if key in dictb.keys():
            if dicta[key] == dictb[key]:
                Same.append(key)
    return dicta.keys(), dictb.keys()


Results = deep_compare(dict1, dict2)

print(Results)
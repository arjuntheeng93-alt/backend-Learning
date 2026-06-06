import copy
original = [[1, 2], [3, 4]]
shallow = original.copy()
deep = copy.deepcopy(original)

original[1].append(99)

print(original)
print(shallow)
print(deep)
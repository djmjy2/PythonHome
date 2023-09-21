import copy

original = [1, 2, 3]
# target = original
target = copy.deepcopy(original) #

print(original,target)

original[0]=12321
print(original,target)
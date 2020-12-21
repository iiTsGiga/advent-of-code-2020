def searchForAllergen():
    for allerg in allergens:
        n, ingr = allergens[allerg]
        fnd = []
        for i in ingr:
            if ingr[i] == n:
                fnd.append(i)
        if len(fnd) == 1:
            allergens.pop(allerg)
            return fnd[0]

# this keeps track of the allergens and the possible ingredients which could be the allergen
# allergens = {allergen: [howOftenDoesItAppear, {possibleIngredient: howOftenDoesItAppearTogetherWithTheAllergen}]}
# example:
# allergens = {'dairy': [2, {'mxmxvkd': 2, 'kfcds': 1, 'sqjhc': 1, 'nhms': 1, 'trh': 1, 'fvjkl': 1, 'sbzzf': 1}], 'fish': [2, {'mxmxvkd': 2, 'kfcds': 1, 'sqjhc': 2, 'nhms': 1, 'sbzzf': 1}], 'soy': [1, {'sqjhc': 1, 'fvjkl': 1}]}
# since dairy comes up 2 times, and mxmxvkd is the only possible ingredient that also came up 2 times in combination with dairy, we know dairy must be mxmxvkd
# then remove mxmxvkd from every other possibleIngredients-list, remove the allergen because we found it and then look for the next case
# do this until all ingredients that contain allergens were found and then remove them from allIngredients, the new length is the answer for part 1

allergens = dict()
allIngredients = []
for line in open("day21_input.txt").readlines():
    ingr, allerg = line.strip().split(" (contains ")
    allerg = allerg[:-1].split(", ")
    ingr = ingr.split()
    for i in ingr:
        allIngredients.append(i)
    for a in allerg:
        if a not in allergens:
            allergens[a] = [0, dict()]
        allergens[a][0] += 1
        for i in ingr:
            if i not in allergens[a][1]:
                allergens[a][1][i] = 0
            allergens[a][1][i] += 1

print(allergens)

found = []
while len(allergens) > 0:
    found.append(searchForAllergen())
    for allergen in allergens:
        if found[-1] in allergens[allergen][1]:
            allergens[allergen][1].pop(found[-1])

for f in found:
    while f in allIngredients:
        allIngredients.remove(f)
print(len(allIngredients))

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

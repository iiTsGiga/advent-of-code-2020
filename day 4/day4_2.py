passports = [entry.split() for entry in ''.join(line for line in open("day4_input.txt")).split("\n\n")]

byr = [1920, 2002]
iyr = [2010, 2020]
eyr = [2020, 2030]
hgt = [(150, 193), (59, 76)]
ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

valid = 0
for pp in passports:
    values = [line[:3] for line in pp]
    if len(pp) == 8 or (len(pp) == 7 and "cid" not in values):
        for value in pp:
            v = value[:3]
            if v == "cid":
                continue
            elif v == "byr":
                x = int(value[4:])
                if x < byr[0] or x > byr[1]:
                    break
            elif v == "iyr":
                x = int(value[4:])
                if x < iyr[0] or x > iyr[1]:
                    break
            elif v == "eyr":
                x = int(value[4:])
                if x < eyr[0] or x > eyr[1]:
                    break
            elif v == "hgt":
                x = int(value[4:-2])
                if value[-2:] == "cm" and (x < hgt[0][0] or x > hgt[0][1]):
                    break
                elif value[-2:] == "in" and (x < hgt[1][0] or x > hgt[1][1]):
                    break
                elif value[-2:] != "cm" and value[-2:] != "in":
                    break
            elif v == "hcl":
                if value[4] != "#" or len(value[5:]) != 6:
                    break
                invalid = False
                for c in value[5:]:
                    if c not in "0123456789abcdef":
                        invalid = True
                        break
                if invalid:
                    break
            elif v == "ecl" and value[4:] not in ecl:
                break
            elif v == "pid":
                if len(value[4:]) != 9:
                    break
                invalid = False
                for c in value[4:]:
                    if c not in "0123456789":
                        invalid = True
                        break
                if invalid:
                    break
        else:
            valid += 1

print(valid)

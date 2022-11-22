# dictionary comp1
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# new= sentence.split(" ")
# result={items:len(items) for items in new}
# print(result)


# weather_c={
#     "Monday":12,
#     "Tuesday":14,
#     "Wednesday":15,
#     "Thursday":14,
#     "Friday":21,
#     "Saturday":22,
#     "Sunday":24,
# }
#
# result={days:((degree * 9/5)+32) for (days,degree) in weather_c.items() }
#
# print(result)


# def capital_indexes(number):
#     letters = [number.index(items) for items in number.strip() if items.isupper()]
#     return letters
#
#
# print(capital_indexes("HeLlO"))
import re
def definite(number):
    item = [items for items in number if items not in Acceptable]
    if number in item:
        return True
    else:
        return False


def total(number):
    L = []
    if '-' in number:
        for items in number.split('-'):
            if len(items) == 4:
                L.append(items)
    elif ' ' in number:
        for items in number.split(' '):
            if len(items) == 4:
                L.append(items)
    elif '' in number:
        L = number

    tot = [len(items)for items in L]
    return sum(tot)

def repetitive(number):
    f = number.replace(' ', '')
    s = f.replace('-', '')
    v = []
    choice = []
    for match in re.finditer(r'([0-9])\1+', s):
        v.append(match)
    for items in v:
        choice.append( items.group())
    new = [1 for item in choice if len(item) >= 4]
    if 1 in new:
        return True
    else:
        return False


Acceptable = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', ' ']

numbers = '5123 - 3567 - 8912 - 3456'
def solution (numbers):
    ch =[letter for letter in str(numbers).strip()]
    valid= [item for item in ch[0] if item == '4' or item == '5' or item == '6']
    # print(valid)
    if ch[0] == '4' or ch[0] == '5' or ch[0] == '6':
        if len(ch) <= 19:
            if not definite(ch):
                if total(numbers) == 16:
                    if not repetitive(numbers):
                        print("Valid")




                    else:
                        # print("There is four or more repetitive numbers")
                        return 'Invalid'
                else:
                    # print("not totaling to 16")
                    return 'Invalid'
            else:
                # print("Number does not consist of only digits")
                return 'Invalid'
        else:
            # print(f"invalid card number length {len(ch)}")
            return 'Invalid'
    else:
        # print("The card number is invalid. It should start with 4,5,6")
        return 'Invalid'

print(solution(N))
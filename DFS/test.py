# N = 2.125

# a = ["zero","one","two","three","four","five","six","seven","eight","nine"]
# b = ["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
# c = ["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

# S = str(N)
# S = S.split(".")
# ans = "point "

# for s in S[1]:
#     ans += f"{a[int(s)]} "

# print(ans)

NUM_ENG = {
    '0' : 'zero',
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine',
    '10' : 'ten',
    '11' : 'eleven',
    '12' : 'twelve',
    '13' : 'thirteen',
    '14' : 'fourteen',
    '15' : 'fifteen',
    '16' : 'sixteen',
    '17' : 'seventeen',
    '18' : 'eighteen',
    '19' : 'nineteen',
    '20' : 'twenty',
    '30' : 'thirty',
    '40' : 'forty',
    '50' : 'fifty',
    '60' : 'sixty',
    '70' : 'seventy',
    '80' : 'eighty',
    '90' : 'ninety'
}


def get_hundred(num):
    if len(num) == 1:
        return NUM_ENG[num] + " hundred"
    if len(num) == 2:
        if num in NUM_ENG.keys():
            return NUM_ENG[num]
        else:
            return NUM_ENG[num[0]+"0"] + " " + NUM_ENG[num[1]]
    if num[1:] in NUM_ENG:
        return get_hundred(num[0]) + NUM_ENG[num[1:]]
    else:
        return get_hundred(num[0]) + " " + NUM_ENG[num[1]+"0"] + " " + NUM_ENG[num[2]]

def get_thousand(num):
    if len(num) == 1:
        return NUM_ENG[num] + " thousand"
    if len(num) == 2:
        if num in NUM_ENG.keys():
            return NUM_ENG[num] + " thousand"
        else:
            return NUM_ENG[num[0]+"0"] + " " + NUM_ENG[num[1]] + " thousand"
    if num[1:] in NUM_ENG:
        return get_hundred(num[0]) + NUM_ENG[num[1:]] + " thousand"
    else:
        return get_hundred(num[0]) + " " + NUM_ENG[num[1]+"0"] + " " + NUM_ENG[num[2]] + " thousand"

def get_million(num):
    if len(num) == 1:
        return NUM_ENG[num] + " million"
    if len(num) == 2:
        if num in NUM_ENG.keys():
            return NUM_ENG[num] + " million"
        else:
            return NUM_ENG[num[0]+"0"] + " " + NUM_ENG[num[1]] + " million"
    if num[1:] in NUM_ENG:
        return get_hundred(num[0]) + " " + NUM_ENG[num[1:]] + " million"
    else:
        return get_hundred(num[0]) + " " + NUM_ENG[num[1]+"0"] + " " + NUM_ENG[num[2]] + " million"

def get_billion(num):
    if len(num) == 1:
        return NUM_ENG[num] + " billion"
    if len(num) == 2:
        if num in NUM_ENG.keys():
            return NUM_ENG[num] + " billion"
        else:
            return NUM_ENG[num[0]+"0"] + " " + NUM_ENG[num[1]] + " billion"
    if num[1:] in NUM_ENG:
        return get_hundred(num[0]) + " " + NUM_ENG[num[1:]] + " billion"
    else:
        return get_hundred(num[0]) + " " + NUM_ENG[num[1]+"0"] + " " + NUM_ENG[num[2]] + " billion"


    
N = "12345"
if 4 <= len(N) <= 6:
    print(get_thousand(N[:-3]) + " " + get_hundred(N[-3:]))
 
M = "121234567"
if 7 <= len(M) <= 9:
    print(get_million(M[:-6]) + " " + get_thousand(M[-6:-3]) + " " + get_hundred(M[-3:]))

K = "112123456789"
if 10 <= len(K) <= 12:
    print(get_billion(K[:-9]) + " " + get_million(K[-9:-6]) + " " + get_thousand(K[-6:-3]) + " " + get_hundred(K[-3:]))

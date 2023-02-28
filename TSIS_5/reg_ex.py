import re 

def exercise_1(text):
    pattern = r'ab*'
    if re.match(pattern, text):
        print('YES')
    else:
        print('NO')

def exercise_2(text):
    pattern = r'\w*ab{2,3}?\w*'
    if re.match(pattern, text):
        print('YES')
    else:
        print('NO')
exercise_2('abb')
def exercise_3(text):
    pattern = r'[a-z]*_[a-z]*'
    if re.match(pattern, text):
        print('YES')
    else:
        print('NO')

def exercise_4(text):
    pattern = r'[A-Z][a-z]*'
    if re.match(pattern, text):
        print('YES')
    else:
        print('NO')
exercise_4('Nursat')

def exercise_5(text):
    pattern = r'\w*a.*b$'
    if re.match(pattern, text):
        print('YES')
    else:
        print('NO')

def exercise_6(text):
    pattern = r'[ |,|.]'
    return re.sub(pattern, ':', text)
print(exercise_6('I, you. de'))


# def exercise_7(text):
#     pattern = r'(.*)_([a-z])(.*)'
#     matches = re.search(pattern, text)
#     text = matches.group(1) + matches.group(2).upper() + matches.group(3)
#     return text
    
# print(exercise_7('snake_case'))

def exercise_8(text):
    return [s for s in re.split(r'([A-Z][a-z]*)', text) if s]
print(exercise_8('AppleBananaOrange'))

def exercise_9(text):
    pattern = r'([A-Z].*)([A-Z].*)'
    return re.sub(pattern, r'\1 \2', text)
print(exercise_9('NursatMen'))

# def exersice_10(text):
#     pattern = r'([A-Z][^A-Z]*)?([A-Z][^A-Z]*)?([A-Z][^A-Z]*)?'
#     matches = re.search(pattern, text)
#     result = matches.group(1).lower()+'_'+matches.group(2).lower()+'_'+matches.group(3).lower()
#     return result

# print(exersice_10('MyNameIs'))

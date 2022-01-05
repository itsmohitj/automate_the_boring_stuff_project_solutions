arr = ['apples', 'bananas', 'tofu', 'cats']
def comma_code(arr):
    new_arr = []
    for i in range(len(arr)):
        if i == len(arr) - 1:
            new_arr.append('and ' + arr[i])
        else:
            new_arr.append(arr[i] + ', ')
    return ''.join(new_arr)
print(comma_code(arr))
from typing import List


def sort_by_ext(files: List[str]):
    list_l = []
    list_r = []
    for item in files:
        if item.rsplit('.', 1)[0] == '' or item.rsplit('.', 1)[-1] == '':
            list_l.append(item)
        else:
            list_r.append(item)
    print(f'---1--- \nL: {list_l},\nR: {list_r}')
    list_l = sorted(list_l, key=lambda x: x[1])
    list_r = sorted(list_r, key=lambda x: x[x.rfind('.'):])
    list_l = sorted(list_l, key=lambda x: len(x))
    # list_r = sorted(list_r, key=lambda x: len(x))
    print(f'---2--- \nL: {list_l},\nR: {list_r}')
    return list_l + list_r


print(sort_by_ext(["1.cad","2.bat","1.aa","1.bat"])

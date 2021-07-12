x = ['i', 't', ' ', ' ', 'w', 'a', 's', ' ', ' ', 'a', ' ', ' ', 'g', 'o', 'o', 'd', ' ', ' ', 'd', 'a', 'y']
idx = 0
while idx < len(x):
    if x[idx] == ' ':
        x.pop(idx)
    else:
        idx += 1
print(x)
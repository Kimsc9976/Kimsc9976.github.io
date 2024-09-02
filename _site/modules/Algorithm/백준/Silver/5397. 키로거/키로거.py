def keylog(txt):
    left = []
    right = []

    for char in txt:
        if char == '<' and left:
            right.append(left.pop())
        elif char == '>' and right:
            left.append(right.pop())
        elif char == '-' and left:
            left.pop()
        elif char != '<' and char != '>' and char != '-':
            left.append(char)

    rlt = ''.join(left) + ''.join(list(reversed(right)))
    return rlt

N = int(input())
for i in range(N):
    text = input()
    print(keylog(text))
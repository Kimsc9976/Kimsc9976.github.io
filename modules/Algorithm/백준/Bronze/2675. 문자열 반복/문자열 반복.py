T = int(input())
    
for i in range(T):
    n, text = input().split()
    n = int(n)
    text_len = len(text)
    for j in range(text_len):
        print(text[j]*n,end="")
    print()
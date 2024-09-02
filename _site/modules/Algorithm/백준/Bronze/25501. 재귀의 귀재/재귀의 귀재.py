N = int(input())

def isPalindrome(s):
    cnt = 0
    
    def recursion(s, l, r):
        nonlocal cnt
        cnt += 1
        if l >= r: 
            return 1
        elif s[l] != s[r]: 
            return 0
        else: 
            return recursion(s, l+1, r-1)
    
    a = recursion(s, 0, len(s)-1)
    return a, cnt
    



for _ in range(N):
    text = input()
    
    a = isPalindrome(text)
    print(a[0],a[1])



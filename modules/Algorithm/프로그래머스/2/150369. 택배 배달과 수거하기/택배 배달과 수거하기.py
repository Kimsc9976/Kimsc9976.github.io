    
    
'''
1, 0, 2, 0, 1, 0, 2
0, 2, 0, 1, 0, 2, 0


7번집 2개 챙겨감
올 때 6번집 2개 챙겨옴
7 + 7

1번 3번집 챙겨감
올 때 4번집 1개 챙겨옴
5 + 5

3번집 2개 챙겨감
2번집 2개 챙겨옴
3+ 3
'''

def solution(cap, n, deliveries, pickups):
    
    ans = 0

    have_to_deliever = 0
    have_to_pickup = 0
    for i in range(n-1, -1, -1):
        have_to_deliever += deliveries[i]
        have_to_pickup += pickups[i]
        
        while have_to_deliever > 0 or have_to_pickup > 0:
            have_to_deliever -= cap
            have_to_pickup -= cap
            pickups[i] -= cap
            deliveries[i] -= cap
            ans += (i+1)*2
        

    return ans

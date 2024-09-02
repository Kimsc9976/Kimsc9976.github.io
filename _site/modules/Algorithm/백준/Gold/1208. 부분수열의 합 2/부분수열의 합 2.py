LEFT_DICT = dict()
RIGHT_DICT = dict()


# seq: 부분수열, lst: 원본 리스트, sum_v: 누적합, idx: 현재 인덱스, option: left | right
def Backtracking(seq, lst, sum_v, idx, option):
    if option == 'LEFT':
        if sum_v in LEFT_DICT.keys():
            LEFT_DICT[sum_v] += 1
        else:
            LEFT_DICT[sum_v] = 1
    elif option == 'RIGHT':
        if sum_v in RIGHT_DICT.keys():
            RIGHT_DICT[sum_v] += 1
        else:
            RIGHT_DICT[sum_v] = 1

    for i in range(idx, len(lst)):
        next_lst = seq + [lst[i]]
        next_sum = sum_v + lst[i]
        Backtracking(next_lst, lst, next_sum, i+1, option)
        next_lst.pop()


N, S = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
mid = len(arr)//2
end = len(arr)

Backtracking([], arr[start:mid], 0,  0, 'LEFT')
Backtracking([], arr[mid:end], 0, 0, 'RIGHT')

count = 0
for left in LEFT_DICT.keys():
    if (S - left) in RIGHT_DICT.keys():
        count += LEFT_DICT[left] * RIGHT_DICT[(S - left)]

if S == 0:
    count -= 1
print(count)
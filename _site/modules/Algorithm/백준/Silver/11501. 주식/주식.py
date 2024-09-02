def solution(n, stocks):
    benefit = [0] * n
    for s in range(n):
        max = stocks[s].pop()
        while stocks[s]:
            item = stocks[s].pop()
            if item <= max:
                benefit[s] += max - item
            else:
                max = item

    return benefit


if __name__ == "__main__":
    n = int(input())
    stocks = []
    for _ in range(n):
        m = int(input())
        stocks.append(list(map(int, input().split())))
    result = solution(n, stocks)
    for r in result:
        print(r)
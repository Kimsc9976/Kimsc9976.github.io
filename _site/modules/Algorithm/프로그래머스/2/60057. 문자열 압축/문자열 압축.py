def solution(s):
    LENGTH = len(s)
    answer = LENGTH

    for size in range(1, LENGTH):
        compressed = ""

        splited = [s[i:i+size] for i in range(0, LENGTH, size)]
        count = 1
        for a in range(1, len(splited)):
            if splited[a-1] == splited[a]:
                count += 1
            else:
                word = f"{count}{splited[a-1]}" if count > 1 else splited[a-1]
                compressed += word
                count = 1
        word = f"{count}{splited[-1]}" if count > 1 else splited[-1]
        compressed += word
        answer = min(answer, len(compressed))
        
    return answer
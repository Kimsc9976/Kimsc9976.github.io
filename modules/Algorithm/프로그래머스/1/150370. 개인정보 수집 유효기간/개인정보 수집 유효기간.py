def solution(today, terms, privacies):
    answer = []
    yy, mm, dd = today.split('.')

    term_info = {}
    for term in terms:
        t, d = term.split(' ')
        term_info[t] = int(d)
    
    for idx, privacy in enumerate(privacies):
        date_time = privacy[:10]
        t = privacy[-1]
        
        date = term_info[t]
        target_y = date // 12
        target_m = date % 12
        
        pre_yy, pre_mm, pre_dd = date_time.split('.')
        
        cal_y = (((int(pre_yy) + target_y) - int(yy)) * 12)* 28
        cal_m = (int(pre_mm) + target_m - int(mm)) * 28
        cal_d = (int(pre_dd) - int(dd))
        
        if (cal_y + cal_m + cal_d) <= 0 :
            answer.append(idx+1)
    
    return answer
import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        
        Map<String, HashSet<String>> hm = new HashMap<String, HashSet<String>>(id_list.length);
        Map<String, Integer> reportCount = new HashMap<String, Integer>();
        
        // 코드 최적화 부분
        HashSet<String> reportedSet = new HashSet<>(); // 중복 신고 확인용 HashSet

        // HashSet으로 중복신고 를 방지하도록 작업한다.
        for (String reportInfo : report){
            if(reportedSet.add(reportInfo)){ // 중복 신고가 아닐 경우에만 처리
                String[] _report = reportInfo.split(" ");
                String reporter = _report[0];
                String target = _report[1];


                // computeIfAbsent를 활용해 3줄을 코드를 1줄로 줄일 수 있다.
                hm.computeIfAbsent(reporter, x -> new HashSet<>()).add(target);

                // 중복신고를 방지해두었기 때문에 for문을 한번 더 돌 필요가 없다.
                reportCount.put(target, reportCount.getOrDefault(target, 0) + 1);
            }
        }
//         for (int n = 0; n < report.length; n ++){
//             String reportInfo = report[n];
//             String[] _report = reportInfo.split(" ");
//             String reporter = _report[0];
//             String target = _report[1];
            
//             HashSet<String> targets = hm.getOrDefault(reporter, new HashSet<>());
//             targets.add(target);
//             hm.put(reporter, targets);
//         } 
        
//         for (String key : hm.keySet()) {
//             HashSet<String> targets = hm.get(key);
            
//             for (String target : targets){
//                 Integer cnt = reportCount.getOrDefault(target, 0);
//                 cnt ++;
//                 reportCount.put(target, cnt);
//             }
//         }

    for (int i = 0; i < id_list.length; i++) {
        String reporter = id_list[i];
        HashSet<String> targets = hm.getOrDefault(reporter, new HashSet<>());
        int c = 0;

        for (String target : targets) {
            Integer cnt = reportCount.getOrDefault(target, 0);
            if (cnt >= k) {
                c++;
            }
        }
        answer[i] = c;
    }
        
        
        return answer;
    }
}

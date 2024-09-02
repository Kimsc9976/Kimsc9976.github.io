
import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(br.readLine());
		Queue<Integer> qu = new LinkedList<>();
		int ans=0;
		for (int i=0;i<n;i++) {
			String txt = br.readLine();
			String state=txt.split(" ")[0];
			if (state.equals("push")) {
				int num = Integer.parseInt(txt.split(" ")[1]);
				qu.add(num);
				ans=num;
				
			}
			else if (state.equals("pop")) {
				if (qu.isEmpty()) {
					sb.append(-1+"\n");
				}
				else {
					sb.append(qu.poll()+"\n"); //반환 후 제거
				}
			}
			else if (state.equals("size")) {
				if (qu.isEmpty()) {
					sb.append(0+"\n");
				}
				else {
					sb.append(qu.size()+"\n");
				}
			}
			else if (state.equals("empty")) {
				if (qu.isEmpty()) {
					sb.append(1+"\n");
				}
				else {
					sb.append(0+"\n");
				}
			}
			else if (state.equals("front")) {
				if (qu.isEmpty()) {
					sb.append(-1+"\n");
				}
				else {
					sb.append(qu.peek()+"\n");
				}
			}
			else if (state.equals("back")) {
				if (qu.isEmpty()) {
					sb.append(-1+"\n");
				}
				else {
					sb.append(ans+"\n");
				}
			}
			
		}
		System.out.println(sb);

	}
}


	
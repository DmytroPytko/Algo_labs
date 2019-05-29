import java.util.*;

import java.io.*;


public class Main {

    private static String[] relations;
    private static long[] salary;

    private static long dfs(int i) {
        int j;

        if (salary[i] > 0) {
            return salary[i];
        }

        for (j = 0; j < relations.length; j++) {
            if (relations[i].charAt(j) == 'Y') {
                salary[i] = salary[i] + dfs(j);
            }
        }

        if (salary[i] == 0) {
            salary[i] = 1;
        }

        return salary[i];
    }


    public static void main(String[] args) throws IOException {
        Scanner con = new Scanner(new FileReader("bosses.in"));

        while (con.hasNext()) {

            int n = con.nextInt();

            relations = new String[n];

            for (int i = 0; i < n; i++) {
                relations[i] = con.next();
            }

            long result = 0;

            salary = new long[n];

            for (int i = 0; i < n; i++) {
                if (salary[i] == 0) {
                    dfs(i);
                }
            }


            for (int i = 0; i < n; i++) {
                result = result + salary[i];
            }

            System.out.println(result);
        }

        con.close();
    }

}

 
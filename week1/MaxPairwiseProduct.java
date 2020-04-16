import java.util.*;
import java.io.*;

public class MaxPairwiseProduct {
    static Long getMaxPairwiseProduct(int[] numbers) {
        int max_product = 0;
        int n = numbers.length;
        int maxIndex1 = -1;
        int maxIndex2 = -1;

        for (int index = 0; index < n; ++index) {
            if((maxIndex1  == -1) || (numbers[index] > numbers[maxIndex1])){
		        maxIndex1 = index;
	        }
        }

	    for (int index = 0; index < n; ++index) {
            if((maxIndex2  == -1) || (numbers[index] > numbers[maxIndex2] && index != maxIndex1)){
		        maxIndex2 = index;
	        }
        }

        return  (Long.valueOf(numbers[maxIndex1]) * Long.valueOf(numbers[maxIndex2]));
    }

    public static void main(String[] args) {
        FastScanner scanner = new FastScanner(System.in);
        int n = scanner.nextInt();
        int[] numbers = new int[n];
        for (int i = 0; i < n; i++) {
            numbers[i] = scanner.nextInt();
        }
        System.out.println(getMaxPairwiseProduct(numbers));
    }

    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        FastScanner(InputStream stream) {
            try {
                br = new BufferedReader(new
                    InputStreamReader(stream));
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
    }

}

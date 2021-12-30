package day1;

/**
 * Lösung 1 7
 * Lösung 2 5
 */
public class Day1 {

    public static void main(String[] args) {
        int[] nums = {199, 200, 208, 210, 200, 207, 240, 269, 260, 263};
        int count = 0, prevNum = 0;

//************************* Lösung 1 *************************
        for (int i = 0; i < nums.length - 1; i++) {
            prevNum = nums[i];
            if (prevNum < nums[i + 1]) {
                count += 1;
            }
        }
        System.out.printf("Lösung 1 ist: %s%n", count);

//************************* Lösung 2 *************************
        count = 0;
        int sum = 0, sum2 = 0;
        for (int i = 0; i < nums.length - 3; i++) {
            sum = nums[i] + nums[i + 1] + nums[i + 2];
            sum2 = nums[i + 1] + nums[i + 2] + nums[i + 3];
            if (sum < sum2) {
                count += 1;
            }
        }
        System.out.printf("Lösung 2 ist: %s%n", count);
    }
}

package day1;

/**
 * Lösung 1 514579
 * Lösung 2 241861950
 */
public class day1_2020 {

    public static void main(String[] args) {
        int[] nums = {1721, 979, 366, 299, 675, 1456};

//************************* Lösung 1 *************************
        out:
        for (int num : nums) {
            for (int num2: nums) {
                if (num + num2 == 2020) {
                    System.out.println(num * num2);
                    break out;
                }
            }
        }

//************************* Lösung 2 *************************
        out:
        for (int num : nums) {
            for (int num2: nums) {
                for (int num3 :nums) {
                    if (num + num2 + num3 == 2020) {
                        System.out.println(num * num2 * num3);
                        break out;
                    }
                }
            }
        }
    }
}

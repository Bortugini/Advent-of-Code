package day6;

import java.util.concurrent.CopyOnWriteArrayList;

/**
 * Lösung 1 5934
 */
public class Day6 {

    public static void main(String[] args) {
        int[] days = {3, 4, 3, 1, 2};
        // Creating an object of CopyOnWriteArrayList class
        // Declaring object of LanternFish type
        CopyOnWriteArrayList<LanternFish> fishes = new CopyOnWriteArrayList<LanternFish>();

        for (int day : days) {
            fishes.add(new LanternFish(day));
        }

        for (int i = 0; i < 80; i++) {
            for (LanternFish fish : fishes) {
                if (fish.getStartDay() == 0) {
                    fishes.add(new LanternFish(8));
                    fish.minusDay();
                }else {
                    fish.minusDay();
                }
            }
        }

        System.out.printf("Total Fische: %d%n", fishes.size());
    }
}

package day6;

public class LanternFish {
    private int startDay = 0;

    public LanternFish(int startDay) {
        this.startDay = startDay;
    }

    public int getStartDay() {
        return startDay;
    }

    public void minusDay() {
        this.startDay -= 1;
        if (this.startDay < 0) {
            startDay = 6;
        }
    }
}

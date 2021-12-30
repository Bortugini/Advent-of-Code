package day2;

/**
 * Lösung 1 150
 * Lösung 2 900
 */
public class Day2 {

    public static void main(String[] args) {
        String[] commands = {"forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"};
        int depth = 0, horizontal = 0;
//************************* Lösung 1 *************************
        for (String comand : commands) {
            if (comand.contains("forward")) {
                horizontal += Integer.parseInt(comand.split(" ")[1]);
            }else if (comand.contains("down")) {
                depth += Integer.parseInt(comand.split(" ")[1]);
            }else if (comand.contains("up")) {
                depth -= Integer.parseInt(comand.split(" ")[1]);
            }
        }
        System.out.printf("Lösung 1: %d%n", depth * horizontal);
//************************* Lösung 2 *************************
        depth = 0;
        horizontal = 0;
        int aim = 0;

        for (String comand : commands) {
            if (comand.contains("forward")) {
                horizontal += Integer.parseInt(comand.split(" ")[1]);
                depth += Integer.parseInt(comand.split(" ")[1]) * aim;
            }else if (comand.contains("down")) {
                aim += Integer.parseInt(comand.split(" ")[1]);
            }else if (comand.contains("up")) {
                aim -= Integer.parseInt(comand.split(" ")[1]);
            }
        }
        System.out.printf("Lösung 2: %d%n", depth * horizontal);
    }
}

import java.util.Scanner;

public class Password {
    public static void main(String[] args) {
        System.out.println("Enter the passw0rd");
        Scanner sc = new Scanner(System.in);
        String pass = sc.next();
        if (checkLength(pass) && checkFormat(pass) && checkSecret(pass)) {
            System.out.println("Correct");
        } else {
            System.out.println("Incorrect");
        }
        sc.close();
    }

    static boolean checkLength(String pass) {
        int len = pass.length();
        return ~(len << 2) == -65;
    }

    private static boolean checkFormat(String pass) {
        return pass.matches("FLAG\\{[0-9]*\\}");
    }

    private static boolean checkSecret(String pass) {
        char[] content = pass.substring(5, pass.length()-1).toCharArray();
        int[] arr = new int[content.length];
        for (int i = 0; i < content.length; i++) {
            arr[i] = Character.getNumericValue(content[i]);
        }
        if(arr[0]!=7)
            return false;

        for (int i = 1; i < arr.length; i++) {
            if((arr[i] != (arr[i-1] + 3) % 10)){
                return false;
            }
        }
        return true;
    }

}
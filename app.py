import java.util.Scanner;

public class SimpleJavaProgram {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Print Hello World
        System.out.println("Hello, World!");

        // Take two numbers from user
        System.out.print("Enter first number: ");
        int num1 = sc.nextInt();

        System.out.print("Enter second number: ");
        int num2 = sc.nextInt();

        // Add the numbers
        int sum = num1 + num2;
        System.out.println("The sum is: " + sum);
    }
}

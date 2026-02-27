/**
 * A simple main class to test our CI/CD pipeline.
 */
public class Main {

  /**
   * The entry point of the application.
   *
   * @param args command line arguments
   */
  public static void main(String[] args) {
    System.out.println("Hello, CI/CD World!");

    int firstNum = 5;
    int secondNum = 10;
    int sum = add(firstNum, secondNum);

    System.out.println("The sum is: " + sum);
  }

  /**
   * Adds two integers together.
   *
   * @param a the first number
   * @param b the second number
   * @return the sum of the two numbers
   */
  public static int add(int a, int b) {
    return a + b;
  }
}
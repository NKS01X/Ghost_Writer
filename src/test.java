import java.util.*; // Unused import (Checkstyle hates this)

public class test 
{ // Curly brace is on the wrong line
    public static void main(String[] args) {
        System.out.println("Let's break the pipeline!");
        
int first_number=5; // Horrible indentation, underscores in name, no spaces around '='
      int secondNumber = 10;
      
    System.out.println( Calculate(first_number,secondNumber) ); // Weird spacing
    }

    public static int Calculate(int a,int b) // Method name is capitalized, missing space after comma
    {
        return a+b; // Missing spaces around the plus sign
    }
}
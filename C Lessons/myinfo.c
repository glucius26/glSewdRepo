#include <stdio.h>

int main() {
    // Declare a char array for name, an int for age, a float for GPA
    // Print each one using printf with the right format specifier
    // Hint: %s for strings, %d for int, %.1f for float with 1 decimal
    char name[] = "Griffin";
    int age = 18;
    float gpa = 9999.9999;

    printf("Name: %s\n", name);
    printf("Age: %d\n", age);
    printf("gpa: %f\n", gpa);
    return 0;
}
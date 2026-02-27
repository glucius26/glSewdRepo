#include <stdio.h>

// Write your fahrenheitToCelsius function here
// Remember: return type is float, parameter type is float
float fahrenheitToCelsius(float temp){
    float C = (temp - 32) * 5.0 / 9.0;
    printf("%f", C);
}


int main() {
    // Call your function with 32, 212, 72, and 98.6
    // Print each result using printf with %.2f
    // Format: "XX.XX F = XX.XX C"
    fahrenheitToCelsius(212);
    return 0;
}
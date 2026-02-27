#include <stdio.h>

// Write your getGrade function here
// Takes an int (score), returns a char (letter grade)
// Use if/else if/else to check the ranges
int getGrade(int score){
    if (score <= 59){
        printf("Score: %d -> Grade: F", score);
    } else if (score <= 69){
        printf("Score: %d -> Grade: D", score);
    } else if (score <= 79){
        printf("Score: %d -> Grade: C", score);
    } else if (score <= 89) {
        printf("Score: %d -> Grade: B", score);
    } else if (score <= 100){
        printf("Score: %d -> Grade: A", score);
    }
}


int main() {
    // Test with 95, 82, 74, 61, 45
    // Print each like: "Score: 95 -> Grade: A"
getGrade(70);
    return 0;
}
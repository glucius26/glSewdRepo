#include <stdio.h>

// Write your weightedAverage function here
// Takes 6 floats (3 scores and 3 weights), returns a float
float weightedAverage(float s1, float s2, float s3, float w1, float w2, float w3) {
    return (s1 * w1) + (s2 * w2) + (s3 * w3);
}

int main() {
    float homework = 85.0;
    float midterm = 78.0;
    float finalExam = 92.0;

    float hwWeight = 0.40;
    float midWeight = 0.25;
    float finalWeight = 0.35;

    printf("Homework: %.2f x %.2f = %.2f\n", homework, hwWeight, homework * hwWeight);
    printf("Midterm: %.2f x %.2f = %.2f\n", midterm, midWeight, midterm * midWeight);
    printf("Final Exam: %.2f x %.2f = %.2f\n", finalExam, finalWeight, finalExam * finalWeight);

    float grade = weightedAverage(homework, midterm, finalExam, hwWeight, midWeight, finalWeight);

    printf("Final Grade: %.2f\n", grade);
    return 0;
}
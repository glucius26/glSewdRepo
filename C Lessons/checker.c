#include <stdio.h>

int main() {
    int num = 4;

    // Check if positive, negative, or zero and print the result
    // Then check if even or odd and print the result
if (num == 0){
    printf("Zero\n");
} else if (num < 0){
    printf("Negative\n");
} else {
    printf("Positive\n");
}

if (num % 2 == 0){
printf("Even\n");
} else {
    printf("Odd\n");
}
    return 0;
}
#include <stdio.h>

// Write your max function here
// Takes two ints, returns an int
int max (int a, int b) {
    if (a > b){
        printf("Max(%d, %d) = %d", a, b, a);
    }
    else{
        printf("Max(%d, %d) = %d", b, a, b);
    }
}

int main() {
    // Test with: (7, 3), (2, 9), (-5, -1), (4, 4)
    // Print each result like: "max(7, 3) = 7"
    max(4, 4);
    return 0;
}
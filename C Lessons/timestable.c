#include <stdio.h>

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    int ans = 0;
    // Use a for loop from 1 to 10
    // For each iteration, print: num x i = result
    // Example: "5 x 1 = 5"
for (int i = 1; i <= 10; i++) {
    ans = num * i;
    printf("%d x i = %d\n", num, ans);
}
    return 0;
}
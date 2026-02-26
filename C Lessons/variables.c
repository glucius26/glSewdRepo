#include <stdio.h>

int main() {
    int apples = 12;
    int eaten = 5;
    int remaining = apples - eaten;

    printf("Started with %d apples\n", apples);
    printf("Ate %d apples\n", eaten);
    printf("Apples left: %d\n", remaining);

    float price = 0.75;
    float totalCost = apples * price;
    printf("Total cost at $%.2f each: $%.2f\n", price, totalCost);

    return 0;
}
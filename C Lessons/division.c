#include <stdio.h>

int main() {
    int a = 10;
    int b = 3;
    int intResult = a / b;
    printf("int / int: %d / %d = %d\n", a, b, intResult);

    float c = 10.0;
    float d = 3.0;
    float floatResult = c / d;
    printf("float / float: %.f / %.1f = %.4f\n", c, d, floatResult);

    float castResult = (float)a / b;
    printf("(float)int / int: %d / %d = %.4f\n", a, b, castResult);

    float wrongResult = a / b;
    printf("Wrong way: %d / %d = %.4f\n", a, b, wrongResult);

    return 0;
}
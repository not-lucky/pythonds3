#include <stdio.h>

int main()
{
    char x;
    scanf("%c", &x);
    int i = x;
    if ((65 <= i && i <= 90) || (97 <= i && i <= 122))
        printf("The entered character is an alphabet.");
    else
        printf("The entered character is NOT an alphabet.");
}
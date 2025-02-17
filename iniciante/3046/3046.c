#include <stdio.h>
#include <stdlib.h>

int input_dados(){
    int n;
    char input[5];

    scanf("%5s", input);
    n = atoi(input);
    return n;
}

int main(){
    int r, n = input_dados();
    r = ((n+1)*(n+2))/2;
    printf("%d\n", r);

    return 0;
}
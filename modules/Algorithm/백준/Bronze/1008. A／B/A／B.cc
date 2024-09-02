#include <stdio.h>

int main(){
    int A;
    int B;
    
    scanf("%d %d",&A, &B);
    double C = (double)A/B;
    printf("%.9lf", C);
    return 0;
}
#include <stdio.h>

int main(){
    int year;
    scanf("%d", &year);
       
    if ((year % 4 == 0) && (year % 100 != 0))
    {printf("%d", 1);}
    
    else if(year % 100 == 0)
    {
        if(year % 400 == 0)
        {printf("%d", 1);}
        else{printf("%d", 0);}
    }
    else{printf("%d", 0);}


    return 0;
}
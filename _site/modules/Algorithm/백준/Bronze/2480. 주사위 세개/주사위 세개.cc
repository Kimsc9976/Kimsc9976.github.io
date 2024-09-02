#include <stdio.h>

int main(){
    int dice[3];
    
    scanf("%d %d %d", &dice[0], &dice[1], &dice[2]);
    
    if ((dice[0] == dice[1]) && (dice[1] == dice[2]))
    {
        printf("%d", 10000 + dice[0] *1000);
    }
    else if ((dice[0] == dice[1]) || (dice[0] == dice[2]) || (dice[1] == dice[2]))
    {
        if (dice[0] == dice[1] || dice[0] == dice[2])
        {printf("%d", 1000 + dice[0] *100);}
        else
        {printf("%d", 1000 + dice[2] *100);} 
    }
    else
    {
        int for_multi = dice[0];
        for (int i = 0; i < 3; i++)
        {
            for(int j = i; j <3; j++)
            {
                if (for_multi <= dice[j])
                {for_multi = dice[j];}
            }
        }
        printf("%d", for_multi * 100);
    }
    
    return 0;    
}
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>

int main()
{
    int size = 9;
    int num_array[size];

    for (int i = 0; i<size; i++)
    {
        scanf("%d", &num_array[i]);
    }

    int max = 0;
    int idx;
    for(int i = 0; i<size; i++)
    {
        if (num_array[i] > max)
        {
            idx = i;
            max = num_array[i];
        }
    }
    printf("%d\n", max);
    printf("%d", idx+1);

    return 0;
}
    

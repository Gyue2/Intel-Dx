```c
#include <stdio.h>
int main() {
	int i, j;
	printf("정수 2개 입력 : ");
	scanf("%d%d", &i,&j);
	printf("%d + %d = %d\n",i,j,(i+j));
	printf("%d - %d = %d\n",i,j,(i-j));
	printf("%d * %d = %d\n",i,j,(i*j));
	printf("%d / %d = %d\n",i,j,(i/j));
	printf("%d %% %d = %d\n",i,j,(i%j));
	
    return 0;
}
```
-------------------------------------------------------
```c
#include <stdio.h>
int main() {
	int i, j;
	printf("정수 2개 입력 : ");
	scanf("%d%d", &i,&j);
	printf("\n%d << %d = %d\n",i,j,(i << j));
	printf("%d >> %d = %d\n",i,j,(i >> j));
	
    return 0;
}
```
-------------------------------------------------------
```c
#include <stdio.h>
int main() {
	int i, j;
	printf("정수 2개 입력 : ");
	scanf("%d%d", &i,&j);
	printf("\n%d > %d = %d\n",i,j,(i > j));
	printf("%d >= %d = %d\n",i,j,(i >= j));
	printf("%d < %d = %d\n",i,j,(i < j));
	printf("%d <= %d = %d\n",i,j,(i <= j));
	printf("%d == %d = %d\n",i,j,(i == j));
	printf("%d != %d = %d\n",i,j,(i != j));
	
    return 0;
}
```
---------------------------------------------------
```c
#include <stdio.h>
int main() {
	int i, j;
	printf("정수 2개 입력 : ");
	scanf("%d%d", &i,&j);
	printf("\n%d & %d = %d\n",i,j,(i & j));
	printf("%d ^ %d = %d\n",i,j,(i ^ j));
	printf("%d | %d = %d\n",i,j,(i | j));

    return 0;
}
```
-------------------------------------------------------
```c
#include <stdio.h>
int main() {
	int i, j;
	printf("논리값 2개 입력 : ");
	scanf("%d%d", &i,&j);
	printf("\n!(%d) = %d\n",i,!i);
	printf("%d && %d = %d\n",i,j,(i && j));
	printf("%d || %d = %d\n",i,j,(i || j));

    return 0;
}
```
----------------------------------------------------------

```c
#include <stdio.h>
int main() {
	int i, j, temp;
	printf("논리값 2개 입력 : ");
	scanf("%d%d", &i,&j);
    temp = (i > j)?100:200;
    printf("%d\n",temp);


    return 0;
}
```
------------------------------------------------------------
```c
#include <stdio.h>
int main() {
    int i = 0;
    int j = 0;
    
    i = 0;
    i = i + 1;
    printf("i = %d\n",i);
    i = 0;
    i += 1 ;
    printf("i = %d\n",i);
    i = 0;
    ++i;
    printf("i = %d\n",i);
    i = 0;
    i++;
    printf("i = %d\n",i);
    i = 0;
    j = ++i;
    printf("i = %d, j = %d\n",i,j);
    i = 0;
    j = i++;
    printf("i = %d, j = %d\n",i,j);
    
    return 0;
}

```
-------------------------------------------------------
```
#include <stdio.h>
int main() {
    int score;
    printf("점수 입력 : ");
    scanf("%d", &score);
    if(score >= 90)
        printf("A 등급");
    else if (score >= 80) 
        printf("B 등급");
    else if (score >= 70) 
        printf("C 등급");
    else
        printf("D 등급");
    return 0;
}
```
-----------------------------------------------------
```c
#include <stdio.h>
int main() {
    int score;
    printf("점수 입력 : ");
    scanf("%d", &score);
    
    switch(score/10) {
        case 10:
        case 9:
            printf("A 등급\n"); break;
        case 8:
            printf("B 등급\n"); break;
        case 7:
            printf("C 등급\n"); break;
        case 6:
            printf("D 등급\n"); break;
        default:
            printf("F 등급\n"); break;
    }
    
            return 0;
}
```
---------------------------------------------------
```c
#include <stdio.h>
int main() {
    int i, sum;
    int limit;

    printf("정수 입력 : ");
    scanf("%d", &limit);

    for(i=1, sum=0; i<=limit; i++){
        sum += i;
    }
    printf("1부터 %d까지의 합은 %d 입니다. \n", limit,sum);
          
        
    return 0;
}
```

--------------------------------------------------------
```c
#include <stdio.h>
int main() {
    int i, j;
    int step;

    printf("정수 입력 : ");
    scanf("%d", &step);
    printf("\n");
    for(i=0; i<=step; i++){
        for(j = 0; j <= i; j++)
            {
                printf("*");
            }
        printf("\n");
    }
        
    return 0;
}
```
-------------------------------------------------------------

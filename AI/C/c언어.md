```
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
```
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
```
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
```
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


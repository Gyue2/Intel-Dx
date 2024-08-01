#include <stdio.h>
int main(){
	int base, height;

	printf("밑변 입력 : ");
	scanf("%d", &base);
	printf("높이 입력 : ");
	scanf("%d", &height);
	printf("사각형의 면적 = %d\n" , (base*height));

	return 0;
}


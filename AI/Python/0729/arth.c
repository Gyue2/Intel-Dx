#include<stdio.h>
int main() {
	int number1, number2;
	printf("첫 번째 변수 : ");
	scanf("%d", &number1);
	printf("두 번째 변수 : ");
	scanf("%d", &number2);

	printf("%d + %d = %d\n", number1, number2, (number1+number2));
	printf("%d - %d = %d\n", number1, number2, (number1-number2));
	printf("%d * %d = %d\n", number1, number2, (number1*number2));
	printf("%d / %d = %.2f\n", number1, number2, ((float)number1/number2));
	printf("%d %% %d = %d\n", number1, number2, (number1%number2));

	return 0;
}

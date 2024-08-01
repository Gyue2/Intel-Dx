import random

def guess_number():
    number_to_guess = random.randint(1, 1000)
    attempts = 0

    print("1부터 1000 사이의 숫자를 맞춰보세요!")

    while True:
        guess = int(input("숫자를 입력하세요: "))
        attempts += 1

        if guess < number_to_guess:
            print("더 큰 숫자입니다.")
        elif guess > number_to_guess:
            print("더 작은 숫자입니다.")
        else:
            print(f"축하합니다! {attempts}번 만에 숫자를 맞췄습니다.")
            break

if __name__ == "__main__":
    guess_number()
    

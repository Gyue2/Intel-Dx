listEx01 = list(range(10))
print(listEx01)

str1 = 'This is a Sample String'
HP = '010-1234-5678'
email = 'abcd1234@naver.com'
for i in str1:
    print(i)

count = sum(1 for l in listEx01 if l >= 5)
print(count)

str2 = str1.split()
print(str1)
print(str2)
print(f'{str1}는 {len(str2)}개의 단어로 구성되어 있습니다.')

str3 = HP.split('-')
print(str3)

uID, domain = email.split('@')
print(uID)
print(domain)

menu = 0
friends = []

while menu != 9:
    print('''
-------------------
1. 친구 리스트 출력
2. 친구 추가
3. 친구 삭제
4. 이름 변경
9. 종료
''')
    menu = int(input('메뉴를 선택하세요 : '))
    
    if menu == 1:
        print(friends)
    elif menu == 2:
        friends.append(input('이름을 입력하세요 : '))
    elif menu == 3:
        del_frd = input('삭제할 이름 : ')
        if del_frd in friends:
            friends.remove(del_frd)
        else:
            print('\n 없는데요?')
    elif menu == 4:
        ago_name = input('변경 대상 : ')
        if ago_name in friends:
            friends[friends.index(ago_name)] = input('새로운 이름 : ')
        else:
            print('\n없는데요?')
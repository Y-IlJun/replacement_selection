num = int(input("몇번 돌리실 꺼에요?"))
for i in range(num):

    n = int(input("인자 몇개 하실꺼에요?"))

    all_List = list(map(int, input().split()))
    list1 = all_List[0:5]  # 첫번째 리스트에 버퍼 만큼 넣기
    for h in range(5):
        all_List.pop(0)

    run = list()  # 첫 번째 run 리스트
    freeze_List = list()
    r=1
    for k in range(n):
        if len(list1) == 0:  # freeze일 경우
            r+=1
            print("all_freeze")
            # run 인자 파일에 작성
            with open("replacement_output2.txt", "a") as file:  # 'w' -> 'a'로 변경
                file.write(f"{run}\n")  # run을 append 모드로 덧붙여 저장
            run.clear()
            all_List = freeze_List + all_List
            freeze_List.clear()
            if len(all_List) >= 5:
                list1 = all_List[0:5]  # 앞에서부터 5개만 가져오기
                for h in range(5):
                    all_List.pop(0)  # 앞에서부터 5개를 pop하여 all_List에서 제거
            else:
                list1 = all_List[:]  # all_List가 5개보다 적으면 모든 원소를 가져옴
                all_List.clear()  # all_List가 비게끔 clear

        min_element = min(list1)  # 리스트에서 가장 작은 값 찾기
        min_element_index = list1.index(min_element)  # 그 값의 인덱스 찾기
        run.append(min_element)  # run에 작은 수 적어넣음
        list1.remove(min_element)  # 작은 수 삭제
        if all_List:
            list1.insert(min_element_index, all_List[0])  # all_list에 첫번째 요소 삽입
            x = all_List.pop(0)  # x는 다음 채울 수
        else:
            x = run[-1]

        if run:  # run이 비어있지 않다면
            if x >= run[-1]:  # 다음 채울 수와 아까 run에 넣은 수 비교
                print("if 실행")
                # x가 run[0]보다 크면 종료
            else:
                # list1에 들어온 수를 freeze 리스트에 넣고 list1의 그 자리를 채우지 않는다
                print("else 실행")
                freeze_List.append(list1[min_element_index])  # append로 freeze 리스트에 추가
                list1.pop(min_element_index)  # 그 자리를 채우지 않음

        print(f"run은 {run}")
        print(f"list1은 {list1}")
        print(f"all은 {all_List}")
        print(f"freeze는 {freeze_List}")

    # 마지막 run 리스트가 있을 경우 추가
    if run:
        with open("replacement_output2.txt", "a") as file:  # 'w' -> 'a'로 변경
            file.write(f"{run}\n")  # run을 append 모드로 덧붙여 저장
        run.clear()
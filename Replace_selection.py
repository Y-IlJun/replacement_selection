#input 파일 읽고 한줄씩 분리후 lines에 넣기
with open("C:\\Users\\dlfwn\\OneDrive\\바탕 화면\\zz\\replacement_input.txt", "r") as file:
    line = file.readlines()
#output 파일 쓰기전에 리셋
with open("C:\\Users\\dlfwn\\OneDrive\\바탕 화면\\zz\\replacement_output.txt", "w") as f:
    f.write("")


<<<<<<< HEAD
num = int(line[0].strip()) #input의 첫번째 줄인 몇번 정렬할지 읽기
index = 1# line의 1번 인덱스로 초기화

for h in range(num):#num만큼 정렬 반복
    n = int(line[index].strip())  # 정렬할 값의 개수
    index += 1
    all_List = list(map(int, line[index].strip().split()))  # 정렬할 정수를 공백 없애고 all_List에 넣음
    index += 1
    list1 = all_List[:5]  # 버퍼 초기화
    all_List = all_List[5:]  # 버퍼에서 가져온 후 남은 정수를 all_List에 두어 삭제를 용이하게 함
    run = []  # 현재 run
    runs = []  # 모든 run을 저장
    freeze_List = []  # freeze 리스트

    while list1 or freeze_List or all_List: #셋중 하나라도 있다면 실행
        if not list1:  # 버퍼가 비었을 때
            runs.append(run)  # 현재 run 저장
            run = []#run을 다시 초기화
            list1 = freeze_List[:5]  # 모두 freeze 된 경우 다시 정렬을 위해 채움
            freeze_List = freeze_List[5:] #freeze 빠진거 제외하고 다시 초기화

            if len(list1) < 5 and all_List: #list1이 버퍼 크기인 5보다 작을 경우 그리고 all_List가 존재하면
                add_count = 5 - len(list1) #가져와야할 수
                list1.extend(all_List[:add_count]) #가져와야할 수 만큼 채움 list1 뒤에 채움
                all_List = all_List[add_count:]#빠진 걸 제외한 후 다시 초기화

        if not list1:  # list1이 비었을 때 종료
            break

        # 버퍼에서 가장 작은 값 찾기
        min_element = min(list1)
        min_index = list1.index(min_element)#빠진 자리의 index를 min_index에 삽입
        run.append(min_element)  # run에 min_element 추가
        list1.pop(min_index)  # list1에서 제거

        if all_List:
            next_value = all_List.pop(0)  # 남은 리스트에서 다음 값 가져오기
            if next_value >= min_element:  # 정렬 순서 유지
                list1.insert(min_index, next_value)#all_List에서 다음 값을 가져와 min_element의 인덱스에 삽입
            else:  # freeze로 이동
                freeze_List.append(next_value)

    # 남은 run 저장
    if run:
        runs.append(run)

    # 결과 출력
    with open("C:\\Users\\dlfwn\\OneDrive\\바탕 화면\\zz\\replacement_output.txt", "a") as f:
        f.write(f"{len(runs)}\n")  # run 개수
        for r in runs:
            f.write(" ".join(map(str, r)) + "\n")
=======
    all_List = list(map(int, input().split())) #정렬할 element 입력 받는 리스트
    list1 = all_List[0:5]  # 첫번째 리스트에 버퍼 만큼 넣기
    for h in range(5):
        all_List.pop(0)

    run = list()  # 메모리 개념
    freeze_List = list() #freeze를 위한 리스트
    r=1 #run 갯수 카운트
    
    for k in range(n):
        if len(list1) == 0:  # freeze일 경우
            r+=1 
            print("all_freeze")
            # run 인자 파일에 작성
            with open("replacement_output2.txt", "a") as file:
                file.write(f"{run}\n") 
            run.clear()
            all_List = freeze_List + all_List
            freeze_List.clear()
            if len(all_List) >= 5:
                list1 = all_List[0:5]  # 앞에서부터 5개만 가져오기
                for h in range(5):
                    all_List.pop(0)  #5개를 pop하여 all_List에서 없앰
            else:
                list1 = all_List[:]  # all_List가 5개보다 적으면 모든 원소를 가져옴
                all_List.clear()  #all 초기화

        min_element = min(list1)  # 리스트에서 가장 작은 값 찾기
        min_element_index = list1.index(min_element)  #인덱스 찾기
        run.append(min_element)  # run에 작은 수 적어넣음
        list1.remove(min_element) 
        if all_List:
            list1.insert(min_element_index, all_List[0])
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
                freeze_List.append(list1[min_element_index])
                list1.pop(min_element_index)  # 그 자리를 채우지 않음

        print(f"run은 {run}")
        print(f"list1은 {list1}")
        print(f"all은 {all_List}")
        print(f"freeze는 {freeze_List}")

    # 마지막 run 리스트가 있을 경우 추가
    if run:
        with open("replacement_output2.txt", "a") as file:
            file.write(f"{run}\n")
        run.clear()
>>>>>>> 96fed91fbc85afbabd2aec707cfe5dae408159eb

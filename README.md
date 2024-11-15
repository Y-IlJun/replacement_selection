"# replacement_selection" 

#시작전 기틀잡기
1.5개 받아오기(리스트)
2.run 생성->리스트가 all_freeze인지 확인
3.그중 가장 작은 수 run으로 보내기->freeze 여부 확인
4.리스트에 다음 수 채우기
5.리스트와 run 숫자 비교
6.if 리스트 수 < run 숫자 :
    리스트 수->freeze
7.freeze 안된 수 중 작은 수 run
8. 4,5,6,7 반복
9.리스트 수가 모두 freeze면 run2 생성 

#freeze를 나타내는 법
1.리스트 2개를 이용하기
  freeze인 경우 freeze 리스트로 따로 빼기
2....

#코드 수정해야할 부분
1.output에 run 사용갯수 먼저 표시하기
2.몇번 돌릴지 num 사용하여 여러번 입력 받을 수 있게 하기
3.코드 함수화 해서 깔끔하게 만들기


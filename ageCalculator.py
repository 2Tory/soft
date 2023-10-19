from datetime import datetime

# 사용자로부터 생년월일 입력 받기
birth_date = input("생년월일을 입력하세요 (예: 2000-01-01): ")

# 현재 날짜 가져오기
current_date = datetime.now()

# 사용자 입력을 날짜 형식으로 변환
birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

# 나이 계산
age = current_date.year - birth_date.year

# 현재 월과 생일 월 비교
if current_date.month < birth_date.month or (current_date.month == birth_date.month and current_date.day < birth_date.day):
    age -= 1

# 결과 출력
print("당신의 나이는 {}세 입니다.".format(age))

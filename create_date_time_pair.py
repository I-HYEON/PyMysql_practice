import random
import datetime

def generate_datetime_pairs(start, end, num_pairs):
    """
    주어진 범위 내에서 서로 다른 두 datetime 쌍을 생성하고,
    시작 시간이 종료 시간보다 항상 빠른지 확인하여 datetime 쌍을 생성합니다.
    :param start: 시작 날짜(datetime 객체)
    :param end: 종료 날짜(datetime 객체)
    :param num_pairs: 생성할 datetime 쌍의 개수
    :return: datetime 쌍의 리스트
    """
    datetime_pairs = []
    for _ in range(num_pairs):
        while True:
            start_time = random_datetime(start, end)
            end_time = random_datetime(start_time, end)
            if start_time < end_time:
                datetime_pairs.append((start_time, end_time))
                break
    return datetime_pairs

def random_datetime(start, end):
    """
    start와 end 사이의 무작위 datetime 객체를 생성하여 반환합니다.
    :param start: 시작 날짜(datetime 객체)
    :param end: 종료 날짜(datetime 객체)
    :return: 무작위 datetime 객체
    """
    delta = end - start
    random_delta = random.randint(0, delta.days)
    random_time = random.random() * 86400  # 1 day = 86400 seconds
    return start + datetime.timedelta(days=random_delta, seconds=random_time)

# 예시: 2024년 1월 1일부터 2024년 12월 31일까지의 무작위 날짜와 시간 쌍 5개 생성
start_date = datetime.datetime(2024, 1, 1)
end_date = datetime.datetime(2024, 12, 31)
datetime_pairs = generate_datetime_pairs(start_date, end_date, 2)

created_at_vals = []
modified_at_vals = []
for pair in datetime_pairs:
    created_at_vals.append(pair[0])
    modified_at_vals.append(pair[1])

print("시작",created_at_vals)
print("끝",modified_at_vals)
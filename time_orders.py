h, m = map(int, input('Время начала сборки через пробел час и минута: ').split())
c = int(input('Количество заказов: '))
avg = [4.18, 4.41, 4.63]
t1 = round((c * avg[2] // 60))
t2 = round((c * avg[2] % 60))
time_h = ((h + t1) + (m + t2) // 60)
time_m = ((m + t2) % 60)
print(f'Примерное время сборки: {t1} ч.{t2} мин.')
print(f'Примерное время окончания сборки: {time_h} ч.{time_m} мин.')

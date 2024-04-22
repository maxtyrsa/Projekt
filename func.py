def _kpi_(url, start_date, end_date):
	import pandas as pd
	import numpy as np
	src = url
	df = pd.read_csv('files/'+src+'csv')
	df = df[df['date'].between(start_date, end_date)]
	mp = df.query("branch == 'MP'") \
	.groupby('date', as_index=False) \
	.agg({'place': 'sum'}) \
	.rename(columns={'place': 'counts'})

	kf = df.query("branch == 'KF'") \
	.groupby('date', as_index=False) \
	.agg({'place': 'count'}) \
	.rename(columns={'place': 'counts'})

#Формула расчета KPI: Индекс KPI = ((Факт – База) / (Норма – База)) * 100%. Прежде чем начинать разработку системы KPI, необходимо задать три уровня эффективности: База. Минимальное допустимое значение, которое служит нулевой точкой для отсчета результатов. Норма. Уровень удовлетворительного значения, учитывающий обстоятельства: ситуацию на рынке, сложность работы, возможности конкретного сотрудника. Цель. Уровень выше норматива, к которому следует стремиться.

	mp['kpi'] = round((mp.counts-10)/(96-10)*100, 2)
	mp.sort_values('date', ascending=False)

	kf['kpi'] = round((kf.counts-1)/(24-1)*100, 2)
	kf.sort_values('date', ascending=False)


	def f(row):
	 if row['kpi'] < 25:
			 val = 0.001
	 elif row['kpi'] < 50:
			 val = 0.002
	 elif row['kpi'] < 75:
			 val = 0.003
	 elif row['kpi'] < 90:
			 val = 0.004
	 elif row['kpi'] < 100:
			 val = 0.005
	 else :
			 val = 0.006
	 return val
	#create new column 'Good' using the function above
	mp['weight'] = mp.apply (f, axis=1)
	mp['result'] = mp.kpi*mp.weight
	mp['money'] = mp.result*880.952381

	kf['weight'] = kf.apply (f, axis=1)
	kf['result'] = kf.kpi*kf.weight
	kf['money'] = kf.result*880.952381

	print ('*'*20, 'KPI Маркетплейс', '*'*20)
	print(mp)
	print('Сумма: ', round((mp.result * 880.952381).sum(), 2))
	print ('*'*20, 'KPI Купи Флакон', '*'*20)
	print(kf)
	print('Сумма: ', round((kf.result * 880.952381).sum(), 2))
	print ('*'*20, 'Итог', '*'*20)
	print('Итого сумма: ', round((mp.result * 880.952381).sum() + (kf.result * 880.952381).sum(), 2))
	print('*'*20, 'Маркетплейс', '*'*20)
	df_mp = df.query(f'branch == "MP"').groupby('t_c', as_index=False)['place'].sum().sort_values('place', ascending=False)
	df_mp['percent'] = df_mp.place/df_mp.place.sum()*100
	print(df_mp)
	print('В среднем за день: ', round(np.median(df_mp.place)), 'шт')
	print('*'*20, 'Купи Флакон', '*'*20)
	df_kf = df.query(f'branch == "KF"').groupby('t_c', as_index=False)['place'].count().sort_values('place', ascending=False)
	df_kf['percent'] = df_kf.place/df_kf.place.sum()*100
	print(df_kf)
	print('В среднем за день: ', round(np.median(df_kf.place)), 'шт')


def _order_(url, start_date, end_date):
	import numpy as np
	import pandas as pd
	src = url
	df = pd.read_csv('files/'+src+'csv')
	df = df[df['date'].between(start_date, end_date)]
	mp = df.query("branch == 'MP'")[['date', 'amount', 't_c']].reset_index(drop=True).rename(columns={'amount': 'counts'}).sort_values('date', ascending=True)

	kf = df.query("branch == 'KF'")[['date', 'number', 't_c']].reset_index(drop=True).sort_values('date', ascending=True)
	kf.number = kf.number.astype(int)
	print('*'*20, 'Маркетплейс', '*'*20)
	print(mp)
	print('*'*20, 'Купи Флакон', '*'*20)
	print(kf)
def _time_orders_(h, m, c):
	h, m = map(int, input('Время начала сборки через пробел час и минута:').split())
	c = int(input('Количество заказов:'))
  	avg = [4.18, 4.41, 4.63]
  	t1 = round((c * avg[2] // 60))
	t2 = round((c * avg[2] % 60))
	time_h = ((h + t1) + (m + t2) // 60)
	time_m = ((m + t2) % 60)
	print(f'Примерное время сборки: {t1} ч. {t2} мин.')
	print(f'Примерное время окончания сборки: {time_h} ч.  {time_m} мин.')
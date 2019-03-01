import numpy as np
import pandas as df
import sys
from datetime import *
from time import *
import csv

# 祝日のデータを読み込む
def import_Pholiday():
	get_data = []

	#祝日データ読み込み先のパス
	path = './import_data/holiday_data.csv'
	with open(path,'r',encoding="utf-8_sig") as f:
		reader = csv.reader(f)
		for row in reader:
			get_data.append(row)

	return get_data

# csv出力先
def write_csv(data):
	# ソースと同じディレクトリにsome.csvとして書き出す
	with open('some.csv', 'w') as f:
		writer = csv.writer(f, lineterminator='\n')
		for i in range(0,len(data)):
			writer.writerow(data[i])

def main():
	#作成するトレンド日数
	trendDay = 1860

	# [日付,月,火,水,木,金,土,日,祝日,祝日の名前,休]
	trend = [[]]
	arr = ["日付","月","火","水","木","金","土","日","祝日","祝日の名前","休日","年末年始"]

	# 今日の日付を選択
	day_now = datetime.today()

	ph_day = import_Pholiday()

	for i in range(len(ph_day)):
		ph_day[i][1] = datetime.strptime(ph_day[i][1], '%Y/%m/%d')
		ph_day[i][1] = datetime.strftime(ph_day[i][1], '%Y%m%d')

	# 日付のフォーマット型を整形
	first_day = day_now.replace(day=1)
	day = datetime.strftime(first_day, '%Y%m%d')
	print(day)

	trend[0] =arr

	# 各日にちのトレンドデータを作成
	for i in range(0,trendDay):
		trend.append([0]*12)
		first_day = first_day - timedelta(days=1)
		day = datetime.strftime(first_day, '%Y%m%d')
		trend[i][0] = day

		if first_day.weekday() == 0:
			trend[i][1] = 1
		elif first_day.weekday() == 1:
			trend[i][2] = 1
		elif first_day.weekday() == 2:
			trend[i][3] = 1
		elif first_day.weekday() == 3:
			trend[i][4] = 1
		elif first_day.weekday() == 4:
			trend[i][5] = 1
		elif first_day.weekday() == 5:
			trend[i][6] = 1
		elif first_day.weekday() == 6:
			trend[i][7] = 1

		if str(day) in str(ph_day):
			trend[i][8] = 1
			for j in range(len(ph_day)):
				if str(day) == str(ph_day[j][1]):
					trend[i][9] = str(ph_day[j][3])

		if str(trend[i][0]).endswith('1231') or str(trend[i][0]).endswith('1231') or str(trend[i][0]).endswith('0101') or str(trend[i][0]).endswith('0102') or str(trend[i][0]).endswith('0103'):
			trend[i][11] = 1

		if trend[i][6] == 1 or trend[i][7] == 1 or trend[i][8] == 1 or trend[i][11]:
			trend[i][10] = 1

		#print(trend[i])

	#print(trend[0])
	#print(trend[1])
	write_csv(trend)

if __name__ == '__main__':
	main()
import numpy as np
import pandas as pd
from datetime import datetime

resources_path = './Resourses/table-1.xls'
results_path = './Resourses/Results/'

# date = '24-02'
# constants = ['BR_Header', 'Godilov', '001','BR','Good','0']
df = pd.read_excel(resources_path)
print(len(df)) #для проверки кол-ва строк в исходном файле
# print(df)
counter = 0

for i in range(len(df)):
    # print(row)
    row = df.iloc[i] # строка, тип - Series (словарь)
    # Обращение к элементам строки - по ключу
    # print(df.iloc[i])
    ser_num = row['номер']
    diameter = round(row['Diam_Okp1'], 3)
    diameter_int = row['Diam_Okp1'].astype(np.int64)

    #Считываем дату и приводим ее
    # к нужному формату согласно ТЗ
    date_old = row['дата']
    # print(date_old)
    date_new = date_old[8:10] + '/' + \
               date_old[3:5] + '/' + \
               date_old[:2] + ' ' + date_old[11:18] + ':00'

    # print(date_new)
    date_time = datetime.strptime(date_new, '%y/%m/%d %H:%M:%S')
    date = str(date_time.year)[2:4] + '-' + str(date_time.month).rjust(2, '0')

    # print(date_time, date)

    string = 'BR' + str(diameter_int)
    # print(type(date_time))

    #создаем строку в формате .csv для записи в файл
    res_arr = [date_time, 'Godilov', date, '001', ser_num, string, diameter, 'Good', 0, 'Good']
    res = 'BR_Header' + '\n' + ','.join(map(str, res_arr))
    # print(res)

    #создаем файл с именем - согласно тз
    file_name = 'Manual_BR_001_' + str(ser_num) + '.csv'
    f = open(results_path + file_name, 'w')
    f.write(res)
    f.close()
    counter += 1
print(counter) #для проверки кол-ва итераций в цикле

import os
from cryptography.fernet import Fernet
from keys import secret_key

fernet_key =Fernet(secret_key)

#создаю список отчетов за месяц и вывожу даты за которые нет данных
list_files_spy = os.listdir('./spy_reports/')
date_october_2023 =  ["01_10_2023" , "02_10_2023", "11_10_2023", "03_10_2023" , "04_10_2023", "12_10_2023","05_10_2023" , "06_10_2023", "13_10_2023",
                      "07_10_2023" , "08_10_2023", "14_10_2023", "09_10_2023" , "10_10_2023", "15_10_2023", "16_10_2023" , "17_10_2023", "18_10_2023",
                      "19_10_2023" ,"20_10_2023", "21_10_2023", "22_10_2023" , "23_10_2023", "24_10_2023", "25_10_2023" , "26_10_2023", "27_10_2023",
                      "28_10_2023" , "29_10_2023", "30_10_2023", "31_10_2023"]
sort_list_files_spy = sorted(list_files_spy)
str1 = ''.join(sort_list_files_spy)
print("=Даты за которые отсутсвует отчет=")
for elem in  date_october_2023:
    if  elem not in str1 :
        print(f'За {elem} отчета нет')
print("======Конец списка==========")
# дешифрую отчеты которые есть и сохраняю в директории decrypted_report
for file in list_files_spy:
    with open(f'./spy_reports/{file}', 'r') as f:
        data_decode = fernet_key.decrypt(f.read()).decode()

    with open(f'./decrypted_reports/{file}', "w") as f:
        f.write(data_decode)









import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

xl_path = "C:\\Users\\sunch\\Desktop\\Цифр_прорыв\\"  # Путь до файла
xl_name = "Семьи с детьми до 18 лет по МО.xlsx"  # Название документа Excel
xl = pd.ExcelFile(xl_path + xl_name)

# Словарь { Район : [100 * Количество малобеспеченных семей / Общее количество семей] }
data = {}
sheets = xl.sheet_names  # Названия листов
for sheet in sheets:
    df = xl.parse(sheet, usecols=[2, 2], engine="openpyxl", skiprows=[0, 1], names=["Families"])
    values = df.values
    data[sheet] = round(100 * int(values[12][0]) / int(values[1][0]), 2)

# Сортировка словаря по значению
sorted_tuples = sorted(data.items(), key=lambda item: item[1])
print(sorted_tuples)
sorted_data = {k: v for k, v in sorted_tuples}


# Шрифт на графике
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }
plt.rcdefaults()
labels = [str(i) + "%" for i in list(sorted_data.values())]
plt.barh(list(sorted_data.keys()), list(sorted_data.values()), align='center', alpha=0.5, color='b')
plt.xlim(0, 100)
plt.grid()
plt.xticks(np.arange(0, 100, 10))
plt.xlabel('% Малообеспеченных семей от общего колоичества семей', fontdict=font)
plt.title('TODO', fontdict=font)


plt.show()


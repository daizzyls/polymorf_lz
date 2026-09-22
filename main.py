from data_set import DataProcessing

data = DataProcessing('var1.csv')

data.split()
removed = -data
print(f"Количество повторяющихся строк в наборе данных: {data.total_deleted}")
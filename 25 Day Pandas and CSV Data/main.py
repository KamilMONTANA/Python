import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
#
# def f(x):
#     x = x * 1.8 + 32
#     return float(x)
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

data = pandas.read_csv("squirrel_data.csv")

grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]
cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]

grey_squirrels_count = len(grey_squirrels)
black_squirrels_count = len(black_squirrels)
cinnamon_squirrels_count = len(cinnamon_squirrels)

print(grey_squirrels_count)
print(black_squirrels_count)
print(cinnamon_squirrels_count)

data_dict ={
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [grey_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")


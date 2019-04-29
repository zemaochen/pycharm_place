import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1.读取csv
data = pd.read_csv('pollution.csv')
#2.去除无效值行
data = data.dropna()
#3.统计每一年的数据条数
years = data.groupby(['year']).size()
years = np.array(years.index)
yearMeanPm = []#存PM2.5计算结果
yearMeanTemp = []#存TEMP计算结果
yearMeanPres = []#存气压计算结果
yearSumIws = []#存降雨量计算结果
for year in years:
    # 提出当前年的数据
    current_year_data = data.loc[data['year'] == year]
    # 对当年数据求平均值
    yearMean = current_year_data['pm2.5'].mean()
    # 存起来
    yearMeanPm.append(yearMean)
    print(str(year) + '年的日平均pm2.5:\n' + str(yearMean))
    # 气温
    yearMean = current_year_data['TEMP'].mean()
    yearMeanTemp.append(yearMean)
    print(str(year) + '年的日平均气温:\n' + str(yearMean))
    # 气压
    yearMean = current_year_data['PRES'].mean()
    yearMeanPres.append(yearMean)
    print(str(year) + '年的日平均气压:\n' + str(yearMean))
    # 年累计降雨量
    yearSum = current_year_data['Iws'].sum()
    yearSumIws.append(yearSum)
    print(str(year) + '年累计降雨量:\n' + str(yearSum))
    print('\n')
# PM2.5
x = range(len(yearMeanPm))
rects1 = plt.bar(x=x, height=yearMeanPm, width=0.5, color='green')
plt.ylabel('pm2.5')
plt.xlabel('year')
plt.title("2010-2014 PM2.5 of day")
plt.xticks([index for index in x], years)
plt.ylim(0, 120)
for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(int(height)), ha="center", va="bottom")
plt.show()
x = range(len(yearMeanTemp))
rects2 = plt.bar(x=x, height=yearMeanTemp, width=0.5, color='red')

# y轴取值范围
plt.ylim(0, 20)
plt.ylabel('℃')
plt.xticks([index for index in x], years)
plt.xlabel('year')
plt.title("2010-2014 temperature average of day ")
for rect in rects2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(int(height)), ha="center", va="bottom")
plt.show()

#折线图 2X2子图
plt.rcParams['figure.figsize'] = (20, 10)
# 221:pm2.5
plt.suptitle('2010-2014')
plt.subplot(221)
plt.plot(years, yearMeanPm, c='red')
plt.xticks(rotation=45)
plt.xlabel('year')
plt.ylabel('pm2.5')
plt.title('PM2.5 average of day')

# 气温
plt.subplot(222)
plt.plot(years, yearMeanTemp, c='blue')
plt.xticks(rotation=45)
plt.xlabel('year')
plt.ylabel('temperature')
plt.title('temperature average of day')

# 气压
plt.subplot(223)
plt.plot(years, yearMeanPres, c='black')
plt.xticks(rotation=45)
plt.xlabel('year')
plt.ylabel('presure')
plt.title('presure average of day')

# 累计降雨量
plt.subplot(224)
plt.plot(years, yearSumIws, c='gray')
plt.xticks(rotation=45)
plt.xlabel('year')
plt.ylabel('mm')
plt.title('annual rainfall')
plt.show()

max_months = []
for year in years:
    # 每一年的数据
    current_year_data = data.loc[data['year'] == year, ['month', 'day', 'pm2.5']]
    # 重新对当前年的月排列 并对pm2.5 只取pm2.5列的值 并降序排列
    month_mean = current_year_data.groupby(['month'])['pm2.5'].mean().sort_values(ascending=False)
    max_months.append(month_mean.index[0])
    max_month = month_mean.index[0]
    max_month_data = current_year_data.loc[current_year_data['month'] == max_month, ['day', 'pm2.5']]
    # 求当月日均pm2.5
    max_month_day_mean_pm = max_month_data.groupby(['day']).mean()
    days = max_month_day_mean_pm.size
    # 取出当前月的每天的pm2.5均值
    pm_values = max_month_day_mean_pm['pm2.5'].values
    colors = ['yellow', 'red', 'green', 'blue', 'black']
    plt.plot(range(days), pm_values, color=colors[year % 10], label=str(year))

plt.legend()  # 让图例生效
xnames = [str(x) for x in range(0, 31)]
plt.xticks(range(31), list(range(1, 32)), rotation=1)
plt.xlabel('day')
plt.ylabel('pm2.5')
plt.show()




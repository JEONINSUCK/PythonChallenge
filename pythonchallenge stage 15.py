import re
import calendar as cal
def cal_year(year):
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return True
    else:
        return False
data = []
for year in range(1000,2017):
    if cal_year(year)==True:
        data.append(year)
    else:
        continue

string = ""
f = []
for i in data:
    string+=str(i)

q = re.compile('[1]..[6]')
year_data = q.findall(string)
print(year_data)
result = []
for i in year_data:
    if (cal.weekday(int(i),1,26)==0):
        print(cal.prmonth(int(i),1))
        result.append(i)

print(year_data)
print(result)
for i in result:
    print(cal.prmonth(int(i), 1))

#print(cal.calendar(1976))
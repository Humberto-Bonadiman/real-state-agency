from datetime import datetime, date

dat = datetime.now().date()
da = date(2022, 11, 20)

print(dat)
print(da)
print(da < dat)

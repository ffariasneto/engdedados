from datetime import date, datetime, time, timedelta

data = date(2024, 10, 8)
print(data)
print(date.today())

data_hora = datetime(2024, 10, 8, 9, 55, 25)
print(data_hora)
print(datetime.today())

hora = time(10, 20, 0)
print(hora)

# Criando data e hora
d = datetime(2024, 10, 8, 10, 8, 50)
print(d)

d = d + timedelta(weeks=1)
print(d)
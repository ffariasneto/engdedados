from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))

print(datetime.strptime(data_hora_str, mascara_en))




























# import datetime

# d = datetime.datetime.now()

# # Formatando data e hora
# print(d.strftime("%d/%m/%Y %H:%M"))

# # Convertendo string para datetime

# date_string = "20/07/2023 15:30"
# d = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
# print(d)
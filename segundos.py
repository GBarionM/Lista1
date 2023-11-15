s = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = s // 86400
hrest = s % 86400
horas = hrest // 3600
mrest = hrest % 3600
minutos = mrest // 60
segundos = mrest % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")

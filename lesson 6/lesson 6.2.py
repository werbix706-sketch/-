seconds = int (input())
days = seconds // 86400
remainder = seconds % 86400
hours = remainder // 3600
remainder = remainder % 3600
minutes = remainder // 60
seconds = remainder % 60
hours = str(hours).zfill(2)
minutes = str(minutes).zfill(2)
seconds = str(seconds).zfill(2)

if days % 100 in [11,12,13,14]:
    day_word = 'дней'

elif days % 10 == 1:
    day_word = 'день'
elif days % 10 in [2,3,4]:
    day_word = 'дня'

else:
    day_word = 'дней'

print(days, day_word + "," , hours + ':' + minutes + ":" + seconds)


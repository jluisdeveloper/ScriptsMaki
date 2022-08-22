import pywhatkit
import datetime
now = datetime.datetime.now()

# print( now.minute + 1)

numbers = ["+51932678688", "+51950708464", "+51956759171", "+51959788121"]

message = 'te envio el brochure: \nhttps://bit.ly/3c3jDpZ \nBot WhatsAPP MAKI TEST'

for i in numbers:
  pywhatkit.sendwhatmsg(i, message, now.hour, now.minute + 1)

# pywhatkit.sendwhatmsg("+51930802146", message, now.hour, now.minute + 1)
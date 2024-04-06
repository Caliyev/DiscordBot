# # Ve işte bir metin dosyasının tamamını nasıl yeniden yazabileceğimiz:
# f = open('metinbelgesi.txt', 'w', encoding='utf-8')
# text = '2024'
# f.write(text)
# f.close()

# Bu kod parçacığı bir metin dosyasının tamamını okumamızı sağlar
# f = open('metinbelgesi.txt', 'r', encoding='utf-8')
# text = f.read()
# print(text)
# f.close()

# Daha kısa bir versiyonu:
with open('metinbelgesi.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# with open('images/cat.jpg', 'rb') as f:
#         picture = discord.File(f)
    

import os
print(os.listdir('M2L1\images'))
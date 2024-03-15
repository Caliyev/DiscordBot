import random

# Kullanıcıdan parola uzunluğunu girmesini isteyin
password_length = int(input("Lütfen parola uzunluğunu giriniz: "))

# Kullanıcının parolasında bulunabilecek tüm karakterleri içeren bir değişken
characters = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Parolayı saklayacağınız değişkeni oluşturun
password = ""

# Karakterler değişkeninden rastgele bir karakter seçip parola değişkenine ekleyin
for i in range(password_length):
    password += random.choice(characters)

# Elde edilen parolayı konsola yazdırın
print(f"Oluşturulan parola: {password}")

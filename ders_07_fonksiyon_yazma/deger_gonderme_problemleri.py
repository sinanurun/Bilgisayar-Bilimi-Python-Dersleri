def say_n(n):
    for i in range(1, n + 1):
        print(i, end=" ")
    print()
for i in range(1, 11):
    say_n(i) # say_n fonksiyonuna i değişken değeri parametre olarak giriliyor
    #say_n() Fonksiyon çağırıldığında eksik parametre hatası verir.
    #say_n(3, 5) Fonksiyon çağırıldığında fazla parametre hatası verir.
    #say_n(3.2) Tam sayı olmadığı için çalışma zamanı hatası verir.
    #say_n("ali") Tam sayı olmadığı için çalışma zamanı hatası verir str yollandığı için.
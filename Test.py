# -*- coding: cp1254 -*-
ths = open("D://SonucTest.txt", "w")
karaktertoplayici1 = []#boş bir karaktertoplayıcı adında bir dizi oluşturuyoruz

testkarakter = []#boş bir testkarakter adında bir dizi oluşturuyoruz
import time#süre değerlerini almak için time kütüphanesini çağırıyoruz


def rasgeleKarakter(kackezuretsin1):#rasgeleKarakter adında tek tek sayı almak için bir method oluşturuyoruz. bu method rasgeleliği test etmek için oluşturuldu
    formul = 1#formul değişkenini oluşturuyoruz.

    saniye = time.time()#saniye değişkeninin içine 1 ocak 1970'den bu yana geçen saniye değerini alıyoruz
    toplam = saniye#toplam değişkeninin içibe atıyoruz saniye değerini

    krt = ""#krt adında gelen karakterleri tutacak bir değişkken oluşturuyoruz
    for x in range(1, kackezuretsin1 + 1):#kaç tane sayı olmasını belirliyor bu döngü
        for i in range(1, 3):#bu for döngüsü değerleri dönderiyor.
            for j in range(1, i):#bu for döngüsü saniyeden alan değeri rasgele çarpım kuralı için işlem dönderiyor
                toplam = toplam * 3#alınan saniye değerini 3 sayısı ile çarpıyoruz

        formul = toplam % 25#sonuç olarak aldığımız değerin sayı aralığı olarak mod 25'ini alıyoruz. 25 sayısı 25 tane harf olduğu için bırakıldı

        if formul < 0:#saniyeden alınan değerler çarpım durumunda negatife düşmemesi için bir şart sundum
            formul = formul * -1#negatif değeri pozitif yapıyoruz
            formul = formul + 97#en düşük ascii değeri olan a harfi 97'ye tamamladım. değerin alt sınırı belli olsun diye.
            krt = chr(int(formul))#aldığımız sayııyı int ile ondalıklı sayıdan kurtarıp chr komutu ile karaktere çeviriyoruz ve krt içine atıyoruz
            karaktertoplayici1.append(krt)#karaktertoplayıcı dizisine append komutu ile alınan karakterleri ekliyoruz
            c = str(x)#str komutu ile x değerini döngüde alıp her defasında hangi karakter olduğunu elirtiyoruz. sayaç görevi görüyor.


        else:
            formul = formul + 97#en düşük ascii değeri olan a harfi 97'ye tamamladım. değerin alt sınırı belli olsun diye.
            krt = chr(int(formul))#aldığımız sayııyı int ile ondalıklı sayıdan kurtarıp chr komutu ile karaktere çeviriyoruz ve krt içine atıyoruz
            karaktertoplayici1.append(krt)#karaktertoplayıcı dizisine append komutu ile alınan karakterleri ekliyoruz
            c = str(x)#str komutu ile x değerini döngüde alıp her defasında hangi karakter olduğunu elirtiyoruz. sayaç görevi görüyor.


def test():# test adında bir method oluşturduk
    basarilisayac = 0# basarili ve basarisiz durumları saymak icin int degiskenler
    basarisizsayac = 0# basarili ve basarisiz durumları saymak icin int degiskenler
    rasgeleKarakter(100)# rastgelekarakter fonksiyonundan 100 tane rastgele karakter üretiyoruz
    for i in range(1, 101): # 100 karakter oldugu icin range de 1-11 arası sayac donderiyoruz
        testkarakter.append(karaktertoplayici1[i - 1])# testkarakter dizisine rastgele karakterleri ekliyoruz

    for ii in range(1, 101):# test icin en bastan rastgele karakterler uretiyoruz
        rasgeleKarakter(100)# rastgelekarakter fonksiyonundan 100 tane rastgele karakter üretiyoruz

        karakter1 = str(testkarakter[ii - 1])# rastgele uretilen karakterleri string turune cevirip bos karakter1 stringine atıyoruz
        karakter2 = str(karaktertoplayici1[ii - 1])# rastgele uretilen karakterleri string turune cevirip bos karakter2 stringine atıyoruz

        if (karakter1 == karakter2):# en basta uretilen karakter ile sonradan uretilen karakter aynı mı diye kontrol ediyoruz
            basarisizsayac = basarisizsayac + 1# aynı ise durumu basarisiz gorup basarısız sayacı 1 arttırıyoruz

        elif (karakter1 != karakter2):# en basta uretilen karakter ile sonradan uretilen karakter farklı mı diye kontrol ediyoruz
            basarilisayac = basarilisayac + 1# farklı ise basarilisayac i 1 arttiriyoruz

    if (basarisizsayac > basarilisayac):# eger basarisiz durum basarili durumdan buyuk ise test basarisiz
        print("test basarili\n")
        ths.write("Test Başarılı")

    if (basarilisayac > basarisizsayac):# eger basarili durum basarisiz durumdan buyuk ise test basarili
        print("test basarisiz\n")
        ths.write("Test Başarısız")

test() # test fonksiyonunun cagrisini yapiyoruz
ths.close()


# -*- coding: cp1254 -*-
ths = open("D://SonucTest.txt", "w")
karaktertoplayici1 = []#bo� bir karaktertoplay�c� ad�nda bir dizi olu�turuyoruz

testkarakter = []#bo� bir testkarakter ad�nda bir dizi olu�turuyoruz
import time#s�re de�erlerini almak i�in time k�t�phanesini �a��r�yoruz


def rasgeleKarakter(kackezuretsin1):#rasgeleKarakter ad�nda tek tek say� almak i�in bir method olu�turuyoruz. bu method rasgeleli�i test etmek i�in olu�turuldu
    formul = 1#formul de�i�kenini olu�turuyoruz.

    saniye = time.time()#saniye de�i�keninin i�ine 1 ocak 1970'den bu yana ge�en saniye de�erini al�yoruz
    toplam = saniye#toplam de�i�keninin i�ibe at�yoruz saniye de�erini

    krt = ""#krt ad�nda gelen karakterleri tutacak bir de�i�kken olu�turuyoruz
    for x in range(1, kackezuretsin1 + 1):#ka� tane say� olmas�n� belirliyor bu d�ng�
        for i in range(1, 3):#bu for d�ng�s� de�erleri d�nderiyor.
            for j in range(1, i):#bu for d�ng�s� saniyeden alan de�eri rasgele �arp�m kural� i�in i�lem d�nderiyor
                toplam = toplam * 3#al�nan saniye de�erini 3 say�s� ile �arp�yoruz

        formul = toplam % 25#sonu� olarak ald���m�z de�erin say� aral��� olarak mod 25'ini al�yoruz. 25 say�s� 25 tane harf oldu�u i�in b�rak�ld�

        if formul < 0:#saniyeden al�nan de�erler �arp�m durumunda negatife d��memesi i�in bir �art sundum
            formul = formul * -1#negatif de�eri pozitif yap�yoruz
            formul = formul + 97#en d���k ascii de�eri olan a harfi 97'ye tamamlad�m. de�erin alt s�n�r� belli olsun diye.
            krt = chr(int(formul))#ald���m�z say��y� int ile ondal�kl� say�dan kurtar�p chr komutu ile karaktere �eviriyoruz ve krt i�ine at�yoruz
            karaktertoplayici1.append(krt)#karaktertoplay�c� dizisine append komutu ile al�nan karakterleri ekliyoruz
            c = str(x)#str komutu ile x de�erini d�ng�de al�p her defas�nda hangi karakter oldu�unu elirtiyoruz. saya� g�revi g�r�yor.


        else:
            formul = formul + 97#en d���k ascii de�eri olan a harfi 97'ye tamamlad�m. de�erin alt s�n�r� belli olsun diye.
            krt = chr(int(formul))#ald���m�z say��y� int ile ondal�kl� say�dan kurtar�p chr komutu ile karaktere �eviriyoruz ve krt i�ine at�yoruz
            karaktertoplayici1.append(krt)#karaktertoplay�c� dizisine append komutu ile al�nan karakterleri ekliyoruz
            c = str(x)#str komutu ile x de�erini d�ng�de al�p her defas�nda hangi karakter oldu�unu elirtiyoruz. saya� g�revi g�r�yor.


def test():# test ad�nda bir method olu�turduk
    basarilisayac = 0# basarili ve basarisiz durumlar� saymak icin int degiskenler
    basarisizsayac = 0# basarili ve basarisiz durumlar� saymak icin int degiskenler
    rasgeleKarakter(100)# rastgelekarakter fonksiyonundan 100 tane rastgele karakter �retiyoruz
    for i in range(1, 101): # 100 karakter oldugu icin range de 1-11 aras� sayac donderiyoruz
        testkarakter.append(karaktertoplayici1[i - 1])# testkarakter dizisine rastgele karakterleri ekliyoruz

    for ii in range(1, 101):# test icin en bastan rastgele karakterler uretiyoruz
        rasgeleKarakter(100)# rastgelekarakter fonksiyonundan 100 tane rastgele karakter �retiyoruz

        karakter1 = str(testkarakter[ii - 1])# rastgele uretilen karakterleri string turune cevirip bos karakter1 stringine at�yoruz
        karakter2 = str(karaktertoplayici1[ii - 1])# rastgele uretilen karakterleri string turune cevirip bos karakter2 stringine at�yoruz

        if (karakter1 == karakter2):# en basta uretilen karakter ile sonradan uretilen karakter ayn� m� diye kontrol ediyoruz
            basarisizsayac = basarisizsayac + 1# ayn� ise durumu basarisiz gorup basar�s�z sayac� 1 artt�r�yoruz

        elif (karakter1 != karakter2):# en basta uretilen karakter ile sonradan uretilen karakter farkl� m� diye kontrol ediyoruz
            basarilisayac = basarilisayac + 1# farkl� ise basarilisayac i 1 arttiriyoruz

    if (basarisizsayac > basarilisayac):# eger basarisiz durum basarili durumdan buyuk ise test basarisiz
        print("test basarili\n")
        ths.write("Test Ba�ar�l�")

    if (basarilisayac > basarisizsayac):# eger basarili durum basarisiz durumdan buyuk ise test basarili
        print("test basarisiz\n")
        ths.write("Test Ba�ar�s�z")

test() # test fonksiyonunun cagrisini yapiyoruz
ths.close()


# -*- coding: cp1254 -*-
ths = open("D://Sonuc.txt", "w")

karaktertoplayici1 = []#bo� bir karaktertoplay�c� ad�nda bir dizi olu�turuyoruz
import time#s�re de�erlerini almak i�in time k�t�phanesini �a��r�yoruz




def rasgeleKarakter(kackezuretsin1):#rasgeleKarakter ad�nda tek tek karakter almak i�in bir method olu�turuyoruz
    formul = 1#formul de�i�kenini olu�turuyoruz.

    saniye = time.time()#saniye de�i�keninin i�ine 1 ocak 1970'den bu yana ge�en saniye de�erini al�yoruz
    toplam = saniye#toplam de�i�keninin i�ibe at�yoruz saniye de�erini

    krt = ""#krt ad�nda gelen karakterleri tutacak bir de�i�kken olu�turuyoruz
    for x in range(1, kackezuretsin1 + 1):#bu for d�ng�s� ka� tane karakter olu�turaca��n� kullan�c�dan alacak de�er ile belirliyor.
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
            print(c+".Rasgele Karakter:"+karaktertoplayici1[x-1])#x de�eri 1 den ba�lad��� i�in 1 azaltt�k. bu sayede dizi indeks 0 dan ba�layarak print komutu ile ekrana yazd�r�yoruz
            ths.write(c+".Rasgele Karakter:"+karaktertoplayici1[x-1]+"\n")


        else:#gelen de�er pozitifse
            formul = formul + 97#en d���k ascii de�eri olan a harfi 97'ye tamamlad�m. de�erin alt s�n�r� belli olsun diye.
            krt = chr(int(formul))#ald���m�z say��y� int ile ondal�kl� say�dan kurtar�p chr komutu ile karaktere �eviriyoruz ve krt i�ine at�yoruz
            karaktertoplayici1.append(krt)#karaktertoplay�c� dizisine append komutu ile al�nan karakterleri ekliyoruz
            c = str(x)#str komutu ile x de�erini d�ng�de al�p her defas�nda hangi karakter oldu�unu elirtiyoruz. saya� g�revi g�r�yor.
            print(c+".Rasgele Karakter:"+karaktertoplayici1[x-1])#x de�eri 1 den ba�lad��� i�in 1 azaltt�k. bu sayede dizi indeks 0 dan ba�layarak print komutu ile ekrana yazd�r�yoruz
            ths.write(c + ".Rasgele Karakter:" + karaktertoplayici1[x - 1]+"\n")

def Kelimeolustur(kackezuretsin):#kelime olu�ruemak i�in method olu�turuyoruz. ka� tane kelime olmas� gerekti�ini girdi olarak veriyoruz
    formul = 1#formul de�i�kenini olu�turuyoruz.

    saniye = time.time()#saniye de�i�keninin i�ine 1 ocak 1970'den bu yana ge�en saniye de�erini al�yoruz
    toplam = saniye#toplam de�i�keninin i�ibe at�yoruz saniye de�erini
    krt = ""#krt ad�nda gelen karakterleri tutacak bir de�i�kken olu�turuyoruz
    karaktertoplayici2 = ""#karaktertoplay�c� ad�nda gelen karakterleri tutacak bir de�i�kken olu�turuyoruz
    for x in range(1, kackezuretsin + 1):#bu d�ng� ka� tane kelime �retmesi i�in olu�turdum
        for i in range(1, 3):#bu for d�ng�s� de�erleri d�nderiyor.
            for j in range(1, i):#bu for d�ng�s� saniyeden alan de�eri rasgele �arp�m kural� i�in i�lem d�nderiyor
                toplam = toplam * 3#al�nan saniye de�erini 3 say�s� ile �arp�yoruz

        formul = toplam % 25#sonu� olarak ald���m�z de�erin say� aral��� olarak mod 25'ini al�yoruz. 25 say�s� 25 tane harf oldu�u i�in b�rak�ld�
        if formul < 0:#saniyeden al�nan de�erler �arp�m durumunda negatife d��memesi i�in bir �art sundum
            formul = formul * -1#negatif de�eri pozitif yap�yoruz
            formul = formul + 97#en d���k ascii de�eri olan a harfi 97'ye tamamlad�m. de�erin alt s�n�r� belli olsun diye.
            krt = chr(int(formul))#ald���m�z say��y� int ile ondal�kl� say�dan kurtar�p chr komutu ile karaktere �eviriyoruz ve krt i�ine at�yoruz
            karaktertoplayici2+=krt#krt i�indeki de�erleri karaktertoplay�c� i�ine at�yoruz
            c = str(x)#str komutu ile x de�erini d�ng�de al�p her defas�nda hangi karakter oldu�unu elirtiyoruz. saya� g�revi g�r�yor.


        else:#gelen de�er pozitifse
            formul = formul + 97#en d���k ascii de�eri olan a harfi 97'ye tamamlad�m. de�erin alt s�n�r� belli olsun diye.
            krt = chr(int(formul))#ald���m�z say��y� int ile ondal�kl� say�dan kurtar�p chr komutu ile karaktere �eviriyoruz ve krt i�ine at�yoruz
            karaktertoplayici2+=krt#krt i�indeki de�erleri karaktertoplay�c� i�ine at�yoruz
            c = str(x)#str komutu ile x de�erini d�ng�de al�p her defas�nda hangi karakter oldu�unu elirtiyoruz. saya� g�revi g�r�yor.

    print(karaktertoplayici2)#ald���m�z karakterleri kelime halinde yazd�r�yor
    ths.write("kelime:")
    ths.write(karaktertoplayici2)
    ths.write("\n")

def Cumleolusturma(kackezuretsin,sayi):#c�mle olu�turmak i�in bir method olu�turduk
    formul = 1#formul de�i�kenini olu�turuyoruz.

    saniye = time.time()#saniye de�i�keninin i�ine 1 ocak 1970'den bu yana ge�en saniye de�erini al�yoruz
    toplam = saniye#toplam de�i�keninin i�ibe at�yoruz saniye de�erini
    krt = ""#krt ad�nda gelen karakterleri tutacak bir de�i�kken olu�turuyoruz
    cumleolusturma = ""#cumleolusturma ad�nda gelen karakterleri tutacak bir de�i�kken olu�turuyoruz
    for a in range(1,sayi+1):#c�mle i�inde ka� tane kelime olmas�n� kullan�c�dan al�yoruz
        for x in range(1, kackezuretsin + 1):#kelimelerin ka� harfli olmas� i�in kullan�c�dan al�nan de�er ile i�lem yapmas� i�in d�nd��r�yor
            for i in range(1, 3):#bu for d�ng�s� de�erleri d�nderiyor.
                for j in range(1, i):#bu for d�ng�s� saniyeden alan de�eri rasgele �arp�m kural� i�in i�lem d�nderiyor
                    toplam = toplam * 3#al�nan saniye de�erini 3 say�s� ile �arp�yoruz

            formul = toplam % 25#sonu� olarak ald���m�z de�erin say� aral��� olarak mod 25'ini al�yoruz. 25 say�s� 25 tane harf oldu�u i�in b�rak�ld�
            if formul < 0:#saniyeden al�nan de�erler �arp�m durumunda negatife d��memesi i�in bir �art sundum
                formul = formul * -1#negatif de�eri pozitif yap�yoruz
                formul = formul + 97#en d���k ascii de�eri olan a harfi 97'ye tamamlad�m. de�erin alt s�n�r� belli olsun diye.
                krt = chr(int(formul))#ald���m�z say��y� int ile ondal�kl� say�dan kurtar�p chr komutu ile karaktere �eviriyoruz ve krt i�ine at�yoruz
                cumleolusturma+=krt#krt den al�nan de�erleri cumleolustur de�i�kenine at�yoruz
                c = str(x)#str komutu ile x de�erini d�ng�de al�p her defas�nda hangi karakter oldu�unu elirtiyoruz. saya� g�revi g�r�yor.


            else:#gelen de�er pozitifse
                formul = formul + 97#en d���k ascii de�eri olan a harfi 97'ye tamamlad�m. de�erin alt s�n�r� belli olsun diye.
                krt = chr(int(formul))#ald���m�z say��y� int ile ondal�kl� say�dan kurtar�p chr komutu ile karaktere �eviriyoruz ve krt i�ine at�yoruz
                cumleolusturma+=krt#krt i�indeki de�erleri cumleolusturma i�ine at�yoruz.
                c = str(x)#str komutu ile x de�erini d�ng�de al�p her defas�nda hangi karakter oldu�unu elirtiyoruz. saya� g�revi g�r�yor.
        cumleolusturma+=" "#olu�turulan kelimeleri ay�rmak i�in cumleolu�turma listesine her d�ng�de bo�luk karakteri ekleniyor
    print(cumleolusturma)#cumleolustur de�erini yazd�r�yoruz
    ths.write("Cumle:")
    ths.write(cumleolusturma+"\n\n")

def VerilenIkiKarakterAras�(karakter1,karakter2):#iki karakter aras�nda rasgele de�er �retmesi i�in bir method olu�turuyoruz
    formul=1#formul de�i�kenini olu�turuyoruz.
    saniye=time.time()#saniye de�i�keninin i�ine 1 ocak 1970'den bu yana ge�en saniye de�erini al�yoruz
    karakter=""#karakter adl� de�i�kene de�erler at�l�yor.
    sayi1=int(karakter1)#al�nan ilk de�er sayi1 de�i�kenine at�yoruz
    sayi2=int(karakter2)#al�nan son de�er sayi2 de�i�kenine at�yoruz
    toplam=sayi2-98#burada son de�eri belirliyoruz.ascii ye g�re en d���k karakterin de�eri ekliyoruz

    for a in range(1,3):#yan yana veya tek yazd�rma yapmak i�in bu d�ng�y� kullan�yoruz
        for i in range(1,3):#bu for d�ng�s� de�erleri d�nderiyor.
            for j in range(1,i):#bu for d�ng�s� saniyeden alan de�eri rasgele �arp�m kural� i�in i�lem d�nderiyor
                saniye=saniye*3#al�nan saniye de�erini 3 say�s� ile �arp�yoruz
        formul=saniye%toplam#gelen �arp�m de�erini �st s�n�r� al�nan toplam de�eri ile bir s�n�r belirliyoruz

        if formul<0:#saniyeden al�nan de�erler �arp�m durumunda negatife d��memesi i�in bir �art sundum
            formul=formul*-1#negatif de�eri pozitif yap�yoruz
            formul=formul+97#en d���k ascii de�eri olan a harfi 97'ye tamamlad�m. de�erin alt s�n�r� belli olsun diye


            karakter+=chr(int(formul))#karakter adl� listeye ekleme yap�yoruz karaktere �evirerek
        else:#gelen de�er pozitifse
            formul=formul+97#en d���k ascii de�eri olan a harfi 97'ye tamamlad�m. de�erin alt s�n�r� belli olsun diye.
            karakter += chr(int(formul))#karakter adl� listeye ekleme yap�yoruz karaktere �evirerek

    print("Verilen �ki Karakter("+chr(int(sayi1))+","+chr(int(sayi2))+"):" + chr(int(formul)))#verilen de�erler aras� tek karakter yazd�r�yor
    print("Verilen �ki Karakter("+chr(int(sayi1))+","+chr(int(sayi2))+"):" + karakter)#karakter listesi yazd�r�l�yor

    ths.write("Verilen iki karakter("+chr(int(sayi1))+","+chr(int(sayi2))+"):"+chr(int(formul))+"\n")
    ths.write("Verilen �ki Karakter("+chr(int(sayi1))+","+chr(int(sayi2))+"):" + karakter+"\n")








karakter1 = ""#karakter1 listesi olu�turduk
karakter2 = ""#karakter2 listesi olu�turduk
x=int(input("kac deger uretilsin\n"))#rasgele ka� de�er olu�turmak i�in de�er al�yor
rasgeleKarakter(x)#de�eri rasgeleKarakter methoduna g�nderiyor



print("\n\n############## RASTGELE KEL�ME OLU�TURMA ##############\n\n")
ths.write("\n\n############## RASTGELE KEL�ME OLU�TURMA ##############\n\n")
y = int(input("kac harfli rasgele kelime uretilsin?\n"))#ka� harfli bir kelime oluu�turulmas�n� istiyor ve input ile y ye at�yor
Kelimeolustur(y)#al�nan y de�eri Kelimeolustur methoduna g�nderiyor



print("\n\n############## RASTGELE C�MLE OLU�TURMA ##############\n\n")
ths.write("\n\n############## RASTGELE C�MLE OLU�TURMA ##############\n\n")
kelimeuzunlugu = int(input("C�mledeki kelimeler kac harfli olsun?\n"))#ka� harfli kelime olmas� i�in de�er al�yor
cumleuzunlugu=int(input("kac kelime olustursun?"))#c�mlenin ka� kelime olmas�n� al�yor
Cumleolusturma(kelimeuzunlugu,cumleuzunlugu)#Cumleolusturma methhoduna g�nderiyoruz de�erleri



VerilenIkiKarakterAras�(97,111)#a ile o karakterleri aras�nda rasgele de�er �retmesi i�in program i�i hethoda girdi g�nderdik


ths.close()
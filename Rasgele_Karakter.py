# -*- coding: cp1254 -*-
ths = open("D://Sonuc.txt", "w")

karaktertoplayici1 = []#boş bir karaktertoplayıcı adında bir dizi oluşturuyoruz
import time#süre değerlerini almak için time kütüphanesini çağırıyoruz




def rasgeleKarakter(kackezuretsin1):#rasgeleKarakter adında tek tek karakter almak için bir method oluşturuyoruz
    formul = 1#formul değişkenini oluşturuyoruz.

    saniye = time.time()#saniye değişkeninin içine 1 ocak 1970'den bu yana geçen saniye değerini alıyoruz
    toplam = saniye#toplam değişkeninin içibe atıyoruz saniye değerini

    krt = ""#krt adında gelen karakterleri tutacak bir değişkken oluşturuyoruz
    for x in range(1, kackezuretsin1 + 1):#bu for döngüsü kaç tane karakter oluşturacağını kullanıcıdan alacak değer ile belirliyor.
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
            print(c+".Rasgele Karakter:"+karaktertoplayici1[x-1])#x değeri 1 den başladığı için 1 azalttık. bu sayede dizi indeks 0 dan başlayarak print komutu ile ekrana yazdırıyoruz
            ths.write(c+".Rasgele Karakter:"+karaktertoplayici1[x-1]+"\n")


        else:#gelen değer pozitifse
            formul = formul + 97#en düşük ascii değeri olan a harfi 97'ye tamamladım. değerin alt sınırı belli olsun diye.
            krt = chr(int(formul))#aldığımız sayııyı int ile ondalıklı sayıdan kurtarıp chr komutu ile karaktere çeviriyoruz ve krt içine atıyoruz
            karaktertoplayici1.append(krt)#karaktertoplayıcı dizisine append komutu ile alınan karakterleri ekliyoruz
            c = str(x)#str komutu ile x değerini döngüde alıp her defasında hangi karakter olduğunu elirtiyoruz. sayaç görevi görüyor.
            print(c+".Rasgele Karakter:"+karaktertoplayici1[x-1])#x değeri 1 den başladığı için 1 azalttık. bu sayede dizi indeks 0 dan başlayarak print komutu ile ekrana yazdırıyoruz
            ths.write(c + ".Rasgele Karakter:" + karaktertoplayici1[x - 1]+"\n")

def Kelimeolustur(kackezuretsin):#kelime oluşruemak için method oluşturuyoruz. kaç tane kelime olması gerektiğini girdi olarak veriyoruz
    formul = 1#formul değişkenini oluşturuyoruz.

    saniye = time.time()#saniye değişkeninin içine 1 ocak 1970'den bu yana geçen saniye değerini alıyoruz
    toplam = saniye#toplam değişkeninin içibe atıyoruz saniye değerini
    krt = ""#krt adında gelen karakterleri tutacak bir değişkken oluşturuyoruz
    karaktertoplayici2 = ""#karaktertoplayıcı adında gelen karakterleri tutacak bir değişkken oluşturuyoruz
    for x in range(1, kackezuretsin + 1):#bu döngü kaç tane kelime üretmesi için oluşturdum
        for i in range(1, 3):#bu for döngüsü değerleri dönderiyor.
            for j in range(1, i):#bu for döngüsü saniyeden alan değeri rasgele çarpım kuralı için işlem dönderiyor
                toplam = toplam * 3#alınan saniye değerini 3 sayısı ile çarpıyoruz

        formul = toplam % 25#sonuç olarak aldığımız değerin sayı aralığı olarak mod 25'ini alıyoruz. 25 sayısı 25 tane harf olduğu için bırakıldı
        if formul < 0:#saniyeden alınan değerler çarpım durumunda negatife düşmemesi için bir şart sundum
            formul = formul * -1#negatif değeri pozitif yapıyoruz
            formul = formul + 97#en düşük ascii değeri olan a harfi 97'ye tamamladım. değerin alt sınırı belli olsun diye.
            krt = chr(int(formul))#aldığımız sayııyı int ile ondalıklı sayıdan kurtarıp chr komutu ile karaktere çeviriyoruz ve krt içine atıyoruz
            karaktertoplayici2+=krt#krt içindeki değerleri karaktertoplayıcı içine atıyoruz
            c = str(x)#str komutu ile x değerini döngüde alıp her defasında hangi karakter olduğunu elirtiyoruz. sayaç görevi görüyor.


        else:#gelen değer pozitifse
            formul = formul + 97#en düşük ascii değeri olan a harfi 97'ye tamamladım. değerin alt sınırı belli olsun diye.
            krt = chr(int(formul))#aldığımız sayııyı int ile ondalıklı sayıdan kurtarıp chr komutu ile karaktere çeviriyoruz ve krt içine atıyoruz
            karaktertoplayici2+=krt#krt içindeki değerleri karaktertoplayıcı içine atıyoruz
            c = str(x)#str komutu ile x değerini döngüde alıp her defasında hangi karakter olduğunu elirtiyoruz. sayaç görevi görüyor.

    print(karaktertoplayici2)#aldığımız karakterleri kelime halinde yazdırıyor
    ths.write("kelime:")
    ths.write(karaktertoplayici2)
    ths.write("\n")

def Cumleolusturma(kackezuretsin,sayi):#cümle oluşturmak için bir method oluşturduk
    formul = 1#formul değişkenini oluşturuyoruz.

    saniye = time.time()#saniye değişkeninin içine 1 ocak 1970'den bu yana geçen saniye değerini alıyoruz
    toplam = saniye#toplam değişkeninin içibe atıyoruz saniye değerini
    krt = ""#krt adında gelen karakterleri tutacak bir değişkken oluşturuyoruz
    cumleolusturma = ""#cumleolusturma adında gelen karakterleri tutacak bir değişkken oluşturuyoruz
    for a in range(1,sayi+1):#cümle içinde kaç tane kelime olmasını kullanıcıdan alıyoruz
        for x in range(1, kackezuretsin + 1):#kelimelerin kaç harfli olması için kullanıcıdan alınan değer ile işlem yapması için döndüürüyor
            for i in range(1, 3):#bu for döngüsü değerleri dönderiyor.
                for j in range(1, i):#bu for döngüsü saniyeden alan değeri rasgele çarpım kuralı için işlem dönderiyor
                    toplam = toplam * 3#alınan saniye değerini 3 sayısı ile çarpıyoruz

            formul = toplam % 25#sonuç olarak aldığımız değerin sayı aralığı olarak mod 25'ini alıyoruz. 25 sayısı 25 tane harf olduğu için bırakıldı
            if formul < 0:#saniyeden alınan değerler çarpım durumunda negatife düşmemesi için bir şart sundum
                formul = formul * -1#negatif değeri pozitif yapıyoruz
                formul = formul + 97#en düşük ascii değeri olan a harfi 97'ye tamamladım. değerin alt sınırı belli olsun diye.
                krt = chr(int(formul))#aldığımız sayııyı int ile ondalıklı sayıdan kurtarıp chr komutu ile karaktere çeviriyoruz ve krt içine atıyoruz
                cumleolusturma+=krt#krt den alınan değerleri cumleolustur değişkenine atıyoruz
                c = str(x)#str komutu ile x değerini döngüde alıp her defasında hangi karakter olduğunu elirtiyoruz. sayaç görevi görüyor.


            else:#gelen değer pozitifse
                formul = formul + 97#en düşük ascii değeri olan a harfi 97'ye tamamladım. değerin alt sınırı belli olsun diye.
                krt = chr(int(formul))#aldığımız sayııyı int ile ondalıklı sayıdan kurtarıp chr komutu ile karaktere çeviriyoruz ve krt içine atıyoruz
                cumleolusturma+=krt#krt içindeki değerleri cumleolusturma içine atıyoruz.
                c = str(x)#str komutu ile x değerini döngüde alıp her defasında hangi karakter olduğunu elirtiyoruz. sayaç görevi görüyor.
        cumleolusturma+=" "#oluşturulan kelimeleri ayırmak için cumleoluşturma listesine her döngüde boşluk karakteri ekleniyor
    print(cumleolusturma)#cumleolustur değerini yazdırıyoruz
    ths.write("Cumle:")
    ths.write(cumleolusturma+"\n\n")

def VerilenIkiKarakterArası(karakter1,karakter2):#iki karakter arasında rasgele değer üretmesi için bir method oluşturuyoruz
    formul=1#formul değişkenini oluşturuyoruz.
    saniye=time.time()#saniye değişkeninin içine 1 ocak 1970'den bu yana geçen saniye değerini alıyoruz
    karakter=""#karakter adlı değişkene değerler atılıyor.
    sayi1=int(karakter1)#alınan ilk değer sayi1 değişkenine atıyoruz
    sayi2=int(karakter2)#alınan son değer sayi2 değişkenine atıyoruz
    toplam=sayi2-98#burada son değeri belirliyoruz.ascii ye göre en düşük karakterin değeri ekliyoruz

    for a in range(1,3):#yan yana veya tek yazdırma yapmak için bu döngüyü kullanıyoruz
        for i in range(1,3):#bu for döngüsü değerleri dönderiyor.
            for j in range(1,i):#bu for döngüsü saniyeden alan değeri rasgele çarpım kuralı için işlem dönderiyor
                saniye=saniye*3#alınan saniye değerini 3 sayısı ile çarpıyoruz
        formul=saniye%toplam#gelen çarpım değerini üst sınırı alınan toplam değeri ile bir sınır belirliyoruz

        if formul<0:#saniyeden alınan değerler çarpım durumunda negatife düşmemesi için bir şart sundum
            formul=formul*-1#negatif değeri pozitif yapıyoruz
            formul=formul+97#en düşük ascii değeri olan a harfi 97'ye tamamladım. değerin alt sınırı belli olsun diye


            karakter+=chr(int(formul))#karakter adlı listeye ekleme yapıyoruz karaktere çevirerek
        else:#gelen değer pozitifse
            formul=formul+97#en düşük ascii değeri olan a harfi 97'ye tamamladım. değerin alt sınırı belli olsun diye.
            karakter += chr(int(formul))#karakter adlı listeye ekleme yapıyoruz karaktere çevirerek

    print("Verilen İki Karakter("+chr(int(sayi1))+","+chr(int(sayi2))+"):" + chr(int(formul)))#verilen değerler arası tek karakter yazdırıyor
    print("Verilen İki Karakter("+chr(int(sayi1))+","+chr(int(sayi2))+"):" + karakter)#karakter listesi yazdırılıyor

    ths.write("Verilen iki karakter("+chr(int(sayi1))+","+chr(int(sayi2))+"):"+chr(int(formul))+"\n")
    ths.write("Verilen İki Karakter("+chr(int(sayi1))+","+chr(int(sayi2))+"):" + karakter+"\n")








karakter1 = ""#karakter1 listesi oluşturduk
karakter2 = ""#karakter2 listesi oluşturduk
x=int(input("kac deger uretilsin\n"))#rasgele kaç değer oluşturmak için değer alıyor
rasgeleKarakter(x)#değeri rasgeleKarakter methoduna gönderiyor



print("\n\n############## RASTGELE KELİME OLUŞTURMA ##############\n\n")
ths.write("\n\n############## RASTGELE KELİME OLUŞTURMA ##############\n\n")
y = int(input("kac harfli rasgele kelime uretilsin?\n"))#kaç harfli bir kelime oluuşturulmasını istiyor ve input ile y ye atıyor
Kelimeolustur(y)#alınan y değeri Kelimeolustur methoduna gönderiyor



print("\n\n############## RASTGELE CÜMLE OLUŞTURMA ##############\n\n")
ths.write("\n\n############## RASTGELE CÜMLE OLUŞTURMA ##############\n\n")
kelimeuzunlugu = int(input("Cümledeki kelimeler kac harfli olsun?\n"))#kaç harfli kelime olması için değer alıyor
cumleuzunlugu=int(input("kac kelime olustursun?"))#cümlenin kaç kelime olmasını alıyor
Cumleolusturma(kelimeuzunlugu,cumleuzunlugu)#Cumleolusturma methhoduna gönderiyoruz değerleri



VerilenIkiKarakterArası(97,111)#a ile o karakterleri arasında rasgele değer üretmesi için program içi hethoda girdi gönderdik


ths.close()
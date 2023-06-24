
def menu():
    print("Kütüphane otomasyonu")
    while True:
        print("1-Kitap Ekle")
        print("2-Kitap Sil")
        print("3-Kitap Güncelle")
        print("4-Kitap Listele")
        print("5-Kitap Ara")
        print("6-Okur Girişi")
        print("7-Programdan Çıkış")
        secim = input("Lütfen yapmak istediğiniz işlemi seçin (0-7):")
        if secim == "1":
            secimler(1)
        elif secim == "2":
            secimler(2)
        elif secim == "3":
            secimler(3)
        elif secim == "4":
            secimler(4)
        elif secim == "5":
            secimler(5)
        elif secim == "6":
            secimler(6)

        elif secim == "7":
            print("Çıkış Yapılıyor!\n")
            break

        else:
            print("Geçerli seçim yapınız!\n")


def secimler(secim_no):
    if secim_no == 1:
        def kitap_ekle():
            kitap_numaralari = {}
            try:
                print("Kitap Ekleme İşlemi Bölümü")
                with open("20010011034.txt", "a", encoding="utf-8") as file:
                    kitap_adet = int(input("Girilecek kitap adedi kaçtır?"))
                    kitap_numaralari = {}


                    for i in range(kitap_adet):
                        kitap = {}

                        girilen_kitap_no = input(f"{i + 1}. Kitap numarası->")

                        if girilen_kitap_no in kitap_numaralari:
                            print("Bu kitap numarası zaten kullanılmıştır. Lütfen farklı bir numara girin.")
                            continue

                        kitap_numaralari[girilen_kitap_no] = True

                        kitap_tur = input("Kitap türü->")
                        kitap["kitap türü"] = kitap_tur

                        kitap_adet = input("Kütüphanedeki kitap adedi->")
                        kitap["kitap adedi"] = kitap_adet

                        kitap_ad = input("Kitap adı->")
                        kitap["kitap adı"] = kitap_ad

                        basim_yili = input("Kitabın basım yılı->")
                        kitap["basım yılı"] = basim_yili

                        yazar_no = input(f"Yazar numarası->")
                        kitap["yazar numarası"] = yazar_no

                        # Kitap bilgilerini dosyaya yazdırma
                        file.write(girilen_kitap_no + " ")
                        for key, value in kitap.items():
                            file.write(value + " ")
                        file.write("\n")

                print("Kitap ekleme işlemi başarıyla gerçekleştirilmiştir.")
            except:
                print("Hata...")

        kitap_ekle()
    elif secim_no == 2:
        def kitap_sil():
            try:
                print("Kitap Silme İşlemi Bölümü")
                with open("20010011034.txt", "r", encoding="utf-8") as file:
                    olay = None
                    kitaplar = {}
                    kitap_no = input("Silmek istediğiiniz kitap numarasını giriniz->")
                    for satir in file.readlines():
                        eleman = satir.strip().split(" ")
                        anahtar, deger = eleman[0], eleman[1:]
                        kitaplar[anahtar] = deger
                        print(kitaplar[anahtar])
                        if kitap_no == anahtar:
                            olay = True
                            kitaplar.pop(anahtar)
                    if olay == True:
                        with open("20010011034.txt", "w", encoding="utf-8") as dosya:
                            for anahtar in kitaplar.keys():
                                if kitaplar[anahtar]:
                                    dosya.write(anahtar)
                                    for i in range(len(kitaplar[anahtar])):
                                        dosya.write(" " + kitaplar[anahtar][i])
                                    dosya.write("\n")
                        print("Kitap silme işleminiz başarıyla gerçekleştirilmiştir.")
                    else:
                        print("Silinecek kitapla ilgili kayıt bulunamadı!")
            except:
                print("Hata...")

        kitap_sil()
    elif secim_no == 3:
        def kitap_guncelle():
            print("Kitap Güncelleme İşlemi Bölümü")
            with open("20010011034.txt", "r", encoding="utf-8") as file:
                olay = None
                kitaplar = {}
                kitap_no = input("Güncellemek istediğiniz kitap numarasını giriniz->")
                for satir in file.readlines():
                    eleman = satir.split(" ")
                    anahtar, deger = eleman[0], eleman[1:]
                    kitaplar[anahtar] = deger
                    if kitap_no == anahtar:
                        olay = True
                        kit_tur = input(f"{kitap_no}. kitabın yeni türü->")
                        kit_adet = input(f"{kitap_no}. kitabın yeni sayısı->")
                        kit_ad = input(f"{kitap_no}. kitabın yeni adı->")
                        bas_yili = input(f"{kitap_no}. kitabın yeni basım yılı->")
                        yeni_yazarNo = input(f"{kitap_no}. yazarın yeni numarası->")
                        kitap = []
                        kitap.append(kit_tur)
                        kitap.append(kit_adet)
                        kitap.append(kit_ad)
                        kitap.append(bas_yili)
                        kitap.append(yeni_yazarNo)
                        kitaplar[kitap_no] = kitap
                if olay == True:
                    with open("20010011034.txt", "w", encoding="utf-8") as dosya:
                        for anahtar in kitaplar.keys():
                            dosya.write(anahtar)
                            for i in range(len(kitaplar[anahtar])):
                                dosya.write(" " + kitaplar[anahtar][i])
                            dosya.write("\n")  
                    print("Güncelleme işlemi başarıyla gerçekleştirildi.\n")
                else:
                    print("Güncellenecek kitapla ilgili kayıt bulunamadı!")
            file.close()

        kitap_guncelle()


    elif secim_no == 4:
        def kitap_listele():
            print("Kitap Listeleme İşlemi Bölümü")
            with open("20010011034.txt", "r", encoding="utf-8") as file:
                kitaplar = {}
                for satir in file.readlines():
                    eleman = satir.split(" ")
                    anahtar, deger = eleman[0], eleman[1:]
                    kitaplar[anahtar] = deger
                for anahtar in kitaplar.keys():
                    print(anahtar, end=" ")
                    for i in range(len(kitaplar[anahtar])):
                        print(kitaplar[anahtar][i], end=" ")
                    print()
            file.close()

        kitap_listele()
    elif secim_no == 5:
        def kitap_ara():
            print("Kitap Arama İşlemi Bölümü")

            try:
                kitap_no = input("Aranacak kitabın numarasını giriniz: ")
                with open("20010011034.txt", "r", encoding="utf-8") as file:
                    kitaplar = {}
                    for satir in file.readlines():
                        eleman = satir.split()
                        if eleman:
                            anahtar, deger = eleman[0], eleman[1:]
                            kitaplar[anahtar] = deger
                    if kitap_no in kitaplar:
                        print(kitap_no,end=" ")

                        for deger in kitaplar[kitap_no]:
                            print(deger,end=" ")
                        print()

                    else:
                        print("Aranacak kitapla ilgili kayıt bulunamadı!")

                file.close()
            except Exception as e:
                print("Hata:", e)
                raise

        kitap_ara()
    elif secim_no == 6:

        def okur_girisi():
            simdiki_yil = int(input("Günümüz yılını giriniz->"))
            print("Okur Ekleme İşlemi Bölümü")
            try:
                okur_numaralari = {}
                okurlar = {}

                okur_adet = int(input("Kaç okur girişi yapılacak?"))
                with open("20010011034_Okur.txt", "a", encoding="utf-8") as file:
                    okur_numaralari = {}

                    for i in range(okur_adet):
                        okur = {}

                        girilen_okur_no = input(f"{i + 1}. Okur numarası->")

                        if girilen_okur_no in okur_numaralari:
                            print("Bu okur numarası zaten kullanılmıştır. Lütfen farklı bir numara girin.")
                            continue

                        okur_numaralari[girilen_okur_no] = True

                        okur_ad = input(f"{i + 1}.Okurun adı->")
                        okur_soyad = input(f"{i + 1}.Okurun soyadı->")
                        dogum_tarihi = int(input(f"{i + 1}.Alıcının doğum tarihini giriniz->"))
                        yas = simdiki_yil - dogum_tarihi
                        kitap_ad = input("Okurun aldığı kitabın adını giriniz->")
                        kayit_tarihi = int(input(f"{i + 1}.Okurun kayıt tarihini giriniz->"))
                        
                        # Kitap bilgilerini dosyaya yazdırma
                        file.write(girilen_okur_no + " " + "\n")
                        okur["okurun adı"] = okur_ad
                        okur["okurun soyadı"] = okur_soyad
                        okur["okurun yaşı"] = yas
                        okur["okurun aldığı kitap"] = kitap_ad
                        okur["okurun kayıt tarihi"] = kayit_tarihi
                        file.write(f"Okur adı: {okur['okurun adı']}\n")
                        file.write(f"Okur soyadı: {okur['okurun soyadı']}\n")
                        file.write(f"Okur yaşı: {okur['okurun yaşı']}\n")
                        file.write(f"Okur'un aldığı kitap adı:: {okur['okurun aldığı kitap']}\n")
                        file.write(f"Okur'un kütüphaneye kayıt tarihi: {okur['okurun kayıt tarihi']}\n")
                        file.write("\n")
                        # print(okur)

                print("Okur girişi işlemi başarıyla gerçekleştirilmiştir.")

            except Exception as e: #kapsamlı hatayı görmek için
                print("Hata:", e)
                raise

        okur_girisi()




menu()


# Default değişkenler:

hemofili_a_sayisi = 0
hemofili_b_sayisi = 0
profilaksi_hemofili_a_sayisi = 0
profilaksi_hemofili_b_sayisi = 0
agir_sayisi = 0
orta_sayisi = 0
hafif_sayisi = 0
hemofili_a_inhibitor = 0
hemofili_b_inhibitor = 0
orta_profilaksi_sayisi = 0
hemofili_a_faktor_P_sayisi = 0
hemofili_a_faktor_R_sayisi = 0
hemofili_b_faktor_P_sayisi = 0
hemofili_b_faktor_R_sayisi = 0
F8_Plazma_1000 = 0
F9_Plazma_1000 = 0
F8_Reko_1000 = 0
F9_Reko_1000 = 0
F8_Plazma_500 = 0
F9_Plazma_500 = 0
F8_Reko_500 = 0
F9_Reko_500 = 0
F8_Plazma_250 = 0
F9_Plazma_250 = 0
F8_Reko_250 = 0
F9_Reko_250 = 0
_4_haftalik_genel_ilac_tutari = 0
yillik_genel_ilac_tutari = 0
kullanilacak_genel_ilac_mik = 0
hemofili_a_max_ilac = 0
hemofili_a_max_ilac_tc = ""
hemofili_a_max_ilac_ad = ""
hemofili_a_max_ilac_siddet = ""
hemofili_a_max_ilac_kg = 0
hemofili_a_max_ilac_turu = ""
hemofili_a_max_ilac_4_hafta_mik = 0
hemofili_a_max_ilac_4_hafta_tutar = 0
hemofili_b_max_ilac = 0
hemofili_b_max_ilac_tc = ""
hemofili_b_max_ilac_ad = ""
hemofili_b_max_ilac_siddet = ""
hemofili_b_max_ilac_kg = 0
hemofili_b_max_ilac_turu = ""
hemofili_b_max_ilac_4_hafta_mik = 0
hemofili_b_max_ilac_4_hafta_tutar = 0
max_4_hafta_ilac_tutari_tc = ""
max_4_hafta_ilac_tutari_ad = ""
max_4_hafta_ilac_tutari_hastalik = ""
max_4_hafta_ilac_tutari_hastalik_siddet = ""
max_4_hafta_ilac_tutari_kg = 0
max_4_hafta_ilac_tutari_ilac_turu = ""
max_4_hafta_ilac_tutari_ilac_mik = 0
max_4_hafta_ilac_tutari = 0

# İnhibitore default olarak false değeri verdik ilerde True'ya dönüşürse inhibitör var sayılacak.

inhibitor = False

# Hasta başına bilgi almak için default olarak True ile başlayan while döngüsü kullandık
# Döngü sonunda eğer girdi "H" veya "h" olursa break komutuyla döngüden çıkacak.
# Yani bir nevi Do While döngüsü

while True:
    ad_soyad = input("Hastanın adını soyadını giriniz: ")
    tc_no = input("Hastanın TC numarasını giriniz: ")
    hastalik_tipi = ""

    # Girdi kontrolü

    while hastalik_tipi not in ["A","a","B","b"]:
        hastalik_tipi = input("Hastalık tipini giriniz(A,a,B,b): ")

    faktor_mik = -1
    while not 0 <= faktor_mik < 50:
        faktor_mik = float(input("Kandaki faktör miktarını giriniz(%): "))

    inhibitor_mik = -1
    while inhibitor_mik < 0:
        inhibitor_mik = float(input("Kanda oluşan antikor miktarını giriniz: "))

    # İnhibitörlü hastalarda hemofili A ve B için sayaç

    if inhibitor_mik > 5:
        inhibitor = True
    if hastalik_tipi == "A" or hastalik_tipi == "a":
        hemofili_a_sayisi += 1
        if inhibitor == True:
            hemofili_a_inhibitor = + 1
    else:
        hemofili_b_sayisi += 1
        if inhibitor == True:
            hemofili_b_inhibitor = + 1

    # Hastalık şiddeti ataması, ve sayaçları. Ayrıca profilaksi durumu belirlenir

    siddet = ""
    yillik_kanama = -1
    if faktor_mik < 1:
        siddet = "Ağır"
        agir_sayisi += 1
    elif faktor_mik < 5:
        siddet = "Orta"
        orta_sayisi += 1
        while yillik_kanama < 0: #Yıllık kanama girdisi sadece hastalık seviyesi orta ise alınacak
            yillik_kanama = int(input("Son 1 yılda meydana gelen kanama sayısını giriniz: "))
    else:
        siddet = "Hafif"
        hafif_sayisi += 1

    # Profilaksi default olarak False atandı. Şartlar oluşması durumunda True atanır.

    profilaksi = False
    if siddet == "Ağır":
        profilaksi = True
    elif siddet == "Orta" and yillik_kanama > 36:
        profilaksi = True
        orta_profilaksi_sayisi += 1

    # Profilaksi tedavisine alım durumunda gerekli girdiler kontrol edilerek alınır.

    if profilaksi == True:
        hasta_kg = -1
        while hasta_kg < 0:
            hasta_kg = float(input("Lütfen hastanın kütlesini giriniz(kg): "))
        faktor_turu = ""
        while faktor_turu not in ["P","p","R","r"]:
            faktor_turu = input("Lütfen kullanılacak faktör ilacının türünü giriniz(P,p,R,r): ")

        # En son çıktı alırken ilaç çeşidinde plazma ve rekombinant yerinde p,P,r,R çıkmaması için ayrı değişken oluşturulur.

        if faktor_turu == "P" or faktor_turu == "p":
            ilacin_turu = "Plazma kaynaklı"
        else:
            ilacin_turu = "Rekombinant"

    # İlk girdilerin sonuçları ekrana yazdırılır (Profilaksi alan & almayanlar için ortak)

    print("TC no:",tc_no)
    print("Ad Soyad:",ad_soyad)
    print("Hastalığın şiddeti ve tipi:", siddet ,"şiddetli Hemofili", hastalik_tipi)

    # Profilaksi tedavisine alınacak hastaların diğer bilgileri hesaplanıp yazıdırılır.

    if profilaksi == True:
        print("Profilaksi tedavisi uygulanacaktır.")
        if hastalik_tipi == "A" or hastalik_tipi == "a":
            faktor_artis = 2  # Bir ünite ilaç ile kg başına % lik artış (Hem - A)
            haftalik_ilac = 3  # Bir haftada kaç kez ilaç kullanacağı (Hem - A)
            profilaksi_hemofili_a_sayisi += 1
            if faktor_turu == "P" or faktor_turu == "p":
                hemofili_a_faktor_P_sayisi += 1
            else:
                hemofili_a_faktor_R_sayisi += 1
        else:
            faktor_artis = 1  # Bir ünite ilaç ile kg başına % lik artış (Hem - B)
            haftalik_ilac = 2  # Bir haftada kaç kez ilaç kullanacağı (Hem - B)
            profilaksi_hemofili_b_sayisi += 1
            if faktor_turu == "P" or faktor_turu == "p":
                hemofili_b_faktor_P_sayisi += 1
            else:
                hemofili_b_faktor_R_sayisi += 1
        if faktor_turu == "P" or faktor_turu == "p":
            print("Hasta plazma kaynaklı ilaç kullanacaktır.")
            ilac_birim_ucret = 1.25
        else:
            print("Hasta rekombinant kaynaklı ilaç kullanacaktır.")
            ilac_birim_ucret = 1.5

        # Haftada kaç kere ilaç kullanılacağı

        print("Hasta hafatda" ,haftalik_ilac, "kez ilaç kullanacaktır.")

        # Hastanın kullanması gereken ilaç başına minimum ünite miktarı hesaplanır, ekrana yazddırılır.

        min_ilac_miktari = ((40-faktor_mik)/faktor_artis)*hasta_kg
        print("Tek seferde kullanılması gerekn minimum ilaç miktarı", min_ilac_miktari,"ünitedir.")

        # Hastanın minimum kullanması gereken flakon miktarları hesaplanır

        flak_500_mik = 0
        flak_250_mik = 0
        flak_1000_mik = min_ilac_miktari//1000
        kalan_ilac_mik = min_ilac_miktari % 1000
        if kalan_ilac_mik > 750:
            flak_1000_mik += 1
        elif kalan_ilac_mik > 500:
            flak_500_mik += 1
            flak_250_mik += 1
        elif kalan_ilac_mik > 250:
            flak_500_mik += 1
        else:
            flak_250_mik += 1

        #Hastanın bir defada kullanacağı ilaç miktarı hesaplanır.

        kullanilacak_ilac_mik = flak_1000_mik*1000 + flak_500_mik * 500 + flak_250_mik * 250
        kullanilacak_genel_ilac_mik += kullanilacak_ilac_mik  #Tüm hastaların kullandığı toplam ilaç miktarını hesaplayan sayaç

        # Sonuçlar ekrana yazdırılır.

        print("Bir seferde kullanılacak ilaç miktarı:", kullanilacak_ilac_mik, "Ünite")
        print("1000'lik flakon miktarı:", flak_1000_mik)
        print("500'lük flakon miktarı:", flak_500_mik)
        print("250'lik flakon miktarı:", flak_250_mik)

        # Bir ilaç tutarı, 4 haftalık ve yıllık ilaç tutarlarıyla, yıllık tüm hastaları kapsayan ilaç tutarını hesaplayan sayaç

        ilac_tutari = kullanilacak_ilac_mik * ilac_birim_ucret
        _4_haftalik_ilac_tutari = haftalik_ilac * ilac_tutari * 4
        yillik_ilac_tutari = haftalik_ilac * ilac_tutari * 52
        _4_haftalik_genel_ilac_tutari += _4_haftalik_ilac_tutari
        yillik_genel_ilac_tutari += yillik_ilac_tutari
        print("4 haftalık ilaç tutarı:", _4_haftalik_ilac_tutari, "TL dir.")

        # Hemofili-A hastaları için max ilaç kullanan hastanın bilgileri

        if hastalik_tipi == "A" or hastalik_tipi == "a":
            if kullanilacak_ilac_mik > hemofili_a_max_ilac:
                hemofili_a_max_ilac = kullanilacak_ilac_mik
                hemofili_a_max_ilac_tc = tc_no
                hemofili_a_max_ilac_ad = ad_soyad
                hemofili_a_max_ilac_siddet = siddet
                hemofili_a_max_ilac_kg = hasta_kg
                hemofili_a_max_ilac_turu = ilacin_turu
                hemofili_a_max_ilac_4_hafta_mik = 4 * haftalik_ilac * kullanilacak_ilac_mik
                hemofili_a_max_ilac_4_hafta_tutar = _4_haftalik_ilac_tutari

            # Ayrıca Hemofili-A hastalarının toplam kullandıkları Rekombinant ve Plazma kaynaklı flakon sayıları

            if faktor_turu == "P" or faktor_turu == "p":
                F8_Plazma_1000 += flak_1000_mik
                F8_Plazma_500 += flak_500_mik
                F8_Plazma_250 += flak_250_mik
            else:
                F8_Reko_1000 += flak_1000_mik
                F8_Reko_500 += flak_500_mik
                F8_Reko_250 += flak_250_mik

        # Hemofili-B hastaları için max ilaç kullanan hastanın bilgileri

        else:
            if kullanilacak_ilac_mik > hemofili_b_max_ilac:
                hemofili_b_max_ilac = kullanilacak_ilac_mik
                hemofili_b_max_ilac_tc = tc_no
                hemofili_b_max_ilac_ad = ad_soyad
                hemofili_b_max_ilac_siddet = siddet
                hemofili_b_max_ilac_kg = hasta_kg
                hemofili_b_max_ilac_turu = ilacin_turu
                hemofili_b_max_ilac_4_hafta_mik = 4 * haftalik_ilac * kullanilacak_ilac_mik
                hemofili_b_max_ilac_4_hafta_tutar = _4_haftalik_ilac_tutari

            # Ayrıca Hemofili-B hastalarının toplam kullandıkları Rekombinant ve Plazma kaynaklı flakon sayıları

            if faktor_turu == "P" or faktor_turu == "p":
                F9_Plazma_1000 += flak_1000_mik
                F9_Plazma_500 += flak_500_mik
                F9_Plazma_250 += flak_250_mik
            else:
                F9_Reko_1000 += flak_1000_mik
                F9_Reko_500 += flak_500_mik
                F9_Reko_250 += flak_250_mik

        # Tüm hastalar arasında ilaç tutarı en yüksek olan hastanın bilgileri

        if _4_haftalik_ilac_tutari > max_4_hafta_ilac_tutari:
            max_4_hafta_ilac_tutari_tc = tc_no
            max_4_hafta_ilac_tutari_ad = ad_soyad
            max_4_hafta_ilac_tutari_hastalik = hastalik_tipi
            max_4_hafta_ilac_tutari_hastalik_siddet = siddet
            max_4_hafta_ilac_tutari_kg = hasta_kg
            max_4_hafta_ilac_tutari_ilac_turu = ilacin_turu
            max_4_hafta_ilac_tutari_ilac_mik = 4 * haftalik_ilac * kullanilacak_ilac_mik
            max_4_hafta_ilac_tutari = _4_haftalik_ilac_tutari

    # Profilaksi == False durumu

    else:
        print("Hasta profilaksi tedavisine alınmayacaktır.")

    #Yeni hasta bilgilerinin alınıp alınmayacağı sorulur ve ona göre while döngüsününden çıkılacağına karar verilir.

    baska_hasta=""
    while baska_hasta not in ["E","e","H","h"]:
        baska_hasta = input("Başka hasta girdisi yapmak istiyor musunuz(E,e;H,h): ")
    if baska_hasta == "H" or baska_hasta == "h":
        break

# Toplam hasta sayısı ve hasta şiddeti oranları

toplam_hasta_sayisi = hemofili_a_sayisi + hemofili_b_sayisi
agir_oran = 100 * agir_sayisi/toplam_hasta_sayisi
orta_oran = 100 * orta_sayisi/toplam_hasta_sayisi
hafif_oran = 100 * hafif_sayisi/toplam_hasta_sayisi

# Hemofili A ve B inhibitör oranları

hemofili_a_inhibitor_oran = 100 * hemofili_a_inhibitor/hemofili_a_sayisi
hemofili_b_inhibitor_oran = 100 * hemofili_b_inhibitor/hemofili_b_sayisi

# Hemofili A ve B profilaksi tedavisine alım oranı

profilaksi_hemofili_a_oran = 100 * profilaksi_hemofili_a_sayisi/hemofili_a_sayisi
profilaksi_hemofili_b_oran = 100 * profilaksi_hemofili_b_sayisi/hemofili_b_sayisi

# Orta şiddetli hemofili hastalarından profilaksi tedavisine alınacakların oranı

orta_profilaksi_oran = 100 * orta_profilaksi_sayisi/orta_sayisi

# Profilaksi için tedarik edilmesi gereken 4 haftalık toplam Rekombinant ve Plazma kaynaklı Faktör 8 & 9 üniteleri
# Ayrıca yine ilaç çeşidi, miktarı ve türüne göre ayrı sayaçlar kullanarak herbirinin kaç defa kullanıldığı da sayıldı.

f8_4_haftalik_toplam_reko = (F8_Reko_250 * 250 + F8_Reko_500 * 500 + F8_Reko_1000 * 1000) * 12
f8_4_haftalik_toplam_plazma = (F8_Plazma_250 * 250 + F8_Plazma_500 * 500 + F8_Plazma_1000 * 1000) * 12
f9_4_haftalik_toplam_reko = (F9_Reko_250 * 250 + F9_Reko_500 * 500 + F9_Reko_1000 * 1000) * 8
f9_4_haftalik_toplam_plazma = (F9_Plazma_250 * 250 + F9_Plazma_500 * 500 + F9_Plazma_1000 * 1000) * 8

# Hemofili A & B hastalarının Rekombinant ve Plazma kaynaklı ilaç kullanım oranlar

hemofili_a_faktor_P_orani = 100 * hemofili_a_faktor_P_sayisi/profilaksi_hemofili_a_sayisi
hemofili_a_faktor_R_orani = 100 * hemofili_a_faktor_R_sayisi/profilaksi_hemofili_a_sayisi
hemofili_b_faktor_P_orani = 100 * hemofili_b_faktor_P_sayisi/profilaksi_hemofili_b_sayisi
hemofili_b_faktor_R_orani = 100 * hemofili_b_faktor_R_sayisi/profilaksi_hemofili_b_sayisi

# Yıllık ortalama ilaç tutarı (TL)

yillik_ort_ilac_tutari = yillik_genel_ilac_tutari/toplam_hasta_sayisi

# Hasta başına kullanılan ortalama ilaç miktarı (ünite)

kullanilacak_ort_ilac_mik = kullanilacak_genel_ilac_mik/toplam_hasta_sayisi

# Yukarıda hesaplanan değerler sırasıyla ekrana yazdırılır.

print("Hemofili-A sayısı: ", hemofili_a_sayisi)
print("Hemofili-B sayısı: ", hemofili_b_sayisi)
print("Ağır hemofili hastalarının sayısı", agir_sayisi,"oranı %", format(agir_oran, ".2f"))
print("Orta seviyeli hemofili hastalarının sayısı", orta_sayisi, "oranı %", format(orta_oran, ".2f"))
print("Hafif seviyeli hastaların sayısı", hafif_sayisi, "oranı %", format(hafif_oran, ".2f"))
print("Hemofili-A hastalarında bulunan inhibitör oranı: %", format(hemofili_a_inhibitor_oran, ".2f"))
print("Hemofili-B hastalarında bukunan inhibitör oranı: %", format(hemofili_b_inhibitor_oran, ".2f"))
print("Profilaksi uygulanacak Hemofili-A hastası sayısı: ", profilaksi_hemofili_a_sayisi, "ve oranı %", format(profilaksi_hemofili_a_oran, ".2f"))
print("Profilaksi uygulanacak Hemofili-B hastası sayısı: ", profilaksi_hemofili_b_sayisi, "ve oranı %", format(profilaksi_hemofili_b_oran, ".2f"))
print("Orta şiddetli hemofili hastaları içerisinde profilaksi uygulanan hastaların oranı: %", format(orta_profilaksi_oran, ".2f"))
print("Profilaksi uygulanan Hemofili-A hastaları içinde plazma kaynaklı ilaç kullananların oranı: %", format(hemofili_a_faktor_P_orani, ".2f"))
print("Profilaksi uygulanan Hemofili-B hastaları içinde plazma kaynaklı ilaç kullananların oranı: %", format(hemofili_b_faktor_P_orani, ".2f"))
print("Profilaksi uygulanan Hemofili-A hastaları içinde  rekombinant ilaç kullananların oranı: %", format(hemofili_a_faktor_R_orani, ".2f"))
print("Profilaksi uygulanan Hemofili-B hastaları içinde  rekombinant ilaç kullananların oranı: %", format(hemofili_b_faktor_R_orani, ".2f"))
print("4 haftalık toplam kullanılan plazma kaynaklı faktör-8 miktarı: ", f8_4_haftalik_toplam_plazma, "Ünite")
print("4 haftalık toplam kullanılan rekombinant faktör-8 miktarı: ", f8_4_haftalik_toplam_reko, "Ünite")
print("4 haftalık toplam kullanılan plazma kaynaklı faktör-9 miktarı: ", f9_4_haftalik_toplam_plazma, "Ünite")
print("4 haftalık toplam kullanılan rekombinant faktör-9 miktarı: ", f9_4_haftalik_toplam_reko, "Ünite")
print("4 haftalık toplan kullanılan 1000 ünitelik flakon sayısı :", (F8_Plazma_1000 + F8_Reko_1000) * 12 + (F9_Plazma_1000 + F9_Reko_1000) * 8)
print("4 haftalık toplan kullanılan 500 ünitelik flakon sayısı :", (F8_Plazma_500 + F8_Reko_500) * 12 + (F9_Plazma_500 + F9_Reko_500) * 8)
print("4 haftalık toplan kullanılan 250 ünitelik flakon sayısı :", (F8_Plazma_250 + F8_Reko_250) * 12 + (F9_Plazma_250 + F9_Reko_250) * 8)

# SGK ortalamaları

print("SGK 4 haftalık toplam", _4_haftalik_genel_ilac_tutari, "TL ve yıllık toplam",yillik_genel_ilac_tutari,"TL ilaç tutarı karşılamaktadır." )
print("SGK ortalama 1 hasta için yıllık toplam", format(kullanilacak_ort_ilac_mik, ".2f"), \
      "Ünite ilacı karşılamış, ve kişi başı ortalama", format(yillik_ort_ilac_tutari, ".2f"),"TL harcamıştır.")

# İlaç kullanım miktarı en yüksek Hemofili-A hastasının bilgileri

print("4 haftalık ilaç kullanım miktarı en fazla olan Hemofili-A hastasının, \nTC no'su: ",hemofili_a_max_ilac_tc)
print("Adı soyadı: ",hemofili_a_max_ilac_ad)
print("Hastalık şiddeti: ",hemofili_a_max_ilac_siddet)
print("Ağırlığı:",hemofili_a_max_ilac_kg,"kq" )
print("Kullandığı ilaç türü: ",hemofili_a_max_ilac_turu)
print("4 haftalık toplam kullandığı ilaç:",hemofili_a_max_ilac_4_hafta_mik,"Ünite")
print("4 haftalık toplam ilaç tutarı:",hemofili_a_max_ilac_4_hafta_tutar,"TL")

# İlaç kullanım miktarı en yüksek Hemofili-B hastasının bilgileri

print("4 haftalık ilaç kullanım miktarı en fazla olan Hemofili-B hastasının, \nTC no'su: ",hemofili_b_max_ilac_tc)
print("Adı soyadı: ",hemofili_b_max_ilac_ad)
print("Hastalık şiddeti: ",hemofili_b_max_ilac_siddet)
print("Ağırlığı:",hemofili_b_max_ilac_kg,"kq" )
print("Kullandığı ilaç türü: ",hemofili_b_max_ilac_turu)
print("4 haftalık toplam kullandığı ilaç:",hemofili_b_max_ilac_4_hafta_mik,"Ünite")
print("4 haftalık toplam ilaç tutarı:",hemofili_b_max_ilac_4_hafta_tutar,"TL")

# İlaç tutarı en yüksek Hemofili hastasının bilgileri

print("4 haftalık ilaç tutarı en çok olan hastanın \nTC no'su:",max_4_hafta_ilac_tutari_tc)
print("Adı soyadı:",max_4_hafta_ilac_tutari_ad)
print("Hastalık tipi:",max_4_hafta_ilac_tutari_hastalik)
print("Hastalığının şiddeti:",max_4_hafta_ilac_tutari_hastalik_siddet)
print("Ağırlığı", max_4_hafta_ilac_tutari_kg, "kg")
print("Kullandığı ilaç türü:",max_4_hafta_ilac_tutari_ilac_turu)
print("4 haftalık toplam kullandığı ilaç:",max_4_hafta_ilac_tutari_ilac_mik,"Ünite")
print("4 haftalık toplam ilaç tutarı:",max_4_hafta_ilac_tutari,"TL'dir.")


print("\n\n    ------------ Program sonu ------------")
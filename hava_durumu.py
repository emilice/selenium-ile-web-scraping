from selenium import webdriver
from bs4 import BeautifulSoup

browserProfile = webdriver.ChromeOptions()
browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'tr,tr_TR'})
browser = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe", chrome_options=browserProfile)

il = input("İl: ").lower().capitalize()
ilce = input("İlçe: ").lower().capitalize()
url = browser.get(f"https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il={il}&ilce={ilce}")

kaynak = browser.page_source
soup = BeautifulSoup(kaynak, "html.parser")

anlikDurumTarih = soup.find("span",{"class":"ad_time ng-binding"})
anlikHava = soup.find("div", {"class":"anlik-sicaklik-havadurumu-ikonismi ng-binding"})
anlikDerece = soup.find("div", {"class":"anlik-sicaklik-deger ng-binding"})
anlikNem = soup.find("div", {"class":"anlik-nem-deger-kac ng-binding"})

print(f"""
İl: {il}/{ilce}
Tarih: {anlikDurumTarih.text}
Hava: {anlikHava.text}
Sıcaklık: {anlikDerece.text}°C
Nem: %{anlikNem.text}
""")

if (anlikHava.text=="Sıcak"):
    print("Hava sıcak \nAy yeter gebericem, esmiyor!")
elif (anlikHava.text=="Açık"):
    print("Hava açık, hava tişört giymek uygundur.")
elif (anlikHava.text=="Az Bulutlu"):
    print("Hava bulutlu, yanınıza ince bir hırka alabilirsiniz")
elif (anlikHava.text=="Çok Bulutlu"):
    print("Hava çok bulutlu, yanınıza hırka alabilirsiniz. \nYağmur yağma ihtimaline karşı yanınıza şemsiye alabilirsiniz.")
elif (anlikHava.text=="Sağanak Yağışlı"):
    print("Hava sağnak yağışlı, yanınıza şemsiye alabilirsiniz..")
elif (anlikHava.text=="Yağışlı"):
    print("Hava yağışlı görünüyor, yanınıza mutlaka şemsiye alınız.")
elif (anlikHava.text=="Soğuk"):
    print("Hava soğuk \nBu kadar soğuk olma be",{il}, "faturaları sen ödemiyorsun.")
else:
    print("Böyle bir hava durumu tanımlı değil")
    
browser.quit()

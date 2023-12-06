import time
from tkinter import*
import random
import pyautogui

sayac=0#skoru tutacak olan değişken

def fonk():#mavi butona basıldığında çalışacak olan fonksiyon
    x_konum_list = [1500, 700, 1100]#kartların x konumları
    random.shuffle(x_konum_list)#listedeki elemanların sırası rastgele değişecek
    x1=x_konum_list[0]#buton1 x konumu
    x2=x_konum_list[1]#buton2 x konumu
    x3=x_konum_list[2]#butonK x konumu
    buton1.place(x=x1,y=100)#buton1 konumu
    buton2.place(x=x2, y=100)#buton2 konumu
    butonK.place(x=x3, y=100)#butonK konumu
    buton1.config(bg="orange",activebackground="blue")#buton1 turuncu gözükecek tıklandığında mavi olacak
    buton2.config(bg="orange",activebackground="blue")#buton2 turuncu gözükecek tıklandığında mavi olacak


def kirmizi():#kırmızı butona tıklandığında çalışacak olan fonksiyon
    global sayac #yukarıda tanımlanan sayac değişkeninin fonksiyonda çalışabilmesi için
    x_konum_list = [1500, 700, 1100]
    random.shuffle(x_konum_list)
    x1 = x_konum_list[0]
    x2 = x_konum_list[1]
    x3 = x_konum_list[2]
    buton1.place(x=x1, y=100)
    buton2.place(x=x2, y=100)
    butonK.place(x=x3, y=100)
    sayac=sayac+1#skoru 1 artıracak
    butonK.config(activebackground="red",bg="orange")#butonK turuncu gözükecek tıklandığında kırmızı olacak
    pyautogui.moveTo(69,104)#sayacın artmasını sağlayan butona gidecek
    pyautogui.doubleClick(button="left")#sayac butonuna tıklayacak
    sayacButon["text"] = sayac #sayacın tuttuğu skoru butonda gösterecek



pencere = Tk()#pencere aç
pencere.title("Kırmızı Kartı Bul")#pencerenin ismi
pencere.geometry("1919x1079")#pencere boyutu
aciklaEtiket=Label(pencere)#pencerede etiket oluşturacak
buton1 = Button(pencere)#pencerede buton oluşturacak
buton2 = Button(pencere)#pencerede buton oluşturacak
butonK = Button(pencere)#pencerede buton oluşturacak
sayacButon= Button(pencere)#pencerede buton oluşturacak
zaman=Button(pencere)#pencerede buton oluşturacak
buton1.config(bg="blue", padx="120", pady="215", command=fonk)#buton1in rengi, x ve y yönünde büyüklüğü ve tıklandığında ne yapacağı
buton2.config(bg="blue", padx="120", pady="215", command=fonk)#buton2nin rengi, x ve y yönünde büyüklüğü ve tıklandığında ne yapacağı
butonK.config(bg="red", padx="120", pady="215", command=kirmizi)#butonKnın rengi, x ve y yönünde büyüklüğü ve tıklandığında ne yapacağı
sayacButon.config(text=" ", bg="orange", fg="red",padx="25", pady="15", command=fonk)#sayacButonun üzerindeki metin, buton rengi, metin rengi rengi, x ve y yönünde büyüklüğü ve tıklandığında ne yapacağı
aciklaEtiket= Label(pencere, text=""" kartlardan
ikisinin
ön yüzü mavi
diğeri kırmızı.
kırmızı olanı
bulmaya çalış!
bu oyun 100
saniye
sürecek""", bg="blue", fg="white", padx="150", pady="380", font=("Vertana ",20))#etiketin üzerindeki metin, etiketin rengi,metin rengi, etiketin x v y yönünde büyüklükleri ve yazının fontu ve büyüklüğü




i=0#zamanı tutan değişken
def fzaman():#zaman butonuna tıklandığında çalışacak fonksiyon
    global i
    i=i+1#zamanı bir artır
    time.sleep(1)#1 saiye bekle
    zaman.config(text=str(i),padx="25", pady="15")#zaman butonundaki textte zamanı göster
    pencere.after(100,fzaman)#sürekli olarak zamanın artmasını sağladı
    if i==100:
        pyautogui.moveTo(1885, 15)#kapatma butonuna imleci taşıdı
        pyautogui.doubleClick(button="left")#kapatma butonuna tıkla



zaman=Button(pencere, text= "BAŞLA",padx="600", pady="450", command=fzaman)#başta zaman butonunun üzerindeki metin, butonun x ve y yönünde büyüklüğü ve tıklandığında ne yapacağı
zaman.place(x=550, y=30)
buton1.place(x=700, y=100)
buton2.place(x=1500, y=100)
butonK.place(x=1100, y=100)
sayacButon.place(x=36, y=30)
aciklaEtiket.place(x=36, y=100)
#etiket ve butonların pencere üzerinde konumları

mainloop()#pencerenin ve butonların sürekli olarak açık ve görünür olmasını sağladı
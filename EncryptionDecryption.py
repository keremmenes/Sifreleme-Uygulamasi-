import random
from typing import OrderedDict
def _init_(self):
    self.Cıktı=""

def encrypt(Sifre):
    Sifrele=Sifre[::-1]
    ilk=""
    ikinci=""
    list=[]
    for i in Sifre:
        a=random.randint(5,20)
        ilk=ilk+chr(ord(i)-a)
        list.append(chr(a+55))
    for i in Sifrele:
        a=random.randint(5,20)
        ikinci=ikinci+chr(ord(i)-a)
        list.append(chr(a+50))
    alist="".join(list)
    Cıktı=ilk+ikinci+alist
    print(Cıktı)

def decrypt(Cıktı):
    uzun=len(Cıktı)
    Sifre=Cıktı
    sifreCoz1=uzun/4
    i=0
    CozulmusSifre=""
    
    while i < int(sifreCoz1):
        b=(ord(Sifre[i+int(sifreCoz1*2)])-55)
        CozulmusSifre=CozulmusSifre+(chr(ord(Sifre[i])+b))
        i=i+1
    print(CozulmusSifre)


sifreOlustur=input(" Oluşturulacak şifreyi giriniz  : ")
encrypt(sifreOlustur)
sifreCozdur=input(str(" Çözülecek şifreyi giriniz  : "))
decrypt(sifreCozdur)

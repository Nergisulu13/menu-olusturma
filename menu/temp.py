# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

while True:
    print("Lütfen bir işlem seçiniz:")
    print("1 - Sisteme Üye Ol")
    print("2 - Sisteme Giriş Yap")
    print("3 - Şifremi Unuttum")
    print("4 - Çıkış")
    
    secim = input("Seçiminizi girin (1-4): ")
    
    if secim == "1":
        print("Sisteme üye ol seçildi.")
        isim=input("isim:")
        print("isminiz",isim)
        soyad=input("soyadınız:")
        print("soyadınız",soyad)
        evadresiniz=input("ev adresiniz:")
        print ("ev adresiniz",evadresiniz)
        ailebireysayısı=input("birey sayısı:")
        print("aile birey sayısı",ailebireysayısı)
        tcno=input("tc nonuz:")
        print("tc numaranız",tcno)
        print("Sisteme üye oldunuz")
        
    elif secim == "2":
        print("Sisteme giriş yap seçildi.")
        şifre=input("şifre:")
        print("şifreniz",şifre)
        print("adınızı ve soyadınız giriniz.")
        ad=input("adınız:")
        soyad=input("soyadınız:")
        
    elif secim == "3":
        print("Şifremi unuttum seçildi.")
        şifre=input("Lütfen yeni bir şifre giriniz:")
        print("Girdiğiniz şifre",şifre)
    elif secim == "4":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim! Lütfen 1-4 arasında bir seçim yapın.")
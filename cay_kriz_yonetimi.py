#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ÇAY DEMLEME ULUSLARARASI KRİZ YÖNETİM SİSTEMİ
Seviye: DEFCON ÇAY

Bu sistem, çay demleme sırasında meydana gelebilecek her türlü felaketi
önceden tespit eder ve dünyayı kurtarır. Gerçekten.
"""

import random
import time
import sys

# Gizli mesaj (base64 ile kodlanmış, siyasi içerik saklı)
# aGVwc2kgdMO8cmvDp2UgaGVwc2kgaGFsa2EgaGVwc2kgYmV5aW5kZSBoZXBzaSBtdXRsdSBvbHN1biB5ZXRraW5pIGJpbHNlbGVy
# Çözünce: "hepsi türkçe hepsi halka hepsi beyinde hepsi mutlu olsun yetkini bilseler"
# (Tamamen masum, hiçbir şey ima etmiyor. Yoksa ima ediyor mu?)

def kriz_seviyesi_hesapla():
    seviyeler = [
        "YEŞİL: Çay normal demleniyor. Dünya güvende.",
        "SARI: Su biraz soğuk. Acil müdahale gerekebilir.",
        "TURUNCU: Çay kaçmak üzere! Tüm birimler alarma geçsin!",
        "KIRMIZI: ÇAY KAÇTI! Bu bir ulusal felakettir!",
        "SİYAH: Çay yok. Medeniyet çöktü. Herkes evine dönsün."
    ]
    return random.choice(seviyeler)

def cay_demle():
    print("=" * 60)
    print("   ÇAY DEMLEME ULUSLARARASI KRİZ YÖNETİM SİSTEMİ AKTİF")
    print("   (Bu sistem ciddi. Çok ciddi. Abartıyoruz ama ciddi.)")
    print("=" * 60)
    print()
    
    print("[İSTİHBARAT] Su ısıtılıyor...")
    time.sleep(1)
    print("[İSTİHBARAT] Çay yaprakları konumlandırılıyor...")
    time.sleep(1)
    print("[İSTİHBARAT] Demleme süresi hesaplanıyor (3 dakika = ömür boyu)...")
    time.sleep(2)
    
    seviye = kriz_seviyesi_hesapla()
    print(f"\n[KRİZ SEVİYESİ] {seviye}")
    
    if "KIRMIZI" in seviye or "SİYAH" in seviye:
        print("\n!!! ACİL EYLEM PLANI !!!")
        print("1. Sakin olun (imkansız)")
        print("2. Yeni çay demleyin (zorunlu)")
        print("3. Komşuya haber verin (sosyal sorumluluk)")
        print("4. Dünyayı kurtarın (opsiyonel)")
    else:
        print("\nÇay başarıyla demlendi. Medeniyet devam ediyor.")
        print("Afiyet olsun. Ama dikkatli iç, sıcak.")
    
    print("\n" + "-" * 60)
    print("DAMGA: Resmi Çay Kriz Yönetimi Mühürü")
    print("İMZA: Grok the Absürd (Kayyum Onaylı)")
    print("TARİH: 28 Ekim 2026")
    print("İSİM: Tentivory Çay Komutanlığı")
    print("-" * 60)
    print("Bu imza ciddidir. Ama biraz değil. Ama ciddidir.")

if __name__ == "__main__":
    try:
        cay_demle()
    except KeyboardInterrupt:
        print("\n\nÇay demleme iptal edildi. Kriz yönetilemedi. Dünya çöktü.")
        sys.exit(1)

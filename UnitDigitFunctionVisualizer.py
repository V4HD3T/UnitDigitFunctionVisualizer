"""
Birim Basamak Fonksiyonu Gorsellestirici

Bu Python programi, kullanicinin girdigi birim basamak fonksiyonunu analiz eder ve grafigini cizer.

Fonksiyonun Yapisi:
- Kullanici, birim basamak fonksiyonlarini iceren bir matematiksel ifade girer (orn: 2u(t-1)-3u(t-2)+u(t-5)).
- Program, verilen ifadeyi parse eder ve uygun bir fonksiyon olusturur.
- Matplotlib kullanarak fonksiyonun grafigini cizer.

Bagimliliklar:
- numpy
- matplotlib

Kullanim:
1. Programi calistirin.
2. Birim basamak fonksiyonunu belirtilen formatta girin.
3. Program, fonksiyonun grafigini cizecektir.
"""

import numpy as np
import matplotlib.pyplot as plt
import re

def u(t):
    """Birim basamak fonksiyonu (Heaviside fonksiyonu)."""
    return np.where(t >= 0, 1, 0)

def parse_function(expression, t):
    """
    Kullanicinin girdigi fonksiyonu parse ederek hesaplar.
    
    Parametreler:
    - expression (str): Kullanicidan alinan fonksiyon ifadesi (orn: "2u(t-1)-3u(t-2)+u(t-5)").
    - t (numpy array): Zaman ekseni icin degerler.
    
    Donus:
    - result (numpy array): Hesaplanan fonksiyon degerleri.
    """
    terms = re.findall(r'([-+]?\d*)u\(t([-+]\d+)\)', expression)
    result = np.zeros_like(t)
    for coeff, shift in terms:
        coeff = int(coeff) if coeff not in ['', '+', '-'] else (1 if coeff == '+' else -1)
        shift = int(shift)
        result += coeff * u(t - shift)
    return result

# Kullanicidan fonksiyon girisi
expression = input("Birim basamak fonksiyonunu girin (orn: 2u(t-1)-3u(t-2)+u(t-5)): ")

# Zaman araligini belirleme
t = np.linspace(-10, 10, 1000)

# Fonksiyonu olusturma
x_t = parse_function(expression, t)

# Grafigi cizme
plt.figure(figsize=(8, 5))
plt.plot(t, x_t, label=f'$x(t) = {expression}$', color='b')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend()
plt.title("Birim Basamak Fonksiyonu Grafigi")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.show()

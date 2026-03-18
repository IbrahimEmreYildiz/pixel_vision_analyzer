# 🔍 Pixel Vision Analyzer

Görüntüleri piksel matrisi olarak işleyen, parlaklık analizi yapan ve kenar tespiti gerçekleştiren Python projesi.
Gerçek bir kamera veya görüntü dosyası olmadan NumPy ile görüntü işleme mantığını simüle eder.

---

## 📌 Proje Hakkında

Bu proje, bir görüntüyü piksel matrisi olarak temsil eder ve şu analizleri yapar:

- 📊 Ortalama parlaklık hesaplama
- 🌑 Karanlık / Aydınlık tespiti
- 🔲 Kenar benzeri değişimlerin analizi
- 🎲 Rastgele piksel matrisi üretimi
- 📂 Dosyadan matris yükleme

---

## 🛠️ Kullanılan Teknolojiler

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

---

## 📁 Proje Yapısı

```
vision_project/
├── main.py            → Programın giriş noktası, menü
├── image_loader.py    → Dosyadan matris yükleme ve rastgele matris üretimi
├── analyzer.py        → Parlaklık, karanlık/aydınlık ve kenar analizi
├── utils.py           → Yardımcı fonksiyonlar, pixel generator
└── image.txt          → Örnek piksel matrisi verisi
```

---

## ▶️ Kurulum ve Çalıştırma

1. Repoyu klonla:
```bash
git clone https://github.com/IbrahimEmreYildiz/vision_project.git
cd vision_project
```

2. NumPy'ı yükle:
```bash
pip install numpy
```

3. Programı çalıştır:
```bash
python main.py
```

---

## 📋 Kullanım

Program başlatılınca menü gelir:

```
*******MENU*******
1-Show analyze results
2-Quit
Choose one of them:
```

Seçenek 1'de iki seçenek sunulur:
- **1** → `image.txt` dosyasından piksel matrisi yükle
- **0** → Rastgele piksel matrisi üret (boyutu sen belirle)

---

## 💡 Örnek Çıktı

```
Brightness:  134.72
Picture is lighter.
Edge Count:  8
Pixels:  [(0, 1), (1, 3), (2, 0), (2, 2), (3, 1), (3, 3), (4, 0), (4, 2)]
```

---

## 🧠 Kullanılan Python Konuları

- OOP (Sınıf ve Nesneler)
- NumPy (Array işlemleri, randint, mean, diff)
- Generator ve Iterator
- Dosya okuma
- Hata yönetimi
- Modüller

---

## 👨‍💻 Geliştirici

**İbrahim Emre Yıldız**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ibrahim%20Emre%20Y%C4%B1ld%C4%B1z-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ibrahim-emre-yildiz)
[![GitHub](https://img.shields.io/badge/GitHub-IbrahimEmreYildiz-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/IbrahimEmreYildiz)
[![Gmail](https://img.shields.io/badge/Gmail-iemreis803@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:iemreis803@gmail.com)

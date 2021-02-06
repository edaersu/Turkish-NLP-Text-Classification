# NLP- Sentiment Analysis

## PreProcessing
Her bir satır aşağıdaki gibi noktalama işaretlerinden, özel karakterlerden temizlendi ve varsa link, mail adresi gibi bağlantılar kaldırıldı.<br><br>
<img src="github/pre.jpg">

## Zemberek
Java ile yazılmış türkçe nlp kütüphanesi olan Zemberek bilgisayarımızdaki JVM(java virtual machine) çalıştırarak ve gerekli dosyaları import edilerek kullanıldı. Bu doslayarı [buradaki linkte](https://drive.google.com/drive/folders/1nvc9FQyHQjGDNj85UgWeGSFhL1b8W4dd?usp=sharing) bulabilirsiniz.
Dosyaların görünümü şu şekilde:

<img src="github/files.jpg" align="left">
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
Zemberek java kodu içerisindeki TurkishMorphology, TurkishSpellChecker, TurkishSentenceNormalizer classlarının methodları kullanıldı.
Zemberek sonucundaki çıktı: <br><br>
<img src="github/zemberek.jpg" align="left"><br><br><br><br><br><br>
<br><br><br><br><br><br><br>

## Pre-trained Bert
Pre-trained bert modeli import edildikten sonra bazı denemelerin sonuçları<br><br>
<img src="github/bert.jpg" align="left">



Proje üyeleri:
    Furkan Kaya (Grup lideri)   191216002
    Azat Turunç                 191216054

Programı çalıştırmak için:
    Python çalıştırma ortamınızda pandas ve numpy kütüphaneleri bulunmalıdır.
    Main.py dosyasını terminale "python .\main.py" komudunu girerek çalıtırabilirsiniz.
    Sizden şifrelenmesini istediğiniz metni isteyecek giriş yaptıktan sonra entera bastığınızda
    otomatik olarak önce şifreleme ve sonra şifresini çözme adımlarını konsola basacaktır.

-Hocam sistemin çalışma modunun ecb olduğunu düşünüyoruz ama tam da anlayamadık aklımızda
soru işaretleri var. Biz ikisini de araştırdık daha sonrasında sizden özel olarak farklarını
öğrenmek istiyoruz.-

Sorular:
1. Bu sistemin ait olduğu çalışma modunun adı nedir?
    Hocam sistemin çalışma modunun ecb olduğunu düşünüyoruz ama tam da anlayamadık aklımızda soru işaretleri var. Biz ikisini de araştırdık daha sonrasında sizden özel olarak farklarını öğrenmek istiyoruz. Alttaki soruları da ikisine birden cevap vererek yanıtladık. İnşallah kabul edersiniz.
    
    Sistemin kullandığı çalışma moduna ECB modu (Electronic Code Book Mode) denir. ECB
    Sistemin kullandığı çalışma moduna CBC modu (Cipher Block Chaining Mode) denir. CBC
    
2. Sistemin savunmasız kalmasına neden olabilecek saldırı türleri nelerdir?
    oracle attack, flipping attack ve pasif saldırılar sistemin açıklarından faydalanarak savunmasız bırakabilir. (sistemi ECB)
    oracle attack ve flipping attack adlı saldırı türleri ile sistemin açıklarından faydalanarak savunmasız bırakabilir. (sistemi CBC)

3. Algoritma size göre standartlaştırılacak kadar güvenli mi? Neden?
    Bizce yapılmaz çünkü aynı giriş blokları aynı sonucu verdiği için herhangi bir saldırı yöntemi kullanmadan bile sadece şifrelenmiş veri deşifre edilebilir. (ECB)

    Bizce basit şifreleme kullanılmaz ise kullanılabilir çünkü biri şifrelenmiş veriyi ele geçirse bile hangi sıradan nasıl şifrelediğimizi bilemeyeceği için kırması olası değildir. (CBC)

4. Algoritma, güvenliğin temel hedeflerini sağlıyor mu?(Gizlilik, Bütünlük, Erişilebilirlik)
    Bizce sağlar örneklendirmek gerekirse:
        Gizlilik : Şifrelenmiş veriyi herkes okuyamaz.
        Bütünlük : Sadece anahtar sahibi girdiği şifreli veriyi deşifre edebilir.
        Erişilebilirlik : İstendiğinde girilen veri şifrelenebilir ve anahtarlar ile şifrelenmiş veri deşifre edilebilir. ECB/CBC

5. Şifreli metnin şifresini çözdükten sonra orijinal düz metni nasıl elde edebiliriz? çözülmez ise sebebinedir?
    Çözülebilir. Şifrelenmesi için geçirilen tüm adımları tersine bir şekilde tekrar uygularsak başladığımız noktaya geri dönmüş oluruz. Şifrelenmesi için kullanılan anahtarları şifre çözümünde kullanırız.

6. Algoritmanın zayıf yönleri nelerdir? Bunları nasıl çözülmelidir?

    Algoritmada aynı giriş blokları aynı sonuç blokları ile eşleştiği için tekrarlanan şifreli metin bloklarından dolayı girilen veri şifrelenmiş ise bile hala okunabilir bir halde olur. Buna da şimdiki kodda dahi çözüm geliştirmiş durumdayız metni xor öncesi ve sonrasında karıştırarak son cevabın içinde olabildiğince az tekrar geçmesini sağlıyoruz. Saldırganın yapılan karıştırma işlemini bilmeden ve anahtarına sahip olmadan geri döndürmesi mümkün değildir.(ECB)

    Algoritmadaki şifrelemenin ardışık olması parallelleştirilememesi bu algoritmanın ana sorunlarından biridir. Bunu çözmenin yolu ise "ciphertext stealing metodu"nu kullanarak çözebiliriz. (CBC)


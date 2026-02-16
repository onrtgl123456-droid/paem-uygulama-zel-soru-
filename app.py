import streamlit as st
import random

# Sayfa Ayarları
st.set_page_config(page_title="PAEM 100 Soru Bankası Final", page_icon="👮")

# --- 100 SORULUK TAM VE GÜNCEL VERİ SETİ ---
if 'questions' not in st.session_state:
    st.session_state.questions = [
        # MEVZUAT VE POLİS HUKUKU (35 Soru)
        {"soru": "PVSK'ya göre parmak izi alınan kişilerin kayıtları kaç yıl sonra silinir?", "secenekler": ["10", "20", "40", "80", "Ölümden 5 yıl sonra"], "cevap": "80"},
        {"soru": "7068 Sayılı Kanun'a göre 'Görevi kötüye kullanmak' cezası nedir?", "secenekler": ["Aylıktan Kesme", "10 Ay Durdurma", "24 Ay Durdurma", "Meslekten Çıkarma", "Kınama"], "cevap": "Meslekten Çıkarma"},
        {"soru": "PVSK Ek Madde 4'e göre polisin silah kullanma yetkisi için kaç ikaz yeterlidir?", "secenekler": ["1", "2", "3", "Sayı sınırı yok", "Havaya ateş şarttır"], "cevap": "1"},
        {"soru": "7068'e göre 'Kumar oynamak' cezasının karşılığı nedir?", "secenekler": ["Aylıktan kesme", "10 Ay Durdurma", "24 Ay Durdurma", "Meslekten Çıkarma", "Kınama"], "cevap": "24 Ay Durdurma"},
        {"soru": "Polis memurlarının yıllık izin süresi 10 yıldan fazla hizmette kaç gündür?", "secenekler": ["20", "25", "30", "40", "45"], "cevap": "30"},
        {"soru": "3201 ETK'ya göre emniyet teşkilatında 'Komiser' rütbesinde bekleme süresi kaçtır?", "secenekler": ["2", "3", "4", "5", "6"], "cevap": "4"},
        {"soru": "7068'e göre 'Amire saygısızlık' cezasının karşılığı nedir?", "secenekler": ["Uyarma", "Kınama", "Aylıktan Kesme", "Durdurma", "İhraç"], "cevap": "Aylıktan Kesme"},
        {"soru": "PVSK'ya göre önleme araması kararı mülki amir tarafından verilirse kaç saat içinde hakime sunulur?", "secenekler": ["12", "24", "48", "72", "96"], "cevap": "24"},
        {"soru": "EGM Yüksek Disiplin Kurulu Başkanı kimdir?", "secenekler": ["Emniyet Genel Müdürü", "Bakan Yardımcısı", "Personel Başkanı", "Teftiş Kurulu Başkanı", "Hukuk Müşaviri"], "cevap": "Emniyet Genel Müdürü"},
        {"soru": "7068'e göre disiplin cezalarına karşı kaç gün içinde dava açılabilir?", "secenekler": ["15", "30", "45", "60", "90"], "cevap": "60"},
        {"soru": "657 DMK'ya göre aday memurluk süresi en fazla kaçtır?", "secenekler": ["1", "2", "3", "4", "5"], "cevap": "2"},
        {"soru": "PVSK'ya göre zor kullanma yetkisi hangi maddede düzenlenmiştir?", "secenekler": ["4/A", "5", "9", "13", "16"], "cevap": "16"},
        {"soru": "Polis Akademisi Başkanı kim tarafından atanır?", "secenekler": ["EGM", "İçişleri Bakanı", "Cumhurbaşkanı", "YÖK", "MEB"], "cevap": "Cumhurbaşkanı"},
        {"soru": "Emniyet hizmetleri sınıfı emeklilik yaş haddi kaçtır?", "secenekler": ["52", "55", "58", "60", "65"], "cevap": "55"},
        {"soru": "7068'e göre 'Yalan beyanda bulunmak' cezası nedir?", "secenekler": ["Kınama", "Aylıktan Kesme", "Durdurma", "İhraç", "Uyarma"], "cevap": "Durdurma"},
        {"soru": "PVSK'ya göre adli arama kararı gecikmesinde sakınca bulunan hallerde kimden alınır?", "secenekler": ["Vali", "Emniyet Müdürü", "Cumhuriyet Savcısı", "İçişleri Bakanı", "Kaymakam"], "cevap": "Cumhuriyet Savcısı"},
        {"soru": "Emniyet Teşkilatında en yüksek rütbe hangisidir?", "secenekler": ["1. Sınıf Emniyet Müdürü", "Sınıf Üstü Emniyet Müdürü", "Genel Müdür", "Kurul Başkanı", "Daire Başkanı"], "cevap": "Sınıf Üstü Emniyet Müdürü"},
        {"soru": "Polis Bakım ve Yardım Sandığı'nın kısa adı?", "secenekler": ["POLSAN", "POLVAK", "EGMVAK", "POYAS", "POLBYS"], "cevap": "POLSAN"},
        {"soru": "PVSK 4/A'ya göre durdurma yetkisi neye dayanır?", "secenekler": ["Tecrübe ve Makul Sebep", "Yeterli Şüphe", "Somut Delil", "Amir Emri", "İhbar"], "cevap": "Tecrübe ve Makul Sebep"},
        {"soru": "7068'e göre 'Siyasi partiye girmek' cezası nedir?", "secenekler": ["Durdurma", "Maaş Kesme", "Meslekten Çıkarma", "Kınama", "Uyarma"], "cevap": "Meslekten Çıkarma"},
        {"soru": "657'ye göre mazeret izni (evlilik) kaç gündür?", "secenekler": ["3", "5", "7", "10", "15"], "cevap": "7"},
        {"soru": "Bekçilerin çalışma saatleri kural olarak ne zaman başlar?", "secenekler": ["Güneş batışı", "Saat 20:00", "Güneş doğuşu", "Saat 22:00", "Amir belirler"], "cevap": "Güneş batışı"},
        {"soru": "Polisin kıyafet yönetmeliğini hangi makam çıkarır?", "secenekler": ["TBMM", "Cumhurbaşkanı", "İçişleri Bakanlığı", "EGM", "Akademi"], "cevap": "İçişleri Bakanlığı"},
        {"soru": "PVSK'ya göre polisin mülki görevleri dışında kalan görevleri hangisidir?", "secenekler": ["Adli", "İdari", "Siyasi", "Yardım", "Hepsi"], "cevap": "Hepsi"},
        {"soru": "7068'e göre 'İşkence yapmak' cezasının karşılığı nedir?", "secenekler": ["Durdurma", "Aylıktan Kesme", "Meslekten Çıkarma", "Kınama", "6 Ay Hapis"], "cevap": "Meslekten Çıkarma"},
        {"soru": "PVSK Madde 5'e göre parmak izi kimlerden alınmaz?", "secenekler": ["Gözaltına alınanlar", "Silah ruhsatı alanlar", "Ehliyet alanlar", "Pasaport alanlar", "Tanıklar"], "cevap": "Tanıklar"},
        {"soru": "ETK'ya göre 'Başkomiser' rütbesinde bekleme süresi kaçtır?", "secenekler": ["2", "3", "4", "5", "6"], "cevap": "3"},
        {"soru": "7068'e göre kınama cezasının zamanaşımı süresi ne kadardır?", "secenekler": ["1 ay", "6 ay", "1 yıl", "2 yıl", "5 yıl"], "cevap": "6 ay"},
        {"soru": "Adli aramada konutta arama hangi saatlerde yapılamaz?", "secenekler": ["Gece", "Gündüz", "Öğle", "Bayramda", "Hafta sonu"], "cevap": "Gece"},
        {"soru": "PVSK Ek 6'ya göre polisin istihbarat faaliyetleri için kimden izin alınır?", "secenekler": ["Vali", "Bakan", "Hakim", "Savcı", "EGM"], "cevap": "Hakim"},
        {"soru": "657'ye göre devlet memuruna hediye yasağına kim karar verir?", "secenekler": ["Bakanlar Kurulu", "Etik Kurulu", "TBMM", "Cumhurbaşkanı", "Vali"], "cevap": "Etik Kurulu"},
        {"soru": "7068'e göre bir yıl içinde 20 gün göreve gelmemek?", "secenekler": ["Kınama", "Durdurma", "Maaş Kesme", "İhraç", "Uyarma"], "cevap": "İhraç"},
        {"soru": "PVSK'ya göre silah kullanmadan önce ne yapılmalıdır?", "secenekler": ["İhtar", "Havaya ateş", "Kelepçeleme", "Gaz kullanma", "Gözaltı"], "cevap": "İhtar"},
        {"soru": "ETK'ya göre emniyet teşkilatında 'Emniyet Amiri' rütbesinde bekleme süresi?", "secenekler": ["2", "3", "4", "5", "6"], "cevap": "4"},
        {"soru": "7068'e göre 'Denetim görevini yapmamak' cezası?", "secenekler": ["Uyarma", "Kınama", "Aylıktan Kesme", "Durdurma", "İhraç"], "cevap": "Aylıktan Kesme"},

        # ANAYASA VE HUKUK (35 Soru)
        {"soru": "Anayasa Mahkemesi üye sayısı kaçtır?", "secenekler": ["11", "13", "15", "17", "19"], "cevap": "15"},
        {"soru": "AYM üyelerinin görev süresi kaç yıldır?", "secenekler": ["4", "6", "9", "12", "15"], "cevap": "12"},
        {"soru": "RTÜK üyelerini kim seçer?", "secenekler": ["Cumhurbaşkanı", "TBMM", "İletişim Başkanlığı", "YÖK", "Danıştay"], "cevap": "TBMM"},
        {"soru": "Milli Güvenlik Kurulu'nun başkanı kimdir?", "secenekler": ["Cumhurbaşkanı", "İçişleri Bakanı", "Genelkurmay Başkanı", "MSB", "Yardımcı"], "cevap": "Cumhurbaşkanı"},
        {"soru": "CMK'ya göre gözaltı süresi toplu suçlarda en fazla kaç gündür?", "secenekler": ["2", "4", "7", "12", "15"], "cevap": "4"},
        {"soru": "YSK kaç asıl üyeden oluşur?", "secenekler": ["5", "7", "9", "11", "13"], "cevap": "7"},
        {"soru": "HSK'nın başkanı kimdir?", "secenekler": ["Yargıtay Başkanı", "Adalet Bakanı", "Danıştay Başkanı", "CB", "AYM Başkanı"], "cevap": "Adalet Bakanı"},
        {"soru": "CMK'ya göre el koyma kararını hakim kaç saat içinde onaylar?", "secenekler": ["12", "24", "48", "72", "96"], "cevap": "48"},
        {"soru": "Tanıklıktan çekinme hakkı CMK'nın kaçıncı maddesidir?", "secenekler": ["45", "50", "60", "75", "100"], "cevap": "45"},
        {"soru": "OHAL süresi bir seferde en fazla kaç ay olabilir?", "secenekler": ["2", "4", "6", "9", "12"], "cevap": "6"},
        {"soru": "TBMM seçimleri kaç yılda bir yapılır?", "secenekler": ["3", "4", "5", "6", "7"], "cevap": "5"},
        {"soru": "Milletvekili seçilme yaşı kaçtır?", "secenekler": ["18", "21", "25", "30", "40"], "cevap": "18"},
        {"soru": "HSK kaç üyeden oluşur?", "secenekler": ["11", "13", "15", "17", "21"], "cevap": "13"},
        {"soru": "Siyasi partilerin kapatılması davasını kim açar?", "secenekler": ["Yargıtay Başsavcısı", "AYM Başkanı", "Adalet Bakanı", "CB", "TBMM Bşk."], "cevap": "Yargıtay Başsavcısı"},
        {"soru": "Devlet Denetleme Kurulu kime bağlıdır?", "secenekler": ["TBMM", "Cumhurbaşkanı", "Sayıştay", "Danıştay", "YÖK"], "cevap": "Cumhurbaşkanı"},
        {"soru": "AYM üyelerinin yaş haddi kaçtır?", "secenekler": ["60", "65", "67", "70", "72"], "cevap": "65"},
        {"soru": "Kamu Başdenetçisini kim seçer?", "secenekler": ["Cumhurbaşkanı", "TBMM", "Danıştay", "Yargıtay", "HSK"], "cevap": "TBMM"},
        {"soru": "Uyuşmazlık Mahkemesi Başkanı nereden seçilir?", "secenekler": ["AYM", "Yargıtay", "Danıştay", "Sayıştay", "TBMM"], "cevap": "AYM"},
        {"soru": "TCK'ya göre 'Kasten Öldürme' cezası nedir?", "secenekler": ["Ağır Müebbet", "Müebbet", "20 Yıl", "25 Yıl", "30 Yıl"], "cevap": "Müebbet"},
        {"soru": "CMK 100. madde konusu nedir?", "secenekler": ["Gözaltı", "Tutuklama", "Arama", "Tanıklık", "El koyma"], "cevap": "Tutuklama"},
        {"soru": "Savunma hakkı anayasanın kaçıncı maddesidir?", "secenekler": ["36", "38", "40", "42", "45"], "cevap": "36"},
        {"soru": "Bakanlıkların kurulması ne ile olur?", "secenekler": ["Kanun", "Yönetmelik", "CB Kararnamesi", "Tüzük", "Genelge"], "cevap": "CB Kararnamesi"},
        {"soru": "Sayıştay üyelerini kim seçer?", "secenekler": ["Cumhurbaşkanı", "TBMM", "Yargıtay", "Danıştay", "Genel Kurul"], "cevap": "TBMM"},
        {"soru": "CMK'ya göre adli tatil ne zaman biter?", "secenekler": ["20 Temmuz", "31 Ağustos", "1 Eylül", "5 Eylül", "15 Eylül"], "cevap": "31 Ağustos"},
        {"soru": "Cumhurbaşkanı seçilme yaşı kaçtır?", "secenekler": ["18", "25", "30", "40", "45"], "cevap": "40"},
        {"soru": "Sayıştay Başkanı kaç yıl için seçilir?", "secenekler": ["4", "5", "6", "10", "12"], "cevap": "5"},
        {"soru": "Uluslararası Ceza Mahkemesi (UCM) nerededir?", "secenekler": ["Lahey", "Strazburg", "Brüksel", "Viyana", "Berlin"], "cevap": "Lahey"},
        {"soru": "İnsan Hakları Evrensel Bildirgesi hangi yıl kabul edildi?", "secenekler": ["1945", "1948", "1950", "1954", "1960"], "cevap": "1948"},
        {"soru": "Anayasa Mahkemesi ne zaman kurulmuştur?", "secenekler": ["1924", "1961", "1982", "1945", "1950"], "cevap": "1961"},
        {"soru": "Mülkiyet hakkı ne ile kısıtlanabilir?", "secenekler": ["CBK", "Kanun", "Yönetmelik", "Tüzük", "Genelge"], "cevap": "Kanun"},
        {"soru": "Danıştay üyelerinin 1/4'ünü kim seçer?", "secenekler": ["HSK", "TBMM", "Cumhurbaşkanı", "Yargıtay", "AYM"], "cevap": "Cumhurbaşkanı"},
        {"soru": "Yargıtay Cumhuriyet Başsavcısını kim seçer?", "secenekler": ["HSK", "TBMM", "Cumhurbaşkanı", "Yargıtay Üyeleri", "Adalet Bakanı"], "cevap": "Cumhurbaşkanı"},
        {"soru": "Milli Güvenlik Kurulu ne kadar sürede bir toplanır?", "secenekler": ["Ayda bir", "İki ayda bir", "Üç ayda bir", "Haftalık", "Yıllık"], "cevap": "İki ayda bir"},
        {"soru": "Yönetmeliklerin iptali davası nereye açılır?", "secenekler": ["AYM", "Danıştay", "Yargıtay", "Sayıştay", "İdare Mahkemesi"], "cevap": "Danıştay"},
        {"soru": "Hakimler ve Savcılar Kurulu kaç daireden oluşur?", "secenekler": ["1", "2", "3", "4", "5"], "cevap": "2"},

        # TARİH, GÜNCEL VE GENEL KÜLTÜR (30 Soru)
        {"soru": "Lozan Antlaşması hangi yıl imzalanmıştır?", "secenekler": ["1920", "1921", "1922", "1923", "1924"], "cevap": "1923"},
        {"soru": "İstiklal Marşı'nın bestecisi kimdir?", "secenekler": ["M. Akif", "Osman Zeki Üngör", "Ziya Gökalp", "Cemal Reşit Rey", "Yahya Kemal"], "cevap": "Osman Zeki Üngör"},
        {"soru": "Türkiye'nin en yüksek dağı hangisidir?", "secenekler": ["Erciyes", "Süphan", "Ağrı", "Kaçkar", "Nemrut"], "cevap": "Ağrı"},
        {"soru": "Nutuk hangi yılları kapsar?", "secenekler": ["1919-23", "1919-27", "1923-38", "1915-20", "1920-30"], "cevap": "1919-27"},
        {"soru": "Türk Bayrağı Kanunu yılı?", "secenekler": ["1923", "1936", "1983", "1924", "1950"], "cevap": "1983"},
        {"soru": "Savunma sanayi projesi 'KAAN' nedir?", "secenekler": ["Tank", "İHA", "Savaş Uçağı", "Gemi", "Füze"], "cevap": "Savaş Uçağı"},
        {"soru": "Hatay'ın ana vatana katıldığı yıl?", "secenekler": ["1923", "1938", "1939", "1940", "1924"], "cevap": "1939"},
        {"soru": "İlk kadın vali kimdir?", "secenekler": ["Lale Aytaman", "Tansu Çiller", "Meral Akşener", "Fatma Şahin", "Güler İleri"], "cevap": "Lale Aytaman"},
        {"soru": "UNESCO Dünya Mirası listesine en son giren yerimiz (2023)?", "secenekler": ["Gordion", "Göbeklitepe", "Efes", "Ani", "Arslantepe"], "cevap": "Gordion"},
        {"soru": "Karasuları genişliği kural olarak kaç mildir?", "secenekler": ["3", "6", "12", "24", "200"], "cevap": "6"},
        {"soru": "Nobel Edebiyat Ödülü alan ilk Türk yazar?", "secenekler": ["Yaşar Kemal", "Orhan Pamuk", "Aziz Nesin", "Elif Şafak", "Nazım Hikmet"], "cevap": "Orhan Pamuk"},
        {"soru": "En çok sınır komşumuz olan ülke?", "secenekler": ["Irak", "İran", "Suriye", "Yunanistan", "Bulgaristan"], "cevap": "Suriye"},
        {"soru": "Türkiye'nin ilk yerli otomobili?", "secenekler": ["Anadol", "Devrim", "Togg", "Murat", "Şahin"], "cevap": "Devrim"},
        {"soru": "Milli Mücadele'de ilk kurşunu kim atmıştır?", "secenekler": ["Hasan Tahsin", "Kara Fatma", "Sütçü İmam", "Mehmet Çavuş", "Şahin Bey"], "cevap": "Mehmet Çavuş"},
        {"soru": "Atatürk'ün naaşının Anıtkabir'e nakledildiği yıl?", "secenekler": ["1938", "1945", "1953", "1960", "1939"], "cevap": "1953"},
        {"soru": "Erzurum Kongresi Başkanı kimdir?", "secenekler": ["Mustafa Kemal", "Rauf Orbay", "Kazım Karabekir", "İsmet İnönü", "Refet Bele"], "cevap": "Mustafa Kemal"},
        {"soru": "Dünya Sağlık Örgütü (WHO) merkezi neresidir?", "secenekler": ["New York", "Paris", "Cenevre", "Londra", "Roma"], "cevap": "Cenevre"},
        {"soru": "NATO'ya en son katılan üye ülke?", "secenekler": ["Finlandiya", "İsveç", "Ukrayna", "Makedonya", "Arnavutluk"], "cevap": "İsveç"},
        {"soru": "Türk lirasından 6 sıfır ne zaman atıldı?", "secenekler": ["2000", "2005", "2010", "1995", "2002"], "cevap": "2005"},
        {"soru": "İlk kadın Başbakanımız?", "secenekler": ["Lale Aytaman", "Tansu Çiller", "Meral Akşener", "Güler Sabancı", "Türkan Saylan"], "cevap": "Tansu Çiller"},
        {"soru": "TBMM kaç yılında açılmıştır?", "secenekler": ["1919", "1920", "1921", "1922", "1923"], "cevap": "1920"},
        {"soru": "Modern Olimpiyatlar ilk kez nerede yapıldı?", "secenekler": ["Atina", "Paris", "Londra", "Roma", "Berlin"], "cevap": "Atina"},
        {"soru": "Ayasofya hangi yıl cami oldu (son hali)?", "secenekler": ["2018", "2019", "2020", "2021", "2022"], "cevap": "2020"},
        {"soru": "TC'nin ilk anayasası hangisidir?", "secenekler": ["1876", "1921", "1924", "1961", "1982"], "cevap": "1921"},
        {"soru": "Sivil Savunma Teşkilatı kime bağlıdır?", "secenekler": ["EGM", "AFAD", "Jandarma", "TSK", "MSB"], "cevap": "AFAD"},
        {"soru": "Emniyet Genel Müdürlüğü hangi bakanlığa bağlıdır?", "secenekler": ["MSB", "Adalet", "İçişleri", "Dışişleri", "CB"], "cevap": "İçişleri"},
        {"soru": "Mustafa Kemal'e 'Atatürk' soyadı hangi yıl verildi?", "secenekler": ["1923", "1930", "1934", "1938", "1924"], "cevap": "1934"},
        {"soru": "Interpol merkezi nerededir?", "secenekler": ["Paris", "Lyon", "Marsilya", "Brüksel", "Viyana"], "cevap": "Lyon"},
        {"soru": "Mavi Vatan doktrinini ortaya atan amiral?", "secenekler": ["Cihat Yaycı", "Cem Gürdeniz", "Soner Polat", "Özden Örnek", "Uğur Akar"], "cevap": "Cem Gürdeniz"},
        {"soru": "Türkiye'nin en büyük gölü?", "secenekler": ["Tuz", "Van", "Beyşehir", "Eğirdir", "İznik"], "cevap": "Van Gölü"}
    ]
    random.shuffle(st.session_state.questions)

# --- UYGULAMA MOTORU ---
if 'idx' not in st.session_state: st.session_state.idx = 0
if 'skor' not in st.session_state: st.session_state.skor = 0

st.title("🚓 PAEM 100 SORU BANKASI")

if st.session_state.idx < len(st.session_state.questions):
    q = st.session_state.questions[st.session_state.idx]
    st.progress((st.session_state.idx + 1) / len(st.session_state.questions))
    
    st.subheader(f"Soru {st.session_state.idx

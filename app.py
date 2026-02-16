import streamlit as st
import random

# Sayfa Ayarları
st.set_page_config(page_title="PAEM 100 Soru Bankası", page_icon="👮", layout="centered")

# --- TELEFON UYGULAMASI GÖRÜNÜMÜ İÇİN CSS ---
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #0e1117;
        color: white;
        border: 1px solid #31333F;
    }
    .stProgress > div > div > div > div {
        background-color: #2e7d32;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 100 SORULUK TAM VERİ SETİ ---
if 'questions' not in st.session_state:
    st.session_state.questions = [
        # MEVZUAT VE POLİS HUKUKU (1-35)
        {"soru": "PVSK'ya göre parmak izi kayıtları kaç yıl sonra silinir?", "secenekler": ["10", "20", "40", "80", "100"], "cevap": "80"},
        {"soru": "7068'e göre 'Görevi kötüye kullanmak' cezasının karşılığı nedir?", "secenekler": ["Kınama", "10 Ay Durdurma", "24 Ay Durdurma", "Meslekten Çıkarma", "Maaş Kesme"], "cevap": "Meslekten Çıkarma"},
        {"soru": "PVSK Ek Madde 4'e göre polisin silah kullanma yetkisi için kaç ikaz yeterlidir?", "secenekler": ["1", "2", "3", "Sayı sınırı yok", "5"], "cevap": "1"},
        {"soru": "7068'e göre 'Kumar oynamak' cezasının karşılığı nedir?", "secenekler": ["Aylıktan kesme", "10 Ay Durdurma", "24 Ay Durdurma", "Meslekten Çıkarma", "Kınama"], "cevap": "24 Ay Durdurma"},
        {"soru": "3201 ETK'ya göre Komiser rütbe bekleme süresi kaçtır?", "secenekler": ["2", "3", "4", "5", "6"], "cevap": "4"},
        {"soru": "EGM Yüksek Disiplin Kurulu Başkanı kimdir?", "secenekler": ["Emniyet Genel Müdürü", "Bakan Yardımcısı", "Personel Başkanı", "Teftiş Başkanı", "Hukuk Müşaviri"], "cevap": "Emniyet Genel Müdürü"},
        {"soru": "7068'e göre 'Amire saygısızlık' cezasının karşılığı nedir?", "secenekler": ["Uyarma", "Kınama", "Aylıktan Kesme", "Durdurma", "İhraç"], "cevap": "Aylıktan Kesme"},
        {"soru": "PVSK'ya göre önleme araması kararı mülki amir tarafından verilirse kaç saat içinde hakime sunulur?", "secenekler": ["12", "24", "48", "72", "96"], "cevap": "24"},
        {"soru": "Polis Akademisi Başkanı kim tarafından atanır?", "secenekler": ["EGM", "İçişleri Bakanı", "Cumhurbaşkanı", "YÖK", "MEB"], "cevap": "Cumhurbaşkanı"},
        {"soru": "7068'e göre disiplin cezalarına karşı kaç gün içinde dava açılabilir?", "secenekler": ["15", "30", "45", "60", "90"], "cevap": "60"},
        {"soru": "657 DMK'ya göre aday memurluk süresi en fazla kaçtır?", "secenekler": ["1", "2", "3", "4", "5"], "cevap": "2"},
        {"soru": "PVSK'ya göre zor kullanma yetkisi hangi maddede düzenlenmiştir?", "secenekler": ["4/A", "5", "9", "13", "16"], "cevap": "16"},
        {"soru": "Emniyet hizmetleri sınıfı emeklilik yaş haddi kaçtır?", "secenekler": ["52", "55", "58", "60", "65"], "cevap": "55"},
        {"soru": "7068'e göre 'Yalan beyanda bulunmak' cezası nedir?", "secenekler": ["Kınama", "Aylıktan Kesme", "Durdurma", "İhraç", "Uyarma"], "cevap": "Durdurma"},
        {"soru": "PVSK'ya göre adli arama kararı gecikmesinde sakınca bulunan hallerde kimden alınır?", "secenekler": ["Vali", "Emniyet Müdürü", "Savcı", "Bakan", "Kaymakam"], "cevap": "Savcı"},
        {"soru": "Emniyet Teşkilatında en yüksek rütbe hangisidir?", "secenekler": ["1. Sınıf Emniyet Müdürü", "Sınıf Üstü Emniyet Müdürü", "Genel Müdür", "Kurul Başkanı", "Daire Başkanı"], "cevap": "Sınıf Üstü Emniyet Müdürü"},
        {"soru": "Polis Bakım ve Yardım Sandığı'nın kısa adı?", "secenekler": ["POLSAN", "POLVAK", "EGMVAK", "POYAS", "POLBYS"], "cevap": "POLSAN"},
        {"soru": "PVSK 4/A'ya göre durdurma yetkisi neye dayanır?", "secenekler": ["Tecrübe ve Makul Sebep", "Yeterli Şüphe", "Somut Delil", "Amir Emri", "İhbar"], "cevap": "Tecrübe ve Makul Sebep"},
        {"soru": "7068'e göre 'Siyasi partiye girmek' cezası nedir?", "secenekler": ["Durdurma", "Maaş Kesme", "Meslekten Çıkarma", "Kınama", "Uyarma"], "cevap": "Meslekten Çıkarma"},
        {"soru": "657'ye göre mazeret izni (evlilik) kaç gündür?", "secenekler": ["3", "5", "7", "10", "15"], "cevap": "7"},
        {"soru": "Bekçilerin çalışma saatleri kural olarak ne zaman başlar?", "secenekler": ["Güneş batışı", "Saat 20:00", "Güneş doğuşu", "Saat 22:00", "Amir belirler"], "cevap": "Güneş batışı"},
        {"soru": "Polisin kıyafet yönetmeliğini hangi makam çıkarır?", "secenekler": ["TBMM", "Cumhurbaşkanı", "İçişleri Bakanlığı", "EGM", "Akademi"], "cevap": "İçişleri Bakanlığı"},
        {"soru": "7068'e göre 'İşkence yapmak' cezasının karşılığı nedir?", "secenekler": ["Durdurma", "Aylıktan Kesme", "Meslekten Çıkarma", "Kınama", "6 Ay Hapis"], "cevap": "Meslekten Çıkarma"},
        {"soru": "PVSK Madde 5'e göre parmak izi kimlerden alınmaz?", "secenekler": ["Gözaltına alınanlar", "Silah ruhsatı alanlar", "Ehliyet alanlar", "Pasaport alanlar", "Tanıklar"], "cevap": "Tanıklar"},
        {"soru": "ETK'ya göre 'Başkomiser' rütbesinde bekleme süresi kaçtır?", "secenekler": ["2", "3", "4", "5", "6"], "cevap": "3"},
        {"soru": "7068'e göre kınama cezasının zamanaşımı süresi ne kadardır?", "secenekler": ["1 ay", "6 ay", "1 yıl", "2 yıl", "5 yıl"], "cevap": "6 ay"},
        {"soru": "Adli aramada konutta arama hangi saatlerde yapılamaz?", "secenekler": ["Gece", "Gündüz", "Öğle", "Bayramda", "Hafta sonu"], "cevap": "Gece"},
        {"soru": "PVSK Ek 6'ya göre polisin istihbarat faaliyetleri için kimden izin alınır?", "secenekler": ["Vali", "Bakan", "Hakim", "Savcı", "EGM"], "cevap": "Hakim"},
        {"soru": "657'ye göre devlet memuruna hediye yasağına kim karar verir?", "secenekler": ["Bakanlar Kurulu", "Etik Kurulu", "TBMM", "Cumhurbaşkanı", "Vali"], "cevap": "Etik Kurulu"},
        {"soru": "7068'e göre bir yıl içinde 20 gün göreve gelmemek?", "secenekler": ["Kınama", "Durdurma", "Maaş Kesme", "İhraç", "Uyarma"], "cevap": "İhraç"},
        {"soru": "PVSK'ya göre silah kullanmadan önce ne yapılmalıdır?", "secenekler": ["İhtar", "Havaya ateş", "Kelepçeleme", "Gaz kullanma", "Gözaltı"], "cevap": "İhtar"},
        {"soru": "ETK'ya göre 'Emniyet Amiri' rütbesinde bekleme süresi?", "secenekler": ["2", "3", "4", "5", "6"], "cevap": "4"},
        {"soru": "7068'e göre 'Denetim görevini yapmamak' cezası?", "secenekler": ["Uyarma", "Kınama", "Aylıktan Kesme", "Durdurma", "İhraç"], "cevap": "Aylıktan Kesme"},
        {"soru": "Polis memurlarının yıllık izin süresi 1-10 yıl hizmette kaç gündür?", "secenekler": ["15", "20", "25", "30", "45"], "cevap": "20"},
        {"soru": "PVSK Ek Madde 4 hangi yıl yürürlüğe girmiştir?", "secenekler": ["2001", "2007", "2015", "2018", "2020"], "cevap": "2007"},

        # ANAYASA VE HUKUK (36-70)
        {"soru": "Anayasa Mahkemesi üye sayısı kaçtır?", "secenekler": ["11", "13", "15", "17", "19"], "cevap": "15"},
        {"soru": "AYM üyelerinin görev süresi kaç yıldır?", "secenekler": ["4", "6", "9", "12", "15"], "cevap": "12"},
        {"soru": "RTÜK üyelerini kim seçer?", "secenekler": ["CB", "TBMM", "İletişim Bşk.", "YÖK", "Danıştay"], "cevap": "TBMM"},
        {"soru": "Milli Güvenlik Kurulu'nun başkanı kimdir?", "secenekler": ["CB", "İçişleri Bak.", "Genelkurmay", "MSB", "Yardımcı"], "cevap": "CB"},
        {"soru": "CMK'ya göre gözaltı süresi toplu suçlarda en fazla kaç gündür?", "secenekler": ["2", "4", "7", "12", "15"], "cevap": "4"},
        {"soru": "YSK kaç asıl üyeden oluşur?", "secenekler": ["5", "7", "9", "11", "13"], "cevap": "7"},
        {"soru": "HSK'nın başkanı kimdir?", "secenekler": ["Yargıtay Bşk.", "Adalet Bakanı", "Danıştay Bşk.", "CB", "AYM Bşk."], "cevap": "Adalet Bakanı"},
        {"soru": "CMK'ya göre el koyma kararını hakim kaç saat içinde onaylar?", "secenekler": ["12", "24", "48", "72", "96"], "cevap": "48"},
        {"soru": "Tanıklıktan çekinme hakkı CMK madde kaçtır?", "secenekler": ["45", "50", "60", "75", "100"], "cevap": "45"},
        {"soru": "OHAL süresi bir seferde en fazla kaç ay olabilir?", "secenekler": ["2", "4", "6", "9", "12"], "cevap": "6"},
        {"soru": "TBMM seçimleri kaç yılda bir yapılır?", "secenekler": ["3", "4", "5", "6", "7"], "cevap": "5"},
        {"soru": "Milletvekili seçilme yaşı kaçtır?", "secenekler": ["18", "21", "25", "30", "40"], "cevap": "18"},
        {"soru": "HSK kaç üyeden oluşur?", "secenekler": ["11", "13", "15", "17", "21"], "cevap": "13"},
        {"soru": "Siyasi partilerin kapatılması davasını kim açar?", "secenekler": ["Yargıtay Başsavcısı", "AYM Bşk.", "Adalet Bak.", "CB", "TBMM Bşk."], "cevap": "Yargıtay Başsavcısı"},
        {"soru": "Devlet Denetleme Kurulu kime bağlıdır?", "secenekler": ["TBMM", "Cumhurbaşkanı", "Sayıştay", "Danıştay", "YÖK"], "cevap": "Cumhurbaşkanı"},
        {"soru": "AYM üyelerinin yaş haddi kaçtır?", "secenekler": ["60", "65", "67", "70", "72"], "cevap": "65"},
        {"soru": "Kamu Başdenetçisini kim seçer?", "secenekler": ["CB", "TBMM", "Danıştay", "Yargıtay", "HSK"], "cevap": "TBMM"},
        {"soru": "Uyuşmazlık Mahkemesi Başkanı nereden seçilir?", "secenekler": ["AYM", "Yargıtay", "Danıştay", "Sayıştay", "TBMM"], "cevap": "AYM"},
        {"soru": "TCK'ya göre 'Kasten Öldürme' cezası nedir?", "secenekler": ["Ağır Müebbet", "Müebbet", "20 Yıl", "25 Yıl", "30 Yıl"], "cevap": "Müebbet"},
        {"soru": "CMK 100. madde konusu nedir?", "secenekler": ["Gözaltı", "Tutuklama", "Arama", "Tanıklık", "El koyma"], "cevap": "Tutuklama"},
        {"soru": "Savunma hakkı anayasanın kaçıncı maddesidir?", "secenekler": ["36", "38", "40", "42", "45"], "cevap": "36"},
        {"soru": "Bakanlıkların kurulması ne ile olur?", "secenekler": ["Kanun", "Yönetmelik", "CBK", "Tüzük", "Genelge"], "cevap": "CBK"},
        {"soru": "Sayıştay üyelerini kim seçer?", "secenekler": ["CB", "TBMM", "Yargıtay", "Danıştay", "Kurul"], "cevap": "TBMM"},
        {"soru": "CMK'ya göre adli tatil ne zaman biter?", "secenekler": ["20 Temmuz", "31 Ağustos", "1 Eylül", "5 Eylül", "15 Eylül"], "cevap": "31 Ağustos"},
        {"soru": "Cumhurbaşkanı seçilme yaşı kaçtır?", "secenekler": ["18", "25", "30", "40", "45"], "cevap": "40"},
        {"soru": "Sayıştay Başkanı kaç yıl için seçilir?", "secenekler": ["4", "5", "6", "10", "12"], "cevap": "5"},
        {"soru": "Uluslararası Ceza Mahkemesi (UCM) nerededir?", "secenekler": ["Lahey", "Strazburg", "Brüksel", "Viyana", "Berlin"], "cevap": "Lahey"},
        {"soru": "İnsan Hakları Evrensel Bildirgesi yılı?", "secenekler": ["1945", "1948", "1950", "1954", "1960"], "cevap": "1948"},
        {"soru": "Anayasa Mahkemesi ne zaman kurulmuştur?", "secenekler": ["1924", "1961", "1982", "1945", "1950"], "cevap": "1961"},
        {"soru": "Mülkiyet hakkı ne ile kısıtlanabilir?", "secenekler": ["CBK", "Kanun", "Yönetmelik", "Tüzük", "Genelge"], "cevap": "Kanun"},
        {"soru": "Danıştay üyelerinin 1/4'ünü kim seçer?", "secenekler": ["HSK", "TBMM", "Cumhurbaşkanı", "Yargıtay", "AYM"], "cevap": "Cumhurbaşkanı"},
        {"soru": "Yargıtay Başsavcısını kim seçer?", "secenekler": ["HSK", "TBMM", "Cumhurbaşkanı", "Üyeler", "Adalet Bak."], "cevap": "Cumhurbaşkanı"},
        {"soru": "MGK ne kadar sürede bir toplanır?", "secenekler": ["Ayda bir", "İki ayda bir", "Üç ayda bir", "Haftalık", "Yıllık"], "cevap": "İki ayda bir"},
        {"soru": "Yönetmelik iptali davası nereye açılır?", "secenekler": ["AYM", "Danıştay", "Yargıtay", "Sayıştay", "İdare Mah."], "cevap": "Danıştay"},
        {"soru": "HSK kaç daireden oluşur?", "secenekler": ["1", "2", "3", "4", "5"], "cevap": "2"},

        # TARİH VE GÜNCEL BİLGİLER (71-100)
        {"soru": "Lozan Antlaşması yılı?", "secenekler": ["1920", "1921", "1922", "1923", "1924"], "cevap": "1923"},
        {"soru": "İstiklal Marşı'nın bestecisi?", "secenekler": ["M. Akif", "O. Zeki Üngör", "Z. Gökalp", "C. Reşit Rey", "Y. Kemal"], "cevap": "O. Zeki Üngör"},
        {"soru": "Türkiye'nin en yüksek dağı?", "secenekler": ["Erciyes", "Süphan", "Ağrı", "Kaçkar", "Nemrut"], "cevap": "Ağrı"},
        {"soru": "Nutuk hangi yılları kapsar?", "secenekler": ["1919-23", "1919-27", "1923-38", "1915-20", "1920-30"], "cevap": "1919-27"},
        {"soru": "Savunma sanayi projesi 'KAAN' nedir?", "secenekler": ["Tank", "İHA", "Uçak", "Gemi", "Füze"], "cevap": "Uçak"},
        {"soru": "Hatay'ın ana vatana katıldığı yıl?", "secenekler": ["1923", "1938", "1939", "1940", "1924"], "cevap": "1939"},
        {"soru": "İlk kadın vali?", "secenekler": ["L. Aytaman", "T. Çiller", "M. Akşener", "F. Şahin", "G. İleri"], "cevap": "L. Aytaman"},
        {"soru": "UNESCO Dünya Mirası listesine son giren (2023)?", "secenekler": ["Gordion", "Göbeklitepe", "Efes", "Ani", "Arslantepe"], "cevap": "Gordion"},
        {"soru": "Karasuları genişliği kural olarak kaç mildir?", "secenekler": ["3", "6", "12", "24", "200"], "cevap": "6"},
        {"soru": "En çok sınır komşumuz olan ülke?", "secenekler": ["Irak", "İran", "Suriye", "Yunanistan", "Bulgaristan"], "cevap": "Suriye"},
        {"soru": "Türkiye'nin ilk yerli otomobili?", "secenekler": ["Anadol", "Devrim", "Togg", "Murat", "Şahin"], "cevap": "Devrim"},
        {"soru": "Milli Mücadele'de ilk kurşun (Mehmet Çavuş)?", "secenekler": ["Dörtyol", "İzmir", "Antep", "Maraş", "Urfa"], "cevap": "Dörtyol"},
        {"soru": "Anıtkabir'e nakil yılı?", "secenekler": ["1938", "1945", "1953", "1960", "1939"], "cevap": "1953"},
        {"soru": "Dünya Sağlık Örgütü (WHO) merkezi?", "secenekler": ["NY", "Paris", "Cenevre", "Londra", "Roma"], "cevap": "Cenevre"},
        {"soru": "NATO'ya en son katılan ülke?", "secenekler": ["Finlandiya", "İsveç", "Ukrayna", "Makedonya", "Arnavutluk"], "cevap": "İsveç"},
        {"soru": "TL'den 6 sıfır atılma yılı?", "secenekler": ["2000", "2005", "2010", "1995", "2002"], "cevap": "2005"},
        {"soru": "İlk kadın Başbakanımız?", "secenekler": ["Lale Aytaman", "Tansu Çiller", "Meral Akşener", "Güler Sabancı", "Türkan Saylan"], "cevap": "Tansu Çiller"},
        {"soru": "TBMM açılış yılı?", "secenekler": ["1919", "1920", "1921", "1922", "1923"], "cevap": "1920"},
        {"soru": "Ayasofya cami olma yılı?", "secenekler": ["2018", "2019", "2020", "2021", "2022"], "cevap": "2020"},
        {"soru": "Sivil Savunma kime bağlıdır?", "secenekler": ["EGM", "AFAD", "Jandarma", "TSK", "MSB"], "cevap": "AFAD"},
        {"soru": "EGM hangi bakanlığa bağlıdır?", "secenekler": ["MSB", "Adalet", "İçişleri", "Dışişleri", "CB"], "cevap": "İçişleri"},
        {"soru": "Atatürk soyadı yılı?", "secenekler": ["1923", "1930", "1934", "1938", "1924"], "cevap": "1934"},
        {"soru": "Interpol merkezi?", "secenekler": ["Paris", "Lyon", "Marsilya", "Brüksel", "Viyana"], "cevap": "Lyon"},
        {"soru": "Türkiye'nin en büyük gölü?", "secenekler": ["Tuz", "Van", "Beyşehir", "Eğirdir", "İznik"], "cevap": "Van"},
        {"soru": "Mavi Vatan terimini ilk kullanan?", "secenekler": ["C. Yaycı", "C. Gürdeniz", "S. Polat", "Ö. Örnek", "U. Akar"], "cevap": "C. Gürdeniz"},
        {"soru": "Dede Korkut hikaye sayısı?", "secenekler": ["10", "12", "13", "15", "20"], "cevap": "13"},
        {"soru": "Sinekli Bakkal yazarı?", "secenekler": ["H. Edip", "R. Nuri", "Y. Kadri", "P. Safa", "O. Kemal"], "cevap": "H. Edip"},
        {"soru": "G-20 2024 zirvesi nerede?", "secenekler": ["Brezilya", "Hindistan", "Türkiye", "ABD", "İtalya"], "cevap": "Brezilya"},
        {"soru": "TC'de tek dereceli seçim yılı?", "secenekler": ["1923", "1946", "1950", "1924", "1930"], "cevap": "1946"},
        {"soru": "Alper Gezeravcı rütbesi?", "secenekler": ["Binbaşı", "Yarbay", "Albay", "Yüzbaşı", "Astsubay"], "cevap": "Albay"}
    ]
    random.shuffle(st.session_state.questions)

# --- UYGULAMA MOTORU ---
if 'idx' not in st.session_state: st.session_state.idx = 0
if 'skor' not in st.session_state: st.session_state.skor = 0

st.title("🚓 PAEM 100 SORU BANKASI")

if st.session_state.idx < len(st.session_state.questions):
    q = st.session_state.questions[st.session_state.idx]
    
    # İlerleme Çubuğu
    st.progress((st.session_state.idx + 1) / len(st.session_state.questions))
    
    # Soru Sayısı Başlığı
    st.subheader(f"Soru {st.session_state.idx + 1} / {len(st.session_state.questions)}")
    st.info(q['soru'])
    
    secim = st.radio("Cevap Şıkları:", q['secenekler'], key=f"q_{st.session_state.idx}")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Onayla ✅"):
            if secim == q['cevap']:
                st.success("Doğru! ✨")
                st.session_state.skor += 1
            else:
                st.error(f"Yanlış! ❌ Doğru Cevap: {q['cevap']}")
    
    with col2:
        if st.button("Sonraki Soru ➡️"):
            st.session_state.idx += 1
            st.rerun()
else:
    st.balloons()
    st.header("🏁 Sınav Tamamlandı!")
    st.metric("Toplam Puan", f"{st.session_state.skor} / {len(st.session_state.questions)}")
    
    basari = (st.session_state.skor / len(st.session_state.questions)) * 100
    st.write(f"Başarı Oranı: %{basari:.2f}")
    
    if st.button("Sınavı Baştan Başlat 🔄"):
        st.session_state.idx = 0
        st.session_state.skor = 0
        random.shuffle(st.session_state.questions)
        st.rerun()
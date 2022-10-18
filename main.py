import streamlit as st
import lorem
from numerize import numerize
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
# import streamlit_book as stb
import plotly.express as px
import plotly

st.set_page_config(layout="wide")

# Sidebar

with st.sidebar:
    st.title("Interactive Chart Menu")
    st.write("*Chart* yang dapat diatur diberi tanda * pada judul *chart*-nya")
    # freq = st.selectbox("Masukkan frekuensi", ('D', 'W', 'M', 'Q', 'Y'))
    isquartil = st.selectbox("Jumlah Pengguna Paypal Global dalam Quartil", ('Tidak', 'Ya'))
    # with st.expander("Ketahui lebih lanjut..."):
    #     st.write(lorem.paragraph())

st.title("Steam dan Paypal Diblokir, *Game Developer* dan *Freelancer* Indonesia Terancam?")
st.write("")
st.write("")
# met1, met2, met3, met4, met5, met6, met7, met8, met9, met10 = st.columns(10)
# with met1:
#     image = Image.open("./assets/img/circle.png")
#     st.image(image, width=90)
# with met2:
#     st.markdown("**Ricky Indra Gunawan**")
#     st.write("4 Agustus 2022")
col1, mid, col2 = st.columns([1,1,35])
with col1:
    st.image('./assets/img/circle.png', width=60)
with col2:
    st.markdown("**Ricky Indra Gunawan**<br>4 Agustus 2022", unsafe_allow_html=True)
st.markdown("---")

st.write("""Pada hari Jumat (29/7/2022), Kementerian Komunikasi dan Informatika Republik Indonesia (Kominfo) 
menyatakan **telah melakukan pemutusan akses sementara** kepada sepuluh Penyelenggara Sistem Elektronik (PSE) terpopuler, 
di antaranya **PayPal** dan **Steam** karena belum melakukan pendaftaran regulasi PSE Kominfo hingga pukul 23.59 WIB Jumat (29/7). 
**PayPal** merupakan perusahaan penyedia layanan elektronik yang memfasilitasi pembayaran antar pihak melalui transfer *online*, 
sedangkan **Steam** merupakan wadah bagi *developer game* untuk menjual dan memasarkan *game* ciptaannya serta wadah bagi para penikmat *game* untuk tempat untuk membeli beragam *game* terbaru dengan praktis.
\n
Hal ini tentunya menjadi topik perdebatan yang panas serta memicu berbagai protes dari berbagai kalangan, termasuk komunitas *gamer* atau 
penikmat *video game online* dan para pekerja lepas (*freelancer*) yang menggunakan layanan PSE tersebut.
\n
Terlepas dari kontroversi mengenai peraturan PSE yang ada saat ini, kira-kira seberapa bagian warga negara Indonesia yang akan terkena dampaknya apabila **Steam** dan **Paypal** 
sepenuhnya diblokir dan aspek apa saja yang akan terpengaruh atas kasus pemblokiran layanan dari PSE tersebut?""")

st.subheader("Perkembangan Industri Game di Mata Dunia melalui Steam")
st.write("Perkembangan industri game dunia akan menjadi pembahasan yang menarik untuk kita bahas kali ini. Selama beberapa tahun terakhir, industri game perlahan mulai berkembang dan dikenal banyak orang di seluruh dunia.")
st.write("""Seperti yang dikutip dalam berita Tempo, Ketua Umum Asosiasi Game Indonesia (AGI) Cipto Adiguno menyebut selama 2021 industri game global relatif stagnan. Sebab, menurutnya, pada 2020 ada pertumbuhan yang sangat besar berkat pandemi, sehingga pada tahun 2021 terjadi penyesuaian.

"Diperkirakan tahun depan industri akan kembali tumbuh, antara lain didorong oleh pemain-pemain yang mencoba game ketika pandemi akan tetap bermain walau pandemi berakhir," ujarnya, Minggu, 12 Desember 2021.""")
persen_game=pd.read_csv('./data/persentase_pengguna_internet_yang_main_game.csv', delimiter=';')
fig_persen_game = px.bar(persen_game, x='negara', y='persentase', color="negara", title="Persentase Pengguna Internet Berusia 16-64 Tahun yang Memainkan Game Online dalam Device Apapun")

game_paling_banyak_player=pd.read_csv('./data/most_played_esports_games.csv', delimiter=';')
fig_game_paling_banyak_player = px.bar(game_paling_banyak_player, x='game', y='persentase', color="game", title="Game yang Paling Dimainkan di Indonesia 2021")

game_paling_banyak_ditonton=pd.read_csv('./data/most_watched_esports_games.csv', delimiter=';')
fig_game_paling_banyak_ditonton = px.bar(game_paling_banyak_ditonton, x='game', y='persentase', color="game", title="Game yang Paling Ditampilkan Secara Live di Indonesia 2021")

game_paling_banyak_distreaming=pd.read_csv('./data/most_streamed_esports_games.csv', delimiter=';')
fig_game_paling_banyak_distreaming = px.bar(game_paling_banyak_distreaming, x='game', y='persentase', color="game", title="Game yang Paling Ditonton di Indonesia 2021")

pertumbuhan_pasar_game=pd.read_csv('./data/market_size.csv', delimiter=';')
pertumbuhan_pasar_game['tahun'] = pertumbuhan_pasar_game['tahun'].astype(str)
fig_pertumbuhan_pasar_game = px.bar(pertumbuhan_pasar_game, x='tahun', y='market_size', title="Pertumbuhan Revenue Pasar Game di Indonesia")

total_pengunjung=pd.read_csv('./data/total_visits_game_store.csv', delimiter=';')
fig_total_pengunjung = px.bar(total_pengunjung, x='game_store', y='total_pengunjung', color="game_store", title="Total Pengunjung Website Skala Global")



game_body0, game_body1 = st.columns(2)
with game_body0:
    st.plotly_chart(fig_persen_game, use_container_width=True)
    st.write("Indonesia menempati negara kedua dengan gamer terbanyak di dunia. Hal ini menjadi peluang bagi para developer game agar dapat memasarkan game-nya di Indonesia")
    st.plotly_chart(fig_game_paling_banyak_player, use_container_width=True)
    st.write("Dilihat dari grafik berikut, game-game yang berasal dari PSE yang diblokir oleh Kominfo, yaitu Dota 2, Counter-Strike, Rocket League serta Fortnite menempati top 10 game yang paling banyak dimainkan")
    st.plotly_chart(fig_pertumbuhan_pasar_game, use_container_width=True)
    st.write("Pertumbuhan pasar game di Indonesia dari tahun ke tahun meningkat secara signifikan. Tentunya hal ini menjadi potensi bagi para developer game di Indonesia")
    
with game_body1:
    st.plotly_chart(fig_game_paling_banyak_distreaming, use_container_width=True)
    st.write("Dilihat dari grafik berikut, game-game yang berasal dari PSE yang diblokir oleh Kominfo, yaitu Dota 2, Counter-Strike, Rocket League serta Fortnite menempati top 10 game yang paling banyak dijadikan sebagai bahan video streaming")
    st.plotly_chart(fig_game_paling_banyak_ditonton, use_container_width=True)
    st.write("Dilihat dari grafik berikut, game-game yang berasal dari PSE yang diblokir oleh Kominfo, yaitu Dota 2, Counter-Strike, Rocket League serta Fortnite menempati top 10 game yang paling banyak ditonton")
    st.plotly_chart(fig_total_pengunjung, use_container_width=True)
    st.write("Dilihat grafik total pengunjung website penyedia game store, Steam menempati urutan pertama, diikuti oleh Epic Games Store, Origin dan Ubisoft.")
st.write("Terdapat banyak game buatan Indonesia yang akan rilis di Steam pada tahun 2022. Tentunya, jika Steam diblokir, para developer Indonesia akan kesulitan untuk memasarkan game-nya ke dalam kancah internasional.")
st.write("Untuk informasi lebih lanjut mengenai game buatan Indonesia yang akan rilis pada tahun ini, dapat dicek di https://virtualseasia.com/games-of-2022-indonesia/")
# st.code("import streamlit as st")
# st.text(lorem.paragraph())

#Deklarasi dataset
# df = pd.read_csv("store.csv")

# Data prep
# df['Order Date'] = pd.to_datetime(df['Order Date'])
# df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# End of data prep

# st.dataframe(df)

# metrics

# st.metric("Total Sales", 1000, 10)

# label value delta
# st.metric("Total Profit", "$ 10M", "-2.3%")

# Input
# st.title("Input")

# tombol1 = st.button("Tekan tombol ini")
# st.write(tombol1)
virtual = pd.read_csv("./data/virtualsea2020.csv")
# virtualin = virtual['country'].astype(str)
# virtualin = virtual['total_games'].astype(int)
fig_visualsea = px.bar(virtual, x='country', y='total_games', title='Total Games dari Asia Tenggara yang dirilis dalam platform Steam 2020')
# Plot!
st.subheader("Apakah Kamu Tahu?")
st.write("Negara ASEAN manakah yang merilis game paling banyak di Steam menurut VirtualSEA pada tahun 2020? (Hanya ada satu jawaban)")
q0, q1, q2, q3, q4, q5 = st.columns(6)
with q0:
    st.image('./assets/img/Flag_of_Indonesia.png', width=100)
    a0 = st.checkbox("Indonesia")
with q1:
    st.image('./assets/img/Flag_of_Laos.png', width=100)
    a1 = st.checkbox("Laos")
with q2:
    st.image('./assets/img/Flag_of_Singapore.png', width=100)
    a2 = st.checkbox("Singapore")
with q3:
    st.image('./assets/img/Flag_of_Myanmar.png', width=100)
    a3 = st.checkbox("Myanmar")
with q4:
    st.image('./assets/img/Flag_of_Thailand.png', width=100)
    a4 = st.checkbox("Thailand")
with q5:
    st.image('./assets/img/Flag_of_Cambodia.png', width=100)
    a5 = st.checkbox("Kamboja") 
if a0 and (a1 == False) and (a2 == False) and (a3 == False) and (a4 == False) and (a5 == False):
    # st.write("Anda sudah setuju")
    with st.expander("Selamat, Kamu Benar!"):
        st.write("""
            Fun Fact!
            \nSelain perangkat seluler, PC merupakan platform rilis terpenting bagi pengembang game dari Asia Tenggara.
            Menurut VirtualSEA, Indonesia menjadi negara yang memasarkan game-nya di Steam dengan 124 entri - hampir tidak ada negara lain di Asia Tenggara yang produktif di pasar game PC. 
            \nSingapura, Thailand, dan Filipina juga menunjukkan bahwa mereka dapat mengikuti pasar game di Steam. 
            \nMalaysia, di sisi lain, berfokus pada kualitas daripada kuantitas. 
            \nSedangkan Vietnam dan Myanmar cenderung memainkan peran subordinat. 
            \nSayangnya, game dari negara Kamboja, Laos, Brunei, dan Timor-Leste belum ada di Steam.
        """)
        st.plotly_chart(fig_visualsea, use_container_width=True)
        st.write("Sumber data : https://www.facebook.com/virtualseasia/photos/a.820476861421191/2010678045734394/?_rdc=1&_rdr")
else:
    st.write("Anda belum menjawab/jawaban anda salah.")


st.write("")
st.subheader("Paypal, *\"e-wallet\"* para *freelancer online* di Indonesia")

paypal_global_users = pd.read_csv("./data/paypal_global_users.csv")
paypal_global_users['tahun'] = paypal_global_users['tahun'].astype(str)
fig_pgu = px.line(paypal_global_users, x='tahun', y='jumlah_user', title='Jumlah Pengguna PayPal Tahunan Skala Global 2013-2021 (dalam jutaan)*', markers=True)

paypal_global_users_quartil = pd.read_csv("./data/paypal_active_users.csv", delimiter=';')
fig_pgu_2 = px.line(paypal_global_users_quartil, x='periode', y='jumlah_pengguna', title='Jumlah Pengguna PayPal Tahunan dalam Quartil 2013-2021 (dalam jutaan)*', markers=True)

paypal_with_competitors = pd.read_csv("./data/paypal_and_competitors - Copy.csv")
fig_comp = px.pie(paypal_with_competitors, values='market_share', names='payment_service', title='Pembagian Market Software Payment Processing Skala Global 2022')

paypal_opening0, paypal_opening1 = st.columns(2)
with paypal_opening0:
    if isquartil == 'Ya':
        st.plotly_chart(fig_pgu_2, use_container_width=True)
    else:
        st.plotly_chart(fig_pgu, use_container_width=True)
    st.write("""Paypal mengalami kenaikan yang signifikan dari tahun ke tahun. Tentunya hal ini menandakan bahwa Paypal berhasil menambahkan jumlah usernya hingga saat ini.""")
with paypal_opening1:
    st.plotly_chart(fig_comp, use_container_width=True)
    st.write("""Berdasarkan data yang diperoleh dari datanyze.com, software payment processing dengan pembagian market tertinggi yaitu Paypal sebesar 42,5%. Oleh karena itu, 
    Paypal menjadi cara pembayaran lintas negara yang paling banyak digunakan oleh penduduk di dunia dibandingkan dengan kompetitornya.""")
st.write("""Kementerian Komunikasi dan Informatika telah memblokir Paypal. Namun, Kementerian Komunikasi dan Informatika kemudian membuka blokir PayPal untuk sementara, karena banyak pengguna di Indonesia yang masih menyimpan dananya di Paypal. Pembukaan sementara blok tersebut akan dilakukan mulai 1 hingga 5 Agustus 2022 pukul 23.59 WIB. Artinya mulai 6 Agustus pukul 00.00 WIB PayPal sudah tidak bisa diakses lagi di Indonesia. "Silakan gunakan (masa buka blokir sementara PayPal). Kami menanggapi semua ini karena ada permintaan dari masyarakat yang uangnya masih tertahan di sana," kata Dirjen Aplikasi dan Informasi Kementerian Komunikasi dan Informatika Semuel A Pangerapan, dikutip dari Kompas.com, Minggu (31). Menurut laporan Business of Apps, pengguna aplikasi fintech PayPal di seluruh dunia terus tumbuh setiap tahun selama periode 2013-2021, seperti yang ditunjukkan pada grafik. Pada tahun 2021 jumlah pengguna setiap tahunnya akan mencapai sekitar 426 juta pengguna, meningkat 13% (year-on-year/yoy) dibandingkan tahun 2020 yang masih 377 juta.""")
# paypal_body0, paypal_body1 = st.columns(2)
# with paypal_body0:
    
# with paypal_body1:
    


st.subheader("Posisi Negara Indonesia dalam Pembagian Traffic pada Website Freelancer")
st.write("""
    Traffic pada website merupakan jumlah orang yang mengunjungi website, 
    membuka halaman website, dan durasi saat pengunjung membuka dan membaca halaman pada website. 
    Jadi, saat seseorang sedang mengunjungi website tertentu, 
    kunjungan serta semua link yang pengunjung klik dan follow akan direkam oleh domain website. 
    Nantinya angka-angka akan memberi ide tentang seberapa populernya website tersebut.
    \nPerubahan dalam metrics ini merupakan persentase perubahan dari bulan ke bulan dalam jumlah atau volume traffic.
    \nBerikut **posisi Indonesia** berdasarkan **Traffic** pada **Website Freelancer populer** skala **global** yang telah dikelompokkan berdasarkan negara di dunia dalam periode **April 2022 - Juni 2022 (3 bulan)**.

""")
st.write("Website Freelancer Lokal Populer")
metriclokal1kosong1, metriclokal1, metriclokal1kosong2,metriclokal1kosong3, metriclokal2,   metriclokal1kosong4= st.columns(6)
with metriclokal1:
    st.image('./assets/img/sribulancer.jpg', width=150)
    st.metric(label="sribulancer.com [Posisi 1]", value="96.51%", delta="28.02%")
with metriclokal2:
    st.image('./assets/img/freelancer.png', width=150)
    st.metric(label="freelancer.co.id [Posisi 1]", value="92.85%", delta="20.21%")

st.write("Website Freelancer Global Populer")
metricglobal1akosong1, metricglobal1a, metricglobal1akosong2, metricglobal2a, metricglobal1akosong3, metricglobal3a, metricglobal1akosong4 = st.columns(7)
metricglobal1bkosong1, metricglobal1b, metricglobal1bkosong2, metricglobal1bkosong3, metricglobal2b,metricglobal1bkosong4 = st.columns(6)
with metricglobal1a:
    st.image('./assets/img/99d.png', width=150)
    st.metric(label="99designs.com [Posisi 2]", value="16.14%", delta="32.98%")
with metricglobal2a:
    st.image('./assets/img/dribbble.png', width=150)
    st.metric(label="dribbble.com [Posisi 3]", value="3.66%", delta="9.03%")
with metricglobal3a:
    st.image('./assets/img/fiverr.png', width=150)
    st.metric(label="fiverr.com [Posisi 6]", value="2.83%", delta="1.6%")
with metricglobal1b:
    st.image('./assets/img/behance.png', width=150)
    st.metric(label="behance.net [Posisi 12]", value="2.22%", delta="13.05%")
with metricglobal2b:
    st.image('./assets/img/freelancer.png', width=150)
    st.metric(label="freelancer.com [Posisi 13]", value="1.61%", delta="21.51%")
st.write("Sumber data : https://pro.similarweb.com/")
st.write("List Website Freelancer pada metric di atas hampir semuanya memiliki metode pembayaran internasional dengan menggunakan **Paypal**")
st.write("""Berkaca dari posisi Indonesia yang cukup tinggi berdasarkan traffic tersebut, bisa dikatakan bahwa warga negara Indonesia 
banyak yang mengunjungi website Freelancer Online.""")


kolompertumbuhan0, kolompertumbuhan1 = st.columns(2)
tingkat_pekerja_paruh_waktu=pd.read_csv('./data/tingkat-pekerja-paruh-waktu.csv', delimiter=';')
tingkat_pekerja_paruh_waktu['tahun'] = tingkat_pekerja_paruh_waktu['tahun'].astype(str)
fig_tppw = px.line(tingkat_pekerja_paruh_waktu, x='tahun', y='tingkat_pekerja_paruh_waktu', title='Tingkat Pekerja Paruh Waktu di Indonesia (2016-2021)', markers=True)
with kolompertumbuhan0:
    st.write("""\nHal ini selaju dengan pertumbuhan Freelancer di Indonesia yang semakin meningkat.""")
st.plotly_chart(fig_tppw, use_container_width=True)
st.write("Kemudian, berikut jumlah website yang pernah menggunakan **Paypal**.")
metricwebkosong1, metricweb1, metricwebkosong2, metricwebkosong3, metricweb2, metricwebkosong4 = st.columns(6)
with metricweb1:
    st.image('./assets/img/worldwide.png', width=150)
    st.metric(label="Total Website Secara Global", value="7,246,542")
with metricweb2:
    st.image('./assets/img/Flag_of_Indonesia.png', width=150)
    st.metric(label="Website Lokal", value="6,703")
st.write("Sumber data : https://trends.builtwith.com/websitelist/PayPal")
st.write("Sumber data : https://trends.builtwith.com/websitelist/PayPal/Indonesia")


# Line Chart (Sales)
# freq = st.selectbox("Masukkan frekuensi", ('D', 'W', 'M', 'Q', 'Y'))

# sales = df[['Order Date', 'Sales']].set_index('Order Date').resample(freq).sum()


# cap1, cht1 = st.columns([1, 4])
# with cap1:
#     st.dataframe(sales)

# with cht1:
#     st.line_chart(sales)

# fig1, ax1 = plt.subplots(figsize=(10,10))
# sns.scatterplot(
#     data = df,
#     x='Sales',
#     y='Profit',
#     ax = ax1
# )
# st.pyplot(fig1)


# nama = st.text_input("Masukkan nama kamu")
# st.write("Hello ", nama)

# Image
# image = Image.open("meme-python.jpg")
# st.image(image, caption = "Ini meme")

#Penggunaan kolom
# st.title("Kolom")
# col1, col2, col3 = st.columns(3)
# with col1:
#     st.write(lorem.paragraph())
# with col2:
#     st.write(lorem.paragraph())
# with col3:
#     st.write(lorem.paragraph())

# angka = st.number_input("Masukkan angka", 0)
# if angka % 2 == 0:
#     st.success("Angka genap")
# else:
#     st.error("Angka ganjil")


# The quizz
# st.subheader("Quizz time!")

# stb.single_choice("At what angle is obtained the maximal distance?",
#                 options=["15", "30", "45", "60", "75"], answer_index=2)

# stb.true_or_false("On the moon, the horizontal distance is always larger than on the earth under the same initial velocity and angle.",
#                     answer=True)
st.subheader("Bagaimana reaksi netizen Indonesia di Twitter?")
st.write("Reaksi yang ditunjukkan oleh para netizen pun beragam.")
import plotly.graph_objects as go

rslt = pd.read_csv('./data/fix.csv')
fig = go.Figure(go.Bar(
            x=rslt.frequency,
            y=rslt.word,
            marker=dict(
                color='rgba(50, 171, 96, 0.6)',
                line=dict(
                    color='rgba(50, 171, 96, 1.0)',
                    width=1),
            ),
            orientation='h'))
fig.update_layout(title="Kata yang sering disebutkan di Twitter", yaxis=dict(autorange="reversed"))

fig1, fig2 = st.columns(2)
with fig1:
    st.image('./assets/img/wordcloud.png')
with fig2:
    st.plotly_chart(fig)
st.write("Pada grafik di atas, terdapat sebuah kata yang sempat menjadi trending di Twitter. Netizen di Indonesia menyatakan kekesalannya dengan menggunakan tagar #BlokirKominfo.\n")

st.subheader("Sekarang bagaimana?")
st.write("""Dengan data-data yang ada, dapat disimpulkan bahwa pemblokiran Steam dan Paypal akan 
berdampak pada industri game, e-sport dan bahkan para pekerja lepas yang menerima 
pembayaran upah melalui Paypal. 
\nMeskipun isu ini menuai pro dan kontra, menurut analis industri game Niko Partners, ditemukan setidaknya ada 
empat tujuan utama dari Penyelenggara Sistem Elektronik (PSE) Lingkup Privat (platform digital). 
Empat tujuan tersebut antara lain membangun sistem bagi seluruh Usaha Unit Makro (UMK) di Indonesia, 
menjaga ruang digital Indonesia, melindungi akses publik terhadap platform digital, dan 
menciptakan sistem yang adil antara PSE domestik dan asing, termasuk hal pemungutan pajak.
\nMeskipun Steam dan Paypal merupakan layanan PSE yang cukup esensial bagi developer game dan freelancer, 
kita hanya bisa menunggu PSE domestik maupun asing mendaftar kepada Kominfo sesuai dengan regulasi PSE.
\nPesan untuk para game developer serta freelancer Indonesia agar dapat tetap melanjutkan aktivitasnya, yaitu sebagai berikut.
\n1. Menggunakan platform lain selain Steam.
\nSalah satu platform game distribution yang bersifat open source yang cukup terkenal bagi para developer game yaitu itch.io. 
\n2. Mengganti metode pembayaran selain Paypal.
\nSalah satu metode pembayaran yang cukup digemari di dunia, yaitu Visa dan Mastercard. Anda dapat menggunakan Visa dan Mastercard sebagai alternatif pengganti Paypal.
\n3. Jangan gunakan VPN untuk mengakses Paypal.
\nHal ini dapat menyebabkan akun Paypal Anda terkunci karena sistem keamanan PayPal diketahui tidak mengizinkan penggunaan VPN, atau proxy apa pun untuk mengakses layanan mereka. 
Jika terdeteksi pakai VPN, Paypal akan menganggap akun yang digunakan sedang dipakai oleh orang lain serta dicurigai ada transaksi ilegal. 
Akibatnya akun bisa diblokir atau saldo ditahan. Selain itu, waspada terhadap VPN yang bersifat gratis karena rentan terkena serangan cyber atau virus komputer.""")


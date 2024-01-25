import matplotlib.pyplot as plt
import numpy as np 
import scipy.stats as stats
import seaborn as sns
import os
from warnings import filterwarnings

filterwarnings('ignore')
os.system('clear')
sns.set()


"""
JENIS ANALISIS STATISTIK :

1. ANALISIS DESKRIPTIF (DESCRIPTIVE STATISTICS)
- BERTUJUAN UTUK MENDAPATKAN RINGKASAN UMUM DARI DATA YANG DIMILIKI
- BISA DILAKUKAN DENGAN MEMBUAT VISUALISASI DATA ATAU TABEL RINGKASAN DATA
- TUJUAN UTAMA ADALAH MENDAPATKAN INSIGHTS DAN IDEAS (PEMAHAMAN & LANGKAH APA YANG HARUS DILAKUKAN)

2. ANALISIS INFERENSIAL (INFERENSIAL STATISTICS)
- BERTUJUAN UNTUK MEMBUAT KESIMPULAN DARI DATA YANG DIMILIKI APAKAH DATA MEWAKILI POPULASI YANG SESUNGGUHNYA
SEHINGGA KESIMPULANNYA BISA DIGENERALISIR
- TUJUAN UTAMANYA ADALAH CONCLUSIONS & PREDICTIONS
"""

# MENENTUKAN RATAAN 2 KELOMPOK :
rataan1 = 50 # TINGGI TANAMAN TANPA MENGGUNAKAN PUPUPK
rataan2 = 65 # TINGGI TANAMAN DENGAN MNGGUNAKAN PUPUK 

# MENENTUKAN STANDART DEVIASI (VARIASI) -- SAMA UNTUK 2 KELOMPOK :
sd = 5 # DENGAN STANDART DEVIASI 5 cm 

# UKURAN SAMPLE 2 KELOMPOK :
sample1 = 50 # BANYAKNYA 50 DATA 
sample2 = 40 # BANYAKKNYA 40 DATA

# GENERATE BILANGAN RANDOM :
data1 = np.random.randn(sample1)*sd + rataan1
data2 = np.random.randn(sample2)*sd + rataan2

# MENGGBUNGKAN SAMPLE SIZE (JUMLAH DATA) :
kelompokData = [sample1, sample2]

# MENCARI BATASAN TERKECIL & TERBESAR PADA KEDUA DATA :
batas = [np.min(np.hstack((data1, data2))), np.max(np.hstack((data1, data2)))]

# PLOT DISTRIBUSI DUA KELOMPOK (STATISTIK DSKRIPTIF) :
plt.figure(figsize=(7,5))

a = sns.distplot(data1, hist=False, label='Data 1')
a = sns.distplot(data2, hist=False, label='Data 2')

a.set(ylabel = 'Dencity', xlabel = 'Data', title = 'Plant Data')
plt.legend()

# PEGUJIAN DENGAN STATISTIK (STATISTIK INFERENSIAL)
fig,ax = plt.subplots(1,2, figsize=(8,5), dpi=200)

ax[0].violinplot(data1)
ax[0].plot(1+np.random.randn(sample1)/10, data1, 'o', color='green')
ax[0].set_ylim(batas)

ax[1].violinplot(data2)
ax[1].plot(1+np.random.randn(sample2)/10, data2, 'o', color='blue')
ax[1].set_ylim(batas)


# MELAKUKAN UJI t-test DI JUDUL
t,p = stats.ttest_ind(data1,data2)

# MENCETAK HASIL t-test DI JUDUL
sigtxt = (' ', 'TIDAK')
plt.title('Dua Kelompok {} berbeda secara signifikan! t({})={}, p={}'.format(sigtxt[int(p>.05)],sum(kelompokData)-2,np.round(t,2),np.round(p,6)))

plt.show()
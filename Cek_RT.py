import pandas as pd
import re
from collections import Counter

data = pd.read_excel('Prabowo_Subianto.xlsx')
user_RT = data['content']

# Menggunakan ekspresi reguler untuk mengekstrak nama pengguna
usernames = re.findall(r'RT @(\w+):', ' '.join(user_RT))  # Menggabungkan semua teks dalam satu string

# Menghitung frekuensi kemunculan setiap nama pengguna
username_counts = Counter(usernames)

# Simpan hasil perhitungan ke dalam DataFrame
result_df = pd.DataFrame({'Username': list(username_counts.keys()), 'Count': list(username_counts.values())})

# Simpan DataFrame ke dalam file Excel
result_df.to_excel('hasil_perhitungan.xlsx', index=False)

print("Hasil perhitungan telah disimpan dalam file 'hasil_perhitungan.xlsx'")

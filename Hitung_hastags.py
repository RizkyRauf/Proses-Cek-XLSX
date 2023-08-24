from collections import Counter
import pandas as pd

# Baca data dari Excel
data = pd.read_excel('test.xlsx')
hashtags = data['hashtags'].tolist()

# Menggabungkan semua hashtags menjadi satu list dan menghitung frekuensinya
hashtag_counts = Counter()
for sublist in hashtags:
    if isinstance(sublist, str):  # Periksa apakah nilai adalah string
        tags = sublist.split(', ')
        hashtag_counts.update(tags)

# Membuat DataFrame dari hasil perhitungan
result_df = pd.DataFrame({'Hashtag': list(hashtag_counts.keys()), 'Count': list(hashtag_counts.values())})

# Simpan DataFrame ke dalam file Excel
result_df.to_excel('hasil_perhitungan_hashtags.xlsx', index=False)

print("Hasil perhitungan hashtags telah disimpan dalam file 'hasil_perhitungan_hashtags.xlsx'")

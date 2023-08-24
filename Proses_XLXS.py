import pandas as pd
import datetime
import time

ANIES_FILE = "anies.xlsx"
KEYWORD_FILE = "keyanies.xlsx"
HASHTAG_FILE = "keyhastag.xlsx"
USERNAME_COLUMN = 'username'
CONTENT_COLUMN = 'content'
HASHTAGS_COLUMN = 'hashtags'
SENTIMENT_COLUMN = 'sentiment'
KEY_FOUND_USERNAME_COLUMN = 'key_found_username'
KEY_FOUND_CONTENT_COLUMN = 'key_found_content'
KEY_FOUND_HASHTAGS_COLUMN = 'key_found_hastags'

def main ():
    start_time = time.time()  # Catat waktu awal pemrosesan
    print("Memulai Proses pada", datetime.datetime.now())

    anies_df = pd.read_excel(ANIES_FILE)
    keyword_df = pd.read_excel(KEYWORD_FILE)
    hastag_df = pd.read_excel(HASHTAG_FILE)

    process_username(anies_df, keyword_df)
    process_content(anies_df, keyword_df)
    process_hastags(anies_df, hastag_df)
    update_sentiment(anies_df)

    # Menghitung jumlah data dalam DataFrame
    total_data_count = len(anies_df)

    # Menghitung jumlah data yang memenuhi kriteria
    key_found_count = anies_df[KEY_FOUND_USERNAME_COLUMN].sum() + anies_df[KEY_FOUND_CONTENT_COLUMN].sum() + anies_df[KEY_FOUND_HASHTAGS_COLUMN].sum()

    anies_df.to_excel("anies_processed.xlsx", index=False)

    end_time = time.time()  # Catat waktu akhir pemrosesan
    elapsed_time = end_time - start_time  # Hitung selisih waktu untuk melihat berapa lama pemrosesan berlangsung

    print("Pemrosesan sentiment selesai.")
    print("Waktu yang diperlukan:", elapsed_time, "detik")  # Cetak waktu yang diperlukan
    print("Jumlah total data:", total_data_count)
    print("Jumlah data yang memenuhi kriteria:", key_found_count)

def process_content(anies_df, keyword_df):
    anies_content = anies_df[CONTENT_COLUMN]
    keywords = keyword_df['key'].apply(lambda x: f"RT @{x}:")

    anies_df[KEY_FOUND_CONTENT_COLUMN] = anies_content.apply(lambda x: any(keyword in str(x) for keyword in keywords))

    print("Pemrosesan cek content selesai.")

def process_username(anies_df, keyword_df):
    anies_username = anies_df[USERNAME_COLUMN]
    keywords = keyword_df['key']

    anies_df[KEY_FOUND_USERNAME_COLUMN] = anies_username.apply(lambda x: any(keyword in str(x) for keyword in keywords) if pd.notnull(x) else False)

    print("Pemrosesan cek username selesai.")

def process_hastags(anies_df, hastag_df):
    anies_content = anies_df[HASHTAGS_COLUMN]
    hastags = hastag_df['key_hastags']

    anies_df[KEY_FOUND_HASHTAGS_COLUMN] = anies_content.apply(lambda x: any(keyword in str(x) for keyword in hastags) if pd.notnull(x) else False)

    print("Pemrosesan cek content selesai.")

def update_sentiment(anies_df):
    anies_df[SENTIMENT_COLUMN] = anies_df.apply(
        lambda row: 'positive' if row[KEY_FOUND_USERNAME_COLUMN] or row[KEY_FOUND_HASHTAGS_COLUMN] or row[KEY_FOUND_HASHTAGS_COLUMN] else row[SENTIMENT_COLUMN],
        axis=1
    )

    print("Pemrosesan sentiment selesai.")

if __name__ == "__main__":
    main()
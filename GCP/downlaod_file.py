from google.cloud import storage

client = storage.Client()

bucket = client.bucket("brijesh-bucket-1")

blob = bucket.blob("data.csv")

blob.download_to_filename(r"C:\Users\brije\Downloads\data.csv")

print("Downloaded")
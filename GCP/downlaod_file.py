from google.cloud import storage

client = storage.Client()

bucket = client.bucket("swapnil-bucket-1")

blob = bucket.blob("data.csv")

blob.download_to_filename(r"C:\Users\swap\Downloads\data.csv")

print("Downloaded")

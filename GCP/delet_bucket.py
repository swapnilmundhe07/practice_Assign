# from google.cloud import storage

## deelete all files 
from google.cloud import storage

client = storage.Client()

bucket = client.bucket("swapnil-bucket-2")

for blob in bucket.list_blobs():
    blob.delete()

print("All files deleted.")


client = storage.Client()

bucket = client.bucket("swapnil-bucket-2")

bucket.delete()

print("Bucket deleted.")



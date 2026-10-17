from google.cloud import storage

client = storage.Client()

bucket = client.bucket('swapnil-bucket-1')

for blob in bucket.list_blobs():
    print(blob.name)

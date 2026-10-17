from google.cloud import storage

client = storage.Client()

bucket = client.bucket('brijesh-bucket-1')

for blob in bucket.list_blobs():
    print(blob.name)
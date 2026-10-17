from google.cloud import storage

client = storage.Client()

bucket = client.bucket("brijesh-bucket-1")

blob = bucket.blob("os_repair.txt")

blob.delete()

print("Deleted")
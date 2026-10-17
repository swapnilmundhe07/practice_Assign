from google.cloud import storage

client = storage.Client()

bucket = client.bucket("swapnil-bucket-1")

blob = bucket.blob("os_repair.txt")

blob.delete()

print("Deleted")

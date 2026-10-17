# upload file in your selected bucket of gcp
from google.cloud import storage
client = storage.Client()
bucket = client.bucket("brijesh-bucket-1")

blob = bucket.blob('new_doc.txt')
blob.upload_from_filename(r"C:\Users\brije\OneDrive\Desktop\new_doc.txt")


print("file uploaded")
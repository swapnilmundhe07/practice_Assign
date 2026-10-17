# create bucket using py
from google.cloud import storage

# just use project id dont use project name
client = storage.Client(project ='big-genre-504205-j0' )

bucket = client.create_bucket(
    "brijesh-bucket-2",
    location="US-EAST1"
)

print(f"Bucket : {bucket.name} created.")


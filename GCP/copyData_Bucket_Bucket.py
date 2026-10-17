# copy data from bucket-1 to bucket-2

from google.cloud import storage

client = storage.Client(project ='big-genre-504205-j0')

sources_bucket = client.bucket("swapnil-bucket-1")
dest_bucket = client.bucket("swapnil-bucket-2")

blob = sources_bucket.blob("new_doc.txt")

sources_bucket.copy_blob(
    blob,
    dest_bucket,
    new_name="new_doc2.txt"
)

# add this to move there is no direct MOVE() api for gcloude b-b
# Delete the file from the source bucket
blob.delete()

print(f"Successfully copied!")



## to move 

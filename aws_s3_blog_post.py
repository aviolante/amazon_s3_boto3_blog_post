import boto3

"""
medium blog post code to do basic boto3 commands to access s3, view buckets, view objects,
upload files from local, download files to local, delete objects, and delete buckets
"""

# connect to client / credentials
s3_client = boto3.resource('s3')
print(s3_client)
# s3.ServiceResource()


# create bucket and set bucket object
andre_bucket = s3_client.create_bucket(Bucket='andre.gets.buckets')

# view all bucket names
for bucket in s3_client.buckets.all():
    print(bucket.name)


# add objects to a specific bucket
andre_bucket.put_object(Key='andre/added/a/new/object1')
andre_bucket.put_object(Key='andre/added/a/new/object2')
andre_bucket.put_object(Key='andre/added/a/new/object3')

# view newly uploaded data object
for obj in andre_bucket.objects.all():
    print(obj.key)

# andre/added/a/new/object1
# andre/added/a/new/object2
# andre/added/a/new/object3


# upload local csv to a specific s3 bucket
local_file_path = '/Users/andreviolante/Desktop/data.csv'
key_object = 'andre/added/a/new/object/data.csv'

andre_bucket.upload_file(local_file_path, key_object)

# view newly uploaded data object
for obj in andre_bucket.objects.all():
    print(obj.key)

# andre/added/a/new/object/data.csv
# andre/added/a/new/object1
# andre/added/a/new/object2
# andre/added/a/new/object3


# download an s3 file to local machine
filename = 'downloaded_s3_data.csv'
andre_bucket.download_file(key_object, filename)


# delete a specific object
andre_bucket.Object('andre/added/a/new/object2').delete()

for obj in andre_bucket.objects.all():
    print(obj.key)


# delete the rest of objects in a bucket
andre_bucket.objects.delete()

for obj in andre_bucket.objects.all():
    print(obj.key)


# delete a specific bucket
andre_bucket.delete()

# view all bucket names again
for bucket in s3_client.buckets.all():
    print(bucket.name)

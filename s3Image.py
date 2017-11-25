#!/usr/bin/env python
from datetime import datetime
from time import sleep
import picamera
import os
import tinys3

# S3 Properties
access_key_id = 'A*****Q'  # your access key id here
secret_access_key = 'On*****/g'  # your secret access key here
bucket_name = 'b****r'  # bucket name here

debug = True

# image settings
image_width = 640  # horizontal resolution
image_height = 480  # vertical_res
file_extension = '.jpg'  # file extension
file_name = 'test'  # file name
photo_interval = 60  # Interval between photo (in seconds)
image_folder = 'images'  # folder name

# camera setup
camera = picamera.PiCamera()
camera.resolution = (image_width, image_height)
camera.awb_mode = 'auto'  # ['awb_mode']

# verify image folder exists and create if it does not
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# camera warm-up time
sleep(2)

# endlessly capture images awwyiss
while True:
    # Build filename string
    filepath = image_folder + '/' + file_name + file_extension

    if debug == True:
        print 'Taking photo and saving to path ' + filepath

    # Take Photo
    camera.capture(filepath)

    if debug == True:
        print 'Uploading ' + filepath + ' to s3'

    # Upload to S3
    conn = tinys3.Connection(access_key_id, secret_access_key)
    f = open(filepath, 'rb')
    conn.upload(filepath, f, bucket_name,
                headers={
                    'x-amz-meta-cache-control': 'max-age=60'
                })

    print 'Image Uploaded to s3 '
    # Cleanup
    if os.path.exists(filepath):
        os.remove(filepath)

    # sleep
    sleep(photo_interval)



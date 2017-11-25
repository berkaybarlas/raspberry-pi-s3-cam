# Raspberry Pi Camera Amazon S3 Uploader

## Requirements
- Raspberry Pi + Camera + Internet Connection

## Initial Setup
- Ensure Raspberry Pi Camera has been enabled:
  - Running `sudo raspi-config` will get you into the settings to enable

- Install the `python-picamera` library:
  ```
  sudo apt-get update
  sudo apt-get install python-picamera
  ```

- Install `tinys3` library: `pip install tinys3`

- Change Aws Properties with yours

## Running 
`python s3Image.py`

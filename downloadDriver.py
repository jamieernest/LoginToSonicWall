import requests
import wget
import zipfile
import os

# get the latest chrome driver version number
url = 'https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_STABLE'
response = requests.get(url)
version_number = response.text

# build the donwload url
download_url = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/" + version_number +"/win64/chromedriver-win64.zip"

# download the zip file using the url built above
latest_driver_zip = wget.download(download_url,'chromedriver.zip')

# extract the zip file
with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
    zip_ref.extractall() # you can specify the destination folder path here
# delete the zip file downloaded above
os.remove(latest_driver_zip)
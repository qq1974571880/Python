import exifread
path = "C:\\Github\\Python\\TestData\\test2.jpg"
f = open(path,'rb')
# GPS GPSTimeStamp
# GPS GPSDate
# Image GPSInfo
# Image ExifOffset
# Image UserComment
# EXIF DateTimeOriginal
tags = exifread.process_file(f)
print(tags)
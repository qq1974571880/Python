import exifread
path = "C:\\Github\\Python\\TestData\\test2.jpg"
# path = "C:\\Github\\91Result\\推女神于姬MM扮兔女郎蕾丝23p\\1.jpg"
f = open(path,'rb')
# GPS GPSTimeStamp
# GPS GPSDate
# Image GPSInfo
# Image ExifOffset
# Image UserComment
# EXIF DateTimeOriginal
tags = exifread.process_file(f)
print(tags)
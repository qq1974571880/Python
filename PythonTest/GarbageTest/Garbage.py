from aip import AipImageClassify
APP_ID = '17533824'
API_KEY = 'QO9fpR8uMVot6TyyhRnnGFQF'
SECRET_KEY = 'FuKHRSfz7Sw7eEey2N1KSIsxk1aRWTvt'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


picRootPath = "C:\\Github\\Python\\TestData\\"
picName = "test3.jpg"
image = get_file_content(picRootPath + picName)
# print(picRootPath + picName)
print(client.advancedGeneral(image))

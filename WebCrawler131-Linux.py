import urllib3
import requests
from bs4 import BeautifulSoup
import os

http = urllib3.PoolManager()
headers = {
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name',
        "Referer": "http://www.mm131.net/xinggan/5508.html"}

# Get name url list. Because the web has these classify.
base_url  = "http://www.mm131.net"
url0 = base_url + "/xinggan"
url1 = base_url + "/qingchun"
url2 = base_url + "/xiaohua"
url3 = base_url + "/chemo"
url4 = base_url + "/qipao"
url5 = base_url + "/mingxing"
url_list = [url0, url1, url2, url3, url4, url5]
# Set download path & output file path.
download_path = "/home/poppinzhang/github/WebCrawler131/mm131"
output_path = download_path + "/output.txt"
# If don't need output file, set False.
need_output_file = True
output_list = []

def getPicName(page_num):
    "Get the name of picture group for 'page_num'"
    for name_url in url_list:
        # Get the real name web page url.
        real_name_url = name_url + '/' + str(page_num) + ".html"
        response = requests.get(real_name_url, headers = headers)
        if response.status_code == 200:
            response.encoding = "gbk"
            html = BeautifulSoup(response.text, "html.parser")
            name = html.find('img').get('alt')[:-4]
            print(str(page_num) + ": " + name)
            if need_output_file:
                output_list.append(str(page_num) + ": " + name + "\n")
            return name
    return ""

def getPic(pic_name, page_num):
    "Get & save pictures to local."
    pic_id = 1
    while True:
        pic_url = "https://img1.mmmw.net/pic/" + str(page_num) + '/' + str(pic_id) + ".jpg"
        response = http.request("get", pic_url, headers = headers)
        if response.status != 200:
            return
        if not os.path.exists(download_path):
            os.mkdir(download_path)
        pic_dir_path = download_path + "/" + pic_name
        if not os.path.exists(pic_dir_path):
            os.mkdir(pic_dir_path)
        pic_path = pic_dir_path + "/" + str(pic_id) + ".jpg"
        with open(pic_path, 'wb') as pic:
            pic.write(response.data)
            pic.close()
        pic_id += 1

def main():
    print("When you use the program, you need input web page number.")
    print("If you need all pictures, set begin:0 & end:as big as you like.")
    print("The page number is 5338 in url:https://www.mm131.net/xinggan/5338.html")
    print("If you want to change the download path. You should change the code.")
    print("Have fun~")
    print("----------------------------------------------------------------------")
    # Need get the begin page & end page.
    begin = int(input("Begin page:"))
    end = int(input("End page:"))
    while begin <= end:
        pic_name = getPicName(begin)
        # Can't get the name of picture group.
        # Means the picture group is not exist.
        if pic_name == '':
            begin += 1
            continue
        getPic(pic_name, begin)
        begin += 1
    # Print output info to file.
    if need_output_file:
        with open(output_path, 'ta') as output:
            output.writelines(output_list)
    print("Finished! Have fun~")

if __name__ == '__main__':
    main()

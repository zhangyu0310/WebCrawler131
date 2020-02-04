# WebCrawler131
> A web crawler for mm131.net

## Features
The script can find name of picture group & download picture groups automatically.
The script can assign download path & make dir for all picture groups. 

## Usage
1. Run the python script.
2. Input begin page number & end page number.
3. Wait for download...
4. finished.

## Attention
1. The page number is web id of picture groups.
    like: '5338' in url:```https://www.mm131.net/xinggan/5338.html```
2. If you need all pictures, set begin:0 & end:as big as you like.
3. You can change download path to modify 'download_path'.
    Default path is ```C:\User\Public\Pictures\mm131```
4. The script save output info default, if you not need, modify ```need_output_file = False```
    Default path is ```[download_path]\output.txt```
5. Exe of the script can't modify download path & output file switch.

Have fun.

Thanks for mm131.net
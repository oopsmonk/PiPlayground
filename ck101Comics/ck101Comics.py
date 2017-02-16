#!/usr/bin/env python
import sys,os
import time
import random
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def parseFilelist(filepath):
    start_parsing = datetime.now()
    if not os.path.isfile(filepath):
        print "\'{}\' is not file or not exist...".format(filepath)
        sys.exit()

    with open(filepath) as f:
        volList = f.readlines()

    for volInfo in volList:
        volInfo = volInfo.strip('\n')
        print "parsing {}".format(volInfo)
        volInfoParams = volInfo.split(',')
        volStr = volInfoParams[0].strip()
        if volStr.startswith('#'):
            print "ignore {}".format(volInfo)
            continue

        if len(volInfoParams) == 4:
            ck101ComicDownloader(volInfoParams[3].strip(), volInfoParams[0].strip(), int(volInfoParams[1]), int(volInfoParams[2]))
        else:
            print "invalid line: {}".format(volInfo)
            continue

    print "Total time : {}".format(datetime.now()-start_parsing)

def ck101ComicDownloader(target_dir, volId, start, end):
    start_downloader = datetime.now()
    for index in range(start,end+1):
        imgUrl = "http://comic.ck101.com/vols/{}/{}/3".format(volId, index)
        # print imgUrl
        sleepTime = random.randint(5,30)
        print "Downloading {}[{}/{}], waite {}".format(target_dir, index, end, sleepTime)

        # parsing html 
        res = requests.get(imgUrl).text
        soup = BeautifulSoup(res, "lxml")
        picUrl = soup.find(id='comicPic')['src']

        img_data = requests.get(picUrl).content
        filePath = '{}/{:03}.jpg'.format(target_dir, index)
        # check dir 
        if not os.path.isdir(target_dir):
            os.makedirs(target_dir)

        with open(filePath, 'wb') as handler:
            handler.write(img_data)

        # waite for a moment....
        time.sleep(sleepTime)

    print "Downloader spent: {}".format(datetime.now()-start_downloader)

def usage():
    print "usage: "
    print "{} vol_id start_index end_index save_path".format(os.path.basename(__file__))
    print "{} download-list".format(os.path.basename(__file__))
    print "download-list format: vol_id, start_index, end_index, save_path"

if __name__ == "__main__":

    params = len(sys.argv)
    if params == 5:
        ck101ComicDownloader(sys.argv[4], sys.argv[1], int(sys.argv[2]), int(sys.argv[3])) 
    elif params == 2:
        print "parsing file..."
        parseFilelist(sys.argv[1])
    else:
        usage()
        sys.exit()


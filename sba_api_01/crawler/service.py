import sys
sys.path.insert(0,'/Users/kuku/Desktop/anaconda')

from urllib.request import urlopen
from bs4 import BeautifulSoup

class Service:
    def __init__(self):
        pass

    def bugs_music(self):
        pass

    def naver_movie(self):
        pass

    def naver_cartoon(self, url):
        myparser = 'html.parser' # html.parser : 간단한 HTML과 XHTML 구문 분석기. 표준 라이브러리
        response = urlopen(url)
        soup = BeautifulSoup(response, myparser)
        print(type(soup))

    # 요일별 폴더 생성
    def create_foler_weekend(self):
        weekday_dict = {'mon': '월요일', 'tue': '화요일', 'wed': '수요일', 'thu': '목요일', 'fri': '금요일', 'sat': '토요일', 'sun': '일요일'}

        # shutil : shell utility : 고수준 파일 연산. 표준 라이브러리
        import os, shutil
        myfolder = 'd:\\imsi\\' # 유닉스 기반은 '/'이 구분자

        try:
            if not os.path.exists(myfolder):
                os.mkdir(myfolder)

            for mydir in weekday_dict.values():
                mypath = myfolder + mydir

                if os.path.exists(mypath):
                    # rmtree : remove tree
                    shutil.rmtree(mypath)

                os.mkdir(mypath)

        except FileExistsError as err:
            print(err)

    # 각 이미지를 저장해주는 함수
    def saveFile(mysrc, myweekday, mytitle):
        image_file = urlopen(mysrc)
    filename = myfolder + weekday_dict[myweekday] + '\\' + mytitle + '.jpg'
    # print(mysrc)
    # print(filename)

    myfile = open(filename, mode='wb') # wb : write binary
    myfile.write(image_file.read()) # 바이트 형태로 저장
    myfile.close()


mytarget = soup.find_all('div', attrs={'class': 'thumb'})
print(len(mytarget))

mylist = []  # 데이터를 저장할 리스트

for abcd in mytarget:
    myhref = abcd.find('a').attrs['href']
    myhref = myhref.replace('/webtoon/list.nhn?', '')
    result = myhref.split('&')
    # print(myhref)
    # print(result)
    mytitleid = result[0].split('=')[1]
    myweekday = result[1].split('=')[1]
    # print(mytitleid)
    # print(myweekday)

    imgtag = abcd.find('img')
    mytitle = imgtag.attrs['title'].strip()
    mytitle = mytitle.replace('?','').replace(':','')
    # print(mytitle)

    mysrc = imgtag.attrs['src']
    # print(mysrc)

    saveFile(mysrc,myweekday, mytitle)

    # break

    sublist = []
    sublist.append(mytitleid)
    sublist.append(myweekday)
    sublist.append(mytitle)
    sublist.append(mysrc)
    mylist.append(sublist)
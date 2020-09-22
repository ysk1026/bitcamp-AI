from bs4 import BeautifulSoup
from urllib.request import urlopen
import os, shutil
import sys
sys.path.insert(0, '/Users/youngseonkim/Documents/SbaProjects')
from crawler.entity import Entity
from pandas import DataFrame
import pandas as pd

class Service:
    def __init__(self):
        self.entity = Entity()
        pass
    
    def bugs_music(self):
        pass
    
    def naver_movie(self):
        pass
    
    @staticmethod
    def get_url(url):
        myparser = 'html.parser'
        response = urlopen(url)
        soup = BeautifulSoup(response, myparser)
        print(type(soup))
    
    @staticmethod
    def save_webtoon_file(mysrc, myweekday, mytitle):
        weekday_dict = {'mon':'월요일', 'tue':'화요일', 'wed':'수요일', 'thu':'목요일', 'fri':'금요일', 'sat':'토요일', 'sun':'일요일'}
        myfolder = 'Users\\youngseonkim\\Documents\\imsi\\'
        image_file = urlopen(mysrc)
        filename = myfolder + weekday_dict[myweekday] + '\\' + mytitle + '.jpg'
        myfile = open(filename, mode='wb')
        myfile.write(image_file.read()) # 바이트 형태로 저장
        myfile.close()

    
        try :
            if not os.path.exists(myfolder):
                os.mkdir(myfolder)

            for mydir in weekday_dict.values():
                mypath = myfolder + mydir

                if os.path.exists(mypath):
                    # rmtree : remove tree
                    shutil.rmtree(mypath)

                os.mkdir(mypath)

        except FileExistsError as err :
            print(err)

    @staticmethod
    def save_webtoon_csv(url):
        myparser = 'html.parser'
        response = urlopen(url)
        soup = BeautifulSoup(response, myparser)
        mytarget = soup.find_all('div', attrs={'class':'thumb'})
        mylist = []
        for abcd in mytarget:
            myhref = abcd.find('a').attrs['href']
            myhref = myhref.replace('/webtoon/list.nhn?', '')
            result = myhref.split('&')
            print('My href : %s, Result : %s' %(myhref, result))
            mytitleid = result[0].split('=')[1]
            myweekday = result[1].split('=')[1]
            print('\nMy title id: %s, My weekday : %s' %(mytitleid, myweekday))
            
            imgtag = abcd.find('img')
            mytitle = imgtag.attrs['title'].strip()
            mytitle = mytitle.replace('?', '').replace(':', '')
            print('\nMy title : %s' %mytitle)
            mysrc = imgtag.attrs['src']
            print('\nMy source : %s' %mysrc)
            
            save_webtoon_file(mysrc, myweekday, mytitle)
            
            sublist = []
            sublist.append(mytitleid)
            sublist.append(myweekday)
            sublist.append(mytitle)
            sublist.append(mysrc)
            mylist.append(sublist)
        
        mycolumns = ['타이틀번호', '요일', '제목', '링크']
        myframe = DataFrame(mylist, columns = mycolumns)
        filename = 'cartoon.csv'
        
        myframe.to_csv(filename, encoding = 'utf-8', index=False)
        print(filename + ' 파일로 저장됨')
    
    @staticmethod
    def save_movie_file(movie_src, movie_name):
        myfolder = 'Users\\youngseonkim\\Documents\\movieset'
        image_open = urlopen(movie_src)
        filename = myfolder + movie_name + '.jpg'
        myfile = open(filename, mode='wb')
        myfile.write(image_open.read())
        myfile.close()
        
        try:
            if not os.path.exists(myfolder):
                os.mkdir(myfolder)
        
        except FileExistsError as err:
            print(err)
            
    @staticmethod
    def save_movie_csv(url):
        myurl = url
        response = urlopen(myurl)
        soup = BeautifulSoup(response, 'html.parser')
        mytarget_title = soup.findAll('div', attrs={'class' : 'thumb'})
        mytarget_star = soup.findAll('dd', attrs={'class':'star'})
        mylist0 = []
        mylist1 = []
        
        for title in mytarget_title:
            movie_name = title.find('img').attrs['alt']
            movie_name = movie_name.replace('?','').replace(':','')
            movie_src_full = title.find('img').attrs('src')
            movie_src = movie_src_full.replace('?type=m99_141_2', '')
            sublist = []
            
            sublist.append(movie_name)
            sublist.append(movie_src)
            
            mylist0.append(sublist)
            
            save_movie_file(movie_src, movie_name)

        for star in mytarget_star:
            myhref0 = star.find('a')
            movie_point_full = myhref0.find('span', attrs={'class' : 'num'})
            movie_point = movie_point_full.contents
            
            movie_reserve_full = star.find('div', attrs={'class' : 'star_t1 b_star'})
            
            try:
                movie_reserve = movie_reserve_full.find('span', attrs={'class':'num'}).contents
                
            except AttributeError as err:
                movie_reserve = '미개봉'
                
            sublist = []
            
            sublist.append(movie_point)
            sublist.append(movie_reserve)
            
            mylist1.append(sublist)
    
        mycolumns0 = ['제목', '스크린샷']
        mycolumns1 = ['별점', '예매율']
        myindex = range(0, len(mylist0))
        myframe0 = DataFrame(mylist0, index=myindex, columns=mycolumns0)
        myframe1 = DataFrame(mylist1, index=myindex, columns=mycolumns1)
        
        myframe = pd.concat([myframe0, myframe1], axis = 1)
        filename = '0921_naver_movie_ranking.csv'
        myframe.to_csv(filename, encoding ='utf-8')
        print(filename + ' 파일로 저장됨')
        
                    
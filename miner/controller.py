import nltk
import sys
sys.path.insert(0, '/Users/youngseonkim/Documents/SbaProjects')
from miner.entity import Entity
from miner.service import SamsungService
class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = SamsungService()
        
    def download_dictionary(self):
        nltk.download('all')
    def data_analysis(self):
        entity = Entity()
        service = SamsungService()
        entity.fname = 'kr-Report_2018.txt'
        entity.context = './data/'
        service.extract_token(entity)
        service.extract_hanguel()
        service.conversion_token()
        service.compound_noun()
        entity.fname = 'stopwords.txt'
        service.extract_stopword(entity)
        service.filtering_text_with_stopword()
        service.frequent_text()
        entity.fname = 'D2Coding.ttf'
        service.draw_wordcloud(entity)
if __name__ == '__main__':
    def print_menu():
        print('0. Exit')
        print('1. 사전 다운로드')
        print('2. 삼성 전략보고서 분석')
        return input('Select Menu\n')
    app = Controller()
    while 1:
        menu = print_menu()
        if menu == '1':
            app.download_dictionary()
        if menu == '2':
            app.data_analysis()
        elif menu == '0':
            break
    filename = '문재인대통령신년사.txt'
    app.service.get_data(filename)
    app.service.save_asfile()
    
import sys
sys.path.insert(0, '/Users/youngseonkim/Documents/SbaProjects')
from crawler.entity import Entity
from crawler.service import Service

class Controll:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()
    

if __name__ == '__main__':
    ctrl = Controll()
    service = ctrl.service
    comic_url = 'https://comic.naver.com/webtoon/weekday.nhn'
    movie_url = 'https://movie.naver.com/movie/running/current.nhn'
    service.save_webtoon_csv(comic_url)
    service.save_movie_csv(movie_url)
    
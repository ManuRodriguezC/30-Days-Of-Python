from models.movies import Movie as MovieModel
from schemas.movie import Movie


class MovieService():
    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        return self.db.query(MovieModel).all()

    def get_movie(self, id):
        return self.db.query(MovieModel).filter(MovieModel.id == id).first()
    
    def get_category(self, category):
        return self.db.query(MovieModel).filter(MovieModel.category == category).all()
    
    def create_movie(self, movie: Movie) -> None:
        new = MovieModel(**movie.dict())
        self.db.add(new)
        self.db.commit()

    def update_movie(self, id: int, data: Movie) -> None:
        movie = self.get_movie(id)
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating
        movie.category = data.category
        self.db.commit()

    def delete_movie(self, id) -> None:
        movie = self.get_movie(id)
        self.db.delete(movie)
        self.db.commit()
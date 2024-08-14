from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Select, select
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from movie_api import API_DATA
import json

# Init the APPs
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Bass(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///NewMovies.db"
db = SQLAlchemy(model_class=Bass)
db.init_app(app)


# CREATE TABLE
class Movies_Table(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(1024), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(255), nullable=True)
    img_url: Mapped[str] = mapped_column(String(255), nullable=False)

    
    def __repr__(self):
        return f'<Movie title {self.title}>'
 
# Form for editing the rating and review    
class Movie_Edit(FlaskForm):
    rating = StringField(label='Rating')
    review = StringField(label='Review')
    submit = SubmitField(label='Submit')

# Form for searching the movies    
class Movie_Add(FlaskForm):
    title = StringField(label='Title')
    submit = SubmitField(label='Submit')
    


# Creating table schema in the database.
with app.app_context():
    db.create_all() 
    
# Function to add the movie to DB
def Add_to_database(movie):    
    with app.app_context():
        movie_detail = Movies_Table(title=movie['title'], year=movie['year'],description=movie['description'],
                                    rating = movie['rating'], ranking = movie['ranking'],review = movie['review'],img_url = movie['img_url'])
        db.session.add(movie_detail)
        db.session.commit()
 
#Function to update and change the ratings        
def Update_Rating(Movie_ID, new_rating, new_review):
    with app.app_context():
        value_to_update = db.session.execute(db.select(Movies_Table).where(Movies_Table.id == Movie_ID)).scalar()
        value_to_update.rating = new_rating
        value_to_update.review = new_review
        db.session.commit()
        

# Home page
@app.route("/")
def home():
    result = db.session.execute(db.select(Movies_Table).order_by(Movies_Table.review.desc()))
    all_movies = result.scalars().all()
    return render_template("index.html", all_movies = all_movies)

# Movie Search page
@app.route('/add_Movies', methods=['POST', 'GET'])
def add_movies():
    form = Movie_Add()
    User_Search = form.title.data
    if form.validate_on_submit():
        movie_data = API_DATA(User_Search)
        return render_template('select.html', datas = movie_data)  
    return render_template('add.html', form = form)


@app.route('/edit', methods = ['POST', 'GET'])
def edit():
    form = Movie_Edit()
    new_rating = form.rating.data
    new_review = form.review.data
    id = request.args.get('id')
    if form.validate_on_submit():
        Update_Rating(id, new_rating, new_review)
        return redirect(url_for('home'))
    return render_template('edit.html', form = form)

@app.route('/delete', methods = ['POST', 'GET'])
def delete():
    movie_id = request.args.get('id')
    book_to_delete = db.session.execute(db.select(Movies_Table).where(Movies_Table.id == movie_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/find', methods = ['POST', 'GET'])
def find_movie():
    movie_id = request.args.get('id')
    user_search = request.args.get('movie')
    movie_data = API_DATA(user_search)
    for movie in movie_data:
        print(movie['id'])
        print(movie_id)
        print(type(movie['id']))
        print(type(movie_id))
        
        if str(movie['id']) == movie_id:
            imgage_URL = 'https://image.tmdb.org/t/p/w500'
            img_url = f"{imgage_URL}{movie['poster_path']}"
            with app.app_context():
                movie_detail = Movies_Table(title=movie['original_title'], year=movie['release_date'],description=movie['overview'],
                                            img_url = img_url)
                db.session.add(movie_detail)
                db.session.commit()
                return redirect(url_for('edit', id = movie_detail.id))
    return redirect(url_for('home'))


# Running the code as script
if __name__ == '__main__':
    app.run(debug=True)

from flask import render_template, request, redirect, flash
from models import Movies, db, app
import requests
import os

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

with app.app_context():
    db.create_all()

code = os.getenv("KEY")

@app.route('/')
def main():
    movies = db.session.query(Movies).order_by(Movies.rating.asc()).all()
    return render_template('index.html', movies=movies)

@app.route('/search', methods=['POST', 'GET'])
def search():

    if request.method == 'POST':
        type = request.form.get('type')

        if type == 'search':
            title = request.form.get('title')
            url = f"https://api.themoviedb.org/3/search/movie?query={title}"
            headers = {
                "accept": "application/json",
                "Authorization": "Bearer " + os.getenv('AUTH_TOKEN')
            }
            response = requests.get(url, headers=headers)
            data = response.json()
            movies = data['results']
            start = 'https://image.tmdb.org/t/p/w1280/'
            for movie in movies:
                if movie['poster_path'] != None:
                    movie['img_src'] = start + movie['poster_path']
            header = 'Select a Movie'
            comment = 'Select a movie from the list below by clicking on it.'
            return render_template('search.html', header=header, comment=comment, movies=movies)
        else:
            id = request.form.get('movie')
            return redirect(f'/add/{id}')
    else:
        header = 'Search for a Movie'
        comment = 'Search below the title of the movie and a list of results will show.'
        return render_template('search.html', header=header, comment=comment)

@app.route('/add/<int:id>', methods=['POST', 'GET'])
def add(id):

    start = 'https://image.tmdb.org/t/p/w1280/'
    url = f"https://api.themoviedb.org/3/movie/{id}"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + os.getenv('AUTH_TOKEN')
    }
    response = requests.get(url, headers=headers)
    movie = response.json()
    movie['img_src'] = start + movie['poster_path']

    if request.method == 'POST':
        rating = request.form.get('rating')
        comment = request.form.get('comment')
        input_code = request.form.get('code')

        if input_code != code:
            flash('Code is incorrect!')
            return redirect('/search')

        new_movie = Movies()
        new_movie.id = movie['id']
        new_movie.title = movie['title']
        new_movie.release = movie['release_date']
        new_movie.description = movie['overview']
        new_movie.img = movie['img_src']
        new_movie.comment = comment
        new_movie.rating = rating
        db.session.add(new_movie)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add.html', movie=movie)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    rating = request.form.get('rating')
    comment = request.form.get('comments')
    input_code = request.form.get('code')

    if input_code != code:
        flash('Code is incorrect!')
        return redirect('/')

    movie = db.session.query(Movies).filter(Movies.id == id).first()
    movie.rating = rating
    movie.comment = comment
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete(id):
    input_code = request.form.get('code')

    if input_code != code:
        flash('Code is incorrect!')
        return redirect('/')
    
    movie = db.session.query(Movies).filter(Movies.id == id).first()
    db.session.delete(movie)
    db.session.commit()
    return redirect('/')
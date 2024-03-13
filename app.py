import sqlite3 as sql
from init_db import resetTable
from flask import Flask, render_template, flash, request, url_for, redirect
from werkzeug.exceptions import abort

def get_db_connection():
    dbCon = sql.connect('filmflix.db')
    dbCon.row_factory = sql.Row
    return dbCon

def get_film(id):
    dbCon = get_db_connection()
    film = dbCon.execute('SELECT * FROM tblFilms WHERE filmID = ?',
                        (id,)).fetchone()
    dbCon.close()
    if film is None:
        abort(404)
    return film


app = Flask(__name__)
app.config['SECRET_KEY'] = 'megafilmflix'

@app.route('/')
def index():
    dbCon = get_db_connection()
    search = request.args.get('search')
    if search:
        search='%'+search.lower()+'%'
        films = dbCon.execute('SELECT * from tblFilms WHERE lower(title) LIKE ? OR lower(genre) LIKE ? OR lower(duration) LIKE ? OR lower(ReleaseYear) LIKE ?', (search, search, search, search))
        row = dbCon.execute('SELECT * from tblFilms WHERE lower(title) LIKE ? OR lower(genre) LIKE ? OR lower(duration) LIKE ? OR lower(ReleaseYear) LIKE ?', (search, search, search, search)).fetchone()
        if row == None:
            flash('No results')
            return redirect('/')
            
            
    else:
        films = dbCon.execute('SELECT * from tblFilms').fetchall()
    
    return render_template('index.html',tblFilms=films)



@app.route('/<int:id>')
def film(id):
    film = get_film(id)
    return render_template('film.html', film=film)


@app.route('/addFilm', methods=('GET','POST'))
def add():
    if request.method == 'POST':

        title = request.form['title']
        ReleaseYear = request.form['ReleaseYear']
        rating = request.form['rating']
        duration = request.form['duration']
        genre = request.form['genre']
        trailer = request.form['trailer']
        description = request.form['description']
        allFields = [title, ReleaseYear, rating, duration, genre, trailer, description]

        #Getting the youtube ID from the youtube link supplied
        sub1 = "watch?v="
        sub2 = "&ab_channel"
        idx1 = trailer.index(sub1)
        idx2 = trailer.index(sub2)
        trailer = trailer[(idx1+len(sub1)):idx2]

        if all(allFields) !=True:
            flash('Missing Field(s)')
        else:
            dbCon = get_db_connection()
            dbCon.execute('INSERT INTO tblFilms (title,ReleaseYear,rating,duration,genre,trailer,description) VALUES (?,?,?,?,?,?,?)',
                         (title, ReleaseYear, rating, duration, genre, trailer, description))
            dbCon.commit()
            dbCon.close()
            return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    film = get_film(id)

    if request.method == 'POST':
        title = request.form['title']
        ReleaseYear = request.form['ReleaseYear']
        rating = request.form['rating']
        duration = request.form['duration']
        genre = request.form['genre']
        trailer = request.form['trailer']
        description = request.form['description']
        allFields = [title, ReleaseYear, rating, duration, genre, trailer, description]

        #Getting the youtube ID from the youtube link supplied
        sub1 = "watch?v="
        sub2 = "&ab_channel"
        idx1 = trailer.index(sub1)
        idx2 = trailer.index(sub2)
        trailer = trailer[(idx1+len(sub1)):idx2]

        if all(allFields) !=True:
                flash('Missing Field(s)')
        else:
            dbCon = get_db_connection()
            dbCon.execute('UPDATE tblFilms SET title = ?, ReleaseYear = ?, rating = ?, duration = ?, genre = ?, trailer = ?, description = ?'
                          ' WHERE filmID = ?', 
                          (title, ReleaseYear, rating, duration, genre, trailer, description, id))
            dbCon.commit()
            dbCon.close()
            return redirect(url_for('index'))

    return render_template('edit.html', film = film)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    film = get_film(id)
    dbCon = get_db_connection()
    dbCon.execute('DELETE FROM tblFilms WHERE filmID = ?',
                 (id,))
    dbCon.commit()
    dbCon.close()
    flash("'{}' was successfully deleted!". format(film['title']))
    return redirect(url_for('index'))

@app.route('/refresh')
def refresh():
    dbCon = get_db_connection()
    resetTable()
    flash('Changes were successfully reverted!')
    return redirect(url_for('index'))

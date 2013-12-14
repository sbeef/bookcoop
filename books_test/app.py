from __future__ import absolute_import, unicode_literals

import db

from flask import Flask, render_template, request, redirect, url_for
app = Flask('books_test')


@app.route("/")
def root():
  entries = db.Book.query.all()
  return render_template('index.html', entries=entries)

@app.route("/add", methods=['POST'])
def addbook():
  new_entry = db.Book(title=request.form.get('title'), author = request.form.get('author'),)
  db.db.session.add(new_entry)
  db.db.session.commit()

  return redirect(url_for('root'))


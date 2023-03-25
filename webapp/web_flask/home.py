#!/usr/bin/python3
from flask import Flask, render_template
from . import main
# from ..db_storage import cursor


@main.route('/', strict_slashes=False)
def index():
    """
        function to return Hello HBNB!
    """
    return render_template("index.html")


if __name__ == '__main__':
        main.run(host='0.0.0.0', port=5000)


# begin flask page rendering
# @main.teardown_appcontext
# def teardown_db(exception):
#     """
#     after each request, this method calls .close() (i.e. .remove()) on
#     the current SQLAlchemy Session
#     """
#     cursor.close()
from flask import Flask, jsonify
import pandas as pd

movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

# extraer información importante de dataframe


# variables para almacenar información


# método para obtener información de la base de datos


# /movies api


# /like api


# /dislike api


# /did_not_watch api


if __name__ == "__main__":
  app.run()

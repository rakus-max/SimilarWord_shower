import numpy as np

import requests
import os
import json

from gensim.models import KeyedVectors

FILE_DIR = os.environ.get('FILE_DIR', './data/entity_vector/entity_vector.model.bin')


class Model:
    def predict(self, word):
        model = KeyedVectors.load_word2vec_format(FILE_DIR, binary=True)
        similar = model.most_similar([word])[0][0]
        return similar

model = Model()

def get_model():
    return model

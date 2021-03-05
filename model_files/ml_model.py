import pandas as pd
import numpy as np 
import string
import tensorflow as tf
import random
from keras.models import load_model
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.callbacks import LambdaCallback



##functions
def make_name(model,user_string):
    name = []
    x = np.zeros((1, max_length, char_dim))
    end = False
    i = 0
    any_length = random.randint(5,10)
    name.append(user_string)
    
    while end==False:
        probs = list(model.predict(x)[0,i])
        probs = probs / np.sum(probs)
        index = np.random.choice(range(char_dim), p=probs)
        if i == max_length-2:
            character = '.'
            end = True
        else:
            character = id_to_char[index]
        name.append(character)
        x[0, i+1, index] = 1
        i += 1
        if character == '.':
            end = True
    
    print(''.join(name))
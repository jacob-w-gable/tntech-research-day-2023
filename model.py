import sys
import pandas as pd
import numpy as np
import csv
import ast

from keras.layers import Dense, Dropout, LSTM, LayerNormalization, MultiHeadAttention, Conv1D, MaxPooling1D
from keras.models import Sequential
from keras.models import load_model
from keras.optimizers import SGD
from sklearn.model_selection import train_test_split


def load_data(filename):
    X = []
    y = []

    with open(filename) as file:
        tsv = csv.reader(file, delimiter='\t')
        first = True
        for line in tsv:
            if not first:
                X.append(eval(line[0]))
                y.append(eval(line[1]))
            first = False

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train):
    print("Train size: " + str(len(X_train)))

    model = Sequential()
    model.add(Dense(480, input_shape=(len(X_train[0]),), activation='relu'))
    model.add(Dropout(0.1))
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.1))
    model.add(Dense(192, activation='relu'))
    model.add(Dense(len(y_train[0]), activation='softmax'))

    sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy',
                  optimizer=sgd, metrics=['accuracy'])

    hist = model.fit(X_train, y_train,
                     epochs=100, batch_size=5, verbose=1)

    model.save("model.tf", hist, save_format='tf')

    return model


def test_model(model, X_test, y_test):
    results = model.evaluate(X_test, y_test, batch_size=5)
    predictions = model.predict(X_test)

    binary_predictions = []
    for prediction in predictions:
        chosen_probability = max(prediction)
        binary_prediction = []
        for probability in prediction:
            if probability < chosen_probability:
                binary_prediction.append(0)
            else:
                binary_prediction.append(1)
        has_1 = False
        for prediction_instance in binary_prediction:
            if prediction_instance == 1:
                has_1 = True
                break
        if not has_1:
            print("This doesn't work")
            exit()
        binary_predictions.append(binary_prediction)

    truth_table = []
    for i in range(19):
        truth_table.append([0]*19)

    truth_totals = [0]*19
    chosen_totals = [0]*19

    for i in range(len(binary_predictions)):
        real_index = 0
        for j in range(19):
            if y_test[i][j] == 1:
                break
            else:
                real_index += 1
        if real_index == 19:
            print("real_index overflow")

        chosen_index = 0
        for j in range(19):
            if binary_predictions[i][j] == 1:
                break
            else:
                chosen_index += 1
        if chosen_index == 19:
            print("chosen_index overflow")

        truth_table[real_index][chosen_index] += 1
        truth_totals[real_index] += 1
        chosen_totals[chosen_index] += 1

    usefulness_totals = [0]*19
    usefulness = 0

    for i in range(19):
        for j in range(19):
            distance = abs(i - j) + 1
            usefulness_totals[i] += (truth_table[i][j] / distance)
            usefulness += (truth_table[i][j] / distance)
        usefulness_totals[i] /= truth_totals[i]
    usefulness /= len(X_test)

    print("      1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  |  total  |  class accuracy  |  usefulness")
    for i in range(19):
        index_accuracy = "N/A"
        if truth_totals[i] > 0:
            index_accuracy = truth_table[i][i] / truth_totals[i]
        print(str(i+1) + "    ",
              truth_table[i], "  |  ", truth_totals[i], "  |  ", index_accuracy, "  |  ", usefulness_totals[i])
    print("     ", chosen_totals)
    print("")
    print("prediction count:", len(X_test))
    print("usefulness:", usefulness)
    print("loss, accuracy:", results)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Required arguments: data file")
        exit()

    input_file = sys.argv[1]

    X_train, X_test, y_train, y_test = load_data(input_file)

    if len(sys.argv) == 3:
        if sys.argv[2] == 'new':
            model = train_model(X_train, y_train)
        else:
            model = load_model('model.tf')
    else:
        model = load_model('model.tf')

    test_model(model, X_test, y_test)

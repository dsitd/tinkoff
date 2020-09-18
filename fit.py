story = ''
from random import choice
import pickle


class Model:
    def __init__(self, data=''):
        if data == '':
            self.data = dict()
        else:
            self.data = data
        self.story = ''

    def fit(self, text: str):
        text = ''.join([i.lower() for i in text if i.isalpha() or i in {' ', '\n'}]).split()
        for numWord in range(len(text) - 1):
            if text[numWord] in self.data:
                if text[numWord + 1] not in self.data[text[numWord]]:
                    self.data[text[numWord]] += [text[numWord + 1]]
            else:
                self.data[text[numWord]] = [text[numWord + 1]]


    def del_once(self):
        x = []
        for i in self.data:
            if len(self.data[i]) < 2:
                x.append(i)
        for i in x:
            del self.data[i]

    def save(self):
        with open('data.pickle', 'wb') as f:
            pickle.dump(self.data, f)

    def load(self, name):
        with open('data.pickle', 'rb') as f:
            self.data = pickle.load(f)

    def clear_model(self):
        with open('data.pickle', 'wb') as f:
            pickle.dump({}, f)


def read_file(name):
    f = open(name, 'r', encoding='UTF8')
    text = f.read()
    return text


def fit_and_save(model, name_file_fit):
    model.load('data.pickle')
    model.fit(read_file(name_file_fit))
    model.save()


name = r'dataset.txt'
mod = Model()
mod.load('data.pickle')
mod.genarate(100)
print(mod.story)
print(mod.data['п'])
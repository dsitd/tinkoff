from random import choice
import pickle


class Model:
    # create model
    # data is a dict model
    def __init__(self, data=None):
        if data is None:
            self.data = {}
        else:
            self.data = data

    # fit model
    # text is a dataset for fit
    def fit(self, text: str):
        text = ''.join([i.lower() for i in text if i.isalpha() or i in {' ', '\n'}]).split()
        for numWord in range(len(text) - 1):
            if text[numWord] in self.data:
                if text[numWord + 1] not in self.data[text[numWord]]:
                    self.data[text[numWord]] += [text[numWord + 1]]
            else:
                self.data[text[numWord]] = [text[numWord + 1]]

    # del keys where one word
    def del_once(self):
        x = []
        for i in self.data:
            if len(self.data[i]) == 1:
                x.append(i)
        for i in x:
            del self.data[i]

    # save model into
    def save(self, path='data.pickle'):
        with open(path, 'wb') as f:
            pickle.dump(self.data, f)

    # load model from other file
    def load(self, path_model='data.pickle'):
        with open(path_model, 'rb') as f:
            self.data = pickle.load(f)

    # clear model and save
    def clear_model(self, path_model='data.pickle'):
        with open(path_model, 'wb') as f:
            pickle.dump({}, f)


# correct read file for fit
def read_file(path):
    f = open(path, 'r', encoding='UTF8')
    text = f.read()
    return text


# fit and save model into other file
def fit_and_save(model, path_file_fit='dataset.txt', path_load_file='data.pickle'):
    model.load(path_load_file)
    model.fit(read_file(path_file_fit))
    model.save()


def fit_or_delete():
    mod = Model()
    a = input('input D if you want delete main model or F if you want fit model\n')
    if a == 'D':
        mod.clear_model()
    elif a == 'F':
        path_for_fit = input('input path to text for fit\n')
        mod.fit(read_file(path_for_fit))
        s = input('input S if you want save model into main save '
                  'or '
                  'M if you want save to you file(*.pickle)\n')
        if s == 'S':
            mod.save()
        elif s == 'M':
            path = input('input a path to file\n')
            mod.save(path)

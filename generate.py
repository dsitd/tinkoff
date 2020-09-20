from tinkoff.fit import Model
from random import choice


# generate text
def generate(model: Model, count_word: int, base_text=None):
    if base_text is None:
        base_text = choice(list(model.data))
    base_text = base_text.split()
    for i in range(count_word):
        base_text.append(choice(list(model.data[base_text[-1]])))
    new_text = ' '.join(base_text)
    return new_text


def start_generate():
    a = input('input path to model(*.piclkle) or N if you want main model \n')
    mod = Model()
    if a == 'N':
        mod.load()
    else:
        mod.load(a)

    count = int(input('input count of new word\n'))

    base = input('input base text or N\n')
    if len(base.split()) == 0 or base == 'N':
        base = None
    text = generate(mod, count, base)
    print(text)

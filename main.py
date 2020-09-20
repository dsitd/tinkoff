from tinkoff.fit import fit_or_delete
from tinkoff.generate import start_generate

a = input('input FD if you want fit or delete model or input G if you want generate text\n')
if a == 'FD':
    fit_or_delete()
elif a == 'G':
    start_generate()

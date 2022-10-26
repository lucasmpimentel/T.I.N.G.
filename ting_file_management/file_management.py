import sys


def txt_importer(path_file):
    try:
        if path_file.endswith('.txt'):
            with open(path_file) as arquivo:
                result = arquivo.read().split('\n')
                return result
        else:
            return print('Formato inválido', file=sys.stderr)
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)

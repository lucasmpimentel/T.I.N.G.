import sys
from ting_file_management.file_management import txt_importer

def process(path_file, instance):
    status = True
    for item in instance._queue:
        if item["nome_do_arquivo"] == path_file:
            status = False
            return status
    if status:
        result = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(txt_importer(path_file)),
            "linhas_do_arquivo": (txt_importer(path_file))
        }
        instance.enqueue(result)
        return print(result, file=sys.stdout)


def remove(instance):
    if len(instance):
        result = instance.dequeue()["nome_do_arquivo"]
        return print(f"Arquivo {result} removido com sucesso", file=sys.stdout)
    return print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    try:
        return print(instance.search(position), file=sys.stdout)
    except IndexError:
        return print("Posição inválida", file=sys.stderr)

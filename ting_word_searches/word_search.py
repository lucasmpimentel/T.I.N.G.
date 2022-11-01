def exists_word(word, instance):
    result = []
    for item in instance._queue:
        lista_palavras = []
        for position, data in enumerate(item["linhas_do_arquivo"]):
            if word.lower() in data.lower():
                obj = {"linha": position + 1}
                lista_palavras.append(obj)
            if len(lista_palavras) == 0:
                return []
        response = {
            "palavra": word,
            "arquivo": lista_palavras["nome_do_arquivo"],
            "ocorrencias": lista_palavras
        }
        result.append(response)
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""

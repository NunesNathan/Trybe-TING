import sys
from ting_file_management import file_management


def process(path_file, instance):
    text_list = file_management.txt_importer(path_file)

    if path_file in instance.data:
        return False

    instance.enqueue(path_file)

    result = str({
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text_list),
        "linhas_do_arquivo": text_list
    })

    sys.stdout.write(result)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""

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
    if len(instance.data) > 0:
        poped_file = instance.dequeue()

        sys.stdout.write(f"Arquivo {poped_file} removido com sucesso\n")
    else:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        file_data = file_management.txt_importer(file)

        result = str({
            "nome_do_arquivo": file,
            "qtd_linhas": len(file_data),
            "linhas_do_arquivo": file_data
        })

        sys.stdout.write(result)
    except IndexError:
        return sys.stderr.write("Posição inválida")

import sys


def txt_importer(path_file):
    data = list()

    if path_file.endswith(".txt"):
        try:
            with open(path_file) as file:
                lines = file.readlines()

                for line in lines:
                    data.append(line.strip("\n"))

            return data
        except FileNotFoundError:
            sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    else:
        sys.stderr.write("Formato inválido\n")

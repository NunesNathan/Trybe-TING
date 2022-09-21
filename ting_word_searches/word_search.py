from ting_file_management import file_management, queue


def exists_word(word, instance: queue.Queue):
    finded = list()
    empty_list = list()

    for file_name in instance.data:
        file_text = file_management.txt_importer(file_name)
        occurrencies = {
            "palavra": word,
            "arquivo": file_name,
            "ocorrencias": empty_list
        }

        for i, line in enumerate(file_text):
            if word.lower() in line.lower():
                occurrencies["ocorrencias"].append({
                    "linha": i + 1
                })

        finded.append(occurrencies)

    if len(finded[0]["ocorrencias"]) == 0:
        return empty_list

    return finded

from typing import List


def print_pretty_output_files(file_list :List[str]) -> str:
    """ Красивый вывод файлов в столбик"""
    
    filenames = [f.split(".")[0] for f in file_list]
    return "\n".join(filenames)

def get_pretty_table(data, cell_sep=' | ', header_separator=True) -> str:
    """ Отформатированный вывод """
    
    rows = len(data)
    cols = len(data[0])

    col_width = []
    for col in range(cols):
        columns = [str(data[row][col]) for row in range(rows)]
        col_width.append(len(max(columns, key=len)))

    separator = "-+-".join('-' * n for n in col_width)

    res = ""
    for i, row in enumerate(range(rows)):
        if i == 1 and header_separator:
            res+=separator + "\n"

        result = []
        for col in range(cols):
            item = str(data[row][col]).rjust(col_width[col])
            result.append(item)

        res+=cell_sep.join(result) + "\n"
    
    return res
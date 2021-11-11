"""Utility functions."""

__author__ = "730369129"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()

    return result
    
    
def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(xs: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Data with set number of rows."""
    result: dict[str, list[str]] = {}
    for my_str in xs:
        my_list: list[str] = []
        i: int = 0
        if rows < len(xs[my_str]):
            while i < rows:
                my_list.append(xs[my_str][i])
                i += 1
        else:
            my_list = xs[my_str]
        result[my_str] = my_list
    return result


def select(xs: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Data with only a few column names."""
    result: dict[str, list[str]] = {}
    for my_str in xs:
        i: int = 0
        while i < len(columns):
            if my_str == columns[i]:
                result[my_str] = xs[my_str]
            i += 1 
    return result


def concat(xs: dict[str, list[str]], ys: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concattonate two dictionaries together."""
    result: dict[str, list[str]] = {}
    for my_key in xs:
        result[my_key] = xs[my_key]
    for my_key in ys:
        is_key_present: bool = my_key in result
        if is_key_present is True: 
            i: int = 0
            while i < len(ys[my_key]):
                result[my_key].append(ys[my_key][i])
                i += 1
        else:
            result[my_key] = ys[my_key] 
    return result 


def count(xs: list[str]) -> dict[str, int]:
    """Counting number of str occurances in a list."""
    result: dict[str, int] = {}
    for item in xs:
        is_key_present: bool = item in result
        if is_key_present is True:
            result[item] += 1
        else:
            result[item] = 1
    return result

def count_non_majors(xs: list[str]) -> int:
    """Counting number of non-majors in a list."""
    result: int = 0
    for item in xs:
        if item == 'No':
            result += 1
        if item == 'Yes - Minor':
            result += 1
    return result

def average_major(xs: dict[str, list[str]]) -> dict[str, float]:
    result_sum: dict[str, int] = {}
    result_sum['No'] = 0
    result_sum['Yes'] = 0
    result_count: dict[str, int] = {}
    result_count['No'] = 0
    result_count['Yes'] = 0
    i: int = 0
    while i < len(xs['comp_major']):
        if xs['comp_major'][i] == 'No':
            result_sum['No'] = result_sum['No'] + int(xs['pace'][i])
            result_count['No'] = result_count['No'] + 1
        if xs['comp_major'][i] == 'Yes - minor':
            result_sum['No'] = result_sum['No'] + int(xs['pace'][i])
            result_count['No'] = result_count['No'] + 1
        if xs['comp_major'][i] == ('Yes - BS' or 'Yes - BA'):
            result_sum['Yes'] = result_sum['Yes'] + int(xs['pace'][i])
            result_count['Yes'] = result_count['Yes'] + 1
        i += 1

    result_dict: dict[str, float] = {}
    for key in result_sum:
        result_dict[key] = result_sum[key] / result_count[key]  

    return result_dict


def major_splitter(xs: dict[str, list[str]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    result['No'] = []
    result['Yes'] = []
    i: int = 0
    while i < len(xs['comp_major']):
        if xs['comp_major'][i] == 'No':
            result['No'].append(xs['pace'][i])
        if xs['comp_major'][i] == 'Yes - minor':
            result['No'].append(xs['pace'][i])
        if xs['comp_major'][i] == ('Yes - BS' or 'Yes - BA'):
            result['Yes'].append(xs['pace'][i])
        i += 1

    
    return result
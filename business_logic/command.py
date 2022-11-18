from typing import List
from os import walk
from .exceptions import *
from .pretty_output import *


COMMANDS = ['SELECT', 'FILES', 'SEARCH']


def validate_command(command :str) -> List[str]:
    """ Валидация команды """
    
    command_list :str = command.split(" ")
    if not command_list:
        raise EmptyCommand
    if command_list[0] not in COMMANDS:
        raise NotFoundCommand
    
    if (command_list[0] == 'SELECT' 
        and (len(command_list) != 4 or command_list[2] != 'FROM' 
        or (command_list[1] != "*" and not command_list[1].lstrip("-").isdigit()))):
            raise IncorrectSyntaxSelect
    elif command_list[0] == 'FILES' and len(command_list)!=1:
        raise IncorrectSyntaxFiles
    elif (command_list[0] == 'SEARCH'
         and (len(command_list) != 4 
         or command_list[2] != 'FROM')):
        raise IncorrectSyntaxSearch
    
    return command_list


def execute_command(command_split :List[str]) -> str:
    """ Выполнение команды"""
    
    if command_split[0] == 'SELECT':
        
        data :List[str]= select_by_file(command_split)
        if data:
            return get_pretty_table(data)
        else:
            return "File is empty"
    
    elif command_split[0] == 'FILES':
        files :List[str] = get_files()
        return print_pretty_output_files(files)
    
    elif command_split[0] == 'SEARCH':
        data :List[str] = search_by_file(command_split)
        if data:
            return get_pretty_table(data)
        else:
            return "Search string not found"

def select_by_file(command_split :List[str]) -> List[List[str]]:
    """ Выполнение команды SELECT """
    
    if command_split[3] not in [f.split(".")[0] for f in get_files()]:
        raise FileNotFound
    
    replace_n = lambda x: x.replace('\n','')
    split_delimeter = lambda line : list(map(replace_n, line.split(';')))
    
    with open(f"files/{command_split[3]}.csv") as file:
        list_lines_file = list(map(split_delimeter, file.readlines()))
        
    if not list_lines_file:
        raise EmptyFile
    if command_split[1] == '*':
        return list_lines_file
    
    count_records = int(command_split[1])
    headers = list_lines_file.pop(0)
    if count_records > 0:
        return [headers, *list_lines_file[:count_records]]
    else:
        count_records*=-1
        return [headers, *list_lines_file[::-1][:count_records][::-1]]
    
def search_by_file(command_split :List[str]) -> List[List[str]]:
    """ Выполнение команды SEARCH """
    
    search_str :str = command_split[1]
    replace_n = lambda x: x.replace('\n','')
    split_delimeter = lambda line : list(map(replace_n, line.split(';')))
    search = lambda item: search_str in ";".join(item)
    
    with open(f"files/{command_split[3]}.csv") as file:
        list_lines_file = list(map(split_delimeter,file.readlines()))
        
    headers = list_lines_file.pop(0)
    return [headers,*list(filter(search, list_lines_file))]

def get_files() -> str:
    """ Выполнение команды FILES """
    
    return next(walk("files"), (None, None, []))[2]


class EmptyCommand(Exception):
    """ Возникает при получении пустой строки """
    
    def __init__(self):
        self.value = """
            Ошибка! Вы не ввели команду!          
        """

class NotFoundCommand(Exception):
    """ Возникает при получении неизвестной команды """
    
    def __init__(self):
        self.value = """
            Ошибка! Неизвестная команда            
        """


class IncorrectSyntaxSelect(Exception):
    """ Возникает при некорректом синтаксисе SELECT """
    
    def __init__(self):
        self.value = """
            Ошибка! Некорректный синтаксис команды SELECT!
            Синтаксис команды  SELECT должен быть:
            SELECT {* or +/-number} FROM name_file 
            Например, SELECT -10 FROM users           
        """


class IncorrectSyntaxFiles(Exception):
    """ Возникает при некорректом синтаксисе FILES """
    
    def __init__(self):
        self.value = """
            Ошибка! Некорректный синтаксис команды FILES!
            Синтаксис команды  FILES должен быть:
            FILES 
        """


class IncorrectSyntaxSearch(Exception):
    """ Возникает при некорректом синтаксисе SEARCH """
    
    def __init__(self):
        self.value = """
            Ошибка! Некорректный синтаксис команды SEARCH!
            Синтаксис команды  SEARCH должен быть:
            SEARCH key_word FROM name_file 
            Например, SEARCH Ivan FROM users           
        """
        
class FileNotFound(Exception):
    """ Возникает при отсутствии запрошенного файла пользователем """
    
    def __init__(self):
        self.value = """
            Ошибка! Запрошенный файл не найден!
            Воспользуйтесь коммандой FILES, для вывода доступных файлов          
        """

class EmptyFile(Exception):
    """ Возникает при отсутствии данных в запрошенном файле """
    
    def __init__(self):
        self.value = """
            В файле нет данных!        
        """
        
    
class NoneJsonException(Exception):
    def __init__(self, value) -> None:
        message = f'{value} is a None object, the function expects a dict object.'
        super().__init__(message)

class LangException(Exception):
    def __init__(self, value) -> None:
        super().__init__(f'Selected language in "{value}" does not exist in the list of brainly languages ​​in this package. Try using: "pt" to portuguese, "us" to english, "es" to spanish, "id" to indonesian.')

class HighIndex(Exception):
    def __init__(self) -> None:
        super().__init__('Question/Answer index out of list range. Try using a smaller index.')
        
class NoResults(Exception):
    def __init__(self) -> None:
        super().__init__('We could not find any results for this search.')

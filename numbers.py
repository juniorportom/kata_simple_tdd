
class Numbers:
    def calcular(self, cadena):
        if cadena == "":
            return []
        numbers = cadena.split(",")
        return [len(numbers)]

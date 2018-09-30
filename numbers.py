


class Numbers:
    def calcular(self, cadena):
        if cadena == "":
            return []
        if "," in cadena:
            numbers = cadena.split(",")
            return [len(numbers)]
        else:
            return [1]


class Numbers:
    def calcular(self, cadena):
        if cadena == "":
            return []
        numbers = cadena.split(",")
        min = numbers[0]
        for num in numbers:
            if num < min:
                min = num
        return [len(numbers), int(min)]

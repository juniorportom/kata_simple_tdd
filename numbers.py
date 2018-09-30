
class Numbers:
    def calcular(self, cadena):
        if cadena == "":
            return []
        numbers = cadena.split(",")
        min = numbers[0]
        max = numbers[0]
        for num in numbers:
            if num < min:
                min = num
            if num > max:
                max = num
        return [len(numbers), int(min), int(max)]

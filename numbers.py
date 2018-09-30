
class Numbers:
    def calcular(self, cadena):
        if cadena == "":
            return []
        numbers = cadena.split(",")
        min = int(numbers[0])
        max = int(numbers[0])
        prom = 0
        for num in numbers:
            num = int(num)
            prom = prom + num
            if num < min:
                min = num
            if num > max:
                max = num
        return [len(numbers), min, max, prom/len(numbers)]

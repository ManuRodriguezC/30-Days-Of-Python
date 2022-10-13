class Coche:
    def __init__(self, marca, color, modelo, puertas, velocidad):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.puertas = puertas
        self.velocidad = velocidad

    def __str__(self):
        return "{} is {}, model {} with {} doors and his max speed is {} km/h".format(self.marca, self.color, self.modelo, self.puertas, self.velocidad)

    def acelerar(self):
        self.velocidad += 100
        print("{} is accelerating, this speed is {}".format(self.marca, self.velocidad))

    def frenar(self):
        self.velocidad = 0
        print("The {} is stopping".format(self.marca))

carro_1 = Coche("Porshe", "red", 2022, 2, 300)
print(carro_1)
carro_1.acelerar()
print(carro_1)
carro_1.frenar()

car_2 = Coche("Audi", "Blue", 2020, 4, 290)
print(car_2)
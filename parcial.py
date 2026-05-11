#Estudiante : Michelle Mercado

# Clase base
class Personaje:

    # Constructor
    def __init__(self, vida, ataque, defensa):

        self.__vida = vida
        self.__ataque = ataque
        self.__defensa = defensa

    # Getters
    def get_vida(self):
        return self.__vida

    def get_ataque(self):
        return self.__ataque

    def get_defensa(self):
        return self.__defensa

    # Setters
    def set_vida(self, vida):

        # Validar vida entre 0 y 100
        if vida < 0:
            self.__vida = 0

        elif vida > 100:
            self.__vida = 100

        else:
            self.__vida = vida

    # Método para mostrar estadísticas
    def mostrar_estado(self):

        print("Vida:", self.__vida)
        print("Ataque:", self.__ataque)
        print("Defensa:", self.__defensa)

    # Método atacar
    def atacar(self, objetivo):

        daño = self.__ataque - objetivo.get_defensa()

        if daño < 0:
            daño = 0

        nueva_vida = objetivo.get_vida() - daño
        objetivo.set_vida(nueva_vida)

        print("Ataque básico")
        print("Daño realizado:", daño)


# Clase Guerrero
class Guerrero(Personaje):

    def atacar(self, objetivo):

        # 20% más daño
        daño = int(self.get_ataque() * 1.2) - objetivo.get_defensa()

        if daño < 0:
            daño = 0

        nueva_vida = objetivo.get_vida() - daño
        objetivo.set_vida(nueva_vida)

        print("\nGuerrero usa Golpe Brutal")
        print("Daño realizado:", daño)


# Clase Mago
class Mago(Personaje):

    def atacar(self, objetivo):

        # Ignora defensa
        daño = self.get_ataque()

        nueva_vida = objetivo.get_vida() - daño
        objetivo.set_vida(nueva_vida)

        print("\nMago lanza Bola de Fuego")
        print("Daño realizado:", daño)


# Clase Arquero
class Arquero(Personaje):

    def atacar(self, objetivo):

        daño = self.get_ataque() - objetivo.get_defensa()

        # Doble daño
        if self.get_ataque() > objetivo.get_defensa():
            daño = daño * 2

        if daño < 0:
            daño = 0

        nueva_vida = objetivo.get_vida() - daño
        objetivo.set_vida(nueva_vida)

        print("\nArquero dispara Flecha Precisa")
        print("Daño realizado:", daño)


# Crear personajes
guerrero = Guerrero(100, 30, 20)
mago = Mago(80, 40, 10)

# Mostrar estado inicial
print("===== ESTADO INICIAL =====\n")

print("Guerrero")
guerrero.mostrar_estado()

print("\nMago")
mago.mostrar_estado()

# Batalla
turno = 1

while guerrero.get_vida() > 0 and mago.get_vida() > 0:

    print("\n========== TURNO", turno, "==========")

    # Turno del guerrero
    guerrero.atacar(mago)

    print("Vida restante del mago:", mago.get_vida())

    if mago.get_vida() <= 0:
        print("\nEl mago fue derrotado")
        break

    # Turno del mago
    mago.atacar(guerrero)

    print("Vida restante del guerrero:", guerrero.get_vida())

    if guerrero.get_vida() <= 0:
        print("\nEl guerrero fue derrotado")
        break

    turno += 1

print("\n===== FIN DEL JUEGO =====")
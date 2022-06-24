class Vehiculos():
    def __init__(self, marca, modelo):
        self. marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        self.enmarcha=True
    
    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
        self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


class Moto(Vehiculos):
    
    hcaballito=""
    
    def caballito(self):
       self.hcaballito="Voy haciendo el caballito"
    
    def estado(self): #este método sobreescribe el método estado de la clase padre
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", 
        self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)

class Furgoneta(Vehiculos):

    def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"

class VElectricos():
    def __init__(self):
        self.autonomia=100
    
    def cargarEnergia(self):
        self.cargando=True

class BicicletaElectrica(VElectricos,Vehiculos): #Herencia múltiple, si hay métodos conflictivos con el mismo nombre priva la primera clase referenciada a la izquierda
    pass

miBici= BicicletaElectrica()

miMoto=Moto("Honda","CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta=Furgoneta("Renault","Kangoo")

miFurgoneta.arrancar()
miFurgoneta.estado()
miFurgoneta.carga(False)


class Defase:
    def __init__ (self):
        
        self.compras = []
        self.puestos = []


    def agregar_asiento(self,nuevo_puesto):
        self.puestos.append(nuevo_puesto)

    def comprar_asiento(self,comprador,numero_puesto):
        for puesto in self.puestos:
            if puesto.numero() == numero_puesto and not puesto.estoy_vendido() and not puesto.estoy_reservado() or puesto.numero() == numero_puesto and not puesto.estoy_vendido() and comprador.dni == puesto.reserva["dni"]:
                puesto.cliente(comprador)
                self.compras.append({"nombre":comprador.nombre,
                                     "apellido":comprador.apellido,
                                     "dni":comprador.dni,
                                     "puesto nro":puesto.numero
                                    })

    def reservar_asiento(self,comprador):
        for puesto in self.puestos:
            if not puesto.estoy_vendido() and not puesto.estoy_reservado():
               puesto.reserva_cliente(comprador)
               self.reservas.append({"nombre":comprador.nombre,
                                     "apellido":comprador.apellido,
                                     "dni":comprador.dni,
                                     " numero de puesto ":puesto.numero
                                    })

    def desreservar_puesto(self,numero_puesto):
        for puesto in self.puestos:
            if puesto.numero() == numero_puesto and puesto.estoy_reservado():
               puesto.desreservar()



class Puesto:
    def __init__ (self,un_numero_de_puesto):
        self.numero_puesto = un_numero_de_puesto
        self.comprador = None
        self.esta_vendido = False
        self.esta_reservado = False
        self.reservas = []

    def desreservar(self):
        self.comprador = None
        self.esta_reservado = False

    def numero(self):
        return self.numero_puesto    

    def estoy_vendido(self):
        return self.esta_vendido

    def estoy_reservado(self):
        return self.esta_reservado    

    def cliente(self,cliente):
        self.comprador = cliente 
        self.esta_vendido = True

    def reserva_cliente(self,cliente):
        self.comprador = cliente
        self.esta_reservado = True          



class Cliente:
    def __init__ (self,un_nombre,un_apellido,un_dni,fecha_nacimiento):
        self.nombre = un_nombre
        self.un_apellido = un_apellido
        self.dni = un_dni
        self.fecha_nacimiento = fecha_nacimiento
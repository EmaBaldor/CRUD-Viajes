from utils.dateformat import DateFormat

class Viaje():

    def __init__(self, id_viaje, 
                 fecha=None, 
                 hora=None, 
                 vehiculo=None, 
                 lugares=None, 
                 disponible=None, 
                 finalizado=None,
                 origen=None,
                 destino=None,
                 fecha_creacion=None,
                 activado=None):

        self.id_viaje = id_viaje
        self.fecha = fecha
        self.hora = hora
        self.vehiculo = vehiculo
        self.lugares = lugares
        self.disponible = disponible
        self.finalizado = finalizado
        self.origen = origen
        self.destino = destino
        self.fecha_creacion = fecha_creacion
        self.activado = activado

    def convert_JSON(self):
        return {
            'id_viaje': self.id_viaje,
            'fecha': self.fecha,
            'hora': self.hora,
            'vehiculo': self.vehiculo,
            'lugares': self.lugares,
            'disponible': self.disponible,
            'finalizado': self.finalizado,
            'origen': self.origen,
            'destino': self.destino,
            'fecha_creacion': self.fecha_creacion,
            'activado':self.activado
        }

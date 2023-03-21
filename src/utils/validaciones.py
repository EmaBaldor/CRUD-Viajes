
from database.db import get_connection
from models.entities.viajes import Viaje


class Validar():

    @classmethod  
    def valida_viaje_exist(self,viaje):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                #validacion por fecha y vehiculo
                cursor.execute("Select * from viajes where fecha = %s and hora = %s and vehiculo = %s limit 1",(viaje.fecha,viaje.hora, viaje.vehiculo))
                fila = cursor.rowcount

            connection.close()
            return fila

        except Exception as ex:
            raise Exception(ex)
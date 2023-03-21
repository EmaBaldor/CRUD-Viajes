from database.db import get_connection
from .entities.viajes import Viaje
import json
from flask import jsonify


class viajesModel():

    @classmethod
    def get_viajes(self):
        try:
            connection = get_connection()
            viajes = []

            with connection.cursor() as cursor:
                cursor.execute("""Select * from viajes where finalizado = false order by id_viaje desc""")
                resultset = cursor.fetchall()

                for fila in resultset:
                    viaje = Viaje(
                        fila[0],
                        fila[1].isoformat(),
                        fila[2].isoformat(),
                        fila[3],
                        fila[4],
                        fila[5],
                        fila[6],
                        fila[7].strip(),
                        fila[8].strip(),
                        fila[9],
                        fila[10]
                    )
                    viajes.append(viaje.convert_JSON())

            connection.close()
            return viajes
        except Exception as ex:
            raise Exception(ex)

    # buscar un viaje
    @classmethod
    def get_viaje(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "Select * from viajes WHERE id_viaje = %s", (id,))
                fila = cursor.fetchone()
                viaje = None

                if fila != None:
                    viaje = Viaje(
                        fila[0],
                        fila[1].isoformat(),
                        fila[2].isoformat(),
                        fila[3],
                        fila[4],
                        fila[5],
                        fila[6],
                        fila[7].strip(),
                        fila[8].strip(),
                        fila[9]
                    )
                viaje = viaje.convert_JSON()
                print(viaje)

            connection.close()
            return viaje
        except Exception as ex:
            raise Exception(ex)

    # add viaje

    @classmethod
    def add_viaje(self, viaje):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
             
                cursor.execute("""INSERT INTO viajes (id_viaje,
                                                        fecha,
                                                        hora,
                                                        vehiculo,
                                                        lugares,
                                                        disponible,
                                                        finalizado,
                                                        origen,
                                                        destino)
                                                        VALUES
                                                        (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                                                        (viaje.id_viaje,
                                                        viaje.fecha,
                                                        viaje.hora,
                                                        viaje.vehiculo,
                                                        viaje.lugares,
                                                        viaje.disponible,
                                                        viaje.finalizado,
                                                        viaje.origen,
                                                        viaje.destino))
                fila_afectada = cursor.rowcount
                connection.commit()

            connection.close()
            return fila_afectada
        except Exception as ex:
            raise Exception(ex)


    def get_id():
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("Select max(id_viaje) from viajes")
                id_max = cursor.fetchone()

            connection.close()
            return id_max
        except Exception as ex:
            raise Exception(ex)


    # eliminar viaje
    @classmethod
    def delete_viaje(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("Delete from viajes WHERE id_viaje = %s", (id,))
                connection.commit()
                fila_afectada = cursor.rowcount

            connection.close()
            return fila_afectada
        except Exception as ex:
            raise Exception(ex)

    # modificar viaje
    @classmethod
    def update_viaje(self, viaje):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE viajes SET fecha = %s,
                                                    hora=%s,
                                                    vehiculo=%s,
                                                    lugares=%s,
                                                    disponible=%s,
                                                    finalizado=%s,
                                                    origen=%s,
                                                    destino=%s  
                                                    WHERE id_viaje = %s""", (viaje.fecha,
                                                                                viaje.hora,
                                                                                viaje.vehiculo,
                                                                                viaje.lugares,
                                                                                viaje.disponible,
                                                                                viaje.finalizado,
                                                                                viaje.origen,
                                                                                viaje.destino,
                                                                                viaje.id_viaje))
                connection.commit()
                fila_afectada = cursor.rowcount

            connection.close()
            return fila_afectada
        except Exception as ex:
            raise Exception(ex)
from flask import Blueprint, jsonify, request, send_file


#emtitis
from models.entities.viajes import Viaje
# models
from models.viajesModel import viajesModel
# valida
from utils.validaciones import Validar

main = Blueprint('viajes_blueprint', __name__)

@main.route('/')
def home():
    return send_file('static/index.html')


@main.route('/viajes/')
def get_viajes():

    try:

        viajes = viajesModel.get_viajes()
        return jsonify(viajes)
    
    except Exception as ex:
        return jsonify({'Msjs': str(ex)}), 500


@main.route('/viajes/<id>')
def get_viaje(id):

    try:

        viaje = viajesModel.get_viaje(id)
        if viaje != None:
            return jsonify(viaje)
        else:
            return jsonify({}), 404 
    
    except Exception as ex:
        return jsonify({'Msjs': str(ex)}), 500
    
@main.route('/viajes/add',methods=['POST'])
def add_viaje():

    try:
        #id_viaje=request.json['id_viaje']
        fecha=request.json['fecha']
        hora=request.json['hora']
        vehiculo=request.json['vehiculo']
        lugares=request.json['lugares']
        disponible=request.json['disponible']
        finalizado=request.json['finalizado']
        origen=request.json['origen']
        destino=request.json['destino']
        activado=request.json['activado']

        id = viajesModel.get_id()
        id_viaje = id[0] + 1

        viaje = Viaje(id_viaje,
                      fecha,
                      hora,
                      vehiculo,
                      lugares,
                      disponible,
                      finalizado,
                      origen,
                      destino,
                      activado)

        validacion = Validar.valida_viaje_exist(viaje)

        if validacion == 0:

            filas_afectadas = viajesModel.add_viaje(viaje)

            if filas_afectadas == 1:
                return jsonify({'Msj':'Nuevo viaje creado'},{'fecha':fecha,'hora':hora,'vehiculo':vehiculo,'nro_viaje':id_viaje}),200
            else:
                return jsonify({'Msj':'Error al insertar'}),500
        
        else:
            return jsonify({'Msj':'Ya existe viaje con misma fecha, hora, vehiculo'},{'fecha':fecha,'hora':hora,'vehiculo':vehiculo}),500


    except Exception as ex:
        return jsonify({'Msjs': str(ex)}), 500
    
@main.route('/viajes/delete/<id>',methods=['DELETE'])
def delete_viaje(id):

    try:

        fila_afectada = viajesModel.delete_viaje(id)
        if fila_afectada == 1:
            return jsonify({'Msj':'Se elimino viaje','Id':id})
        else:
            return jsonify({'Msj':'No se elimino el viaje'}), 500 
    
    except Exception as ex:
        return jsonify({'Msjs': str(ex)}), 500
    
@main.route('/viajes/update/<id>',methods=['PUT'])
def update_viaje(id):

    try:

        fecha=request.json['fecha']
        hora=request.json['hora']
        vehiculo=request.json['vehiculo']
        lugares=request.json['lugares']
        disponible=request.json['disponible']
        finalizado=request.json['finalizado']
        origen=request.json['origen']
        destino=request.json['destino']
        activado=request.json['activado']

        viaje = Viaje(id,
                      fecha,
                      hora,
                      vehiculo,
                      lugares,
                      disponible,
                      finalizado,
                      origen,
                      destino,
                      activado)        


        fila_afectada = viajesModel.update_viaje(viaje)
        if fila_afectada == 1:
            return jsonify({'Msj':'Se actualizo viaje','Id':id})
        else:
            return jsonify({'Msj':'No se actualizo el viaje'}), 500 
    
    except Exception as ex:
        return jsonify({'Msjs': str(ex)}), 500
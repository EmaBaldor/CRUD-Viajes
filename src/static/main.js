const viajesForm = document.querySelector('#viajesForm')

let viajes = [];
editar = false;
viajeId = null;

window.addEventListener('DOMContentLoaded', async () => {

    /*solicitar datos*/


    const respuesta = await fetch("/viajes");
    const datos = await respuesta.json()
    viajes = datos
    renderViajes(viajes)


})

viajesForm.addEventListener('submit', async e => {

    /*cargar datos*/

    e.preventDefault()

    const fecha = viajesForm['fecha'].value
    const hora = viajesForm['hora'].value
    const vehiculo = viajesForm['vehiculo'].value
    const lugares = viajesForm['lugares'].value
    const disponible = lugares
    const finalizado = false
    const origen = viajesForm['origen'].value.trim()
    const destino = viajesForm['destino'].value.trim()

    const viajeActual = JSON.stringify({
        fecha,
        hora,
        vehiculo,
        lugares,
        disponible,
        finalizado,
        origen,
        destino
    })

    if (!editar) {

        const response = await fetch('/viajes/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: viajeActual
        })

        const mensaje = await response.json()

        console.log(viajeActual)
        console.log(mensaje)

        viajes.unshift(viajeActual)

    } else {
        
        const response = await fetch(`/viajes/update/${viajeId}`, {
            method: 'PUT',
            headers: {'Content-Type': 'application/json'},
            body: viajeActual

        })


        const mensaje = await response.json()
        console.log(mensaje)
        editar = false;
        viajeId = null;
        

        }

    renderViajes(viajes)

    viajesForm.reset()

})


function renderViajes(viajes) {

    const viajesList = document.querySelector('#viajesList')
    viajesList.innerHTML = ''

    viajes.forEach(viaje => {

        const viajeItem = document.createElement('li')
        viajeItem.classList = 'list-group-item my-2'
        viajeItem.innerHTML = `


        <div class="card">
            <div class="card-header">

                <header class="d-flex justify-content-between align-items-center">
                    
                    
                        <h6>Viaje Nro: 

                            <span class="badge bg-dark">
                                
                                <h5>${viaje.id_viaje}</h5>
                            
                            </span>&ensp;&emsp;
                        
                        </h6>
                    
                    <button class="btn-delete btn btn-danger btn-sm">Eliminar</button>
                    <button class="btn-edit btn btn-outline-light btn-sm">Editar</button>

                </header>

                <h6>Fecha: ${viaje.fecha}</h6>
                <h6>Hora: ${viaje.hora}</h6>
                <h6>Vehiculo: ${viaje.vehiculo}</h6>
                <h6>Lugares: ${viaje.lugares}</h6>
                <h6>Disponibles: ${viaje.disponible}</h6>
                <h6>Origen: ${viaje.origen}</h6>
                <h6>Destino: ${viaje.destino}</h6>

            </div>

            <div class="form-check form-switch">
                <input class="chk-activado form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault">
                <label class="form-check-label" for="flexSwitchCheckDefault">Publicado</label>
            </div>

        </div>
  

        `
       
        const chkActivado = viajeItem.querySelector('.chk-activado')

        chkActivado.addEventListener('click', () => {
            console.log('activado')
        })
       
        
        const btnDelete = viajeItem.querySelector('.btn-delete')

        btnDelete.addEventListener('click', async () => {
            const response = fetch(`/viajes/delete/${viaje.id_viaje}`, {
                method: 'DELETE'
            })

            window.alert("Viaje Nro: "+viaje.id_viaje+" eliminado")
            /*const resp = await response.json()
            console.log(resp)*/
            
            

        })




        const btnEdit = viajeItem.querySelector('.btn-edit')

        btnEdit.addEventListener('click', async (e) => {
            const response = await fetch(`/viajes/${viaje.id_viaje}`);
            const data = await response.json();
            console.log(data)

            viajesForm['fecha'].value = viaje.fecha
            viajesForm['hora'].value = viaje.hora
            viajesForm['vehiculo'].value = viaje.vehiculo
            viajesForm['lugares'].value = viaje.lugares
            viajesForm['origen'].value = viaje.origen
            viajesForm['destino'].value = viaje.destino

            editar = true;
            viajeId = viaje.id_viaje;

        })




        viajesList.append(viajeItem)

    });




}
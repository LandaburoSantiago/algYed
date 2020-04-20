mientras not cola_vacia(cola despegue)
	hora actual = obtener hora()
	dato = frete(cola despegue)
	si dato.hora salida <= hora actual or cola_vacia(cola aterrizaje)
		dato = atencion(cola despegue)
		tiempo(tiempo despegue[tipode vuelo. index(dato.tipo)]
	sino
		si not cola_vacia(cola aterrizaje)
			dato=atencion(cola aterrizaje)
			tiempo(tiempo aterrizaje[tipode vuelo. index(dato.tipo)]

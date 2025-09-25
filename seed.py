from app import db, Usuario, Vinilo, Cancion, Carrito, Pedido, Playlist, Reporte, app

with app.app_context():
    db.create_all()

    if not Usuario.query.first():
        usuarios = [
            Usuario(nombre="Juan Perez", correo="juan@example.com", contraseña="1234", rol="cliente"),
            Usuario(nombre="Ana Torres", correo="ana@example.com", contraseña="abcd", rol="proveedor"),
            Usuario(nombre="Carlos Ruiz", correo="carlos@example.com", contraseña="admin123", rol="admin"),
            Usuario(nombre="Laura Gomez", correo="laura@example.com", contraseña="qwerty", rol="trabajador"),
        ]
        db.session.add_all(usuarios)

        vinilos = [
            Vinilo(nombre="Abbey Road", artista="The Beatles", genero="Rock", anio=1969,
                   caratula="https://url.com/abbey.jpg", precio=120.50, stock=10),
            Vinilo(nombre="Thriller", artista="Michael Jackson", genero="Pop", anio=1982,
                   caratula="https://url.com/thriller.jpg", precio=150.00, stock=5),
            Vinilo(nombre="Back in Black", artista="AC/DC", genero="Rock", anio=1980,
                   caratula="https://url.com/back.jpg", precio=99.99, stock=7),
        ]
        db.session.add_all(vinilos)

        canciones = [
            Cancion(titulo="Come Together", duracion=259, formato="vinilo", calidad="alta", vinilo_id=1),
            Cancion(titulo="Something", duracion=182, formato="vinilo", calidad="alta", vinilo_id=1),
            Cancion(titulo="Billie Jean", duracion=294, formato="vinilo", calidad="alta", vinilo_id=2),
            Cancion(titulo="Beat It", duracion=258, formato="vinilo", calidad="alta", vinilo_id=2),
            Cancion(titulo="Hells Bells", duracion=312, formato="vinilo", calidad="alta", vinilo_id=3),
        ]
        db.session.add_all(canciones)

        carritos = [
            Carrito(usuario_id=1, cancion_id=1, cantidad=1, formato="vinilo", precio=120.50),
            Carrito(usuario_id=1, cancion_id=3, cantidad=1, formato="vinilo", precio=150.00),
        ]
        db.session.add_all(carritos)

        pedidos = [
            Pedido(usuario_id=1, estado="pendiente", metodo_pago="tarjeta", total=270.50),
            Pedido(usuario_id=2, estado="confirmado", metodo_pago="paypal", total=99.99),
        ]
        db.session.add_all(pedidos)

        playlists = [
            Playlist(nombre="Mis Vinilos Favoritos", publica=True, usuario_id=1),
            Playlist(nombre="Colección Rock", publica=True, usuario_id=3),
        ]
        db.session.add_all(playlists)

        reportes = [
            Reporte(tipo="ventas", detalle="Reporte de ventas por género Rock", fecha="2025-09-01"),
            Reporte(tipo="compras", detalle="Historial de compras del usuario Juan Perez", fecha="2025-09-10"),
        ]
        db.session.add_all(reportes)

        db.session.commit()
        print("✅ Datos de prueba insertados en songstock.db")
    else:
        print("ℹ️ La base de datos ya tiene datos, no se insertó nada.")

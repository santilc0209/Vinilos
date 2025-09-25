from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///songstock.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ---------------- Modelos ----------------
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    contraseña = db.Column(db.String(120), nullable=False)
    rol = db.Column(db.String(50), nullable=False)

class Vinilo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    artista = db.Column(db.String(120), nullable=False)
    genero = db.Column(db.String(100))
    anio = db.Column(db.Integer)
    caratula = db.Column(db.String(250))
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)

class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    duracion = db.Column(db.Integer)
    formato = db.Column(db.String(50))
    calidad = db.Column(db.String(50))
    vinilo_id = db.Column(db.Integer, db.ForeignKey('vinilo.id'), nullable=True)

class Carrito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    cancion_id = db.Column(db.Integer, db.ForeignKey('cancion.id'), nullable=False)
    cantidad = db.Column(db.Integer, default=1)
    formato = db.Column(db.String(50))
    precio = db.Column(db.Float, nullable=False)

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    estado = db.Column(db.String(50), default="pendiente")
    metodo_pago = db.Column(db.String(100))
    total = db.Column(db.Float, nullable=False)

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    publica = db.Column(db.Boolean, default=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

class Reporte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50))
    detalle = db.Column(db.Text)
    fecha = db.Column(db.String(50))

# ---------------- Crear DB ----------------
with app.app_context():
    db.create_all()

# ---------------- Helper ----------------
def model_to_dict(obj):
    return {col.name: getattr(obj, col.name) for col in obj.__table__.columns}

def create_endpoints(model, endpoint_name):
    # GET all
    @app.route(f"/{endpoint_name}", methods=["GET"], endpoint=f"get_all_{endpoint_name}")
    def get_all(model=model):
        registros = model.query.all()
        return jsonify([model_to_dict(r) for r in registros])

    # GET by id
    @app.route(f"/{endpoint_name}/<int:registro_id>", methods=["GET"], endpoint=f"get_one_{endpoint_name}")
    def get_one(registro_id, model=model):
        registro = model.query.get_or_404(registro_id)
        return jsonify(model_to_dict(registro))

    # POST
    @app.route(f"/{endpoint_name}", methods=["POST"], endpoint=f"create_{endpoint_name}")
    def create(model=model):
        data = request.json
        nuevo = model(**data)
        db.session.add(nuevo)
        db.session.commit()
        return jsonify(model_to_dict(nuevo)), 201

    # PUT
    @app.route(f"/{endpoint_name}/<int:registro_id>", methods=["PUT"], endpoint=f"update_{endpoint_name}")
    def update(registro_id, model=model):
        registro = model.query.get_or_404(registro_id)
        data = request.json
        for key, value in data.items():
            if hasattr(registro, key):
                setattr(registro, key, value)
        db.session.commit()
        return jsonify(model_to_dict(registro))

    # DELETE
    @app.route(f"/{endpoint_name}/<int:registro_id>", methods=["DELETE"], endpoint=f"delete_{endpoint_name}")
    def delete(registro_id, model=model):
        registro = model.query.get_or_404(registro_id)
        db.session.delete(registro)
        db.session.commit()
        return jsonify({"message": f"{endpoint_name[:-1].capitalize()} eliminado con éxito"})

# ---------------- Endpoints ----------------
create_endpoints(Usuario, "usuarios")
create_endpoints(Vinilo, "vinilos")
create_endpoints(Cancion, "canciones")
create_endpoints(Carrito, "carritos")
create_endpoints(Pedido, "pedidos")
create_endpoints(Playlist, "playlists")
create_endpoints(Reporte, "reportes")

# ---------------- Run ----------------
if __name__ == "__main__":
    app.run(debug=True)

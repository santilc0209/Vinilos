
# 🎵 SongStock Market Place

Proyecto desarrollado en **Python 3 + Flask + SQLite**, que implementa un sistema de gestión para un marketplace de vinilos y canciones.  

Incluye:
- API REST con CRUD completo (Usuarios, Vinilos, Canciones, Carritos, Pedidos, Playlists y Reportes).
- Base de datos en **SQLite** gestionada con **SQLAlchemy**.
- Scripts de inicialización y carga de datos (`seed.py`).
- Documentación de endpoints lista para probar en **Postman**.

-------------------------------------------
📌 Requisitos

- Python 3.9 o superior  
- Pip (gestor de paquetes de Python)  
- (Opcional) Virtualenv para crear un entorno virtual  

-------------------------------------------
⚙️ Instalación

1. Clonar este repositorio:
    git clone https://github.com/TU_USUARIO/songstock-marketplace.git
    cd songstock-marketplace

2. Crear un entorno virtual:
    python3 -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate    # Windows

3. Instalar dependencias:
    pip install -r requirements.txt

-------------------------------------------
🗄️ Base de datos

El proyecto usa **SQLite** (`songstock.db`).  
Para inicializar la base y poblarla con datos de ejemplo:

    python3 seed.py

-------------------------------------------
▶️ Ejecución del servidor

Inicia la aplicación Flask con:

    python3 app.py

Por defecto se abre en:
    http://127.0.0.1:5000

-------------------------------------------
🌐 Endpoints principales

Usuarios
- GET /usuarios
- GET /usuarios/<id>
- POST /usuarios

Vinilos
- GET /vinilos
- GET /vinilos/<id>
- POST /vinilos

Canciones
- GET /canciones
- GET /canciones/<id>
- POST /canciones

Carritos
- GET /carritos
- GET /carritos/<id>
- POST /carritos

Pedidos
- GET /pedidos
- GET /pedidos/<id>
- POST /pedidos

Playlists
- GET /playlists
- GET /playlists/<id>
- POST /playlists

Reportes
- GET /reportes
- GET /reportes/<id>
- POST /reportes

-------------------------------------------
📬 Ejemplo de petición POST

Crear un vinilo:

URL: http://127.0.0.1:5000/vinilos
Headers: Content-Type: application/json
Body:
{
  "nombre": "Random Access Memories",
  "artista": "Daft Punk",
  "genero": "Electrónica",
  "anio": 2013,
  "caratula": "https://url.com/ram.jpg",
  "precio": 200.0,
  "stock": 3
}

-------------------------------------------
🧪 Probar con Postman

Se incluye un archivo **Postman Collection** (`SongStock_API_Full_Coleccion.postman_collection.json`)  
con todas las consultas `GET`, `POST`, `PUT`, y `DELETE` listas para importar.

-------------------------------------------
📊 Diagrama ER (PlantUML)

@startuml
entity "Usuario" as usuario {
  *id : INTEGER <<PK>>
  nombre : VARCHAR(100)
  correo : VARCHAR(120) <<UNIQUE>>
  contraseña : VARCHAR(120)
  rol : VARCHAR(50)
}

entity "Vinilo" as vinilo {
  *id : INTEGER <<PK>>
  nombre : VARCHAR(120)
  artista : VARCHAR(120)
  genero : VARCHAR(100)
  anio : INTEGER
  caratula : VARCHAR(250)
  precio : FLOAT
  stock : INTEGER
}

entity "Cancion" as cancion {
  *id : INTEGER <<PK>>
  titulo : VARCHAR(120)
  duracion : INTEGER
  formato : VARCHAR(50)
  calidad : VARCHAR(50)
  vinilo_id : INTEGER <<FK>>
}

entity "Carrito" as carrito {
  *id : INTEGER <<PK>>
  usuario_id : INTEGER <<FK>>
  cancion_id : INTEGER <<FK>>
  cantidad : INTEGER
  formato : VARCHAR(50)
  precio : FLOAT
}

entity "Pedido" as pedido {
  *id : INTEGER <<PK>>
  usuario_id : INTEGER <<FK>>
  estado : VARCHAR(50)
  metodo_pago : VARCHAR(100)
  total : FLOAT
}

entity "Playlist" as playlist {
  *id : INTEGER <<PK>>
  nombre : VARCHAR(120)
  publica : BOOLEAN
  usuario_id : INTEGER <<FK>>
}

entity "Reporte" as reporte {
  *id : INTEGER <<PK>>
  tipo : VARCHAR(50)
  detalle : TEXT
  fecha : VARCHAR(50)
}

usuario ||--o{ carrito : "tiene"
usuario ||--o{ pedido : "realiza"
usuario ||--o{ playlist : "crea"
vinilo ||--o{ cancion : "incluye"
cancion ||--o{ carrito : "agregada en"
@enduml

-------------------------------------------
🚀 Despliegue en GitHub

1. Inicializar git:
    git init
    git add .
    git commit -m "Primer commit - SongStock Market Place"

2. Conectar remoto:
    git remote add origin https://github.com/TU_USUARIO/songstock-marketplace.git
    git branch -M main
    git push -u origin main

-------------------------------------------
👨‍💻 Autor

Desarrollado por **Santiago López**  
📍 Proyecto académico - 8vo semestre  

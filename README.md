mi_app/
│
├── main.py # Punto de entrada
├── actividades.db # Base de datos SQLite
│
├── db/
│ └── conexion.py # Lógica de conexión y creación de base de datos
│
├── gui/
│ ├── **init**.py
│ ├── menu_principal.py # Menú principal con botones
│ ├── persona_form.py # Pantalla para administrar personas
│ ├── contrato_form.py # Pantalla para registrar contratos
│ └── informe_form.py # Pantalla para ingresar informes
│
└── controllers/
├── persona_controller.py # Funciones de base de datos para PERSONA
└── contrato_controller.py # (y así para cada módulo)

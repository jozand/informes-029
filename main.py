from db.conexion import inicializar_base_datos
from gui.menu_principal import mostrar_menu_principal

def main():
    inicializar_base_datos()
    mostrar_menu_principal()

if __name__ == "__main__":
    main()
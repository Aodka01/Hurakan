
import os
import shutil


def borrar_archivos(carpeta):
    if os.path.exists(carpeta):
        for archivo in os.listdir(carpeta):
            ruta = os.path.join(carpeta, archivo)
            try:
                if os.path.isfile(ruta) or os.path.islink(ruta):
                    os.remove(ruta)   # aquí puede fallar si no tienes permisos
                elif os.path.isdir(ruta):
                    shutil.rmtree(ruta)  # aquí también puede fallar
            except PermissionError:
                print(f"No tienes permisos para borrar: {ruta}")
            except Exception as e:
                print(f"No se pudo borrar {ruta}: {e}")

    else:
        print(f"La carpeta {carpeta} no existe.")

def limpiar_temporales():
    rutas = [
    os.getenv('TEMP'),
    os.path.join(os.getenv('LOCALAPPDATA'), 'Temp')]
    for ruta in rutas:
        print(f"Borrando archivos en: {ruta}")
        borrar_archivos(ruta)
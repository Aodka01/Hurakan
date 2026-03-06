import subprocess

# Lista de servicios que quieres deshabilitar
SERVICIOS = [
    "Spooler",                          # Cola de impresión
    "Fax",                              # Servicio de fax
    "DiagTrack",                        # Telemetría
    "RemoteRegistry",                   # Registro remoto
    "WSearch",                          # Indexador de búsqueda
    "XblGameSave",                      # Xbox Game Save
    "XboxNetApiSvc",                    # Xbox Networking
    "XboxGipSvc",                       # Xbox Input
    "Offline Files",                    # Archivos sin conexión
    "MapsBroker",                       # Mapas
    "RetailDemo",                       # Modo demo
    "WMPNetworkSvc",                    # Red de Windows Media Player
    "CDPSvc",                           # Servicio de Plataforma de Dispositivo Conectado
    "WbioSrvc",                         # Servicio de biometría de Windows
    "ClipSVC",                          # Servicio de cliente de experiencia de Microsoft Store
    "Secondary Logon",                  # Inicio de sesión secundario
    "TabletInputService",               # Servicio de entrada táctil
    "Windows Error Reporting Service",  # Servicio de informes de errores de Windows
    "Windows Biometric Service",        # Servicio de biometría de Windows
]

def deshabilitar_servicios():
    for servicio in SERVICIOS:
        try:
            print(f"🔧 Deshabilitando {servicio}...")
            # Detener el servicio si está corriendo
            subprocess.run(["sc", "stop", servicio], capture_output=True)
            # Deshabilitarlo para que no arranque más
            subprocess.run(["sc", "config", servicio, "start=", "disabled"], capture_output=True)
            print(f"✅ {servicio} detenido y deshabilitado.")
        except Exception as e:
            print(f"❌ Error con {servicio}: {e}")



    
    
        
   
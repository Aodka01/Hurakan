#funcion de opciones de windows
import os
import winreg
import subprocess


def windows_opciones(opcion):
    if opcion == 4:
            try:
                # Activa el plan de energía "Ultimate Performance"
                subprocess.run(["powercfg", "-setactive", "SCHEME_MIN"], check=True)
                print("✅ Plan de energía cambiado a Máximo rendimiento")
            except Exception as e:
                print(f"❌ Error: {e}")

    else:
        comandos = {1: "sfc /scannow", 2: "DISM/Online/Clenup-imagen/RestoreHealth", 3: "chkdsk /f", 5: "taskkill /f /im OneDrive.exe"}
        os.system(comandos[opcion])

def activador_win(win):
    key = ["","TX9XD-98N7V-6WMQ6-BX7FG-H8Q99", "3KHY7-WNT83-DGQKR-F7HPR-844BM", "7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH", 
           "PVMJN-6DFY6-9CCP6-7BKTT-D3WVR", "W269N-WFGWX-YVC9B-4J6C9-T83GX", "MH37W-N47XK-V7XM9-C7227-GCQG9",
             "NPPR9-FWDCX-D2C8J-H872K-2YT43", "DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4", "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2",
               "2WH4N-8QGBV-H22JP-CT43Q-MDWWJ", "WNMTR-4C88C-JK8YV-HQ7T2-76DF9", "2F77B-TNFGY-69QQF-B8YKP-D69TJ"]
    
    selec = key[win]
    os.system("slmgr /skms kms.digiboy.ir")
    os.system("slmgr /skms kms.msguides.com")
    os.system(F"slmgr /ipk {selec}")
    os.system("slmgr /ato")

    print("Windows Activado!")

# funcion de cambiar a windows pro
def cambio_pro():
    os.system("sc config LicenseManager start= auto & net stop LicenseManager")
    os.system("changepk.exe /productkey G4C2N-CDV7R-8FBFG-FB2PV-FJRC6")

# funcion que setea el perfil de rendimiento visual a "Mejor rendimiento"
def set_visual_effects_performance():
    try:
        # Ruta del registro donde se guarda la configuración
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects"
        
        # Abrir la clave en modo escritura
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        
        # Cambiar el valor a 2 (rendimiento)
        winreg.SetValueEx(key, "VisualFXSetting", 0, winreg.REG_DWORD, 2)
        
        # Cerrar la clave
        winreg.CloseKey(key)
        
        print("✅ Perfil de efectos visuales ajustado a 'Mejor rendimiento'")
    except Exception as e:
        print(f"❌ Error al modificar el registro: {e}")
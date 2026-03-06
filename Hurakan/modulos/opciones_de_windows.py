#funcion de opciones de windows
import os


def windows_opciones(opcion):
    comandos = {1: "sfc /scannow", 2: "DISM/Online/Clenup-imagen/RestoreHealth", 3: "chkdsk /f", 4: "powercfg -setactive e9a42b02-d5df-448d-aa00-03f14749eb61",5: "taskkill /f /im OneDrive.exe"}
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
import os 
import shutil
from colorama import init, Fore, Back, Style


#funcion de opciones de windows
def windows_opciones(opcion):
    comandos = {1: "sfc /scannow", 2: "DISM/Online/Clenup-imagen/RestoreHealth", 3: "chkdsk /f", 4: "powercfg -setactive e9a42b02-d5df-448d-aa00-03f14749eb61",5: "taskkill /f /im OneDrive.exe"}
    os.system(comandos[opcion])

# funcion de borrar archivos
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

# funcion de limpiar archivos
def limpiar_temporales():
    rutas = [
    os.getenv('TEMP'),
    os.path.join(os.getenv('LOCALAPPDATA'), 'Temp')]
    for ruta in rutas:
        print(f"Borrando archivos en: {ruta}")
        borrar_archivos(ruta)

# activador de windows 11/10
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

# funcion de herramientas de red
def red(selec):
    comandos_red = {1: "ipconfig /release",2: "ipconfig /renew",3: "ipconfig /flushdns",4: "arp -a",5: "nersh int ip reset",6: "netsh winsock reset",7: "netsh dns cache delete" }
    selcec_red = comandos_red[selec]
    os.system(selcec_red)

while True:
    print(Fore.LIGHTRED_EX + " ▄▄▄      ▒█████   ██████   ██  ██ ▄▄▄▄      ")
    print(                   "▒████▄   ▒██▒  ██▒██    ▒█▒ ██  ██ █████▄    ")
    print(                   "▒██  ▀█▄ ▒██░  ██░██     ██ ████   █▌  ▀█▄  ")
    print(                   "░██▄▄▄▄██▒██   ██░██     █░ ██ ██ ░██▄▄▄▄██ ")
    print(                   " ▓█    ██░ ████▓▒▒███████▒░▒██  ██ ██    ██▒")
    print(                   " ▒▒   ▓▒ ░ ▒░▒░▒░▒ ▒▓▒ ▒ ░ ▒▒▓  ▒  ▒▒   ▓▒ ░")
    print(                   "  ▒   ▒▒ ░ ░ ▒ ▒░░ ░▒  ░ ░ ░ ▒  ▒   ▒   ▒▒ ░")
    print(                   "  ░   ▒  ░ ░ ░ ▒ ░  ░  ░   ░ ░  ░   ░   ▒   ")
    print(                   "      ░  ░   ░ ░       ░     ░          ░  ░ Todo los derechos reservados")
    Fore.RESET

    print(Fore.LIGHTGREEN_EX + "==seleccione el numero de la herramienta=="+ Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + "1.Herramientas de windows🔄️\n2.Herramientas de red🛜\n3.optimizacion debil\n4.optimizacion normal\n5.optimizacion Fuerte (*Demora mas tiempo*)\n6.salir👋\n" + Fore.RESET)
    numero = int(input(Fore.MAGENTA + "introduce la opcion: " + Fore.RESET))

    if numero == 1:
        print(Fore.LIGHTGREEN_EX + "==opciones y herramienas de windows🔄️==" + Fore.RESET)
        print(Fore.LIGHTYELLOW_EX + "1.Escaneo y reparacion de archivos de windows\n2.Reparar imagen de windows\n3.Revisar y reparar el disco\n4.Colocar a windows en maximo rendimiento*Solo se puede vercion pro/superior*\n5.cambiar a windows pro\n6. activar windows\n7.limpiar archivos temporales\n8.cerrar Onedrive\n9.regresar\n" + Fore.RESET)
        opcion = int(input(Fore.MAGENTA + "introduce la opcion: " + Fore.RESET))

        
        if opcion in [1,2,3,4]:
        
            windows_opciones(opcion)

        elif opcion == 5:
            cambio_pro()

        elif opcion == 6:
            print(Fore.LIGHTGREEN_EX + "==Seleccione su version==" + Fore.RESET)
            print(Fore.LIGHTYELLOW_EX + "1.Windows 11/10 Home\n2.Windows 11/10 Home N\n3.Windows 11/10 Home Single Language\n4.Windows 11/10 Home Country Specific\n5.Windows 11/10 Professional\n6.Windows 11/10 Professional N\n7.Windows 11/10 Enterprise\n8.Windows 11/10 Enterprise N\n9.Windows 11/10 Education\n10.Windows 11/10 Education N\n11.Windows 11/10 Enterprise 2015 LTSB\n12.Windows 11/10 Enterprise 2015 LTSB N\n13.regresar" + Fore.RESET)
            eleccion = int(input(Fore.MAGENTA + "introduce la opcion: " + Fore.RED))

            if eleccion in [1,2,3,4,5,6,7,8,9,10,11,12]:
                activador_win(eleccion)
                
                print("activando‼️")

            elif eleccion == 13:
                
                pass

            else:
                print(Fore.RED + "Opcion Invalida" + Fore.RESET)

        elif opcion == 7:
            
            limpiar_temporales()

        elif opcion == 8:
            opcion = 5
            windows_opciones(opcion)
            
            print("OneDrive cerrado‼️")

        elif opcion == 9:
            
            pass
        else:
            print(Fore.RED + "Opcion Invalida" + Fore.RESET)


    elif numero == 2:
        print(Fore.LIGHTGREEN_EX + "==Opciones de red🛜==" + Fore.RESET)
        print(Fore.LIGHTYELLOW_EX + "1. liberar ip actual\n2. Renovar ip\n3. eliminar cache DNS\n4. ver ip <-> mac\n5. restablecer TCP/IP\n6. restablecer winsock (corrige problemas de red)\n7. Optimizar cache DNS\n8. regresar\n" + Fore.RESET)
        opcion_red = int(input(Fore.MAGENTA + "introduce la opcion: " + Fore.RESET))


        if opcion_red in [1, 2, 3, 4, 5, 6, 7]:
            red(opcion_red)

        elif opcion_red == 8:
            
            pass

        else:
            print(Fore.RED + "Opcion Invalida" + Fore.RESET)

    elif numero == 3:
        print(Fore.LIGHTGREEN_EX + "optimizacion debil" + Fore.RESET)
        limpiar_temporales()
        red(3)
        
        print("optimizacion debil realizada‼️")

    elif numero == 4:
        print(Fore.LIGHTGREEN_EX + "optimizacion normal" + Fore.RESET)
        limpiar_temporales()
        red(3)
        red(2)
        red(5)
        red(7)
        windows_opciones(5)
        
        print("optimizacion normal realizada‼️")

    elif numero == 5:
        print(Fore.LIGHTGREEN_EX + "optimizacion fuerte" + Fore.RESET)
        limpiar_temporales()
        windows_opciones(1)
        windows_opciones(2)
        windows_opciones(3)
        windows_opciones(4)
        windows_opciones(5)
        red(3)
        red(2)
        red(5)
        red(7)
        print("optimizacion fuerte realizada‼️")

    elif numero == 6:
        print(Fore.RED + "saliendo..." + Fore.RESET)    
        break
    
    else:
        print(Fore.RED + "Opcion Invalida" + Fore.RESET)
        
    
    



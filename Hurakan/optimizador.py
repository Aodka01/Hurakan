import os 
from colorama import init, Fore, Back, Style
from modulos.opciones_de_windows import windows_opciones
from modulos.Borrar_archivo import borrar_archivos 
from modulos.Borrar_archivo import limpiar_temporales
from modulos.opciones_de_windows import activador_win, cambio_pro
from modulos.opciones_red import red
from modulos.opciones_de_windows import set_visual_effects_performance
from modulos.kill_task import deshabilitar_servicios


#agrega soporte para colores en la consola de winows
os.system('reg add HKCU\\Console /v VirtualTerminalLevel /t REG_DWORD /d 1 /f')



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
        print(Fore.LIGHTYELLOW_EX + "1.Escaneo y reparacion de archivos de windows\n2.Reparar imagen de windows\n3.Revisar y reparar el disco\n4.Colocar a windows en maximo rendimiento*Solo se puede vercion pro/superior*\n5.cambiar a windows pro\n6.activar windows\n7.limpiar archivos temporales\n8.cerrar Onedrive\n9.perfil de rendimiento visual\n10.Deshabilitar servicios inecesarios\n11.regresar\n" + Fore.RESET)
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
            set_visual_effects_performance()

        elif opcion == 10:
            deshabilitar_servicios()
            print("Servicios inecesarios deshabilitados‼️")

        elif opcion == 11:
            pass
        else:
            print(Fore.RED + "Opcion Invalida" + Fore.RESET)


    elif numero == 2:
        print(Fore.LIGHTGREEN_EX + "==Opciones de red🛜==" + Fore.RESET)
        print(Fore.LIGHTYELLOW_EX + "1.liberar ip actual\n2.Renovar ip\n3.eliminar cache DNS\n4.ver ip <-> mac\n5.restablecer TCP/IP\n6.restablecer winsock (corrige problemas de red)\n7.Optimizar cache DNS\n8.regresar\n" + Fore.RESET)
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
        deshabilitar_servicios()
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
        
    
    



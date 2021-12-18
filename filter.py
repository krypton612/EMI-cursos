import os
import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore


emi_url = "https://www.emi.app.info.bo/valida/valida_posgrado.php?P=E*R*M"


def exploitInfoEmi(md5):
    
    peticion = requests.get("https://www.emi.app.info.bo/valida/valida_posgrado.php?P=E*R*M"+md5)
    if peticion.status_code == 200:
        soup = BeautifulSoup(peticion.text, 'html.parser')
        
        tabla_items = soup.find_all('h5')

        nombre=[500]
        curso=[500]
        horas=[10]
        fecha=[500]
        archi=[400]



        i = 0
        almacen = open ('__data__/archivo.txt','a')

        for datos in tabla_items:
            if i == 0:
                nombre = datos.text
            if i == 1:
                curso = datos.text
            if i == 2:
                horas = datos.text
            if i == 3:
                fecha = datos.text
            if i == 4:
                archi = datos.text
            i = i + 1
        almacen.write("======================================\r\n")
        almacen.write(f"Nombre del estudiante  : {nombre}\r\n")
        almacen.write(f"Curso cursado          : {curso}\r\n") 
        almacen.write(f"horas cursadas         : {horas}\r\n")
        almacen.write(f"fecha del curso        : {fecha}\r\n")
        almacen.write(f"archivo del estudiante : {archi}\r\n")

        print(Fore.RESET+ "======================================\n")
        print(Fore.GREEN + f"Nombre del estudiante  : {nombre}\n")
        print(f"Curso cursado          : {curso}\n")
        print(f"horas cursadas         : {horas}\n")
        print(f"fecha del curso        : {fecha}\n")
        print(f"archivo del estudiante : {archi}\n")

    else:
        print("Error")



if __name__ == '__main__':
    sep_pos = -len(os.linesep)
    with open("informacion.txt","r") as archivo:
        for codigo in archivo:
            control = "https://www.emi.app.info.bo/valida/valida_posgrado.php?P=E*R*Mf899139df5e1059396431415e770c6dd"
            if codigo[sep_pos:] == os.linesep:
                codigo = codigo[:sep_pos]
            
            exploitInfoEmi(codigo)
    print(Fore.GREEN + "Se obtuvo todo con exito")


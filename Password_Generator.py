import string
import secrets
import time
import os

print("##########################################################")      
print("GENERAZIONE PASSWORD BY GIUSEPPE MAGLIONE")   
print("##########################################################")  
time.sleep(2)
os.system('cls')


lett= string.ascii_letters
num=string.digits

lung= input("SCEGLI LA LUNGHEZZA DESIDERATA: ")
print("SCEGLI QUALE TIPO TI SERVE \n")
time.sleep(1)
def controllo():

  Password="".join(secrets.choice(lett)for i in range(int(lung)))
  Pin="".join(secrets.choice(num)for i in range(int(lung)))

  scelta= int(input("Clicca 1 Per Generare Una Password, Clicca 2 Per Generare Un Pin : "))
         
  if scelta == 1:
      os.system('cls')
      print("#####################################") 
      print("La Password Generata:",Password)
      print("#####################################")

  if scelta== 2:
     os.system('cls')
     print("#####################################") 
     print("Il Pin Generato:",Pin)  
     print("#####################################")  
     
  if scelta > 2 :
     os.system('cls')
     print("##########################################################") 
     print("HAI INSERITO UN CARATTERE NON VALIDO, RIAVVIA IL PROGRAMMA")
     print("##########################################################") 

controllo()
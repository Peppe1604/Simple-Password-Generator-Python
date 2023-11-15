<a name="Ritorna-sopra"></a>

<br />
  <h3 align="center" color="red">Simple Password Generator </h3>

  <p align="center">
    Un semplice programma per creare password o pin!
    <br />
    <a href="https://github.com/Peppe1604/Simple-Password-Generator-Python"><strong>Esplora il progetto »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Peppe1604/Simple-Password-Generator-Python/issues">Riporta qui i problemi</a>
  </p>
</div>

<!-- CONTENUTI -->
<details>
  <summary>Tabella con Riferimenti</summary>
  <ol>
    <li>
      <a href="#Approposito-del-Progetto">Approposito del Progetto</a>
           <ul>
        <li><a href="#Creato-con">Creato con</a></li>
        </ul>
    </li>
    <li>
      <a href="#Prerequisiti">Prerequisiti</a>
      <ul>
        <li><a href="#Tipo-di-uso">Tipo di uso</a></li>
      </ul>
    </li>
    <li><a href="#Librerie">Librerie</a></li>
       <ul>
        <li><a href="#Libreria-String">String</a></li>
         <li><a href="#Libreria-Secrets">Secrets</a></li>
        <li><a href="#Libreria-Time">Time</a></li>
        <li><a href="#Libreria-Os">Os</a></li>
      </ul>
    <li><a href="#Spiegazione">Spiegazione Codice</a></li>
    <ul>
        <li><a href="#Lunghezza-Password">Lunghezza Password</a></li>
        <li><a href="#Confronti">Confronti</a></li>
        </ul>
  </ol>
</details>


 # Approposito del Progetto :bangbang:

Ciao ho creato questo progetto per uno scopo auto-didattico. Ho iniziato da poco tempo ad usare python e mi sto esercitando nel fare parecchi programmi che potranno (forse) tornare utili. :smile:

Motivi:
* Anche tu potresti imparare qualcosina da questa mia piccola guida :bulb: 
* Potresti scaricare il codice e divertirti nel modificarlo come vuoi :hammer:

<p align="right">:arrow_up:(<a href="#Ritorna-sopra">Ritorna Sopra</a>) :arrow_up:</p> 

### Creato con

Questo progetto è stato creato con il linguaggio di programmazione Python, mediante L'editor Visual Studio Code

* Python version: 3.12.0a1

<p align="right">:arrow_up:(<a href="#Ritorna-sopra">Ritorna Sopra</a>) :arrow_up:</p> 

# Prerequisiti :bangbang:

_Qui sotto ti mostro di cosa hai bisogno prima di poter usare al meglio lo script da me pubblicato._

1. Prima di tutto ti serve un editor di testo 
2. Il download è disponibile per qualsiasi Sistema Operativo
3. link download: [https://code.visualstudio.com/download](https://code.visualstudio.com/download) :link:
 
<p align="right">:arrow_up:(<a href="#Ritorna-sopra">Ritorna Sopra</a>) :arrow_up:</p> 

## Tipo di uso
Una volta scaricato il tuo Editor di testo (come quello citato sopra) sei pronto per incimentarti nel capire cosa ci è scritto dentro.
Quando avrai capito potrai farne l'uso che vuoi e sbizzarirti a modificarlo per renderlo migliore. :cyclone:

<p align="right">:arrow_up:(<a href="#Ritorna-sopra">Ritorna Sopra</a>) :arrow_up:</p> 

# Librerie :books:

_Nell'informatica una libreria è <strong>una raccolta di funzioni e programmi.</strong> Le librerie sono richiamate dai programmi informatici per aggiungere nuove funzionalità al codice e possono essere richiamate anche da programmi differenti._

### Libreria String :bookmark:
Per implementare una libreria nel linguaggio Python basta digitare <strong>import</strong> seguito dal nome della libreria.<br>
Nel programma troverai: 

```Py
   import = string
   ``` 
   <br>
In Python 3.0. Il modulo string contiene parecchie costanti e classi utili per lavorare con oggetti stringa ed unicode e questa discussione si concentrerà su di essi. 
Le costanti nel modulo stringa possono essere usate per specificare categorie di caratteri come ascii_letters e digits (lettere ASCII e cifre). <br>

Nel programma ho richiamato questi parametri nelle variabili <strong>"lett"</strong> e <strong>"num"</strong>
  <br>
   
   ```Py
 lett= string.ascii_letters
num=string.digits
   ``` 
   <br>
   
   ### Libreria Secrets :bookmark:
   _Il modulo secret viene utilizzato per generare numeri casuali crittograficamente forti adatti alla gestione di dati come password, autenticazione dell'account,   token di sicurezza._
     <br>
     
   ```Py
    import= secrets
   ``` 
   <br>
   
   Nel programma ho richiamato questi parametri nelle variabili <strong>"Password"</strong> e <strong>"Pin"</strong>, settandoli automaticamente come stringhe
   <br>
   
   ```Py
    Password="".join(secrets.choice(lett)for i in range(int(lung)))
    Pin="".join(secrets.choice(num)for i in range(int(lung)))
   ``` 
   <br>
   
   Per far funzionare nel modo giusto la libreria ha bisogno di precisi parametri, in questo caso ho deciso che la <strong>"Password"</strong> deve contenere unicamente caratteri grazie al richiamo della variabile <strong>"lett"</strong> precedentemente citata, stessa cosa per il <strong>"Pin"</strong> che deve contenere unicamente numeri grazie al richiamo della variabile <strong>"num"</strong> precedentemente citata
   <br>
   
   ### Libreria Time :bookmark:
  _Il modulo time espone le funzioni della libreria C per manipolare date e tempo._
       <br>
     
   ```Py
    import= time
   ``` 
   <br>
    Nel programma ho richiamato i parametri della libreria con <strong>"time.sleep()"</strong>, settandoli a seconda delle mie preferenze per far "dormire" il programma per poi continuare nella sua esecuzione
   <br>
   
  ### Libreria Os :bookmark:
  _Il modulo os permette di compiere diverse operazioni sul S.O. tramite il programma python. Ad esempio, cancellare o rinominare un file, cambiare i permessi in una cartella, trovare l'estensione di un file, il pathname, ecc._
       <br>
     
   ```Py
    import= os
   ``` 
   <br>
    Nel programma ho utilizzato questa libreria per "sgombrerare" la schermata e renderla più leggibile all'utente grazie all'uso della funzione <strong>os.system('cls')</strong>
<p align="right">:arrow_up:(<a href="#Ritorna-sopra">Ritorna Sopra</a>) :arrow_up:</p> 
    
   <br>
   
   # Spiegazione Codice :unlock:
   
 _Siamo arrivati alla fine del programma, qui ti spiego come l'utente imposta la lunghezza predefinita della password/pin e a cosa serve il confronto  nella parte finale del programma._
 <br>
 
 ## Lunghezza Password :mag_right:
  _Ora ti mostro come l'utente riesce a decidere la lunghezza massima della password/pin che vuole generare:_
   <br>
     
   ```Py
   lung= input("SCEGLI LA LUNGHEZZA DESIDERATA: ")
   ``` 
   <br>
   Grazie a una variabile chiamata "lung" riusciamo a far impostare una dimensione massima da input all'utente
   <br>
   
 ## Confronti :unlock:
  _In questa ultima parte della spiegazione vedrai come si riesce a confrontare a seconda della scelta dell'utente quale tipo di blocco far eseguire_
  <br>
     
   ```Py
    scelta= int(input("Clicca 1 Per Generare Una Password, Clicca 2 Per Generare Un Pin : "))
   ``` 
   <br>
   Grazie a una variabile chiamata "scelta" riusciamo a far scegliere all'utente quale blocco di istruzioni far eseguire, e lo verificheremo grazie a un confronto che ti spiegherò qui sotto
   <br>
   
  ### Primo confronto :white_check_mark:
  Come puoi ben notare ora ti mostro a cosa serve il Primo confronto
  <br>
     
   ```Py
     if scelta == 1:
      os.system('cls')
      print("#####################################") 
      print("La Password Generata:",Password)
      print("#####################################")
   ``` 
   <br>
    Con questo confronto, verifico se l'utente che inserisce il numero, che tipologia di password desidera. In questo caso se l'utente invia il numero 1 il programma gli genere una password casuale con lunghezza scelta proprio dall'utente
       <br>
       
### Secondo confronto :white_check_mark:
  Come puoi ben notare ora ti mostro a cosa serve il Secondo confronto<br>
     
   ```Py
  if scelta== 2:
     os.system('cls')
     print("#####################################") 
     print("Il Pin Generato:",Pin)  
     print("#####################################")  
   ``` 
   <br>
    Con questo confronto, verifico se l'utente che inserisce il numero, che tipologia di password desidera. In questo caso se l'utente invia il numero 2 il programma gli genere un pin casuale con lunghezza scelta proprio dall'utente
       <br>
       
   ### Terzo confronto :white_check_mark:
  Come puoi ben notare ora ti mostro a cosa serve il Terzo confronto<br>
     
   ```Py
   if scelta > 2 :
     os.system('cls')
     print("##########################################################") 
     print("HAI INSERITO UN CARATTERE NON VALIDO, RIAVVIA IL PROGRAMMA")
     print("##########################################################") 
   ``` 
   <br>
    Con questo confronto, verifico se l'utente inserisce un numero maggiore di 2. In questo caso se l'utente invia un numero maggiore di 2 il programma gli genere un messaggio di "errore", perché le decisioni massime che si possono prendere solamente 2 in questo programma, cioè la Password e il Pin.
 <p align="right">:arrow_up:(<a href="#Ritorna-sopra">Ritorna Sopra</a>) :arrow_up:</p> 
       <br><br>
       
## Come contattarmi
 Twitter: - [@Peppe16040](https://twitter.com/Peppe16040):exclamation:

 Project Link: [https://github.com/Peppe1604/Symple-Password-Generator-Python](https://github.com/Peppe1604/Symple-Password-Generator-Python):exclamation:

<p align="right">:arrow_up:(<a href="#Ritorna-sopra">Ritorna Sopra</a>) :arrow_up:</p> 

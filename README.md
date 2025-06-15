# 🔐 Password Generator Avanzato

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Version-2.0-orange.svg" alt="Version">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20MacOS-lightgrey.svg" alt="Platform">
</p>

<p align="center">
  <strong>Un generatore di password sicuro e user-friendly con interfaccia colorata per il terminale</strong>
  <br />
  <em>✨ Ora con installazione automatica per tutte le piattaforme! ✨</em>
  <br /><br />
  <a href="#-installazione">Installazione Rapida</a> •
  <a href="#-demo">Demo</a> •
  <a href="#-caratteristiche">Caratteristiche</a> •
  <a href="#-utilizzo">Utilizzo</a> •
  <a href="#-contribuire">Contribuire</a>
</p>

---

## 🚀 Quick Start

```bash
# Linux/macOS
./install.sh

# Windows
install.bat
```

---

## 📋 Indice

- [Quick Start](#-quick-start)
- [Novità v2.0](#-novità-v20)
- [Demo](#-demo)
- [Caratteristiche](#-caratteristiche)
- [Requisiti](#-requisiti)
- [Installazione](#-installazione)
- [Utilizzo](#-utilizzo)
- [Disinstallazione](#️-disinstallazione)
- [Struttura del Codice](#-struttura-del-codice)
- [Opzioni Disponibili](#-opzioni-disponibili)
- [Sicurezza](#-sicurezza)
- [FAQ](#-faq)
- [Contribuire](#-contribuire)
- [Autore](#-autore)
- [Licenza](#-licenza)

## 🆕 Novità v2.0

- ✅ **Script di installazione automatica** per tutte le piattaforme
- ✅ **Interfaccia colorata** con ASCII art e animazioni
- ✅ **Valutazione sicurezza** in tempo reale con barra visiva
- ✅ **Password personalizzabili** con selezione interattiva dei caratteri
- ✅ **Loading animations** durante la generazione
- ✅ **Box decorativi** per output più leggibile
- ✅ **Script di disinstallazione** inclusi

## 🎬 Demo

<p align="center">
  <img src="demo.gif" alt="Demo del Password Generator" width="600">
</p>

> *Esempio di generazione di una password sicura con valutazione della forza*

## ✨ Caratteristiche

### 🎨 Interfaccia Utente
- **Output colorato**: Interfaccia terminale con colori ANSI per una migliore leggibilità
- **ASCII Art**: Banner accattivante all'avvio
- **Animazioni**: Loading animation durante la generazione
- **Box decorativi**: Output organizzato in box e tabelle

### 🔐 Funzionalità di Sicurezza
- **Generazione crittografica**: Utilizza il modulo `secrets` per una generazione sicura
- **Valutazione forza**: Analisi in tempo reale della sicurezza della password
- **Password personalizzabili**: Scegli esattamente quali caratteri includere
- **Garanzia caratteri**: Le password sicure includono sempre tutti i tipi di caratteri

### 💾 Gestione Password
- **Salvataggio opzionale**: Salva le password generate con etichette personalizzate
- **Log temporale**: Ogni password salvata include data e ora di generazione
- **File di output**: Tutte le password salvate in `passwords_generate.txt`

### 📦 Installazione e Portabilità
- **Script di installazione automatica**: Setup con un click per Windows, Linux e macOS
- **Zero dipendenze**: Usa solo librerie standard Python
- **Cross-platform**: Funziona su tutti i sistemi operativi
- **Disinstallazione pulita**: Script di rimozione inclusi

## 🛠️ Requisiti

### Requisiti Minimi
- **Python**: 3.6 o superiore
- **Sistema Operativo**: Windows, Linux, macOS
- **Terminale**: Con supporto colori ANSI (la maggior parte dei terminali moderni)

### Dipendenze
Il progetto utilizza solo librerie standard Python:
- `string` - Gestione caratteri
- `secrets` - Generazione crittografica
- `time` - Animazioni e timestamp
- `os` - Operazioni di sistema
- `sys` - Informazioni sul sistema
- `datetime` - Gestione date e ore

## 📦 Installazione

### 🚀 Installazione Automatica (Consigliata)

Il progetto include script di installazione automatica per tutte le piattaforme:

#### 🐧 Linux / macOS

```bash
# 1. Clona il repository
git clone https://github.com/Peppe1604/Simple-Password-Generator-Python.git
cd Simple-Password-Generator-Python

# 2. Rendi eseguibile lo script
chmod +x install.sh

# 3. Esegui l'installazione
./install.sh
```

Lo script `install.sh`:
- ✅ Verifica automaticamente Python
- ✅ Crea directory di installazione in `~/.local/share/password-generator`
- ✅ Installa il comando `passgen` nel PATH
- ✅ Crea script di disinstallazione

#### 🪟 Windows

```batch
# 1. Clona il repository (o scarica ZIP)
git clone https://github.com/Peppe1604/Simple-Password-Generator-Python.git
cd Simple-Password-Generator-Python

# 2. Esegui l'installer (doppio click o da prompt)
install.bat
```

Lo script `install.bat`:
- ✅ Verifica automaticamente Python
- ✅ Installa in `%LOCALAPPDATA%\PasswordGenerator`
- ✅ Crea collegamento sul Desktop
- ✅ Opzione per aggiungere al PATH di sistema
- ✅ Crea script di disinstallazione

### 📝 Installazione Manuale

Se preferisci installare manualmente:

#### 1. Clona il Repository

```bash
git clone https://github.com/Peppe1604/Simple-Password-Generator-Python.git
cd Simple-Password-Generator-Python
```

#### 2. Verifica Python

```bash
python --version
# o
python3 --version
```

Assicurati di avere Python 3.6 o superiore.

#### 3. Esegui il Programma

```bash
python Password_Generator.py
# o
python3 Password_Generator.py
```

## 🚀 Utilizzo

### Avvio Rapido

#### Se hai installato con gli script:

**Linux/macOS:**
```bash
# Usa uno di questi comandi da qualsiasi directory
passgen
# oppure
password-generator
```

**Windows:**
- Usa il collegamento sul Desktop "Password Generator"
- Oppure apri il prompt e digita: `passgen`

#### Se usi l'esecuzione manuale:

```bash
# Dalla directory del progetto
python Password_Generator.py
# o
python3 Password_Generator.py
```

### Come Usare il Programma

1. **Scegli un'opzione dal menu**
   - Digita un numero da 1 a 5 per le opzioni
   - Digita 0 per uscire

2. **Imposta la lunghezza**
   - Inserisci un numero tra 4 e 128

3. **Ricevi la tua password**
   - Visualizza la password generata
   - Controlla la valutazione di sicurezza
   - Scegli se salvarla

## 🗑️ Disinstallazione

### Linux/macOS
```bash
# Se hai installato con install.sh
~/.local/share/password-generator/uninstall.sh
```

### Windows
```batch
# Se hai installato con install.bat
# Vai in %LOCALAPPDATA%\PasswordGenerator e esegui:
uninstall.bat

# Oppure usa Pannello di Controllo → Programmi
```

### Esempio di Utilizzo

```
🔐 MENU PRINCIPALE
──────────────────────────────────────────────────
  1. 📝 Password solo lettere
  2. 🔢 PIN solo numeri
  3. 🔤 Password alfanumerica
  4. 🛡️  Password sicura (tutti i caratteri)
  5. ⚙️  Password personalizzata
  0. 🚪 Esci

👉 Scegli un'opzione: 4

📏 Lunghezza desiderata (4-128): 16

⠏ Generazione password sicura...
✓ Generazione password sicura completata!

════════════════════════════════════════════════════════════
║                                                          ║
║  ✅ PASSWORD SICURA GENERATO CON SUCCESSO!              ║
║                                                          ║
════════════════════════════════════════════════════════════

┌────────────────────┐
│  K9@mP#xL2$nQ7&w  │
└────────────────────┘

📊 STATISTICHE:
  • Lunghezza: 16 caratteri
  • Generata: 15:42:33

🔒 ANALISI SICUREZZA:
  ✓ Lunghezza ≥ 8
  ✓ Lunghezza ≥ 12
  ✓ Contiene minuscole
  ✓ Contiene maiuscole
  ✓ Contiene numeri
  ✓ Contiene simboli

💪 Forza:
  [████████████████████████████████████████] FORTE
```

## 📁 Struttura del Codice

### 📂 File del Progetto

```
Simple-Password-Generator-Python/
├── Password_Generator.py    # Script principale
├── README.md               # Documentazione
├── install.sh              # Installer Linux/macOS
├── install.bat             # Installer Windows
└── passwords_generate.txt  # File output (creato dopo primo salvataggio)
```

### 🏗️ Struttura del Codice Principal

```
Password_Generator.py
├── Class Colors          # Definizioni colori ANSI
├── Class PasswordGenerator
│   ├── __init__()       # Inizializzazione
│   ├── clear_screen()   # Pulizia schermo cross-platform
│   ├── print_colored()  # Stampa testo colorato
│   ├── print_box()      # Crea box decorativi
│   ├── print_banner()   # Mostra ASCII art
│   ├── print_loading()  # Animazione caricamento
│   ├── get_lunghezza()  # Input validato lunghezza
│   ├── mostra_menu()    # Menu principale
│   ├── genera_password_base()     # Generazione base
│   ├── genera_password_sicura()   # Generazione sicura
│   ├── genera_password_personalizzata() # Personalizzata
│   ├── mostra_risultato()  # Output formattato
│   ├── valuta_sicurezza()  # Analisi sicurezza
│   ├── salva_password()    # Salvataggio opzionale
│   └── esegui()           # Loop principale
└── Main execution
```

## 🔧 Opzioni Disponibili

### 1. Password Solo Lettere
- Genera password contenenti solo lettere (maiuscole e minuscole)
- Ideale per sistemi che non accettano caratteri speciali

### 2. PIN Solo Numeri
- Genera PIN numerici
- Perfetto per codici di accesso, carte di credito, etc.

### 3. Password Alfanumerica
- Combina lettere e numeri
- Buon compromesso tra sicurezza e compatibilità

### 4. Password Sicura
- Include lettere, numeri e simboli speciali
- Garantisce almeno un carattere per ogni tipo
- Massima sicurezza

### 5. Password Personalizzata
- Scegli esattamente quali tipi di caratteri includere
- Controllo completo sulla composizione

## 🔒 Sicurezza

### Criteri di Valutazione

Il generatore valuta la sicurezza basandosi su:

| Criterio | Punti | Descrizione |
|----------|-------|-------------|
| Lunghezza ≥ 8 | +1 | Minimo consigliato |
| Lunghezza ≥ 12 | +1 | Lunghezza ottimale |
| Lettere minuscole | +1 | Varietà caratteri |
| Lettere maiuscole | +1 | Maggiore entropia |
| Numeri | +1 | Complessità aggiuntiva |
| Simboli speciali | +1 | Massima sicurezza |

### Livelli di Sicurezza

- **🔴 DEBOLE** (0-2 punti): Non consigliata
- **🟡 MEDIA** (3-4 punti): Accettabile per usi non critici
- **🟢 FORTE** (5-6 punti): Consigliata per tutti gli usi

## ❓ FAQ

### Il programma è sicuro?
Sì! Utilizza il modulo `secrets` di Python, progettato specificamente per generazione crittografica sicura.

### Dove vengono salvate le password?
Nel file `passwords_generate.txt` nella stessa directory del programma. **Nota**: questo file non è criptato!

### Come installo il programma?
Usa gli script di installazione automatica:
- **Linux/macOS**: `./install.sh`
- **Windows**: Doppio click su `install.bat`

### Posso usarlo su Windows?
Sì! Il programma è cross-platform e funziona su Windows, Linux e macOS. Usa `install.bat` per l'installazione automatica su Windows.

### I colori non funzionano?
Alcuni terminali potrebbero non supportare i colori ANSI. Il programma funzionerà comunque, solo senza colori. Su Windows 10+ i colori dovrebbero funzionare automaticamente.

### Come disinstallo il programma?
- **Linux/macOS**: Esegui `~/.local/share/password-generator/uninstall.sh`
- **Windows**: Esegui `uninstall.bat` dalla cartella di installazione

### Devo installare dipendenze aggiuntive?
No! Il programma usa solo librerie standard di Python. Non serve pip o installazioni extra.

### Posso modificare i caratteri speciali utilizzati?
Sì! Modifica la variabile `self.speciali` nella classe `PasswordGenerator`.

### Gli script di installazione sono sicuri?
Sì! Gli script:
- Non richiedono privilegi di amministratore (a meno che tu non voglia installare globalmente)
- Non modificano file di sistema critici
- Creano sempre uno script di disinstallazione
- Sono completamente open source e verificabili

## 🤝 Contribuire

Contribuzioni sono sempre benvenute! Ecco come puoi aiutare:

1. **Fork** il progetto
2. Crea un **branch** per la tua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** le tue modifiche (`git commit -m 'Add some AmazingFeature'`)
4. **Push** al branch (`git push origin feature/AmazingFeature`)
5. Apri una **Pull Request**

### Idee per Contribuzioni

- [ ] Aggiungere supporto multi-lingua
- [ ] Implementare GUI con tkinter
- [ ] Aggiungere copia negli appunti
- [ ] Crittografia del file di output
- [ ] Generatore di passphrase
- [ ] Export in formati diversi (JSON, CSV)
- [ ] Integrazione con password manager
- [ ] Supporto per profili di password (salvare configurazioni)
- [ ] Modalità batch per generare multiple password
- [ ] API REST per integrazione con altri tool
- [ ] Versione web del generatore
- [ ] Supporto per password pronounceable
- [ ] Statistiche di utilizzo e report

## 👨‍💻 Autore

**Giuseppe Maglione**

- GitHub: [@Peppe1604](https://github.com/Peppe1604)
- Email: [giuseppe.maglione@example.com](mailto:giuseppe.maglione@example.com)

## 📄 Licenza

Questo progetto è distribuito sotto licenza MIT. Vedi il file [LICENSE](LICENSE) per maggiori dettagli.

---

<p align="center">
  Made with ❤️ by Giuseppe Maglione
  <br>
  ⭐ Se ti piace questo progetto, lascia una stella su GitHub! ⭐
</p>
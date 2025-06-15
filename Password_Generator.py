import string
import secrets
import time
import os
import sys
from datetime import datetime

# Classe per i colori nel terminale
class Colors:
    """Colori ANSI per il terminale"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    # Colori di sfondo
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

class PasswordGenerator:
    def __init__(self):
        self.lettere = string.ascii_letters
        self.numeri = string.digits
        self.speciali = string.punctuation
        self.colors = Colors()
        
    def clear_screen(self):
        """Pulisce lo schermo in modo cross-platform"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_colored(self, text, color="", bold=False, end="\n"):
        """Stampa testo colorato"""
        if bold:
            print(f"{self.colors.BOLD}{color}{text}{self.colors.ENDC}", end=end)
        else:
            print(f"{color}{text}{self.colors.ENDC}", end=end)
    
    def print_box(self, text, color=Colors.CYAN, width=60):
        """Stampa testo in un box decorativo"""
        print(f"{color}{'═' * width}{self.colors.ENDC}")
        padding = (width - len(text) - 2) // 2
        print(f"{color}║{' ' * padding}{text}{' ' * (width - padding - len(text) - 2)}║{self.colors.ENDC}")
        print(f"{color}{'═' * width}{self.colors.ENDC}")
    
    def print_banner(self):
        """Mostra il banner ASCII art"""
        self.clear_screen()
        banner = f"""
{self.colors.CYAN}╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║  {self.colors.BOLD}{self.colors.GREEN}██████╗  █████╗ ███████╗███████╗    ██████╗ ███████╗███╗   ██╗{self.colors.CYAN} ║
║  {self.colors.BOLD}{self.colors.GREEN}██╔══██╗██╔══██╗██╔════╝██╔════╝   ██╔════╝ ██╔════╝████╗  ██║{self.colors.CYAN} ║
║  {self.colors.BOLD}{self.colors.GREEN}██████╔╝███████║███████╗███████╗   ██║  ███╗█████╗  ██╔██╗ ██║{self.colors.CYAN} ║
║  {self.colors.BOLD}{self.colors.GREEN}██╔═══╝ ██╔══██║╚════██║╚════██║   ██║   ██║██╔══╝  ██║╚██╗██║{self.colors.CYAN} ║
║  {self.colors.BOLD}{self.colors.GREEN}██║     ██║  ██║███████║███████║   ╚██████╔╝███████╗██║ ╚████║{self.colors.CYAN} ║
║  {self.colors.BOLD}{self.colors.GREEN}╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝ ╚══════╝╚═╝  ╚═══╝{self.colors.CYAN} ║
║                                                               ║
║           {self.colors.BOLD}{self.colors.WARNING}🔐 GENERATORE PASSWORD BY GIUSEPPE MAGLIONE 🔐{self.colors.CYAN}        ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝{self.colors.ENDC}
        """
        print(banner)
        time.sleep(2)
    
    def print_loading(self, message="Caricamento", duration=1):
        """Mostra un'animazione di caricamento"""
        animation = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        end_time = time.time() + duration
        i = 0
        
        while time.time() < end_time:
            print(f"\r{self.colors.CYAN}{animation[i % len(animation)]} {message}...{self.colors.ENDC}", end="")
            time.sleep(0.1)
            i += 1
        print(f"\r{self.colors.GREEN}✓ {message} completato!{self.colors.ENDC}" + " " * 20)
    
    def get_lunghezza(self):
        """Ottiene e valida la lunghezza desiderata con input colorato"""
        while True:
            try:
                self.print_colored("\n📏 Lunghezza desiderata ", self.colors.CYAN, end="")
                self.print_colored("(4-128)", self.colors.WARNING, end="")
                self.print_colored(": ", self.colors.CYAN, end="")
                
                lung = int(input())
                
                if 4 <= lung <= 128:
                    self.print_colored(f"✅ Lunghezza impostata: {lung} caratteri", self.colors.GREEN)
                    return lung
                else:
                    self.print_colored("❌ La lunghezza deve essere tra 4 e 128 caratteri!", self.colors.FAIL)
                    time.sleep(1)
            except ValueError:
                self.print_colored("❌ Per favore inserisci un numero valido!", self.colors.FAIL)
                time.sleep(1)
    
    def mostra_menu(self):
        """Mostra il menu delle opzioni con colori e icone"""
        print(f"\n{self.colors.CYAN}{'─' * 50}{self.colors.ENDC}")
        self.print_colored("🔐 MENU PRINCIPALE", self.colors.BOLD + self.colors.CYAN, bold=True)
        print(f"{self.colors.CYAN}{'─' * 50}{self.colors.ENDC}\n")
        
        opzioni = [
            ("1", "📝 Password solo lettere", self.colors.GREEN),
            ("2", "🔢 PIN solo numeri", self.colors.BLUE),
            ("3", "🔤 Password alfanumerica", self.colors.WARNING),
            ("4", "🛡️  Password sicura (tutti i caratteri)", self.colors.HEADER),
            ("5", "⚙️  Password personalizzata", self.colors.CYAN),
            ("0", "🚪 Esci", self.colors.FAIL)
        ]
        
        for num, desc, color in opzioni:
            print(f"  {color}{num}. {desc}{self.colors.ENDC}")
        
        print(f"\n{self.colors.CYAN}{'─' * 50}{self.colors.ENDC}")
    
    def genera_password_base(self, lunghezza, caratteri):
        """Genera una password con animazione"""
        self.print_loading("Generazione password", 0.5)
        return "".join(secrets.choice(caratteri) for _ in range(lunghezza))
    
    def genera_password_sicura(self, lunghezza):
        """Genera una password sicura con garanzia di tutti i tipi di caratteri"""
        self.print_loading("Generazione password sicura", 0.7)
        
        if lunghezza < 4:
            return self.genera_password_base(lunghezza, self.lettere + self.numeri + self.speciali)
        
        password = [
            secrets.choice(string.ascii_lowercase),
            secrets.choice(string.ascii_uppercase),
            secrets.choice(string.digits),
            secrets.choice(self.speciali)
        ]
        
        tutti = self.lettere + self.numeri + self.speciali
        for _ in range(lunghezza - 4):
            password.append(secrets.choice(tutti))
        
        secrets.SystemRandom().shuffle(password)
        return ''.join(password)
    
    def genera_password_personalizzata(self, lunghezza):
        """Permette all'utente di personalizzare i tipi di caratteri"""
        caratteri = ""
        print(f"\n{self.colors.CYAN}⚙️  PERSONALIZZAZIONE PASSWORD{self.colors.ENDC}")
        print(f"{self.colors.CYAN}{'─' * 30}{self.colors.ENDC}\n")
        
        opzioni = [
            ("lettere minuscole", string.ascii_lowercase, "🔡"),
            ("lettere maiuscole", string.ascii_uppercase, "🔠"),
            ("numeri", self.numeri, "🔢"),
            ("simboli speciali", self.speciali, "💠")
        ]
        
        for nome, chars, emoji in opzioni:
            self.print_colored(f"{emoji} Includere {nome}? ", self.colors.CYAN, end="")
            self.print_colored("(s/n): ", self.colors.WARNING, end="")
            if input().lower() == 's':
                caratteri += chars
                self.print_colored(f"  ✅ {nome.capitalize()} aggiunte", self.colors.GREEN)
        
        if not caratteri:
            self.print_colored("\n❌ Devi selezionare almeno un tipo di carattere!", self.colors.FAIL)
            return None
        
        return self.genera_password_base(lunghezza, caratteri)
    
    def mostra_risultato(self, password, tipo):
        """Mostra il risultato con formattazione accattivante"""
        self.clear_screen()
        
        # Box per il risultato
        print(f"\n{self.colors.GREEN}{'═' * 60}{self.colors.ENDC}")
        print(f"{self.colors.GREEN}║{' ' * 58}║{self.colors.ENDC}")
        print(f"{self.colors.GREEN}║{self.colors.BOLD}  ✅ {tipo} GENERATO CON SUCCESSO!{' ' * (54 - len(tipo))}║{self.colors.ENDC}")
        print(f"{self.colors.GREEN}║{' ' * 58}║{self.colors.ENDC}")
        print(f"{self.colors.GREEN}{'═' * 60}{self.colors.ENDC}\n")
        
        # Password in un box speciale
        print(f"{self.colors.CYAN}┌{'─' * (len(password) + 4)}┐{self.colors.ENDC}")
        print(f"{self.colors.CYAN}│ {self.colors.BOLD}{self.colors.WARNING} {password} {self.colors.CYAN}│{self.colors.ENDC}")
        print(f"{self.colors.CYAN}└{'─' * (len(password) + 4)}┘{self.colors.ENDC}")
        
        # Informazioni aggiuntive
        print(f"\n{self.colors.BLUE}📊 STATISTICHE:{self.colors.ENDC}")
        print(f"  • Lunghezza: {self.colors.BOLD}{len(password)}{self.colors.ENDC} caratteri")
        print(f"  • Generata: {self.colors.BOLD}{datetime.now().strftime('%H:%M:%S')}{self.colors.ENDC}")
        
        # Valutazione sicurezza
        self.valuta_sicurezza(password)
    
    def valuta_sicurezza(self, password):
        """Valuta la sicurezza con indicatori visivi colorati"""
        print(f"\n{self.colors.BLUE}🔒 ANALISI SICUREZZA:{self.colors.ENDC}")
        
        criteri = [
            ("Lunghezza ≥ 8", len(password) >= 8),
            ("Lunghezza ≥ 12", len(password) >= 12),
            ("Contiene minuscole", any(c.islower() for c in password)),
            ("Contiene maiuscole", any(c.isupper() for c in password)),
            ("Contiene numeri", any(c.isdigit() for c in password)),
            ("Contiene simboli", any(c in self.speciali for c in password))
        ]
        
        punteggio = 0
        for criterio, soddisfatto in criteri:
            if soddisfatto:
                print(f"  {self.colors.GREEN}✓ {criterio}{self.colors.ENDC}")
                punteggio += 1
            else:
                print(f"  {self.colors.FAIL}✗ {criterio}{self.colors.ENDC}")
        
        # Barra di sicurezza visiva
        print(f"\n{self.colors.BLUE}💪 Forza:{self.colors.ENDC}")
        barra_lunghezza = 40
        barra_piena = int((punteggio / 6) * barra_lunghezza)
        
        if punteggio <= 2:
            colore = self.colors.FAIL
            livello = "DEBOLE"
        elif punteggio <= 4:
            colore = self.colors.WARNING
            livello = "MEDIA"
        else:
            colore = self.colors.GREEN
            livello = "FORTE"
        
        print(f"  [{colore}{'█' * barra_piena}{self.colors.ENDC}{'░' * (barra_lunghezza - barra_piena)}] {colore}{livello}{self.colors.ENDC}")
    
    def salva_password(self, password):
        """Chiede se salvare la password con conferma visiva"""
        print(f"\n{self.colors.CYAN}{'─' * 50}{self.colors.ENDC}")
        self.print_colored("💾 Vuoi salvare questa password? ", self.colors.CYAN, end="")
        self.print_colored("(s/n): ", self.colors.WARNING, end="")
        
        if input().lower() == 's':
            self.print_colored("📝 Inserisci un'etichetta: ", self.colors.CYAN, end="")
            nome = input()
            
            with open("passwords_generate.txt", 'a', encoding='utf-8') as f:
                f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {nome}: {password}\n")
            
            self.print_colored("\n✅ Password salvata con successo in 'passwords_generate.txt'", self.colors.GREEN)
            time.sleep(1)
    
    def esegui(self):
        """Metodo principale con gestione colorata"""
        self.print_banner()
        
        while True:
            self.mostra_menu()
            
            self.print_colored("\n👉 Scegli un'opzione: ", self.colors.CYAN, end="")
            
            try:
                scelta = int(input())
            except ValueError:
                self.print_colored("❌ Inserisci un numero valido!", self.colors.FAIL)
                time.sleep(1)
                continue
            
            if scelta == 0:
                self.print_loading("Chiusura in corso", 0.5)
                self.print_colored("\n👋 Grazie per aver usato Password Generator!", self.colors.GREEN, bold=True)
                self.print_colored("   Arrivederci e resta al sicuro! 🔐\n", self.colors.CYAN)
                break
            
            if scelta not in range(1, 6):
                self.print_colored("❌ Opzione non valida! Scegli tra 0 e 5.", self.colors.FAIL)
                time.sleep(1)
                continue
            
            lunghezza = self.get_lunghezza()
            
            # Genera in base alla scelta
            if scelta == 1:
                password = self.genera_password_base(lunghezza, self.lettere)
                tipo = "PASSWORD ALFABETICA"
            elif scelta == 2:
                password = self.genera_password_base(lunghezza, self.numeri)
                tipo = "PIN NUMERICO"
            elif scelta == 3:
                password = self.genera_password_base(lunghezza, self.lettere + self.numeri)
                tipo = "PASSWORD ALFANUMERICA"
            elif scelta == 4:
                password = self.genera_password_sicura(lunghezza)
                tipo = "PASSWORD SICURA"
            elif scelta == 5:
                password = self.genera_password_personalizzata(lunghezza)
                if password is None:
                    continue
                tipo = "PASSWORD PERSONALIZZATA"
            
            self.mostra_risultato(password, tipo)
            self.salva_password(password)
            
            # Chiede se continuare
            print(f"\n{self.colors.CYAN}{'─' * 50}{self.colors.ENDC}")
            self.print_colored("🔄 Vuoi generare un'altra password? ", self.colors.CYAN, end="")
            self.print_colored("(s/n): ", self.colors.WARNING, end="")
            
            if input().lower() != 's':
                self.print_loading("Chiusura in corso", 0.5)
                self.print_colored("\n👋 Grazie per aver usato Password Generator!", self.colors.GREEN, bold=True)
                self.print_colored("   Arrivederci e resta al sicuro! 🔐\n", self.colors.CYAN)
                break
            
            self.clear_screen()

# Controllo se il terminale supporta i colori ANSI
def supporta_colori():
    """Verifica se il terminale supporta i colori ANSI"""
    # Windows
    if os.name == 'nt':
        # Abilita i colori ANSI su Windows 10
        os.system('')
        return True
    # Unix/Linux/MacOS
    return hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()

# Avvia il programma
if __name__ == "__main__":
    if not supporta_colori():
        print("⚠️  Il tuo terminale potrebbe non supportare i colori.")
        print("    L'applicazione funzionerà comunque!\n")
    
    try:
        generator = PasswordGenerator()
        generator.esegui()
    except KeyboardInterrupt:
        print("\n\n⚠️  Programma interrotto dall'utente.")
        print("👋 Arrivederci!\n")
    except Exception as e:
        print(f"\n❌ Si è verificato un errore: {e}")
        print("   Riprova o contatta il supporto.\n")
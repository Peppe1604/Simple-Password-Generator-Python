#!/bin/bash

# Script di installazione per Password Generator
# Compatibile con Linux e macOS

set -e  # Esce se un comando fallisce

# Colori per output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Banner
echo -e "${BLUE}"
echo "╔═══════════════════════════════════════════════════╗"
echo "║     PASSWORD GENERATOR - INSTALLAZIONE            ║"
echo "╚═══════════════════════════════════════════════════╝"
echo -e "${NC}"

# Funzione per stampare messaggi colorati
print_message() {
    echo -e "${2}${1}${NC}"
}

# Controllo permessi
if [[ $EUID -eq 0 ]]; then
   print_message "⚠️  Non eseguire questo script come root!" "$RED"
   exit 1
fi

# Controllo Python
print_message "🔍 Controllo versione Python..." "$YELLOW"

if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    print_message "❌ Python non trovato! Installa Python 3.6+ prima di continuare." "$RED"
    exit 1
fi

# Verifica versione Python
PYTHON_VERSION=$($PYTHON_CMD -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED_VERSION="3.6"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    print_message "❌ Python $PYTHON_VERSION trovato, ma è richiesto Python $REQUIRED_VERSION+" "$RED"
    exit 1
fi

print_message "✅ Python $PYTHON_VERSION trovato!" "$GREEN"

# Crea directory di installazione
INSTALL_DIR="$HOME/.local/share/password-generator"
BIN_DIR="$HOME/.local/bin"

print_message "📁 Creazione directory di installazione..." "$YELLOW"

mkdir -p "$INSTALL_DIR"
mkdir -p "$BIN_DIR"

# Copia i file
print_message "📋 Copia dei file..." "$YELLOW"

cp Password_Generator.py "$INSTALL_DIR/"
cp README.md "$INSTALL_DIR/" 2>/dev/null || true

# Crea script eseguibile
print_message "🔨 Creazione comando 'passgen'..." "$YELLOW"

cat > "$BIN_DIR/passgen" << EOF
#!/bin/bash
cd "$INSTALL_DIR"
$PYTHON_CMD Password_Generator.py "\$@"
EOF

chmod +x "$BIN_DIR/passgen"

# Crea alias alternativo
ln -sf "$BIN_DIR/passgen" "$BIN_DIR/password-generator"

# Verifica se ~/.local/bin è nel PATH
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    print_message "⚠️  Aggiungi $HOME/.local/bin al tuo PATH" "$YELLOW"
    
    # Determina quale file di configurazione shell usare
    if [ -n "$BASH_VERSION" ]; then
        SHELL_CONFIG="$HOME/.bashrc"
    elif [ -n "$ZSH_VERSION" ]; then
        SHELL_CONFIG="$HOME/.zshrc"
    else
        SHELL_CONFIG="$HOME/.profile"
    fi
    
    echo "" >> "$SHELL_CONFIG"
    echo "# Password Generator" >> "$SHELL_CONFIG"
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$SHELL_CONFIG"
    
    print_message "✅ PATH aggiornato in $SHELL_CONFIG" "$GREEN"
    print_message "   Esegui: source $SHELL_CONFIG" "$YELLOW"
fi

# Crea file di disinstallazione
print_message "📝 Creazione script di disinstallazione..." "$YELLOW"

cat > "$INSTALL_DIR/uninstall.sh" << EOF
#!/bin/bash
echo "🗑️  Disinstallazione Password Generator..."
rm -rf "$INSTALL_DIR"
rm -f "$BIN_DIR/passgen"
rm -f "$BIN_DIR/password-generator"
echo "✅ Disinstallazione completata!"
EOF

chmod +x "$INSTALL_DIR/uninstall.sh"

# Test installazione
print_message "🧪 Test installazione..." "$YELLOW"

if [ -x "$BIN_DIR/passgen" ]; then
    print_message "✅ Installazione completata con successo!" "$GREEN"
else
    print_message "❌ Errore durante l'installazione!" "$RED"
    exit 1
fi

# Istruzioni finali
echo ""
print_message "╔════════════════════════════════════════════════╗" "$GREEN"
print_message "║    INSTALLAZIONE COMPLETATA CON SUCCESSO! 🎉   ║" "$GREEN"
print_message "╚════════════════════════════════════════════════╝" "$GREEN"
echo ""
print_message "📌 Per usare il programma:" "$BLUE"
print_message "   • passgen" "$BLUE"
print_message "   • password-generator" "$BLUE"
echo ""
print_message "📌 Per disinstallare:" "$BLUE"
print_message "   • $INSTALL_DIR/uninstall.sh" "$BLUE"
echo ""

# Chiedi se vuole eseguire subito
read -p "Vuoi avviare Password Generator ora? (s/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Ss]$ ]]; then
    exec "$BIN_DIR/passgen"
fi
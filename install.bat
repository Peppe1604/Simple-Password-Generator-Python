@echo off
setlocal enabledelayedexpansion

:: Script di installazione per Password Generator su Windows
:: Richiede diritti di amministratore per alcune operazioni

title Password Generator - Installazione

:: Colori (Windows 10+)
color 0A

:: Banner
echo.
echo ============================================================
echo            PASSWORD GENERATOR - INSTALLAZIONE
echo ============================================================
echo.

:: Controllo Python
echo [*] Controllo installazione Python...

python --version >nul 2>&1
if %errorlevel% neq 0 (
    py --version >nul 2>&1
    if !errorlevel! neq 0 (
        echo [!] ERRORE: Python non trovato!
        echo.
        echo Per favore installa Python 3.6+ da https://python.org
        echo Assicurati di selezionare "Add Python to PATH" durante l'installazione.
        echo.
        pause
        exit /b 1
    ) else (
        set PYTHON_CMD=py
    )
) else (
    set PYTHON_CMD=python
)

:: Verifica versione Python
for /f "tokens=2" %%i in ('%PYTHON_CMD% --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [+] Python %PYTHON_VERSION% trovato!

:: Directory di installazione
set INSTALL_DIR=%LOCALAPPDATA%\PasswordGenerator
set DESKTOP=%USERPROFILE%\Desktop

echo.
echo [*] Creazione directory di installazione...
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

:: Copia file
echo [*] Copia dei file del programma...
copy /Y "Password_Generator.py" "%INSTALL_DIR%\" >nul
if exist "README.md" copy /Y "README.md" "%INSTALL_DIR%\" >nul

:: Crea file batch per esecuzione
echo [*] Creazione comando 'passgen'...

echo @echo off > "%INSTALL_DIR%\passgen.bat"
echo cd /d "%INSTALL_DIR%" >> "%INSTALL_DIR%\passgen.bat"
echo %PYTHON_CMD% Password_Generator.py %%* >> "%INSTALL_DIR%\passgen.bat"

:: Crea collegamento sul desktop
echo [*] Creazione collegamento sul Desktop...

powershell -Command "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%DESKTOP%\Password Generator.lnk'); $Shortcut.TargetPath = '%INSTALL_DIR%\passgen.bat'; $Shortcut.WorkingDirectory = '%INSTALL_DIR%'; $Shortcut.IconLocation = 'shell32.dll,47'; $Shortcut.Description = 'Generatore di Password Sicure'; $Shortcut.Save()"

:: Aggiungi al PATH (opzionale, richiede admin)
echo.
echo [?] Vuoi aggiungere 'passgen' al PATH di sistema? (S/N)
echo     (Richiede privilegi di amministratore)
set /p ADD_PATH=

if /i "%ADD_PATH%"=="S" (
    echo [*] Tentativo di aggiunta al PATH...
    
    :: Controlla privilegi admin
    net session >nul 2>&1
    if %errorlevel% neq 0 (
        echo [!] Privilegi di amministratore richiesti!
        echo     Rilancia questo script come amministratore per aggiungere al PATH.
    ) else (
        :: Aggiungi al PATH di sistema
        setx PATH "%PATH%;%INSTALL_DIR%" /M >nul 2>&1
        if !errorlevel! equ 0 (
            echo [+] Aggiunto al PATH di sistema!
        ) else (
            :: Prova PATH utente
            setx PATH "%PATH%;%INSTALL_DIR%" >nul 2>&1
            echo [+] Aggiunto al PATH utente!
        )
    )
)

:: Crea script di disinstallazione
echo [*] Creazione script di disinstallazione...

echo @echo off > "%INSTALL_DIR%\uninstall.bat"
echo echo. >> "%INSTALL_DIR%\uninstall.bat"
echo echo Disinstallazione Password Generator... >> "%INSTALL_DIR%\uninstall.bat"
echo echo. >> "%INSTALL_DIR%\uninstall.bat"
echo del "%DESKTOP%\Password Generator.lnk" 2^>nul >> "%INSTALL_DIR%\uninstall.bat"
echo timeout /t 2 /nobreak ^>nul >> "%INSTALL_DIR%\uninstall.bat"
echo cd .. >> "%INSTALL_DIR%\uninstall.bat"
echo rmdir /s /q "%INSTALL_DIR%" >> "%INSTALL_DIR%\uninstall.bat"
echo echo. >> "%INSTALL_DIR%\uninstall.bat"
echo echo Disinstallazione completata! >> "%INSTALL_DIR%\uninstall.bat"
echo pause >> "%INSTALL_DIR%\uninstall.bat"

:: Test installazione
echo.
echo [*] Test installazione...

if exist "%INSTALL_DIR%\Password_Generator.py" (
    echo [+] File principale: OK
) else (
    echo [!] File principale: ERRORE
    set INSTALL_ERROR=1
)

if exist "%DESKTOP%\Password Generator.lnk" (
    echo [+] Collegamento Desktop: OK
) else (
    echo [!] Collegamento Desktop: ERRORE
)

:: Risultato finale
echo.
echo ============================================================

if defined INSTALL_ERROR (
    echo            INSTALLAZIONE COMPLETATA CON ERRORI!
    echo.
    echo Alcuni componenti potrebbero non essere stati installati.
) else (
    echo            INSTALLAZIONE COMPLETATA CON SUCCESSO!
    echo.
    echo Password Generator e' stato installato in:
    echo %INSTALL_DIR%
    echo.
    echo Puoi avviarlo:
    echo  - Dal collegamento sul Desktop
    echo  - Digitando 'passgen' nel prompt (se aggiunto al PATH)
    echo  - Eseguendo %INSTALL_DIR%\passgen.bat
    echo.
    echo Per disinstallare:
    echo  - Esegui %INSTALL_DIR%\uninstall.bat
)

echo ============================================================
echo.

:: Chiedi se vuole avviare
echo [?] Vuoi avviare Password Generator ora? (S/N)
set /p START_NOW=

if /i "%START_NOW%"=="S" (
    echo.
    echo Avvio Password Generator...
    start "" "%INSTALL_DIR%\passgen.bat"
)

echo.
pause
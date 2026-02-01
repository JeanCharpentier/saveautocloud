🎒 SAC - Save Auto Cloud (v1.0)

*** ENGLISH ***
SAC (Save Auto Cloud) is a lightweight utility designed to synchronize game saves that do not natively support Cloud saves (retro games, emulators, Epic Games, GOG, etc.) between your Desktop, Laptop, and Steam Deck using Dropbox.

✨ Features
🔄 Auto-Sync: Automatically moves your saves to the Cloud and creates a transparent symbolic link (Junction) for the game.

📂 Smart List: Automatically detects games already synced in your Dropbox folder.

🔍 Integrated Help: Direct link to PCGamingWiki to instantly find your save locations (especially useful for Proton prefixes).

🛡️ Safe: Security alerts and automatic filtering of system/hidden folders.

💾 Persistent: Remembers your Dropbox root path via a sac_config.json file.

🚀 Installation & Launch
🪟 Windows
Download SAC_SaveAutoCloud.exe.

Important: Right-click and select "Run as Administrator" (required to create system directory junctions).

🐧 Steam Deck (SteamOS / Linux)
On Linux, the software runs directly via Python for maximum compatibility.

Copy SAC_SaveAutoCloud.py to your Deck.

Open a terminal (Konsole) in the script's folder.

Run the script:

Bash
python3 SAC_SaveAutoCloud.py
Note: If the system reports a missing Tkinter module, use sudo pacman -S tk (requires a set password).

📖 How to use
Initial Setup (Machine with existing saves):

Select your Dropbox folder.

Enter the Game Name.

Select the local folder where the saves are currently located.

Click ACTIVATE. SAC moves the files to the Cloud and links the folder.

On other machines (Recovery):

Wait for Dropbox to finish syncing.

Launch SAC.

Select the game from the dropdown list.

Select the (usually empty) local save folder on this machine.

Click ACTIVATE.

⚠️ WARNING: Always perform a manual backup of your save files before the first synchronization!

🎁 Dropbox
If you don't have an account yet, you can get 500 MB of bonus space for free by using this referral link:
Get Dropbox for free

Developed for the gaming community. "Carry your adventures in your SAC."

*** FRENCH ***
SAC (Save Auto Cloud) est un utilitaire léger conçu pour synchroniser vos sauvegardes de jeux vidéo qui ne supportent pas nativement le Cloud (vieux jeux, émulateurs, Epic Games, GOG, etc.) entre votre PC fixe, votre Laptop et votre Steam Deck via Dropbox.

✨ Fonctionnalités
🔄 Synchronisation Automatique : Déplace vos sauvegardes vers le Cloud et crée un lien symbolique transparent pour le jeu.

📂 Liste Intelligente : Détecte automatiquement les jeux déjà présents dans votre Dropbox.

🔍 Aide Intégrée : Lien direct vers PCGamingWiki pour trouver l'emplacement de vos sauvegardes (utile pour les préfixes Proton).

🛡️ Sécurisé : Alertes de sécurité et filtrage des dossiers système/cachés.

💾 Mémoire : Retient l'emplacement de votre dossier Dropbox via un fichier sac_config.json.

🚀 Installation & Lancement
🪟 Windows
Téléchargez le fichier SAC_SaveAutoCloud.exe.

Important : Faites un clic droit et choisissez "Exécuter en tant qu'administrateur" (requis pour créer les jonctions de dossiers).

🐧 Steam Deck (SteamOS / Linux)
Sur Linux, le logiciel se lance directement avec Python pour une compatibilité maximale.

Copiez le fichier SAC_SaveAutoCloud.py sur votre Deck.

Ouvrez un terminal (Konsole) dans le dossier du script.

Installez les dépendances si nécessaire (Tkinter est généralement inclus) :

Bash
python3 SAC_SaveAutoCloud.py
Note : Si le système vous indique qu'il manque Tkinter, utilisez la commande sudo pacman -S tk (nécessite d'avoir défini un mot de passe passwd).

📖 Mode d'emploi
Configuration initiale (Machine avec les sauvegardes) :

Sélectionnez votre dossier Dropbox.

Tapez le Nom du jeu.

Sélectionnez le dossier local où se trouvent les sauvegardes actuelles.

Cliquez sur ACTIVER. Le SAC déplace les fichiers vers le Cloud et crée le lien.

Sur les autres machines (Récupération) :

Attendez que Dropbox finisse la synchronisation.

Lancez le SAC.

Sélectionnez le jeu dans la liste déroulante.

Sélectionnez le dossier de destination local (souvent vide ou à créer).

Cliquez sur ACTIVER.

⚠️ ATTENTION : Toujours faire une copie de sauvegarde manuelle de vos fichiers avant la première synchronisation !

🎁 Dropbox
Si vous n'avez pas encore de compte, vous pouvez obtenir 500 Mo de bonus gratuitement en passant par ce lien de parrainage :
Obtenir Dropbox gratuitement

Développé pour la communauté gaming. "Transportez vos aventures dans votre SAC."

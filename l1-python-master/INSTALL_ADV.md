# Installation avancée

## <a name="install_git"></a>Guide d'installation de Git
Un *système de gestion de versions* (*Version Control System* ou *VCS* en anglais) est un logiciel qui conserve une trace de chaque modification importante effectuée sur un ensemble de documents.
Dans le contexte de la programmation, il sauvegarde et suit les modifications d'un ensemble de fichiers sources.

L'outil que nous allons utiliser pour cela se nomme [`git`](https://git-scm.com/).
C'est à l'heure actuelle (en 2023) le logiciel open source le plus utilisé pour cette tâche.

L'outil `git` gérera votre projet localement sur une machine mais il est très utile de faire héberger son projet sur le web.
C'est ce que propose la plateforme [github](https://github.com/).
Ce service offre la possibilité de sauvegarder son projet dans le cloud afin de pouvoir le récupérer de n'importe quelle machine connectée.

### Création d'un compte `github`
À l'adresse https://github.com/join, créer un compte en précisant :
* le nom d'utilisateur (*username*) `uvsqXXXXXXXX` en remplaçant `XXXXXXXX` par votre numéro d'étudiant,
* l'adresse mail (*Email address*) `prenom.nom@ens.uvsq.fr`,
* et un mot de passe (*Password*).

Il faut ensuite consulter les mails à cette adresse pour confirmer l'adresse d'inscription.

### Copier le projet dans son espace `github` personnel
> Un "projet" sous `git` et `github` se nomme un *dépôt* (*repository* en anglais).
> Attention car la notion de projet (*project*) sous `github` est différente.

Le dépôt `git` contenant l'ensemble du projet n'est pas modifiable par tout le monde.
Pour pouvoir faire des changements dessus, il faut donc d'abord le *copier* dans votre espace personnel.
Sous `github`, cette opération se nomme un **fork** et est utilisée pour copier un dépôt entre deux espaces utilisateurs.

La procédure pour cela est la suivante :
1. se rendre sur la page `github` du dépôt à copier (https://github.com/uvsq-info/l1-python dans notre cas),
1. cliquer sur le bouton *Fork* en haut à droite de l'écran
1. sélectionner votre espace personnel comme destination du fork

Vous disposez maintenant d'une copie personnelle du dépôt avec une URL qui devrait ressembler à https://github.com/uvsqXXXXXXXX/l1-python.

### Installer `git`
L'étape suivante consiste à récupérer une copie locale du projet.
Nous utiliserons pour cela l'interface `git` intégrée à l'éditeur de texte.
Cependant, cette dernière s'appuie sur l'outil en ligne de commande `git` que nous allons installer maintenant.

#### Sous Windows
1. Télécharger [git sous Windows](https://git-scm.com/download/win)
1. Double-cliquer sur le fichier téléchargé pour lancer l'installation
1. Conserver les choix par défaut proposés lors de l'installation **sauf pour les étapes en gras ci-dessous** :
    - accepter la licence ("Next")
    - "Select Destination Location", ("Next")
    - "Select Components", ("Next")
    - "Select Start Menu Folder", ("Next")
    - "Choosing the default editor used by Git", **choisir "Use Visual Studio Code as Git's default editor"** ("Next")
    - "Let Git decide" ("Next")
    - "Adjusting your PATH environment", déjà sélectionné "Git from the command line and also from 3rd-party software" ("Next")
    - "Choosing the SSH executable", déjà sélectionné "Use OpenSSH" ("Next")
    - "Choosing HTTPS transport backend", déjà sélectionné "Use the OpenSSL library" ("Next")
    - "Configuring the line ending conversions", déjà sélectionné "Checkout Windows-style, commit Unix-style line endings" ("Next")
    - "Configuring the terminal emulator to use with Git Bash", déjà sélectionné "Use MinTTY (the default terminal of MSYS2)" ("Next")
    - "Choose the default behavior of 'git pull'", "Default (fast-forward or merge)" ("Next")
    - "Choose a credentiel helper", **choisir "None"**("Next")
    - "Configuring extra options", "Enable file system caching" (déjà sélectionné) et "Enable symbolic links" ("Next")
    - "Configuring experimental options", rien n'est sélectionné ("Install")
    - "Completing the Git Setup Wizard", **décocher tout** ("Next")

#### Sous Mac OS
1. Installer [Homebrew](https://brew.sh/)
1. Dans un terminal, taper :
    ```bash
    brew install git
    ```

Une alternative pourrait être d'installer `git` par l'intermédiaire de `conda` ([package git pour conda](https://anaconda.org/conda-forge/git)).

#### Sous Linux
L'installation de `git` est très simple mais dépend de la distribution Linux installée.
Par exemple, avec une distribution `debian`, il suffit de taper dans un terminal :
```bash
sudo apt update
sudo apt install git
```

Pour trouver la commande correspondant à votre système, rendez-vous sur la page [Download for Linux and Unix](https://git-scm.com/download/linux) et choisissez les commandes adéquates.

#### Finaliser et vérifier l'installation
1. Sous Windows, ouvrir un *Git Bash*; sous Mac OS et Linux, ouvrir un terminal et taper :
    ```bash
    git --version
    ```
    qui devrait afficher (les deux derniers numéros peuvent être différents) :
    ```bash
    git version 2.33.0
    ```
1. Dans le même terminal, taper (**en substituant votre prénom et votre nom**) :
    ```bash
    git config --global user.name "Prénom NOM"
    git config --global user.email "prenom.nom@ens.uvsq.fr"
    git config --global color.ui auto
    ```
1. Fermer le terminal

### Récupérer et initialiser le projet localement
Cette étape va consister à créer sur votre machine une copie du dépôt `github`.
Nous utiliserons pour cela Visual Studio Code (abrégé en VSCode dans la suite).

#### Création d'une copie locale du projet
1. Lancer VSCode
1. Cliquer sur l'icone en forme de graphe à 3 noeuds à gauche de l'écran (*Source Control* ou *Ctrl+Shift+G*)
1. Sélectionner "Clone from Github"
1. Cliquez sur "Allow" dans la boite de dialogue puis accepter les différents choix proposés dans le navigateur ou dans une boite de dialogue VSCode (le navigateur doit être celui où le fork a été fait dans votre espace personnel github). 
1. Sélectionner le dépôt "uvsqXXXXXXXX/l1-python" dans la liste déroulante puis choisissez l'emplacement local du projet
1. Ouvrir ensuite le répertoire créé ci-dessus

## <a name="install_virt"></a>Création de l'environnement virtuel Python
Pour isoler l'environnement du projet d'éventuelles autres versions de Python ou de bibliothèques, nous allons créer un environnement `conda` spécifique.

1. Sous Windows, Mac et Linux s'assurer que le répertoire du projet est ouvert dans VSCode puis ouvrir un terminal (menu Terminal/New Terminal ou View/Terminal).
    Taper (Il faut garder sa connexion internet active pendant la création de l'environnement)
    ```bash
    conda env create
    conda activate l1-python
    ```
1. Fermer le terminal en tapant
    ```bash
    exit
    ```

### Si `conda` n'est pas accessible dans le terminal VSCode
Sous Windows, il est possible que `conda` ne soit pas accessible dans le "Command Prompt".
Pour palier ce problème, faire *Ctrl ,* (Ctrl et virgule en même temps), rechercher "terminal.integrated.profiles.windows" et cliquer sur "Edit in settings.json".

Supprimer l'intégralité du contenu du fichier et copier-coller ceci à la place:
```json
{
    "terminal.integrated.profiles.windows": {
        "Command Prompt": {
            "path": [
                "${env:windir}\\Sysnative\\cmd.exe",
                "${env:windir}\\System32\\cmd.exe"
            ],
            "args":["/K", "C:\\Users\\${env:USERNAME}\\miniconda3\\Scripts\\activate.bat C:\\Users\\${env:USERNAME}\\miniconda3"],
            "icon": "terminal-cmd"
        }
    },
    "terminal.integrated.defaultProfile.windows": "Command Prompt"
}
```

Ce qui revient à taper:
```
[« /k », « C:\\users\\moi\\miniconda3\\Scripts\\activate.bat C: C:\\users\\moi\\miniconda3] 
```
dans le « args » du bloc « Command Prompt »
Si le répertoire par défaut pour installer miniconda n'a pas été choisi, adapter le chemin d'installation.
Enfin, utiliser *File/Save* ou Ctrl+S pour sauvegarder vos modifications puis fermer l'onglet settings.json.

Une alternative consiste à :
1. ouvrir un *anaconda prompt* (hors de VSCode)
1. se placer dans le répertoire du projet
1. taper les commandes dans ce terminal (`conda env create`, ...)

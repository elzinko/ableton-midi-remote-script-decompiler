# Ableton Script Decompiler

## Description
Ce projet est un petit utilitaire pour décompiler les fichiers compilés des scripts distants d'Ableton Live dans un autre répertoire en utilisant `uncompyle6`.

## Prérequis
- **Python 3.x** doit être installé sur votre machine.
- **pyenv** pour gérer les versions Python (optionnel mais recommandé).
- **uncompyle6** pour la décompilation des fichiers.

## Installation

### Étape 1 : Installer pyenv (optionnel)
Si vous ne l'avez pas encore installé, voici comment le faire :

```bash
curl https://pyenv.run | bash
```

Ensuite, ajoutez les lignes suivantes à votre fichier `~/.bashrc` ou `~/.zshrc` :

```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Rechargez votre shell :

```bash
source ~/.bashrc  # ou source ~/.zshrc
```

### Étape 2 : Installer la bonne version de Python
Utilisez `pyenv` pour installer et utiliser une version spécifique de Python :

```bash
pyenv install 3.x.x
pyenv global 3.x.x
```

### Étape 3 : Créer un environnement virtuel
Créez et activez un environnement virtuel pour le projet :

```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

### Étape 4 : Installer les dépendances
Installez les dépendances requises avec `pip` :

```bash
pip install -r requirements.txt
```

## Utilisation
Pour décompiler les scripts d'Ableton Live :

```bash
python src/ableton_script_decompiler/decompile.py /chemin/vers/le/dossier/source /chemin/vers/le/dossier/output
```

Remplacez `/chemin/vers/le/dossier/source` et `/chemin/vers/le/dossier/output` par les chemins appropriés.

## Fichiers du projet
- `README.md` : Ce fichier d'instructions.
- `requirements.txt` : Les dépendances Python nécessaires.
- `src/ableton_script_decompiler/decompile.py` : Le script Python principal pour la décompilation.

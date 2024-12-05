# 🖼️ Image Splitter A3 

## 📝 Description
Ce projet permet de transformer une grande image en morceaux imprimables au format A3. Il est particulièrement utile pour créer des posters ou des affiches de grande taille à partir d'une image source.

## ✨ Fonctionnalités
- 🔄 Redimensionnement automatique de l'image source aux dimensions de 4 x A3
- ✂️ Découpage intelligent en 4 morceaux égaux
- 📄 Génération de fichiers PNG haute résolution (300 DPI)
- 📑 Conversion automatique en PDF prêts à imprimer
- 🎯 Optimisé pour l'impression en format A3

## 🚀 Installation

1. Clonez le repository :
```bash
git clone [url-du-repo]
```

2. Créez et activez un environnement virtuel :
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## 💻 Utilisation

1. Placez votre image source nommée `cas.png` dans le dossier du projet
2. Exécutez le script :
```bash
python decoupage_image.py
```

3. Récupérez vos fichiers dans :
   - 📁 `pieces_decoupees/` : Images PNG
   - 📁 `pieces_decoupees_pdf/` : Fichiers PDF

## 📏 Spécifications techniques
- Format de sortie : A3 (420×297mm)
- Résolution : 300 DPI
- Dimensions en pixels : 4961×3508 pixels par page

## 🗂️ Structure des fichiers
```
.
├── decoupage_image.py    # Script principal
├── requirements.txt      # Dépendances Python
├── cas.png              # Image source
├── pieces_decoupees/    # Dossier des PNG découpés
└── pieces_decoupees_pdf/# Dossier des PDF
```

## ⚙️ Dépendances
- Python 3.6+
- Pillow (PIL) 10.0.0+

## 👤 Auteur
K𝛑X

## 📜 License
Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

from PIL import Image
import os

# Dimensions d'une page A3 en pixels (à 300 DPI)
A3_WIDTH = 4961  # 420mm à 300DPI
A3_HEIGHT = 3508  # 297mm à 300DPI

def process_image(image_path):
    # Charger l'image
    img = Image.open(image_path)
    
    # Calculer les dimensions finales (4 fois A3 en paysage)
    target_width = A3_WIDTH * 2
    target_height = A3_HEIGHT * 2
    
    # Redimensionner l'image
    img_resized = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
    
    # Calculer les points de découpe
    mid_width = target_width // 2
    mid_height = target_height // 2
    
    # Découper l'image en 4 morceaux
    pieces = [
        (0, 0, mid_width, mid_height),          # Haut gauche
        (mid_width, 0, target_width, mid_height),    # Haut droite
        (0, mid_height, mid_width, target_height),   # Bas gauche
        (mid_width, mid_height, target_width, target_height)  # Bas droite
    ]
    
    # Créer les dossiers de sortie s'ils n'existent pas
    output_dirs = ["pieces_decoupees", "pieces_decoupees_pdf"]
    for dir in output_dirs:
        if not os.path.exists(dir):
            os.makedirs(dir)
    
    # Sauvegarder chaque morceau
    for i, coords in enumerate(pieces):
        # Découper le morceau
        piece = img_resized.crop(coords)
        
        # Redimensionner au format A3
        piece_resized = piece.resize((A3_WIDTH, A3_HEIGHT), Image.Resampling.LANCZOS)
        
        # Sauvegarder en PNG
        output_path_png = os.path.join("pieces_decoupees", f"piece_{i+1}.png")
        piece_resized.save(output_path_png, "PNG", dpi=(300, 300))
        print(f"Morceau {i+1} sauvegardé en PNG : {output_path_png}")
        
        # Convertir en PDF
        # Convertir en mode RGB si nécessaire (requis pour PDF)
        if piece_resized.mode != 'RGB':
            piece_resized = piece_resized.convert('RGB')
        output_path_pdf = os.path.join("pieces_decoupees_pdf", f"piece_{i+1}.pdf")
        piece_resized.save(output_path_pdf, "PDF", resolution=300.0)
        print(f"Morceau {i+1} sauvegardé en PDF : {output_path_pdf}")

if __name__ == "__main__":
    image_path = "cas.png"
    if os.path.exists(image_path):
        process_image(image_path)
        print("Traitement terminé avec succès!")
    else:
        print(f"Erreur: L'image {image_path} n'a pas été trouvée.")

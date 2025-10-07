from PIL import Image
import numpy as np
import pygame

def load_cards(path="assets/Cards.com.png", resize=(200, 300)):
    """
    Découpe une planche de cartes en dictionnaire {nom: pygame.Surface}.
    Performant, sans chargements multiples de fichiers.
    
    Noms :
        C = Cœur, P = Pique, K = Carreau, T = Trèfle
        Exemple : C1, P10, K11, T13
    """

    # Charger l’image principale avec Pillow
    sprite_sheet = Image.open(path).convert("RGBA")
    sheet_width, sheet_height = sprite_sheet.size

    # Configuration
    cols, rows = 13, 4
    card_width = sheet_width // cols
    card_height = sheet_height // rows

    # Dictionnaire final
    cards = {}

    # Ordre des couleurs (adapté à ton image)
    suits = ["C", "P", "K", "T"]  # Cœur, Pique, Carreau, Trèfle
    values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]

    for row in range(rows):
        for col in range(cols):
            # Coordonnées de découpe
            x1, y1 = col * card_width, row * card_height
            x2, y2 = x1 + card_width, y1 + card_height

            # Découpe avec Pillow
            card = sprite_sheet.crop((x1, y1, x2, y2))

            # Redimensionnement (facultatif)
            if resize:
                card = card.resize(resize, Image.Resampling.LANCZOS)

            # Conversion → bytes → pygame.Surface
            card_bytes = card.tobytes()
            card_surf = pygame.image.frombuffer(card_bytes, card.size, "RGBA")

            # Enregistrer dans le dictionnaire
            key = f"{suits[row]}{values[col]}"
            cards[key] = card_surf

    print(f"✅ {len(cards)} cartes chargées ({resize[0]}x{resize[1]} px chacune)")
    return cards

cards = load_cards()
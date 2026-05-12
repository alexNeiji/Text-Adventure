# 🎮 Text-Adventure

Un jeu d'aventure en Python **100% texte**. Une histoire incroyable à découvrir.

## 📖 Description

Plonge dans un univers fascinant où tes choix façonnent l'histoire! Explore des lieux mystérieux, interagis avec des personnages, résous des énigmes et découvre les secrets d'une aventure épique.

## �� Installation

### Prérequis
- Python 3.8+

### Cloner et lancer
```bash
git clone https://github.com/alexNeiji/Text-Adventure.git
cd Text-Adventure
python main.py
```

## 🎮 Comment jouer

Tape tes commandes pour interagir avec le monde:

| Commande | Description |
|----------|-------------|
| `go [direction]` | Te déplacer (north, south, east, west) |
| `take [objet]` | Prendre un objet |
| `inventory` | Voir ton inventaire |
| `look` | Observer ta location actuelle |
| `talk [personnage]` | Parler à un NPC |
| `use [objet]` | Utiliser un objet |
| `aide` | Afficher l'aide |
| `quit` | Quitter le jeu |

## 📁 Structure du projet

```
Text-Adventure/
├── main.py              # Point d'entrée du jeu
├── game.py              # Logique principale du jeu
├── player.py            # Classe Player
├── room.py              # Classe Room
├── npc.py               # Classe NPC (optionnel)
├── saves/               # Dossier des sauvegardes
└── README.md
```

## ✨ Fonctionnalités

- ✅ Exploration d'un monde persistant
- ✅ Inventaire et système d'objets
- ✅ Sauvegarde/Chargement de partie
- ✅ Dialogues avec des NPCs
- ✅ Énigmes et défis
- ✅ Histoire branching

## 🎯 Prochaines étapes

- [ ] Système de combat
- [ ] Plus de rooms et d'énigmes
- [ ] Quêtes et objectifs
- [ ] Musique/Sons ASCII
- [ ] Fin(s) multiple(s)

## 💡 Conseils de jeu

- Explore chaque coin du monde
- Parle à tous les personnages
- Recueille les objets, tu en auras besoin
- Sauvegarde régulièrement ton progrès

## 🤝 Contribution

C'est un projet personnel, mais les suggestions sont les bienvenues!

## 📄 License

MIT License - Libre d'utilisation

---

**Bon jeu et que l'aventure commence!** 🗡️✨

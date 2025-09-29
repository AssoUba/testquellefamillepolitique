
parties = {
    "LFI": {"nom": "La France Insoumise", "eco": -2, "aut": -1, "cul": -2, "eco_env": -2, "europe": -1},
    "PS": {"nom": "Parti Socialiste", "eco": -1, "aut": -1, "cul": -1, "eco_env": -1, "europe": +1},
    "EELV": {"nom": "Europe Écologie Les Verts", "eco": -1, "aut": -1, "cul": -2, "eco_env": -2, "europe": +2},
    "PCF": {"nom": "Parti Communiste Français", "eco": -2, "aut": -1, "cul": -1, "eco_env": -1, "europe": -1},
    "RE": {"nom": "Renaissance", "eco": +1, "aut": +1, "cul": 0, "eco_env": 0, "europe": +2},
    "LR": {"nom": "Les Républicains", "eco": +2, "aut": +2, "cul": +1, "eco_env": +1, "europe": +1},
    "RN": {"nom": "Rassemblement National", "eco": 0, "aut": +2, "cul": +2, "eco_env": +1, "europe": -2},
    "DLF": {"nom": "Debout la France", "eco": 0, "aut": +2, "cul": +2, "eco_env": 0, "europe": -2},
    "REC": {"nom": "Reconquête", "eco": +1, "aut": +2, "cul": +2, "eco_env": +1, "europe": -2},
    "LO": {"nom": "Lutte Ouvrière", "eco": -2, "aut": -2, "cul": -2, "eco_env": -1, "europe": -2},
    "NPA": {"nom": "Nouveau Parti Anticapitaliste", "eco": -2, "aut": -2, "cul": -2, "eco_env": -1, "europe": -2},
    "PRG": {"nom": "Parti Radical de Gauche", "eco": -1, "aut": 0, "cul": 0, "eco_env": -1, "europe": +1},
    "UDI": {"nom": "Union des Démocrates et Indépendants", "eco": +1, "aut": +1, "cul": 0, "eco_env": 0, "europe": +2},
    "PA": {"nom": "Parti Animaliste", "eco": 0, "aut": -1, "cul": -1, "eco_env": -2, "europe": +1},
    "UDR": {"nom": "Union des Droites pour la République", "eco": +2, "aut": +2, "cul": +2, "eco_env": +1, "europe": -1}
}

def compute_scores(answers):
    axes = {"eco": 0, "aut": 0, "cul": 0, "eco_env": 0, "europe": 0}
    for a in answers:
        for k in axes:
            axes[k] += a.get(k, 0)
    for k in axes:
        axes[k] = round(axes[k] / len(answers), 2)
    return axes

def find_closest_parties(user_scores):
    def distance(party):
        return sum((user_scores[k] - party[k])**2 for k in user_scores)
    scored = [(p["nom"], round(100 - distance(p)*10, 1)) for p in parties.values()]
    return sorted(scored, key=lambda x: -x[1])[:3]

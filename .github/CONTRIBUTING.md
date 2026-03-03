# Guide de contribution à Toolbox_MLObs

Merci de l'intérêt que vous portez à **Toolbox_MLObs** ! Ce projet est actuellement en version **v0.1.1**. 

Nous accueillons avec plaisir toutes les contributions : rapports de bugs, suggestions de fonctionnalités ou améliorations du code.

---

## Installation de l'environnement de développement

Ce projet utilise [uv](https://github.com/astral-sh/uv) pour une gestion ultra-rapide des dépendances.

1. **Cloner le projet** :
   ```bash
   git clone [https://github.com/Lionel-JOURDHIER/Toolbox_MLObs.git](https://github.com/Lionel-JOURDHIER/Toolbox_MLObs.git)
   cd Toolbox_MLObs
   ```

2. **Installer les dépendances** :
   ```bash
   uv sync --all-extras
   ```

3. **Activer l'environnement virtuel :**
   ```bash
   source .venv/bin/activate  # Linux/macOS
    # ou
    .venv\Scripts\activate    # Windows
    ```

## Workflow de travail
Nous suivons un cycle de développement structuré pour garantir la stabilité de **v0.1.1**.

1. **Créer une branche de travail**
    ```bash
    git checkout -b feat/nom-de-votre-feature
    ```

2. **Créer un nouveau fichier**
   * Pour le code source : ajoutez votre fichier .py dans le dossier src/Toolbox_MLObs/ (ou le dossier racine du module).
   * Pour la documentation : utilisez le dossier docs/.

3. **Ajouter votre code**
Développez votre fonctionnalité. N'oubliez pas d'utiliser Ruff pour formater automatiquement votre nouveau fichier :
    ```bash
    uv run ruff check . --fix
    ```
    
4. **Ajouter des tests**
Créez un fichier de test correspondant dans tests/ (ex: test_votre_fichier.py). Vérifiez que tout est au vert :
    ```bash
    uv run pytest
    ```

5. **Soumettre une pull request**
Poussez votre branche sur GitHub et ouvrez une Pull Request. Décrivez clairement l'utilité du nouveau fichier créé.

6. **Attendre la revue de code et les commentaires**
Un responsable (ou Lionel-JOURDHIER) examinera vos changements. Répondez aux commentaires et apportez les ajustements nécessaires avant le merge final.


##Sécurité et Secrets

Afin de protéger l'intégrité du projet, il est strictement interdit de pousser des secrets (clés API, mots de passe, emails personnels) dans le code source.

1. **Utilisez des variables d'environnement** : En local, créez un fichier `.env` (déjà présent dans le `.gitignore`).
2. **Secrets GitHub** : Pour les actions automatisées, les secrets doivent être configurés dans les paramètres du repo (`Settings > Secrets and variables`).
3. **Audit avant commit** : Vérifiez toujours vos changements avec `git diff --cached` avant de valider.
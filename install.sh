#!/usr/bin/env bash
# Installe les dépendances Python du projet, pour un test en local.
# Usage : bash install.sh
#
# Si tu ne te sens pas à l'aise avec le terminal : ce n'est pas grave.
# GitHub Actions installe et lance tout automatiquement, tu n'as pas
# besoin de ce script pour que CardTide fonctionne. Il est là pour plus
# tard, si tu veux tester des modifications avant de les mettre en ligne.
set -e
echo "Installation des dépendances..."
pip install -r requirements.txt
echo "Terminé. Copie .env.example vers .env et remplis tes clés avant de lancer run.sh"

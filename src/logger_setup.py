"""
Configuration centralisée de la journalisation (logging) pour tout le projet.

Objectif : que chaque exécution (locale ou via GitHub Actions) produise des
logs lisibles, avec assez de détail pour diagnostiquer un problème sans
avoir à modifier le code.
"""

import logging
import sys


def get_logger(name: str) -> logging.Logger:
    """
    Retourne un logger configuré, prêt à l'emploi.

    Utilisation :
        from src.logger_setup import get_logger
        logger = get_logger(__name__)
        logger.info("Message")
    """
    logger = logging.getLogger(name)

    # Évite de dupliquer les handlers si get_logger est appelé plusieurs fois
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger

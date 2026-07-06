# Projet : Haute Disponibilité Réseau avec HSRP

## Description
Ce projet concerne la mise en place d'une infrastructure réseau redondante utilisant le protocole HSRP (Hot Standby Router Protocol). L'objectif principal est d'assurer la continuité de service de la passerelle par défaut du VLAN 10, garantissant ainsi une haute disponibilité en cas de panne d'un équipement.

## Architecture Technique
* **Matériel :** Routeurs Cisco ISR 2911, Switch Cisco Catalyst 2960.
* **Protocoles :** HSRP (Mode Active/Standby), Routage Inter-VLAN, Encapsulation 802.1Q (Trunking).
* **Automatisation :** Scripts Python intégrés pour les tests réseau.

## Organisation du dépôt
Ce dépôt contient les ressources suivantes :
* `/docs` : Rapport technique complet (format PDF).
* `/maquette` : Fichier de simulation Packet Tracer (`.pkt`).
* `/captures` : Preuves visuelles de configuration et de validation.
* `/scripts` : Fichiers de configuration CLI (`.txt`) et scripts d'automatisation (`.py`).

## Documentation
Pour une analyse détaillée des tests de basculement et des résultats obtenus, veuillez consulter le rapport présent dans le dossier `/docs`.

## Contributeur
* Lauryn HECQUE--NASCIMENTO

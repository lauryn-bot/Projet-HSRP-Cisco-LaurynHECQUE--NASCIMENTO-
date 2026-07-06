# Projet Haute Disponibilité - Protocole HSRP

## 1. Mission
Ce projet a pour objectif de sécuriser la passerelle par défaut (Gateway) du réseau VLAN 10. En cas de défaillance matérielle ou logicielle, le protocole HSRP assure une continuité de service totale via un basculement automatique.

## 2. Architecture
L'infrastructure déployée repose sur :
* 02 Routeurs Cisco ISR 2911 (Mode Active/Standby).
* 01 Commutateur Cisco Catalyst 2960 (Gestion du Trunk).
* Protocole HSRP pour la redondance de passerelle.

## 3. Contenu du dépôt
* `/docs` : Rapport technique complet du projet (PDF).
* `/maquette` : Maquette Packet Tracer finale (`.pkt`).
* `/captures` : Preuves de validation et résultats de tests.
* `/scripts` : Fichiers de configuration CLI.

## 4. Documentation
Le rapport complet détaillant les objectifs, la méthodologie, la résolution d'incidents et la validation technique est disponible dans le répertoire `/docs`.

## 5. Auteurs
- Lauryn HECQUE--NASCIMENTO
- Mehdi BEN MOULAY

import socket

# Cible : Votre passerelle
target_ip = "192.168.10.1"

print(f"--- DÉBUT DE L'AUDIT SUR {target_ip} ---")

# Balayage de la plage de ports 20 à 30 (pour faire un test rapide)
for port in range(20, 31):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2.0)  # Augmentation du temps d'attente à 2 secondes
    
    result = s.connect_ex((target_ip, port))
    
    if result == 0:
        print(f"[+] Port {port} est OUVERT")
    else:
        # On affiche aussi les ports fermés pour prouver que le scanner travaille
        print(f"[-] Port {port} est FERMÉ")
    
    s.close()

print("--- FIN DE L'AUDIT ---")
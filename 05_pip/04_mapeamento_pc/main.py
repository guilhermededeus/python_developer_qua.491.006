import os 
import platform
import psutil
import socket

print(f"Sistema Operacional: {platform.system()} {platform.release()}")
print(f"Nome do usuário: {os.environ.get("USERNAME")}") 
print(f"IPv4: {socket.gethostbyname(socket.gethostname())}")

# Coleta informações sobre as portas TCP e UDP
print(f"\nPortas abertas:\n")
connectall = psutil.net_connections(kind="inet")
only_udp = [conn for conn in psutil.net_connections(kind="inet") if conn.type == socket.SOCK_DGRAM]

# Separar as informações sobre as portas
only_tcp_listening_ports = [conn.laddr.port for conn in connectall if conn.status == psutil.CONN_LISTEN]
only_udp_listening_ports = [conn.laddr.port for conn in only_udp]

# Remover as portas repetidas da lista
only_tcp_listening_ports = list(set(only_tcp_listening_ports))
only_udp_listening_ports = list(set(only_udp_listening_ports))

# Organizar as portas
only_tcp_listening_ports.sort()
only_udp_listening_ports.sort()

# Mostra as portas TCP
print("-- Portas TCP --")
for port in only_tcp_listening_ports:
    print(f"Porta TCP: {port}")

# Mostra as portas TCP
print("\n-- Portas UDP --")
for port in only_udp_listening_ports:
    print(f"Porta UDP: {port}")
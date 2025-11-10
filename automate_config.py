import csv
from datetime import datetime
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
import os

# Cria pastas se não existirem
os.makedirs("backup", exist_ok=True)
os.makedirs("logs", exist_ok=True)

def load_devices(filename="devices.csv"):
    devices = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            devices.append(row)
    return devices

def load_commands(filename="config_commands.txt"):
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip()]

def log(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open("logs/activity.log", "a") as f:
        f.write(f"{timestamp} {message}\n")
    print(message)

def backup_config(connection, hostname):
    output = connection.send_command("show running-config")
    backup_file = f"backup/{hostname}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(backup_file, "w") as f:
        f.write(output)
    log(f"Backup salvo: {backup_file}")

def configure_device(device, commands):
    try:
        log(f"Conectando a {device['ip']} ({device['device_type']})...")
        connection = ConnectHandler(**device)

        hostname = connection.find_prompt().replace("#", "").replace(">", "")
        backup_config(connection, hostname)

        log(f"Aplicando comandos em {hostname}...")
        output = connection.send_config_set(commands)
        log(f"Configuração aplicada com sucesso em {hostname}!\n{output}")

        connection.save_config()
        connection.disconnect()
    except NetmikoTimeoutException:
        log(f"⛔ Timeout ao conectar a {device['ip']}")
    except NetmikoAuthenticationException:
        log(f"❌ Falha de autenticação em {device['ip']}")
    except Exception as e:
        log(f"⚠️ Erro inesperado em {device['ip']}: {e}")

def main():
    devices = load_devices()
    commands = load_commands()

    for device in devices:
        configure_device(device, commands)

if __name__ == "__main__":
    main()

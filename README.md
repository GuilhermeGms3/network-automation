# ⚙️ Network Automation — Automação de Configuração de Switches e Roteadores

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Netmiko](https://img.shields.io/badge/Netmiko-Automation-orange?logo=cisco)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Ativo-success)

## 📖 Descrição

O **Network Automation** é um projeto que automatiza a **configuração de dispositivos de rede** (switches e roteadores) via **SSH**, utilizando o módulo **Netmiko** em Python.  
Ele conecta-se a múltiplos dispositivos, aplica comandos de configuração padronizados, gera **backups automáticos** das configurações existentes e mantém **logs detalhados** de todas as ações realizadas.

Ideal para administradores de rede que desejam **padronizar**, **automatizar** e **documentar** a configuração da infraestrutura.

---

## 🧠 Conceitos Aplicados

- Automação de redes com **Python + Netmiko**  
- Conexão segura via **SSH**  
- **Backup automático** das configurações  
- **Execução em lote** de comandos  
- Geração de **logs detalhados**  
- Padronização e versionamento de infraestrutura  

---

## 🧰 Tecnologias Utilizadas

- 🐍 **Python 3.10+**  
- 🔌 **Netmiko** — automação SSH para dispositivos de rede  
- 🧱 **Paramiko** — base para conexões seguras  
- 📦 **Docker (opcional)** — execução em ambiente isolado  

---

## 🗂️ Estrutura do Projeto

network-automation/
├── devices.csv # Lista de dispositivos (IP, tipo, usuário, senha)
├── config_commands.txt # Comandos a aplicar
├── backup/ # Configurações salvas automaticamente
├── logs/ # Logs detalhados de execução
├── automate_config.py # Script principal
├── requirements.txt # Dependências do projeto
└── README.md # Este arquivo


---

## ⚙️ Exemplo de Arquivos

### 📄 `devices.csv`
```csv
ip,device_type,username,password
192.168.1.1,cisco_ios,admin,1234
192.168.1.2,mikrotik_routeros,admin,senha123
192.168.1.3,hp_procurve,admin,admin

hostname SW-AUTO
snmp-server community public RO
banner motd #Acesso restrito a pessoal autorizado#


🐍 Execução
1️⃣ Instale as dependências:
pip install -r requirements.txt

2️⃣ Configure seus dispositivos:

Edite o arquivo devices.csv com os IPs e credenciais dos equipamentos.

3️⃣ Defina os comandos:

Adicione os comandos desejados no arquivo config_commands.txt.

4️⃣ Execute o script:
python automate_config.py


O script:

Conecta-se a cada dispositivo via SSH

Faz backup da configuração atual

Aplica os comandos do arquivo

Salva logs detalhados da execução

Exemplo de Log (logs/activity.log)
[2025-11-10 10:30:02] Conectando a 192.168.1.1 (cisco_ios)...
[2025-11-10 10:30:05] Backup salvo: backup/SW1_20251110_103005.txt
[2025-11-10 10:30:08] Aplicando comandos em SW1...
[2025-11-10 10:30:09] Configuração aplicada com sucesso em SW1!


🧩 Possíveis Extensões

🧠 Integração com Ansible para orquestração em larga escala

📧 Envio de relatórios automáticos via e-mail

🌐 Interface web (Flask) para gerenciar execuções

🔒 Uso de .env para proteger senhas e credenciais

⏱️ Execução automática (cron jobs)

🧑‍💻 Exemplo de Execução
<p align="center"> <img src="https://user-images.githubusercontent.com/000000/placeholder.png" width="700" alt="Execução de automação de rede com Netmiko"> </p>

(Substitua por uma captura real do terminal ou print dos logs.)
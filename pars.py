import os
import re

LOG_FILE = "/var/log/auth.log"
BAN_FILE = "banned_ips.txt"
LIMIT = 5
failed_attempts = {}

with open(LOG_FILE, encoding="utf-8") as file:
    for line in file:
        if "Failed password" in line:
            ips = re.findall(r"\d+\.\d+\.\d+\.\d+", line)
            if ips:
                ip = ips[0]
                if ip in failed_attempts:
                    failed_attempts[ip] += 1
                else:
                    failed_attempts[ip] = 1

if not os.path.exists(BAN_FILE):
    open(BAN_FILE, "a").close()

with open(BAN_FILE, "r", encoding="utf-8") as ban_file:
    banned_content = ban_file.read()

for ip, count in failed_attempts.items():
    if count >= LIMIT:

        if ip not in banned_content:
            print(f"Превышение попыток от {ip} ({count} раз). Блокируем!")

            with open(BAN_FILE, "a", encoding="utf-8") as ban_file:
                ban_file.write(f"{ip}\n")

            os.system(f"iptables -A INPUT -s {ip} -j DROP")
            print(f"IP {ip} отправлен в DROP через iptables.")
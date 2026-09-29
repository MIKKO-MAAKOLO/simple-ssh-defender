# Simple SSH Defender

A lightweight Python script for automatically detecting SSH brute-force attackers and blocking them via iptables.

## 🇬🇧 About
- **Log Parsing:** Reads `auth.log` for failed login attempts (`Failed password`).
- **Regular Expressions:** Extracts intruder IPv4 addresses using the `re` module.
- **Attempt Tracking:** Counts failed attempts and maintains a local blocklist (`banned_ips.txt`).
- **Blocking:** Generates firewall rules (`iptables`).

### Usage

sudo python3 pars.py

---
<details>
<summary>🇷🇺 По-русски</summary>

# Simple SSH Defender

Легковесный скрипт на Python для автоматического поиска брутфорсеров по SSH и их блокировки через iptables.

## 🛠 Функционал
- Парсинг логов авторизации (`auth.log`) в поисках неудачных попыток входа (`Failed password`).
- Извлечение IPv4-адресов нарушителей с помощью регулярных выражений (`re`).
- Подсчет количества попыток и автоматическое добавление IP в черный список (`banned_ips.txt`).
- Генерация правил блокировки для фаервола (`iptables`).

## 🚀 Запуск

sudo python3 pars.py

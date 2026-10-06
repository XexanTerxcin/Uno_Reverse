<div align="center">

# Uno_Reverse

**A minimal reverse shell implementation in Python — built as a security research tool to understand how reverse shells work under the hood.**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Early%20Stage-orange?style=for-the-badge)]()
[![Purpose](https://img.shields.io/badge/Purpose-Security%20Research-red?style=for-the-badge)]()

</div>

---

> ### ⚠️ Disclaimer
> This project is intended **strictly for educational and authorized security research purposes only**. It was built as a learning exercise to understand how reverse shells work internally. Do **not** use this on systems you do not own or have explicit written permission to test. Unauthorized use is illegal and unethical. The author assumes no responsibility for misuse.

---

## 📖 About

**Uno_Reverse** is a simple client-server reverse shell written in Python. It consists of two scripts:

| File | Role |
|------|------|
| 🎯 `victim.py` | Connects back to the listener and executes received commands |
| 🎛️ `attacker.py` | Listens for incoming connections and sends commands interactively |

The name **"Uno"** reflects its simplicity — a single, no-frills implementation focused on clarity over features.

> 🚧 **Note:** These scripts are at an **early / initial stage**. The code is intentionally basic and will evolve as the project grows. Expect refactors, new features, and structural changes.

---

## 🎯 Purpose

This repo exists because **you learn best by building**. Reading about reverse shells is one thing; writing the socket logic, handling the shell's I/O, and debugging why your session drops on the first command is another.

**Goals:**
- 🧠 Understand the mechanics of a reverse shell from scratch
- 🔌 Practice socket programming and command execution in Python
- 📝 Document the learning process for others on the same path

---

## ✨ Features

### ✅ Current
- [x] TCP reverse shell connection
- [x] Command execution via `subprocess.getoutput()`
- [x] Interactive command prompt on the listener side
- [x] Clean exit handling with `exit` command
- [x] Welcome message on connection

### 🛠️ Planned
- [ ] Proper interactive shell (real-time stdin/stdout piping)
- [ ] Error handling and reconnection logic
- [ ] File upload / download support
- [ ] Basic encoding or obfuscation for payload delivery
- [ ] Cross-platform testing (Windows / Linux / macOS)
- [ ] Encrypted communication channel

---

## 🧠 Concepts Covered

| Concept | Where it's used |
|---------|-----------------|
| 🌐 Socket programming | `socket.socket()`, `connect()`, `bind()`, `listen()`, `accept()` |
| ⚙️ Command execution | `subprocess.getoutput()` |
| 🔤 Encoding / decoding | `encode()` / `decode()` for byte streams |
| 🔗 Connection handling | `recv()`, `send()`, `close()` |
| 🔁 Loop control | `while True` with `exit` condition |

---

## 📂 Project Structure

```
Uno_Reverse/
├── 🎛️  attacker.py     # Listener / controller side
├── 🎯  victim.py       # Target / client side
└── 📄  README.md
```

---

## 🚀 Usage

> ⚠️ Only run this in an **authorized lab environment** or on machines you own.

### 1️⃣ Configure the target

In `victim.py`, set the listener's IP and port:

```python
SERVER_HOST = "127.0.0.1"   # change to listener IP
SERVER_PORT = 5003
```

### 2️⃣ Start the listener

On the controlling machine:

```bash
python3 attacker.py
```

Expected output:

```
Listening as 0.0.0.0:5003 ...
```

### 3️⃣ Run the client

On the target machine (authorized lab only):

```bash
python3 victim.py
```

### 4️⃣ Send commands

Back on the listener side, you'll see the connection and a prompt:

```
127.0.0.1:54321 Connected!
Enter the command you wanna execute: whoami
```

Type `exit` to close the session cleanly.

---

## 🛣️ Roadmap

- [ ] Replace `subprocess.getoutput()` with a true interactive shell
- [ ] Add multi-client support on the listener
- [ ] Improve buffer handling for large outputs
- [ ] Add logging and session handling
- [ ] Write-up: *"How a reverse shell actually works"*

---

## 📚 Learning Resources

- 📘 Python [`socket`](https://docs.python.org/3/library/socket.html) and [`subprocess`](https://docs.python.org/3/library/subprocess.html) official docs
- 🌐 [Real Python – Socket Programming](https://realpython.com/python-sockets/)
- 🧪 [HackTricks – Shells](https://book.hacktricks.xyz/)
- 🎯 MITRE ATT&CK: [T1059 – Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059/)

---

## 🙏 Acknowledgements

Built while studying security research. Shoutout to the countless blog posts, CTFs, and open-source tools that made the concepts click.

---

<div align="center">

**⭐ Early-stage project — expect breaking changes. Fork, break, and rebuild — that's the whole point.**

</div>
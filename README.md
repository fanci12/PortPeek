# PortPeek

A lightweight, multithreaded TCP port scanner written in Python, built for learning and for checking the security of systems you own.

> **Legal notice:** Only scan computers and networks that you own or have explicit written permission to test. Unauthorized scanning may be illegal in your country. The author is not responsible for misuse.

## Features

- Scans a range of TCP ports on any IP address or hostname
- Fast, using multithreading (100 threads by default)
- Labels common services (SSH, HTTP, HTTPS, MySQL, and more)
- Adjustable port range, timeout, and thread count
- No third-party dependencies (Python standard library only)

## Requirements

- Python 3.8 or newer
- git (optional, only if you want to clone the repository)

Check your Python version:

```bash
python --version
```

On some systems the command is `python3` instead of `python`.

## Installation

### 1. Get the code

```bash
git clone https://github.com/<your-username>/portpeek.git
cd portpeek
```

Or download `port_scanner.py` and put it in a folder of your choice.

### 2. (Optional) Create a virtual environment

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell)**

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

PortPeek currently uses only the standard library, so nothing extra will be installed.

## Usage

```bash
python port_scanner.py <host> [--start START] [--end END] [--timeout SECONDS] [--threads N]
```

| Option      | Description                         | Default |
|-------------|-------------------------------------|---------|
| `host`      | IP address or hostname to scan      | required |
| `--start`   | First port to scan                  | 1       |
| `--end`     | Last port to scan                   | 1024    |
| `--timeout` | Seconds to wait for each port       | 1.0     |
| `--threads` | Number of ports checked at once     | 100     |

### Examples

Scan your own machine (ports 1-1024):

```bash
python port_scanner.py 127.0.0.1
```

Scan a specific range on your router:

```bash
python port_scanner.py 192.168.1.1 --start 1 --end 5000
```

Scan a host with a longer timeout and fewer threads:

```bash
python port_scanner.py scanme.nmap.org --start 20 --end 100 --timeout 2 --threads 50
```

### Sample output

```
Scanning 127.0.0.1 (127.0.0.1) ports 1-1024...
  Port 22 is OPEN (SSH)
  Port 80 is OPEN (HTTP)

Done. Found 2 open port(s).
```

## Roadmap

- [ ] Banner grabbing
- [ ] UDP scanning
- [ ] Export results to CSV / JSON
- [ ] Scan multiple IP addresses (CIDR ranges)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

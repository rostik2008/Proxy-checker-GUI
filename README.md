Proxy Checker

A simple, multi-threaded Python GUI application built with tkinter to check the validity of HTTP/HTTPS proxies from a text file.
✨ Features

    GUI Interface: Easy-to-use graphical interface.

    Proxy File Loading: Load proxies from a proxy.txt file.

    Multi-threaded Checking: Utilizes ThreadPoolExecutor for fast, concurrent proxy validation.

    Real-time Updates: Displays working and non-working proxies in separate text areas as they are checked.

    Progress Bar: Visual feedback on the checking progress.

    Supports Authenticated Proxies: Handles proxies with username and password.

🚀 Getting Started
Prerequisites

Before running the application, make sure you have Python installed (Python 3.x is recommended).

You also need to install the requests library:

pip install requests

Installation

    Clone the repository (or download the script):

    git clone https://github.com/your-username/proxy-checker.git
    cd proxy-checker

    (Note: Replace https://github.com/your-username/proxy-checker.git with your actual repository URL if you host it, or simply save the provided Python code as proxy_checker.py).

    Create your proxy.txt file:
    In the same directory as the proxy_checker.py script, create a file named proxy.txt.

Usage

    Prepare your proxy.txt file:
    Place your proxies in proxy.txt, one proxy per line. The format should be IP:PORT or IP:PORT:USERNAME:PASSWORD.

    Examples:

    192.168.1.1:8080
    203.0.113.45:3128:user:pass123
    10.0.0.10:9000

    Run the application:

    python proxy_checker.py

    Load Proxies:
    Click the "Load proxy.txt" button. The application will confirm how many proxies were loaded.

    Start Checking:
    Click the "Start Checking" button to begin the proxy validation process.
    Working proxies will appear in the "Working Proxies" box, and non-working proxies will appear in the "Non-Working Proxies" box. The progress bar will update as the checks proceed.

    Completion:
    Once all proxies are checked, a message box will pop up summarizing the results.

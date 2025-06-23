import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading


def check_proxy(proxy_line):
    parts = proxy_line.strip().split(':')
    if len(parts) < 2:
        return False, proxy_line

    ip, port = parts[0], parts[1]
    proxies = {
        "http": f"http://{ip}:{port}",
        "https": f"https://{ip}:{port}",
    }

    if len(parts) == 4:
        login, password = parts[2], parts[3]
        proxies = {
            "http": f"http://{login}:{password}@{ip}:{port}",
            "https": f"https://{login}:{password}@{ip}:{port}",
        }

    try:
        response = requests.get("http://www.google.com", proxies=proxies, timeout=5)
        return response.status_code == 200, proxy_line
    except requests.exceptions.RequestException:
        return False, proxy_line


class ProxyCheckerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Proxy Checker")
        self.geometry("700x500")

        self.create_widgets()

    def create_widgets(self):
        # Buttons
        self.load_btn = ttk.Button(self, text="Load proxy.txt", command=self.load_proxies)
        self.load_btn.pack(pady=10)

        self.start_btn = ttk.Button(self, text="Start Checking", command=self.start_checking, state="disabled")
        self.start_btn.pack(pady=5)

        self.progress = ttk.Progressbar(self, orient='horizontal', length=600, mode='determinate')
        self.progress.pack(pady=10)

        # Text boxes
        self.working_label = ttk.Label(self, text="Working Proxies:")
        self.working_label.pack()
        self.working_box = tk.Text(self, height=10, width=80)
        self.working_box.pack(pady=5)

        self.nonworking_label = ttk.Label(self, text="Non-Working Proxies:")
        self.nonworking_label.pack()
        self.nonworking_box = tk.Text(self, height=10, width=80)
        self.nonworking_box.pack(pady=5)

    def load_proxies(self):
        try:
            with open("proxy.txt", "r") as file:
                self.proxies = [line.strip() for line in file if line.strip()]
            self.start_btn.config(state="normal")
            messagebox.showinfo("Loaded", f"Loaded {len(self.proxies)} proxies.")
        except FileNotFoundError:
            messagebox.showerror("Error", "proxy.txt not found!")

    def start_checking(self):
        self.start_btn.config(state="disabled")
        self.working_box.delete(1.0, tk.END)
        self.nonworking_box.delete(1.0, tk.END)
        self.progress['value'] = 0

        thread = threading.Thread(target=self.check_proxies)
        thread.start()

    def check_proxies(self):
        working = []
        nonworking = []
        total = len(self.proxies)
        self.progress['maximum'] = total

        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = {executor.submit(check_proxy, proxy): proxy for proxy in self.proxies}
            for i, future in enumerate(as_completed(futures)):
                is_working, proxy = future.result()
                if is_working:
                    working.append(proxy)
                    self.working_box.insert(tk.END, proxy + "\n")
                else:
                    nonworking.append(proxy)
                    self.nonworking_box.insert(tk.END, proxy + "\n")

                self.progress['value'] = i + 1

        messagebox.showinfo("Done", f"Checked {total} proxies.\nWorking: {len(working)}\nNot working: {len(nonworking)}")
        self.start_btn.config(state="normal")


if __name__ == "__main__":
    app = ProxyCheckerApp()
    app.mainloop()

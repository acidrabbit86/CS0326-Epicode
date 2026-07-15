import tkinter as tk
from tkinter import messagebox
import ipaddress
import socket
import os
import time

# ---------- Palette colori ----------
BG_COLOR = "#1e1e2f"
CARD_COLOR = "#27293d"
ACCENT_COLOR = "#7c5cff"
ACCENT_HOVER = "#6a4be0"
TEXT_COLOR = "#f1f1f6"
SUBTEXT_COLOR = "#9a9ab0"
ERROR_COLOR = "#ff6b6b"
SUCCESS_COLOR = "#4cd964"
ENTRY_BG = "#32344a"

PACKET_SIZE = 1024  # 1 KB


class UDPTestToolGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Strumento di Invio UDP")
        self.root.geometry("440x480")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        self._build_ui()

    # ---------------- UI ----------------

    def _build_ui(self):
        # Pannello centrale (Card)
        card = tk.Frame(self.root, bg=CARD_COLOR, bd=0)
        card.place(relx=0.5, rely=0.5, anchor="center", width=380, height=420)

        title = tk.Label(
            card, text="Generatore di pacchetti UDP", font=("Segoe UI", 16, "bold"),
            bg=CARD_COLOR, fg=TEXT_COLOR
        )
        title.pack(pady=(20, 5))

        subtitle = tk.Label(
            card, text="Invia pacchetti casuali da 1 KB a un target",
            font=("Segoe UI", 9), bg=CARD_COLOR, fg=SUBTEXT_COLOR
        )
        subtitle.pack(pady=(0, 20))

        # --- Campi di inserimento ---
        
        # IP Target
        tk.Label(card, text="Indirizzo IP target", font=("Segoe UI", 10, "bold"),
                 bg=CARD_COLOR, fg=TEXT_COLOR).pack(anchor="w", padx=30)
        self.ip_entry = tk.Entry(
            card, font=("Segoe UI", 11), bg=ENTRY_BG, fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR, relief="flat"
        )
        self.ip_entry.pack(fill="x", pady=(2, 12), ipady=5, padx=30)

        # Porta Target
        tk.Label(card, text="Porta UDP target", font=("Segoe UI", 10, "bold"),
                 bg=CARD_COLOR, fg=TEXT_COLOR).pack(anchor="w", padx=30)
        self.port_entry = tk.Entry(
            card, font=("Segoe UI", 11), bg=ENTRY_BG, fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR, relief="flat"
        )
        self.port_entry.pack(fill="x", pady=(2, 12), ipady=5, padx=30)

        # Numero di pacchetti
        tk.Label(card, text="Numero di pacchetti da inviare", font=("Segoe UI", 10, "bold"),
                 bg=CARD_COLOR, fg=TEXT_COLOR).pack(anchor="w", padx=30)
        self.packets_entry = tk.Entry(
            card, font=("Segoe UI", 11), bg=ENTRY_BG, fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR, relief="flat"
        )
        self.packets_entry.pack(fill="x", pady=(2, 12), ipady=5, padx=30)
        self.packets_entry.insert(0, "1")  # Valore di default

        # Stato dell'operazione
        self.client_status = tk.Label(
            card, text="", font=("Segoe UI", 9), bg=CARD_COLOR, fg=ERROR_COLOR
        )
        self.client_status.pack(pady=(0, 10))

        # Pulsante di invio
        send_btn = tk.Button(
            card, text="Invia pacchetti", font=("Segoe UI", 11, "bold"),
            bg=ACCENT_COLOR, fg="white", activebackground=ACCENT_HOVER,
            activeforeground="white", relief="flat", cursor="hand2",
            command=self._on_send,
        )
        send_btn.pack(fill="x", ipady=8, padx=30)
        send_btn.bind("<Enter>", lambda e: send_btn.config(bg=ACCENT_HOVER))
        send_btn.bind("<Leave>", lambda e: send_btn.config(bg=ACCENT_COLOR))

    # ---------------- Logica Client ----------------

    def _validate_ip(self, value):
        try:
            ipaddress.ip_address(value)
            return True
        except ValueError:
            return False

    def _validate_port(self, value):
        try:
            port = int(value)
            return 1 <= port <= 65535
        except ValueError:
            return False

    def _validate_packets_count(self, value):
        try:
            count = int(value)
            return count > 0
        except ValueError:
            return False

    def _on_send(self):
        ip_value = self.ip_entry.get().strip()
        port_value = self.port_entry.get().strip()
        packets_value = self.packets_entry.get().strip()

        # Validazione input
        if not self._validate_ip(ip_value):
            self.client_status.config(text="IP non valido.", fg=ERROR_COLOR)
            return
        if not self._validate_port(port_value):
            self.client_status.config(text="Porta non valida (1-65535).", fg=ERROR_COLOR)
            return
        if not self._validate_packets_count(packets_value):
            self.client_status.config(text="Numero pacchetti non valido (minimo 1).", fg=ERROR_COLOR)
            return

        port = int(port_value)
        num_packets = int(packets_value)

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(2)

            for _ in range(num_packets):
                # Genera 1024 byte (1 KB) di dati casuali ad ogni ciclo
                payload = os.urandom(PACKET_SIZE)
                sock.sendto(payload, (ip_value, port))

            sock.close()
            
            self.client_status.config(text=f"✓ {num_packets} pacchetti inviati!", fg=SUCCESS_COLOR)
            messagebox.showinfo(
                "Invio completato", 
                f"Inviati con successo {num_packets} pacchetti da {PACKET_SIZE} byte\n(Totale: {num_packets} KB) a {ip_value}:{port}"
            )
        except Exception as e:
            self.client_status.config(text=f"Errore: {e}", fg=ERROR_COLOR)


if __name__ == "__main__":
    root = tk.Tk()
    app = UDPTestToolGUI(root)
    root.mainloop()
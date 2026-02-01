import os
import platform
import subprocess
import shutil
import webbrowser
import json
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

CONFIG_FILE = "sac_config.json"
ICON_FILE = "sac_icon.ico"

class SaveAutoCloud:
    def __init__(self, root):
        self.root = root
        self.root.title("SAC - Save Auto Cloud v1.0")
        self.root.geometry("650x620")
        self.root.configure(padx=20, pady=20)

        # Icône pour Windows
        if os.path.exists(ICON_FILE) and platform.system() == "Windows":
            self.root.iconbitmap(ICON_FILE)

        # --- Section 0 : Alerte Sécurité ---
        warning_frame = tk.Frame(root, bg="#fff3cd", highlightbackground="#ffeeba", highlightthickness=1)
        warning_frame.pack(fill="x", pady=(0, 20))
        tk.Label(warning_frame, text="⚠️ ATTENTION : Effectuez une sauvegarde manuelle de vos fichiers\navant d'utiliser ce logiciel pour la première fois.", 
                 font=("Arial", 9, "bold"), bg="#fff3cd", fg="#856404", pady=10).pack()

        # --- Section 1 : Dropbox Root ---
        tk.Label(root, text="1. Dossier racine Dropbox :", font=("Arial", 10, "bold")).pack(anchor="w")
        self.db_frame = tk.Frame(root)
        self.db_frame.pack(fill="x", pady=5)
        self.db_ent = tk.Entry(self.db_frame, width=60)
        self.db_ent.pack(side="left", expand=True, fill="x")
        tk.Button(self.db_frame, text="Parcourir", command=self.browse_db).pack(side="right", padx=5)

        # --- Section 2 : Nom du Jeu ---
        tk.Label(root, text="2. Nom du jeu :", font=("Arial", 10, "bold")).pack(anchor="w", pady=(15, 0))
        self.game_name_combo = ttk.Combobox(root, width=67)
        self.game_name_combo.pack(fill="x", pady=5)

        # --- Section 3 : Source Folder ---
        header_frame = tk.Frame(root)
        header_frame.pack(fill="x", pady=(15, 0))
        tk.Label(header_frame, text="3. Emplacement des sauvegardes (Local) :", font=("Arial", 10, "bold")).pack(side="left")
        
        tk.Button(header_frame, text="❓ Où est mon jeu ?", font=("Arial", 8, "italic"), 
                  fg="#2980b9", bd=0, cursor="hand2", command=self.open_wiki).pack(side="right")

        self.source_frame = tk.Frame(root)
        self.source_frame.pack(fill="x", pady=5)
        self.source_ent = tk.Entry(self.source_frame, width=60)
        self.source_ent.pack(side="left", expand=True, fill="x")
        tk.Button(self.source_frame, text="Parcourir", command=self.browse_source).pack(side="right", padx=5)

        # --- Bouton Action Principal ---
        self.btn_link = tk.Button(root, text="ACTIVER LA SYNCHRONISATION", bg="#27ae60", fg="white", 
                                  font=("Arial", 12, "bold"), height=2, command=self.process_sync)
        self.btn_link.pack(fill="x", pady=(25, 10))

        # --- Utilitaires ---
        tk.Button(root, text="📂 Explorer mon dossier Cloud", bg="#f8f9fa", font=("Arial", 9), 
                  command=self.open_dropbox_folder).pack(pady=5)

        tk.Frame(root, height=1, bg="lightgray").pack(fill="x", pady=10)

        # --- Referral ---
        tk.Button(root, text="Obtenir une Dropbox gratuitement (+500 Mo)", bg="#0061ff", fg="white", 
                  command=self.open_referral).pack(pady=5)
        
        self.load_config()

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r") as f:
                    config = json.load(f)
                    db_path = config.get("dropbox_path", "")
                    self.db_ent.insert(0, db_path)
                    self.refresh_game_list(db_path)
            except: pass

    def save_config(self, db_path):
        try:
            with open(CONFIG_FILE, "w") as f:
                json.dump({"dropbox_path": db_path}, f)
        except: pass

    def refresh_game_list(self, db_path):
        if os.path.exists(db_path):
            try:
                folders = [f for f in os.listdir(db_path) if os.path.isdir(os.path.join(db_path, f)) and not f.startswith('.')]
                self.game_name_combo['values'] = sorted(folders)
            except: self.game_name_combo['values'] = []

    def open_dropbox_folder(self):
        db_path = self.db_ent.get().strip()
        if os.path.exists(db_path):
            webbrowser.open(os.path.normpath(db_path))
        else:
            messagebox.showwarning("Inaccessible", "Dossier Dropbox invalide.")

    def open_wiki(self):
        game = self.game_name_combo.get().strip()
        url = f"https://www.pcgamingwiki.com/w/index.php?search={game.replace(' ', '+')}" if game else "https://www.pcgamingwiki.com/"
        webbrowser.open(url)

    def browse_db(self):
        path = filedialog.askdirectory()
        if path:
            self.db_ent.delete(0, tk.END)
            self.db_ent.insert(0, path)
            self.refresh_game_list(path)
            self.save_config(path)

    def browse_source(self):
        path = filedialog.askdirectory()
        if path:
            self.source_ent.delete(0, tk.END)
            self.source_ent.insert(0, path)

    def open_referral(self):
        webbrowser.open("https://www.dropbox.com/referrals/AACSMrk1tmg5-h6Q9JYhLiZLllAoWpNLbnE?src=global9")

    def process_sync(self):
        confirm = messagebox.askyesno("Sécurité", "Avez-vous effectué une sauvegarde manuelle de vos fichiers ?")
        if not confirm: return

        src = os.path.normpath(self.source_ent.get().strip())
        db_root = os.path.normpath(self.db_ent.get().strip())
        game_name = self.game_name_combo.get().strip()

        if not all([src, db_root, game_name]):
            messagebox.showerror("Erreur", "Tous les champs sont requis.")
            return

        target_path = os.path.join(db_root, game_name)

        try:
            if os.path.exists(target_path):
                if not messagebox.askyesno("Cloud", f"Lier aux sauvegardes cloud de '{game_name}' ?"): return
                if os.path.exists(src): shutil.rmtree(src)
            else:
                if os.path.exists(src):
                    shutil.copytree(src, target_path)
                    shutil.rmtree(src)
                else: os.makedirs(target_path)

            if platform.system() == "Windows":
                subprocess.run(f'mklink /J "{src}" "{target_path}"', check=True, shell=True)
            else:
                os.symlink(target_path, src)

            messagebox.showinfo("Succès", "Synchronisation SAC v1.0 activée !")
            self.save_config(db_root)
            self.refresh_game_list(db_root)
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec : {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SaveAutoCloud(root)
    root.mainloop()
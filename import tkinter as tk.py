import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import random
import time
import threading
import os

class ImageRouletteApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Roleta de Imagens")
        self.image_paths = []

        self.canvas = tk.Canvas(master, width=400, height=300)
        self.canvas.pack()

        self.select_button = tk.Button(master, text="Selecionar Pasta com Imagens", command=self.selecionar_pasta)
        self.select_button.pack(pady=5)

        self.start_button = tk.Button(master, text="Iniciar Roleta", command=self.iniciar_roleta)
        self.start_button.pack(pady=5)

        self.img_tk = None  # Referência da imagem atual exibida

    def selecionar_pasta(self):
        pasta = filedialog.askdirectory()
        if pasta:
            self.image_paths = self._carregar_imagens_da_pasta(pasta)

    def _carregar_imagens_da_pasta(self, pasta):
        extensoes_validas = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
        return [
            os.path.join(pasta, f)
            for f in os.listdir(pasta)
            if f.lower().endswith(extensoes_validas)
        ]

    def iniciar_roleta(self):
        if not self.image_paths:
            return
        threading.Thread(target=self._rodar_roleta).start()

    def _rodar_roleta(self):
        for _ in range(15):
            img_path = random.choice(self.image_paths)
            self._mostrar_imagem(img_path)
            time.sleep(0.1)
        escolhida = random.choice(self.image_paths)
        self._mostrar_imagem(escolhida)

    def _mostrar_imagem(self, img_path):
        img = Image.open(img_path)
        img = img.resize((400, 300), Image.Resampling.LANCZOS)
        self.img_tk = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img_tk)

# Criar a janela principal
root = tk.Tk()
app = ImageRouletteApp(root)
root.mainloop()

import tkinter as tk
import pandas as pd
from PIL import Image, ImageTk
import main
from tkinter import ttk
import os
import time

matriz = r'.\csv\matriz.csv'
matrizleitura = pd.read_csv(matriz, sep=';', header=None)
rows1, cols1 = matrizleitura.shape

NDC = r'.\csv\cavaleirosDeOuro.csv'
NDCleitura = pd.read_csv(NDC, sep=';', header=None)
rows2, cols2 = NDCleitura.shape

Cosmo = r'.\csv\cavaleirosDeBronze.csv'
Cosmoleitura = pd.read_csv(Cosmo, sep=';', header=None)
rows3, cols3 = Cosmoleitura.shape

def atualizar_csvs():
    global matrizleitura, NDCleitura, Cosmoleitura, rows1, cols1, rows2, cols2, rows3, cols3
    matrizleitura = pd.read_csv(matriz, sep=';', header=None)
    rows1, cols1 = matrizleitura.shape
    NDCleitura = pd.read_csv(NDC, sep=';', header=None)
    rows2, cols2 = NDCleitura.shape
    Cosmoleitura = pd.read_csv(Cosmo, sep=';', header=None)
    rows3, cols3 = Cosmoleitura.shape
    for item in matrix_rects + ndc_rects + ndc_texts + cosmo_rects + cosmo_texts:
        canvas.delete(item)
    matrix_rects.clear()
    ndc_rects.clear()
    ndc_texts.clear()
    cosmo_rects.clear()
    cosmo_texts.clear()
    draw_interface()
    root.after(1000, atualizar_csvs)

root = tk.Tk()
root.title("Os Cavaleiros do Zodíaco: A Saga do Santuário")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
cell_size = 19
root.geometry(f"{screen_width}x{screen_height}+0+0")

fundo = Image.open(r'./Imagens/Fundo.jpg')
fundo = fundo.resize((screen_width, screen_height))
fundoTk = ImageTk.PhotoImage(fundo)

canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack(fill= "both", expand= True)
canvas.image = fundoTk
canvas.create_image(0, 0, image=fundoTk, anchor='nw')

matrix_rects = []
ndc_rects = []
ndc_texts = []
cosmo_rects = []
cosmo_texts = []

button = tk.Button(root, 
                   activebackground='#0B5CB9',
                   activeforeground="#E6AE16",
                   width=15, 
                   height=1, 
                   text='Começar Batalha!', 
                   background='#000000',
                   borderwidth=5,
                   foreground="#0B5CB9",
                   command=lambda: main.main)
button1 = tk.Button(root, 
                   activebackground='#0B5CB9',
                   activeforeground="#E6AE16",
                   width=15, 
                   height=1, 
                   text='Mudar o Caminho', 
                   background='#000000',
                   borderwidth=5,
                   foreground="#0B5CB9",
                   command=lambda: main.main)

buttonCanva = canvas.create_window(1300, 200, anchor=tk.NE, window=button)
buttonCanva = canvas.create_window(1300, 250, anchor=tk.NE, window=button1)

def draw_interface():
    global matrix_rects, ndc_rects, ndc_texts, cosmo_rects, cosmo_texts
    matrix_rects = []
    ndc_rects = []
    ndc_texts = []
    cosmo_rects = []
    cosmo_texts = []
    for r in range(rows1):
        for c in range(cols1):
            if matrizleitura.iloc[r, c] == 14:
                color = "#545454"
            if matrizleitura.iloc[r, c] == 15:
                color = "#808080"
            if matrizleitura.iloc[r, c] == 16:
                color = "#D3D3D3"
            if matrizleitura.iloc[r, c] == 13:
                color = "green"
            if matrizleitura.iloc[r, c] == 0:
                color = "red"
            if matrizleitura.iloc[r, c] < 13 and matrizleitura.iloc[r, c] > 0:
                color = "gold"
            if matrizleitura.iloc[r, c] == 17:
                color = "bronze"
            
            x1 = c * cell_size
            y1 = r * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            rect_id = canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
            matrix_rects.append(rect_id)

    for c, row in NDCleitura.iterrows():
        for r, value in enumerate(row):
            cell_width = 70
            cell_height = 30
            start_x = 1000
            start_y = 300
            x1 = r * cell_width
            y1 = c * cell_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height
            rect_id = canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
            canvas.move(rect_id, 965, 320)
            ndc_rects.append(rect_id)
            text_id = canvas.create_text(start_x + r*cell_width, start_y + (c+1)*cell_height, text=str(value), anchor='center')
            ndc_texts.append(text_id)

    for c, row in Cosmoleitura.iterrows():
        for r, value in enumerate(row):
            cell_width = 100
            cell_height = 30
            start_x = 1300
            start_y = 300
            x1 = r * cell_width
            y1 = c * cell_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height
            rect_id = canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
            canvas.move(rect_id, 1250, 320)
            cosmo_rects.append(rect_id)
            text_id = canvas.create_text(start_x + r*cell_width, start_y + (c+1)*cell_height, text=str(value), anchor='center')
            cosmo_texts.append(text_id)

draw_interface()

atualizar_csvs()

root.mainloop()
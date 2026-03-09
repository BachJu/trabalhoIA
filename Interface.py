import tkinter as tk
import pandas as pd
from PIL import Image, ImageTk
import main
import os
from tkinter import messagebox
from classes.CavaleiroBronze import CavaleiroBronze
from classes.CavaleiroOuro import CavaleiroOuro
from classes.Batalha import BatalhaHeuristica
from classes.buscaA import *

script_dir = os.path.dirname(os.path.abspath(__file__))

matriz = os.path.join(script_dir, 'csv', 'matriz.csv')
matrizleitura = pd.read_csv(matriz, sep=';', header=None)
rows1, cols1 = matrizleitura.shape

original_matriz = matrizleitura.copy()

NDC = os.path.join(script_dir, 'csv', 'cavaleirosDeOuro.csv')
NDCleitura = pd.read_csv(NDC, sep=';', header=None)
rows2, cols2 = NDCleitura.shape

Cosmo = os.path.join(script_dir, 'csv', 'cavaleirosDeBronze.csv')
Cosmoleitura = pd.read_csv(Cosmo, sep=';', header=None)
rows3, cols3 = Cosmoleitura.shape

def atualizar_csvs():
    global matrizleitura, NDCleitura, Cosmoleitura, rows1, cols1, rows2, cols2, rows3, cols3
    if not edit_mode:
        matrizleitura = pd.read_csv(matriz, sep=';', header=None)
        rows1, cols1 = matrizleitura.shape
    for item in ndc_rects + ndc_texts + cosmo_rects + cosmo_texts:
        canvas.delete(item)
    ndc_rects.clear()
    ndc_texts.clear()
    cosmo_rects.clear()
    cosmo_texts.clear()
    draw_interface(current_path)
    root.after(5000, atualizar_csvs)

root = tk.Tk()
root.title("Os Cavaleiros do Zodíaco: A Saga do Santuário")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
cell_size = 19
root.geometry(f"{screen_width}x{screen_height}+0+0")

dados = carregar_matriz()
matr, inicio, fim, casas_lista = dados
custo_matriz, paths = main.calculo_rotas(matr, casas_lista, inicio, fim)
ouro_path = os.path.join(script_dir, 'csv', 'cavaleirosDeOuro.csv')
cavaleirosOuro = CavaleiroOuro.alocarCavaleirosDeOuroCsvParaLista(ouro_path)
bronze_path = os.path.join(script_dir, 'csv', 'cavaleirosDeBronze.csv')
cavaleirosBronze = CavaleiroBronze.alocarCavaleirosDeBronzeCsvParaLista(bronze_path)
ordem_fixa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
batalha = BatalhaHeuristica(cavaleirosBronze, cavaleirosOuro, ordem_fixa)
tempo, batalhas = batalha.h()

fundo = Image.open(os.path.join(script_dir, 'Imagens', 'Fundo.jpg'))
fundo = fundo.resize((screen_width, screen_height))
fundoTk = ImageTk.PhotoImage(fundo)

canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.grid(row=0, column=0, sticky="nsew")
canvas.image = fundoTk
canvas.create_image(0, 0, image=fundoTk, anchor='nw')

text_area = tk.Text(root, height=15, wrap=tk.WORD)
text_area.place(x=1100, y=250, width=400, height=500)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

matrix_rects = []
ndc_rects = []
ndc_texts = []
cosmo_rects = []
cosmo_texts = []

matrix_rects_dict = {}

current_path = []

edit_mode = False

animating = False

def toggle_edit():
    global edit_mode
    edit_mode = not edit_mode
    if edit_mode:
        button1.config(text="Salvar e Sair")
        canvas.bind("<Button-1>", on_canvas_click)
    else:
        button1.config(text="Mudar o Caminho")
        canvas.unbind("<Button-1>")
        save_matrix()
        draw_interface(current_path)

def on_canvas_click(event):
    global matrizleitura
    x, y = event.x, event.y
    col = x // cell_size
    row = y // cell_size
    if 0 <= row < rows1 and 0 <= col < cols1:
        val = matrizleitura.iloc[row, col]
        if val in [14, 15, 16]:
            new_val = {14: 15, 15: 16, 16: 14}[val]
            matrizleitura.iloc[row, col] = new_val
            draw_interface(current_path)

def save_matrix():
    global matriz
    matrizleitura.to_csv(matriz, sep=';', index=False, header=False)

def restore_matrix():
    global matrizleitura
    matrizleitura = original_matriz.copy()
    save_matrix()
    draw_interface(current_path)

def run_simulation():
    global current_path, animating
    if animating:
        animating = False
        button.config(text="Começar Batalha!")
        return
    result, paths = main.main()
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, result)
    all_positions = []
    for path in paths:
        all_positions.extend(path)
    current_path = []
    animating = True
    button.config(text="Parar Animação")
    animate_path(all_positions)

def animate_path(full_path):
    global current_path, animating
    if not animating or not full_path:
        if not full_path and animating:
            animating = False
            button.config(text="Começar Batalha!")
            messagebox.showinfo("Vitória contra o Mestre do Santuário", f"Parabéns Cavaleiros! Vocês salvaram Atena em {tempo + custo_matriz:.2f} minutos!")
            current_path = []
            draw_interface(current_path)
            text_area.delete(1.0, tk.END)
        return
    current_path.append(full_path.pop(0))
    draw_interface(current_path)
    root.after(50, animate_path, full_path)

button = tk.Button(root, 
                   activebackground='#0B5CB9',
                   activeforeground="#E6AE16",
                   width=20, 
                   height=2, 
                   text='Começar Batalha!', 
                   background='#000000',
                   borderwidth=5,
                   foreground="#0B5CB9",
                   font=("Helvetica", 12, "bold"),
                   command=lambda: run_simulation())
button1 = tk.Button(root, 
                   activebackground='#0B5CB9',
                   activeforeground="#E6AE16",
                   width=20, 
                   height=2, 
                   text='Mudar o Caminho', 
                   background='#000000',
                   borderwidth=5,
                   foreground="#0B5CB9",
                   font=("Helvetica", 12, "bold"),
                   command=lambda: toggle_edit())
button2 = tk.Button(root, 
                   activebackground='#0B5CB9',
                   activeforeground="#E6AE16",
                   width=20, 
                   height=2, 
                   text='Restaurar Matriz', 
                   background='#000000',
                   borderwidth=5,
                   foreground="#0B5CB9",
                   font=("Helvetica", 12, "bold"),
                   command=restore_matrix)

buttonCanva = canvas.create_window(1075, 450, anchor=tk.NE, window=button)
buttonCanva = canvas.create_window(1075, 550, anchor=tk.NE, window=button1)
buttonCanva = canvas.create_window(1075, 650, anchor=tk.NE, window=button2)

def draw_interface(path=[]):
    global matrix_rects, ndc_rects, ndc_texts, cosmo_rects, cosmo_texts, matrix_rects_dict
    if not matrix_rects_dict:
        for r in range(rows1):
            for c in range(cols1):
                x1 = c * cell_size
                y1 = r * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                rect_id = canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
                matrix_rects_dict[(r, c)] = rect_id
                matrix_rects.append(rect_id)
    
    for r in range(rows1):
        for c in range(cols1):
            val = matrizleitura.iloc[r, c]
            if val == 14:
                color = "#545454"
            elif val == 15:
                color = "#808080"
            elif val == 16:
                color = "#D3D3D3"
            elif val == 13:
                color = "green"
            elif val == 0:
                color = "red"
            elif val < 13 and val > 0:
                color = "gold"
            elif val == 17:
                color = "#CD7F32"
            else:
                color = "white"
            
            if (r, c) in path:
                color = "#CD7F32"
            
            canvas.itemconfig(matrix_rects_dict[(r, c)], fill=color)

    for c, row in NDCleitura.iterrows():
        for r, value in enumerate(row):
            cell_width = 70
            cell_height = 30
            x1 = 895 + r * cell_width
            y1 = 20 + c * cell_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height
            rect_id = canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
            ndc_rects.append(rect_id)
            text_x = x1 + cell_width // 2
            text_y = y1 + cell_height // 2
            text_id = canvas.create_text(text_x, text_y, text=str(value), anchor='center')
            ndc_texts.append(text_id)

    for c, row in Cosmoleitura.iterrows():
        for r, value in enumerate(row[1:]):
            cell_width = 100
            cell_height = 30
            x1 = 1100 + r * cell_width
            y1 = 20 + c * cell_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height
            rect_id = canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
            cosmo_rects.append(rect_id)
            text_x = x1 + cell_width // 2
            text_y = y1 + cell_height // 2
            text_id = canvas.create_text(text_x, text_y, text=str(value), anchor='center')
            cosmo_texts.append(text_id)

draw_interface(current_path)

atualizar_csvs()

root.mainloop()

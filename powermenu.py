import tkinter as tk;
import os;

# Inicialización de la Ventana
window = tk.Tk();
window.title("Power Menu");
window.geometry("400x230");

# Funciones de sesión
def pwoff():
    os.system("systemctl poweroff")

# Funcion para Reiniciar
def rboot():
    os.system("systemctl reboot")

# Funcion para Cerrar Sesión
def lgout():
    os.system("i3-msg exit")

# Funcion para cerrar la ventana
def close_win(e):
    window.destroy()

# Creación botones de la interfaz
poweroff = tk.Button(
    text="⏻",
    foreground="white",  # Set the text color to white
    background="#DA0037",
    width=8,
    height=4,
    font=("JetBrainsMonoNL Nerd Font", 12),
    borderwidth=1,
    command=pwoff,
);

reboot = tk.Button(
    text="",
    foreground="white",  # Set the text color to white
    background="#03506F",
    width=8,
    height=4,
    font=("JetBrainsMonoNL Nerd Font", 12),
    borderwidth=1,
    command=rboot,
);

logout = tk.Button(
    text="",
    foreground="black",  # Set the text color to white
    background="#FFD369",
    width=8,
    height=4,
    font=("JetBrainsMonoNL Nerd Font", 12),
    borderwidth=1,
    command=lgout
);

# Adición de los botones a la interfaz
poweroff.grid(row=1,column=1,padx=10, pady=10)
reboot.grid(row=1,column=2,padx=10)
logout.grid(row=1,column=3,padx=10)

# Creación de las etiquetas de la intefaz
lblMain = tk.Label(text="¿Qué acción desea realizar?", font=("Source Sans 3", 13))
lblPowerOff = tk.Label(text="Apagar",font=("Source Sans 3", 11))
lblReboot = tk.Label(text="Reiniciar",font=("Source Sans 3", 11))
lblLogOut = tk.Label(text="Salir", font=("Source Sans 3", 11))

# Adición de las etiquetas a la interfaz
lblMain.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
lblPowerOff.grid(row=2, column=1, padx=10, pady=10)
lblReboot.grid(row=2, column=2, padx=10, pady=10)
lblLogOut.grid(row=2, column=3, padx=10, pady=10)
window.bind("<Escape>", lambda e: close_win(e))
window.mainloop();


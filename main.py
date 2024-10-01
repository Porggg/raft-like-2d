# importation des modules necessaires
from tkinter import *
from math import ceil
from random import randint
from time import sleep

# chargement du fichier .txt
with open("Save.txt", "r") as f:
    liste_fic = f.read()

liste = liste_fic.split(",")

game = True

# definitions des attributs du joueur
#health_perso = int(liste[0])
health_perso = 10
#water_perso = int(liste[1])
water_perso = 10
#food_perso = int(liste[2])
food_perso = 10
#nb_feuille = int(liste[3])
nb_feuille = 10
#nb_planche = int(liste[4])  
nb_planche = 10
#nb_metal = int(liste[5])
nb_metal = 10

# coordonnées joueur
#x, y = int(liste[6]), int(liste[7]) # milieu = 910, 507
x, y = 100, 100

# 4 fonctions de déplacements
def move_up(evt):
    # deplacement   
    global x, y
    if y <= 48:
        pass
    else:
        y -= 48

    # insert the image in the canvas
    global image
    image = PhotoImage(file="Perso_up.png")
    la_mere.create_image(x, y, image=image)


def move_down(evt):
    # deplacement
    global x, y
    if y >= 1042:
        pass
    else:
        y += 48
    # insert the image in the canvas
    global image
    image = PhotoImage(file="Perso_down.png")
    la_mere.create_image(x, y, image=image)


def move_right(evt):
    # deplacement
    global x, y
    if x >= 1872:
        pass
    else:
        x += 48
    # insert the image in the canvas
    global image
    image = PhotoImage(file="Perso_right.png")
    la_mere.create_image(x, y, image=image)


def move_left(evt):
    # deplacement
    global x, y
    if x <= 48:
        pass
    else:
        x -= 48
    # insert the image in the canvas
    global image
    image = PhotoImage(file="Perso_left.png")
    la_mere.create_image(x, y, image=image)


# fonction du bouton creation --> menu creation
def menu_creation():

    def description(objet, prix, description, photo):

        def destroy_menu():

            def construire(evt):

                la_mere.create_image(round((evt.x/1920)*40)*48, ceil((evt.y/1020)*20)*48, image=photo)
                fenetre.unbind("<Button-1>")
        

            menu_creation.destroy()
            fenetre.bind("<Button-1>", construire)


        if nb_planche < 2:
            color = 'red'
            status = DISABLED
        elif nb_planche >=2:
            color = 'black'
            status = NORMAL

        Label(frame_crea_right, text=objet, font=(None, 20), bg='dark grey', fg='black').pack(pady=35)
        Label(frame_crea_right, text=prix, font=(None, 15), bg='dark grey', fg=color).pack()
        Label(frame_crea_right, text=description, font=(None, 15), bg='dark grey', fg='black').pack()
        canvas_image = Canvas(frame_crea_right, width=100, height=100, bg='blue')
        canvas_image.pack(pady=100)
        canvas_image.create_image(0, 0, image=fond)
        canvas_image.create_image(50, 50, image=photo)
        Button(frame_crea_right, text='Construire', command=destroy_menu, width=25, height=3, state=status).pack(pady=20)


    # creation de la fenetre
    menu_creation = Toplevel(fenetre)
    menu_creation.geometry("1570x820")
    menu_creation.title('Creation')
    menu_creation.iconbitmap('Icone_creation.ico')
    # creation de la frame sur laquelle les differentes contructions apparaissent
    frame_crea_left = Frame(menu_creation, width=1100, height=730, bg='black')
    frame_crea_left.place(x=0, y=150, height=730, width=1100)
    # creation de la frame sur laquelle la description de la construction selectionnée apparait
    frame_crea_right = Frame(menu_creation, width=470, height=730, bg='dark grey')
    frame_crea_right.place(x=1100, y=150, height=730, width=470)
    # frame titre
    title_frame = Frame(menu_creation, width=1570, height=150, bg='#54615F')
    title_frame.place(x=0, y=0, height=150, width=1570)
    # label titre 
    Label(title_frame, text='Menu Création', fg='black', bg='#54615F', font=(None, 20)).pack(pady=42)
    # label pour radeau
    Label(frame_crea_left, text='Radeau', bg='black', fg='white', font=(None, 10)).grid(column=0, row=0, pady=20)
    # canvas image radeau
    canvas_radeau = Canvas(frame_crea_left, width=100, height=100)
    canvas_radeau.grid(column=0, row=1, padx=75, sticky='n')
    canvas_radeau.create_image(0, 0, image=fond)
    canvas_radeau.create_image(50, 50, image=radeau)
    # selectionner pour radeau
    Button(frame_crea_left, text="Selectionner",
           command=lambda: description('Radeau', 'Coût : 2 planches', 'Une piece de radeau basique.', radeau),
           bg='dark grey').grid(column=0, row=2, pady=20)


def spawn_planche():

    def suite():
        la_mere.delete(one_element)

    one_element = la_mere.create_image(randint(10, 1870), randint(10, 970), image=planche)
    la_mere.after(5000, suite)


# creation de la fenetre
fenetre = Tk()
fenetre.title('Raft')
fenetre.attributes("-fullscreen", 1)
fenetre.configure(bg='white')
fenetre.resizable(False, False)

# evenements
fenetre.bind('z', move_up)
fenetre.bind('s', move_down)
fenetre.bind('d', move_right)
fenetre.bind('q', move_left)
fenetre.bind('a', menu_creation)

# creation de la mere
la_mere = Canvas(fenetre, width=1920, height=1080)
la_mere.pack()
fond = PhotoImage(file='Mer.PNG')
la_mere.create_image(960, 540, image=fond)

# setup
radeau = PhotoImage(file='Radeau.PNG')
la_mere.create_image(960, 528, image=radeau)
la_mere.create_image(960, 576, image=radeau)
la_mere.create_image(910, 528, image=radeau)
la_mere.create_image(910, 576, image=radeau)
image = PhotoImage(file='Perso_up.png')
la_mere.create_image(x, y, image=image)
planche = PhotoImage(file="Planche.PNG")

# bouton construire
marteau = PhotoImage(file='Bouton_construire.PNG')
button_creation = Button(la_mere, width=150, height=150, image=marteau, command=menu_creation)
la_mere.create_window(1800, 960, window=button_creation)

fenetre.mainloop()


# save
with open("Save.txt", "w") as r:
    r.write(str(health_perso) + "," + str(water_perso) + "," + str(food_perso) + "," 
    + str(nb_feuille) + "," + str(nb_planche) + "," + str(nb_metal) + "," 
    + str(x) + "," + str(y))

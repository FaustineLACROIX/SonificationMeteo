import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

    
class Application(tk.Tk):
    # Création de la fenêtre
    def __init__(self, callback):
        super().__init__()
        self.callback = callback  # Fonction à appeler pour envoyer les données à `main.py`
        self.title("Interface Météo-Musicale")
        self.geometry("650x500")

        self.create_widgets()
        

    def create_info_button(self, frame, message):
        return tk.Button(frame, text="i", command=lambda: self.show_info(message), font=("Arial", 8, "bold"), fg="white", bg="#8FBC8F", width=2, height=1, relief=tk.FLAT, bd=0)

    def create_widgets(self):
        # Titre principal
        title_label = tk.Label(self, text="Personnalisation des paramètres musicaux", font=("Arial", 12, "bold"))
        title_label.pack(pady=10)
        
        # Champs texte
        frame_city = tk.Frame(self)
        frame_city.pack(fill=tk.X, padx=10, pady=5)
        city_label = tk.Label(frame_city, text="Nom de la ville :", width=25, anchor="w")
        city_label.pack(side=tk.LEFT)
        self.city_entry = tk.Entry(frame_city, width=30)
        self.city_entry.pack(side=tk.RIGHT, expand=True)
        self.create_info_button(frame_city, "Entrez le nom d'une ville valide, sans majuscule (ex: bordeaux)").pack(side=tk.RIGHT, padx=5)
        
        frame_note = tk.Frame(self)
        frame_note.pack(fill=tk.X, padx=10, pady=10)  # Ajout d'espace
        note_label = tk.Label(frame_note, text="Note de départ :", width=25, anchor="w")
        note_label.pack(side=tk.LEFT)
        self.note_entry = tk.Entry(frame_note, width=30)
        self.note_entry.pack(side=tk.RIGHT, expand=True)
        self.create_info_button(frame_note, "Entrez une note musicale \n(ex: Do4 ou La4)\nLa4 est la note de fréquence : 440Hz").pack(side=tk.RIGHT, padx=5)

        # Cases à cocher exclusives (RadioButtons)
        frame_frequency = tk.Frame(self)
        frame_frequency.pack(fill=tk.X, padx=10, pady=10)  # Ajout d'espace
        frequency_label = tk.Label(frame_frequency, text="Fréquence des notes :", width=25, anchor="w")
        frequency_label.pack(side=tk.LEFT)
        
        self.frequency_var = tk.StringVar(value="1 note / 15 min")
        frequencies = ["1 note / 15 min", "1 note / 30 min", "1 note / 1 h", "1 note / 2 h"]
        
        frame_radio = tk.Frame(self)
        frame_radio.pack(fill=tk.X, padx=10, pady=10)  # Ajout d'espace
        
        for freq in frequencies:
            rb = tk.Radiobutton(frame_radio, text=freq, variable=self.frequency_var, value=freq)
            rb.pack(side=tk.LEFT, padx=5)

        # Menus déroulants pour la météo
        self.weather_conditions = ["Ensoleilé", "Nuageux", "Brumeux", "Pluvieux", "Neigeux", "Orageux"]
        instruments_list = [
                "Piano acoustique", "Piano électrique 1", "Piano électrique 2", "Clavinet", "Harpsichord", "Clavecin", 
                "Piano Honky Tonk", "Piano électrique FM", "Célesta", "Glockenspiel", "Boîte à musique", "Vibraphone", 
                "Marimba", "Xylophone", "Tubular Bells", "Dulcimer", "Orgue à tirettes", "Orgue percussif", "Orgue rock", 
                "Orgue de théâtre", "Orgue à vent", "Accordéon", "Harmonica", "Bandonéon", "Guitare électrique (jazz)", 
                "Guitare folk", "Guitare clean", "Guitare palm-mute", "Guitare overdrive", "Guitare distorsion", 
                "Guitare harmonique", "Basse acoustique", "Basse électrique (doigts)", "Basse électrique (médiator)", 
                "Basse fretless", "Slap Bass 1", "Slap Bass 2", "Synth Bass 1", "Synth Bass 2", "Violon", "Alto", 
                "Violoncelle", "Contrebasse", "Tremolo Strings", "Pizzicato Strings", "Harpe", "Timpani", 
                "Orchestre à cordes 1", "Orchestre à cordes 2", "Chœur Ahh", "Chœur Ooh", "Synth Voice", 
                "Orchestre synthétique", "Trumpet", "Trombone", "Tuba", "Trompette sourdine", "Cor", 
                "Cuivres synthétiques", "Trompette synthétique", "Tuba synthétique", "Cuivres synthétiques 2", 
                "Violon synthétique", "Section de cuivres", "Soprano Saxophone", "Alto Saxophone", "Ténor Saxophone", 
                "Saxophone baryton", "Hautbois", "Basson", "Clarinette", "Flûte", "Flûte piccolo", "Flûte à bec", 
                "Flûte de pan", "Bouteille soufflée", "Shakuhachi", "Whistle", "Ocarina", "Guitare acoustique (nylon)", 
                "Guitare acoustique (acier)", "Guitare électrique (jazz)", "Guitare électrique (clean)", 
                "Guitare électrique (muted)", "Guitare Overdrive", "Guitare distorsion", "Guitare harmonique", 
                "Basse acoustique", "Basse électrique (finger)", "Basse électrique (pick)", "Basse fretless", 
                "Slap Bass 1", "Slap Bass 2", "Synth Bass 1", "Synth Bass 2", "Violon", "Alto", "Violoncelle", 
                "Contrebasse", "Tremolo Strings", "Pizzicato Strings", "Harpe", "Timpani", "Orchestre à cordes 1", 
                "Orchestre à cordes 2", "Ensemble choral", "Ensemble choral (voix synth.)", "Orchestre synthétique", 
                "Ensemble à vent", "Synth-brass 1", "Synth-brass 2", "Saxophone synthétique", "Synth Pad 1 (Fantasia)", 
                "Synth Pad 2 (Warm)", "Synth Pad 3 (Polysynth)", "Synth Pad 4 (Space)", "Synth Pad 5 (Bow)", 
                "Synth Pad 6 (Metal)", "Synth Pad 7 (Halo)", "Synth Pad 8 (Sweep)", "Effet pluie", "Soundtrack", 
                "Crystal", "Atmosphere", "Brightness", "Goblins", "Echoes", "Sci-fi"
            ]


        self.menus = {}
        frame_weather = tk.Frame(self)
        frame_weather.pack(fill=tk.X, padx=10, pady=10)  # Ajout d'espace
            
        for weather in self.weather_conditions:
            frame = tk.Frame(frame_weather)
            frame.pack(fill=tk.X, pady=3)
            label = tk.Label(frame, text=f"{weather} :", width=25, anchor="w")
            label.pack(side=tk.LEFT)
            
            if weather == "Ensoleilé":
                default_instrument = "Violoncelle"
            elif weather == "Nuageux":
                default_instrument = "Ocarina"
            elif weather == "Brumeux":
                default_instrument = "Crystal"
            elif weather == "Pluvieux":
                default_instrument = "Synth pad 6"
            elif weather == "Neigeux":
                default_instrument = "Harpe"
            else:
                    default_instrument = "Timpani"
                    
            menu_var = tk.StringVar(value=default_instrument)
            menu = ttk.Combobox(frame, textvariable=menu_var, values=instruments_list, state="readonly", width=27)
            menu.pack(side=tk.RIGHT, expand=True)
                
            self.create_info_button(frame, f"Choississez un instrument adapté pour jouer l'accompagnement si le temps est {weather}.").pack(side=tk.RIGHT, padx=5)
                
            self.menus[weather] = menu_var

        # Ajout d'espace après Orage
        frame_space = tk.Frame(self, height=15)
        frame_space.pack()
        
        # Bouton de validation
        submit_button = tk.Button(self, text="Valider", command=self.submit)
        submit_button.pack(pady=10)

        # Zone d'affichage du résultat
        #result_label = tk.Label(self, text="", justify=tk.LEFT, wraplength=380)
        #result_label.pack(padx=10, pady=5)

    def show_info(self, message):
        messagebox.showinfo("Information", message)

    def submit(self):
        city = self.city_entry.get()
        if not city:
            # Si la ville est vide, afficher un message d'erreur et arrêter la fonction
            messagebox.showerror("Erreur", "Le champ Ville doit être rempli.")
            return 
        note = self.note_entry.get()
        print(note)
        isNote = re.compile(r"^(Do|Re|Mi|Fa|Sol|La|Si)[0-9]$")
        if not isNote.match(note):
            # Si la note de départ est vide,
            #afficher un message d'erreur et arrêter la fonction
            messagebox.showerror("Erreur", "Le champ Note de départ doit être correctement rempli.")
            return
        freq = self.frequency_var.get()
        instruments = {weather: self.menus[weather].get() for weather in self.weather_conditions}
                
        #print(f"Ville : {city}")
        #print(f"Note de départ : {note}")
        #print(f"Fréquence : {freq}")
        #print("Instruments :", instruments)
        self.callback(city, note, freq, instruments)
                
        #result_label.config(text=f"Ville : {city}\nNote : {note}\nFréquence : {freq}\n" + "\n".join(f"{k} : {v}" for k, v in instruments.items()))



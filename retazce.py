# Kontrola hesla
password = input("Zadajte heslo: ")

if len(password) >= 6:
    print("Heslo bolo úspešne vytvorené!")
else:
    print("Heslo má málo znakov")

# Funkcia na registráciu
def registracia():
    print("User name musí mať od 5 do 15 znakov.")
    user_name = input("Zadajte user name: ")
    
    if 5 <= len(user_name) <= 15:
        print("User name má správny počet znakov.")
    else:
        print("Zadali ste nesprávny počet znakov, skúste znova.")
        return  # Ukončenie funkcie, ak je user name nesprávny
    
    print("Zadajte heslo. Heslo musí obsahovať aspoň jedno veľké písmeno, jedno malé písmeno, aspoň jedno číslo a má mať 6 až 20 znakov.")
    pass1 = input("Zadajte heslo: ")
    
    # Kontrola hesla
    if (
        any(char.islower() for char in pass1) and  # Aspoň jedno malé písmeno
        any(char.isupper() for char in pass1) and  # Aspoň jedno veľké písmeno
        any(char.isdigit() for char in pass1) and  # Aspoň jedno číslo
        6 <= len(pass1) <= 20                      # Dĺžka hesla
    ):
        pass2 = input("Zadajte heslo znova: ")
        if pass1 == pass2:
            print("Heslá sa zhodujú. Registrácia úspešná!")
        else:
            print("Heslá sa nezhodujú, skúste znova.")
    else:
        print("Heslo nespĺňa požiadavky, skúste znova.")

# Zavolanie funkcie registracia
registracia()

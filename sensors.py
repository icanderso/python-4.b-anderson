def read_sensor_data(file_name):
    try:
        with open(file_name, 'r') as file:
            # Načíta hodnoty zo súboru a prevedie ich na celé čísla
            data = [int(line.strip()) for line in file]

        if not data:
            print("Súbor je prázdny.")
            return

        # Výpočet maximálnej, minimálnej hodnoty a priemeru
        max_value, min_value, avg_value = max(data), min(data), sum(data) / len(data)

        # Výstup výsledkov
        print(f"Maximálna hodnota: {max_value}")
        print(f"Minimálna hodnota: {min_value}")
        print(f"Priemer hodnôt: {avg_value:.2f}")

    except FileNotFoundError:
        print(f"Chyba: Súbor '{file_name}' neexistuje.")
    except ValueError:
        print("Chyba: Súbor obsahuje neplatné údaje. Očakávajú sa iba celé čísla.")

# Spustenie programu
file_name = input("Zadajte názov súboru: ")
read_sensor_data(file_name)

def lasit_druka():
    try:
        # Lietotājs ievada datus
        faila_nosaukums = input("Ievadiet faila nosaukumu: ")
        faila_formats = input("Ievadiet faila formātu (paplašinājumu): ")

        # Izveido nosacījumu, sastādot nosaukumu un formātu
        fails = f"{faila_nosaukums}.{faila_formats}"

        with open(fails, 'r', encoding='utf-8') as fails:
            saturs = fails.read()
            print(f"Faila saturs: ")
            print(saturs)
    except FileNotFoundError:
        print(f"Kļūda: Fails '{fails}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: Neizdevās nolasīt failu. Kļūda: {e}")

# Izsaucam funkciju
lasit_druka()

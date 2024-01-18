def vards_faila():
    try:
        # Lietotājs ievada datus
        vards = input("Ievadiet savu vārdu: ")

        # Faila nosaukums
        faila_nosaukums = "cilveks.txt"

        # Ieraksta vārdu failā
        with open(faila_nosaukums, 'w', encoding='utf-8') as fails:
            fails.write(vards)

        print(f"Vārds veiksmīgi ierakstīts failā '{faila_nosaukums}'.")
    except Exception as e:
        print(f"Kļūda: Neizdevās ierakstīt vārdu failā. Kļūda: {e}")

# Izsauc funkciju
vards_faila()

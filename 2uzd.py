import csv

def lasit(csv_fails):
    try:
        with open(csv_fails, 'r', newline='', encoding='utf-8') as fails:
            lasitajs = csv.reader(fails)
            
            # Pārskata un izdrukā otrās kolonnas vērtību
            for rinda in lasitajs:
                if len(rinda) >= 2:  # Pārbauda, vai rindā ir vismaz divas kolonnas
                    kolonna = rinda[1]
                    print(kolonna)
    except FileNotFoundError:
        print(f"Kļūda: Fails '{csv_fails}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: Neizdevās nolasīt failu. Kļūda: {e}")

# Ievada CSV failu
csv_fails = "dats.csv"
lasit(csv_fails)

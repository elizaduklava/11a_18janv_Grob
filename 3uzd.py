def lasit(txt_fails):
    try:
        with open(txt_fails, 'r', encoding='utf-8') as fails:
            rindas = fails.readlines()
            
            # Pārbauda, vai ir pietiekami daudz rindu
            if len(rindas) >= 3:
                tresa_rinda = rindas[2]  # Trešā rinda (rindas indekss sākas no 0)
                print("Trešās rindas saturs:")
                print(tresa_rinda)
            else:
                print("Failā nav pietiekami daudz rindu.")
    except FileNotFoundError:
        print(f"Fails '{txt_fails}' nav atrasts.")
    except Exception as e:
        print(f"Neizdevās nolasīt failu. Kļūda: {e}")

# Ievadiet faila ceļu šeit
faila_teksts = "fails.txt"
lasit(faila_teksts)

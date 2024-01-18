def lasa(txt):
    try:
        with open(txt, 'r', encoding='utf-8') as fails:
            info = fails.read()
            print("Faila saturs: ")
            print(info)
    except FileNotFoundError:
        print(f"Fails '{txt}' nav atrasts.")
    except Exception as e:
        print(f"Neizdevās nolasīt failu. Kļūda: {e}")

# Faila lasīšana
faila_lasis = "fails.txt"
lasa(faila_lasis)

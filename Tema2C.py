Elevi = ["Ana", "Bogdan", "Carmen", "Elena", "Felix"]
Note  = [10, 8, 10, 9, 6]
interogari_nume = ["Ana", "Mara", "Elena", "stop"]

i = 0
while i < len(interogari_nume) and interogari_nume[i] != "stop":
    nume = interogari_nume[i]
    if nume in Elevi:
        index = Elevi.index(nume)
        print(f"{nume} are nota {Note[index]}")
    else:
        print(f"{nume} nu exista in lista de elevi.")
    i += 1

    promovati = 0
    respinsi = 0

    i = 0
    while i < len(Note):
        if Note[i] >= 5:
            promovati += 1
        else:
            respinsi += 1
        i += 1

    print(f"Număr promovați: {promovati}")
    print(f"Număr respinși: {respinsi}")

    note_promovati = []

    i = 0
    while i < len(Note):
        if Note[i] >= 5:
            note_promovati.append(Note[i])
        i += 1

    if len(note_promovati) > 0:
        media = sum(note_promovati) / len(note_promovati)
        print(f"Media promovaților este: {media:.2f}")
    else:
        print("Nu există elevi promovați.")

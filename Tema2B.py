elevi = ["Ana","Bogdan","Carmen","Darius","Elena"]
note  = [9,       7,       10,      4,       8]
for i in range(len(note)):
    if note[i] < 10:
        note[i] += 1
        print("Note actualizate:",note)

elev_nou = "Felix"
nota_elev_nou = 6

elevi.append(elev_nou)
note.append(nota_elev_nou)

print("Liste actualizate:")
print("Elevi:",elevi)
print("Note:",note)

elev_de_sters   ="Darius"
if elev_de_sters in elevi:
    index = elevi.index(elev_de_sters)
    elevi.pop(index)
    note.pop(index)
    print(f"{elev_de_sters} a fost sters.")
else:
    print(f"{elev_de_sters} nu exista in lista.")

print("Liste actualizate:")
print("Elevi:",elevi)
print("Note:",note)

print("\nLista actualizata de elevi si note:")
for i in range(len(elevi)):
    print(f"{elevi[i]} - {note[i]}")

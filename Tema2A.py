elevi = ["Ana","Bogdan","Carmen","Darius","Elena"]
note  = [9,       7,       10,      4,       8]
elev_nou        ="Felix"
nota_elev_nou   = 6
elev_de_sters   ="Darius"
interogari_nume  =["Ana","Mara","Elena","stop"]
absente  = [1, 0, 2, 3, 0]
for e in range(len(note)):
      print(f"{elevi[e]} are nota {note[e]}")
# nota maxima
nota_max = max(note)
indice_max = note.index(nota_max)
print(f"Nota maxima este {nota_max}, obtinuta de {elevi[indice_max]}")
# nota minima
nota_min = min(note)
indice_min = note.index(nota_min)
print(f"Nota minima este {nota_min}, obtinuta de {elevi[indice_min]}")
media = sum(note) / len(note)
print(f"Media de {media:.2f}")
print("Elevii promovati sunt:")
for i in range(len(note)):
    if note[i]>=5:
        print(elevi[i])


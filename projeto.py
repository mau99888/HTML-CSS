livro = ("O Hobbit", "JR.Tolkien", "Ficção Cientifica", "30")
livro2 = ("Frankenstein", "Mary Shelley", "Ficção Cientifica", "25")
livro3 = ("Moby Dick", "Herman Melville", "Ficção Cientifica", "20")
lista_mista = [livro , livro2 , livro3]
print(lista_mista)
novo_livro = ("Jane Eyre", "Charlotte Bronte", "Romance", "15")
print(novo_livro)
print(livro[0])

import matplotlib.pyplot as plt

meses = ['O Hobbit', 'Frankenstein', 'Moby Dick', 'Jane Eyre']

vendas = [30, 25, 20, 15]

plt.bar(meses, vendas, color='royalblue')

plt.xlabel('Ficção Cientifica        x        Romance')

plt.ylabel('Vendas (em unidades)')

plt.title('Ficção Cientifica 75 x 15 Romance')

plt.show()

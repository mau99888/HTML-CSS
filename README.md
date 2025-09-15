import sqlite3
import pandas as pd

conn = sqlite3.connect('vendas.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS vendas1')
cursor.execute('''
CREATE TABLE vendas1 (
id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
data_venda DATE,
produto TEXT,
categoria TEXT,
valor_venda REAL
)
''')


cursor.execute('DROP TABLE IF EXISTS vendas2')
cursor.execute('''
CREATE TABLE vendas2 (
id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
data_venda DATE,
produto TEXT,
categoria TEXT,
valor_venda REAL
)
''')
cursor.execute('''
INSERT INTO vendas2 (data_venda, produto, categoria, valor_venda) VALUES
('2023-01-01', 'Apple', 'Eletrônicos', 3510.00),
('2023-01-05', 'Xiaomi', 'Eletrônicos', 3500.00),
('2023-02-10', 'Sansung', 'Eletrônicos', 3500.00),
('2023-03-15', 'Lacoste', 'Roupas', 400.00),
('2023-03-20', 'Polo', 'Roupas', 450.00),
('2023-04-02', 'Sansung', 'Roupas', 500.00),
('2023-05-05', 'Produto G', 'Livros', 150.00),
('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
('2023-07-20', 'Produto I', 'Roupas', 600.00),
('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
('2023-09-30', 'Produto K', 'Livros', 300.00),
('2023-10-05', 'Produto L', 'Roupas', 450.00),
('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
('2023-12-20', 'Produto N', 'Livros', 250.00);
''')

conn.commit()

vendas2 = pd.read_sql_query('SELECT * FROM vendas2', conn)
display(vendas2)
primeiro_item_vendas2 = vendas2.iloc[0]
print(primeiro_item_vendas2)
conn.close()

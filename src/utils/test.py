'''
    CREATE TABLE IF NOT EXISTS "order" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        quantity INTEGER NOT NULL,
        FOREIGN KEY (product_id) REFERENCES products (id)
    )
'''

'''('INSERT INTO "Product" (name, price, description, size, color, quantity) VALUES (?, ?, ?, ?, ?, ?)',
            ('Nike Zoom', 400, 'the product is of good quality ', 39, 'black and white', 2))
commit()'''
#"SELECT * FROM empleados WHERE nombre LIKE ?", (patron_nombre,)
#"DELETE FROM empleados WHERE id = ?", (id_empleado_a_eliminar,))
 #resul = cur.execute("SELECT * FROM Product WHERE id = ?", (product_id,))
  #      resul.fetchone()
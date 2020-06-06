**Base de datos:**
- Registros con id 0: son registros desconocidos
- Registros con id -1: se ha eliminado su procedencia
- Ej: un usuario quiere eliminar su cuenta. Se eliminan los registros de carrito con ese usuario_id, pero todavía se desea conservar el registro de compras: se reemplaza usuario_id por -1
- [ ] Agregar Usuario con id -1
- [ ] Reordenar campos usuario


**Modulos:**
- [x] AGREGAR REGISTRO DIRECCIONES! < IMPORTANTE
- [x] Añadir producto
- [x] Modificar datos producto
- [x] Añadir a carrito
- [ ] Modificar carrito
- [ ] Registro compra > Afecta stock de productos
- [ ] validaciones ?
- [x] Errores en clases < complicó el código, tal vez lo saquemos

**Ecomerce_app:**
- [x] Login
- [x] Alta usuario
- [x] Baja usuario
- [ ] Modificacion usuario
- [ ] Alta productos
- [ ] Baja productos
- [ ] Modificacion productos

**Agregar:**
- [x] validate_email (necesita py3dns)
- [x] getpass
- [ ] flask

**Hay q estructurar el programa:**
- [x] Guardar modulos en una carpeta común
- [ ] Programa principal en carpeta principal (main.py)

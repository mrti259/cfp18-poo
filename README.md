**Base de datos:**
- Registros con id 0: son registros desconocidos
- Registros con id -1: se ha eliminado su procedencia
- Ej: un usuario quiere eliminar su cuenta. Se eliminan los registros de carrito con ese usuario_id, pero todavía se desea conservar el registro de compras: se reemplaza usuario_id por -1
- [ ] Agregar Usuario con id -1
- [ ] Reordenar campos usuario


**Modulos:**
- [ ] Formulario usuario
- [ ] Formulario producto
- [ ] Formulario direccion
- [ ] validaciones ?

**Ecomerce_app:**
- [x] Login
- [x] Alta usuario
- [x] Baja usuario
- [x] Modificacion usuario
- [ ] Alta productos
- [ ] Baja productos
- [ ] Modificacion productos
- [ ] Alta direccion
- [ ] Baja direccion
- [ ] Modificacion direccion
- [ ] Alta carrito
- [ ] Baja carrito
- [ ] Modificacion carrito
- [ ] Registro compras

**Agregar:**
- [x] validate_email (necesita py3dns)
- [x] getpass
- [ ] flask

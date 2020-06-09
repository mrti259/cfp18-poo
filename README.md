**Base de datos:**
- Registros con id 0: son registros desconocidos
- Registros con id -1: se ha eliminado su procedencia
- Ej: un usuario quiere eliminar su cuenta. Se eliminan los registros de carrito con ese usuario_id, pero todavía se desea conservar el registro de compras: se reemplaza usuario_id por -1
- [ ] Agregar Usuario con id -1
- [ ] Reordenar campos usuario
- [ ] Poner datos de Paises
- [ ] Poner datos de Provincias
- [ ] Poner datos de Ciudades
- [ ] Poner datos de Marcas
- [ ] Poner datos de Categiruas

**Modulos:**
- [ ] Formulario usuario
- [x] Formulario producto
- [ ] Formulario direccion
- [ ] Validador

**Ecomerce_app:**
- [x] Login
- [x] Alta usuario
- [x] Baja usuario
- [x] Modificacion usuario
- [x] Alta productos
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
- [x] flask < crear virtualenv (excluido de git x si genera problemas de compatibilidad en windows y linux)

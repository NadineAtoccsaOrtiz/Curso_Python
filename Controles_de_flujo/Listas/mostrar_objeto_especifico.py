def miObjeto(**valores):
     nuevoObjeto = {
         "nombre":valores["a"],
         "apellido":valores["b"],
         "edad":"",
         "sexo":"",
         "direccion":""
  }
return nuevoObjeto
usuario = {
     "jose",
     "alvares",
     19,
     "toda la vida",
     "alla"
 }

print(miObjeto(a="jose",b="alvares"))

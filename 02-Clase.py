class Madre:


    def __init__(self):
        print("Soy madre")

    def info(self):
        print("Soy madre por segunda vez")

class Padre:
   
   def __init__(self):
      print("Soy padre")

   def info(self):
        print("Soy padre por segunda vez")


class Hijo(Madre, Padre):
    
    def __init__(self):
      super().__init__() # El metodo super pasa el self automaticamente por eso no se pone dentro del parametro
      Padre().__init__() # Tambien puedes hacer referencia al nombre de la clase padre y acceder a sus metodos
      print("Hoy hijo")

    def info(self):
      Madre().info() # Pero cuando tenemos mas de una clase lo mejor es llamarlas por su nombre pero tenemos que agregarle el self en los parametros
      Padre().info()
      print("Soy hijo otra vez")
         



hija = Hijo()

hija.info()

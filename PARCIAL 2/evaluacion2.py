# Se importa la librería hashlib para poder aplicar funciones hash (SHA-256)
import hashlib

# Se importa la librería time para generar marcas de tiempo (timestamp)
import time


# Se define la clase Bloque, que representa cada bloque dentro de la blockchain
class Bloque:

    # Constructor de la clase Bloque
    def __init__(self, indice, mensaje, hash_anterior):
        
        # Índice del bloque dentro de la cadena
        self.indice = indice
        
        # Marca de tiempo del momento en que se crea el bloque
        self.timestamp = time.time()
        
        # Mensaje o datos que se almacenan en el bloque
        self.mensaje = mensaje
        
        # Hash del bloque anterior (permite encadenar los bloques)
        self.hash_anterior = hash_anterior
        
        # Hash propio del bloque, calculado con sus datos
        self.hash = self.calcular_hash()

    # Método para calcular el hash del bloque
    def calcular_hash(self):
        
        # Se concatenan todos los datos importantes del bloque en un solo string
        datos = str(self.indice) + str(self.timestamp) + self.mensaje + self.hash_anterior
        
        # Se aplica el algoritmo SHA-256 al string convertido en bytes
        return hashlib.sha256(datos.encode()).hexdigest()


# Se define la clase Blockchain, que contiene la lista de bloques
class Blockchain:

    # Constructor de la blockchain
    def __init__(self):
        
        # Se inicializa la cadena con el bloque génesis
        self.cadena = [self.crear_bloque_genesis()]

    # Método para crear el primer bloque de la cadena (bloque génesis)
    def crear_bloque_genesis(self):
        
        # Se crea un bloque con índice 0, mensaje inicial y hash anterior en "0"
        return Bloque(0, "Bloque Génesis", "0")

    # Método para agregar un nuevo bloque a la cadena
    def agregar_bloque(self, mensaje):
        
        # Se obtiene el último bloque de la cadena
        anterior = self.cadena[-1]
        
        # Se crea un nuevo bloque con:
        # - índice actual (longitud de la cadena)
        # - mensaje recibido
        # - hash del bloque anterior
        nuevo = Bloque(len(self.cadena), mensaje, anterior.hash)
        
        # Se agrega el nuevo bloque a la cadena
        self.cadena.append(nuevo)

    # Método para mostrar todos los bloques de la cadena
    def mostrar(self):
        
        # Se recorre cada bloque en la cadena
        for bloque in self.cadena:
            
            # Se imprime el índice del bloque
            print("Índice:", bloque.indice)
            
            # Se imprime el mensaje almacenado en el bloque
            print("Mensaje:", bloque.mensaje)
            
            # Se imprime el hash del bloque
            print("Hash:", bloque.hash)
            
            # Se imprime el hash del bloque anterior
            print("Hash anterior:", bloque.hash_anterior)
            
            # Separador visual entre bloques
            print("---------------")


# -----------------------------
# SIMULACIÓN DE DOS SERVIDORES
# -----------------------------

# Se crea una instancia de la blockchain
blockchain = Blockchain()

# Se agrega un bloque simulando un mensaje enviado desde el servidor 1
blockchain.agregar_bloque("Servidor 1: Hola servidor 2")

# Se agrega un bloque simulando la respuesta del servidor 2
blockchain.agregar_bloque("Servidor 2: Hola servidor 1")

# Se agrega un tercer mensaje como confirmación
blockchain.agregar_bloque("Servidor 1: Mensaje recibido")

# Se muestran todos los bloques creados en la blockchain
blockchain.mostrar()
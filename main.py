import math

""" a)
A = (1, -2, 4)
B = (7, 0, 6)
C = (5, 6, -4)
D = (-1, 4, -6)
"""


""" b)
A = (3,2,-2)
B = (1,5,1)
C = (0,2,3)
E = (3, 2, 4)
"""

""" c)
A = (4, 1, 0)
B = (4, 8, 0)
C = (1, 8, 0)
E = (3, 2, 4)
"""

#""" d)
A = (6,0,0)
B = (0,4,0)
C = (0,0,0)
E = (2,2,6)
#"""

# Berechnet den Vektor on Punkt A zu B und gibt diesen als 'tuple' zurück.
def getVector(A, B):
  x = B[0] - A[0]
  y = B[1] - A[1]
  z = B[2] - A[2]
  print((x,y,z))
  return (x, y, z)

# Berechnet das Kreuzprodukt zweier Vektoren und gibt dies als 'tuple' zurück.
def kreuzprodukt(a, b):
  x = a[1]*b[2] - a[2]*b[1]
  y = a[2]*b[0] - a[0]*b[2]
  z = a[0]*b[1] - a[1]*b[0]
  print("Kreuzprodukt: " + str((x,y,z)))
  return (x, y, z)

# Berechnet das Skalarprodukt zweier Vektoren und gibt dies als double zurück.
def skalarprodukt(a, b):
  x = a[0] * b[0]
  y = a[1] * b[1]
  z = a[2] * b[2]
  print("Skalarprodukt: " + str(abs(x-y-z)))
  return x - y - z

# Berechnet den btrag ohne die Wurzel zu ziehen.
def summe(a):
  return a[0]**2 + a[1]**2 + a[2]**2

# Zieht die Wurzel aus einer Zahl.
def sqrt(s):
  return math.sqrt(s)


# a)  Berechnet den Flächeninhalt eines Parallelogramms.
def parallel(A, B, C):
  k = kreuzprodukt(getVector(A,B), getVector(A, C))
  return sqrt(summe(k))

# b)  Berechnet den Flächeninhalt eines Dreiecks.
def dreieck(A, B, C):
  k = kreuzprodukt(getVector(A,B), getVector(A, C))
  return sqrt(summe(k))/2

# c)  Berechnet den Flächeninhalt eines Spats.
def spat(A, B, C, D):
  a = getVector(A, B)
  b = getVector(A, C)
  c = getVector(A, D)

  k = kreuzprodukt(a, b)
  s = skalarprodukt(k, c)
  return abs(s)

# d)  Berechnet den Flächeninhalt einer dreiseitigen Pyramide.
def dreiPyramide(A, B, C, D):
  return (spat(A, B, C, D)/6)

# Ausgabefunktion für Parallelogramm.
def printParallel(A, B, C):
  print("Vektoren: ")
  print("Ergebnis: " + str(parallel(A, B, C)))
  print()

# Ausgabefunktion fürs Dreieck.
def printDreieck(A, B, C):
  print("Vektoren: ")
  print("Ergebnis: " + str(dreieck(A, B, C)))
  print()

# Ausgabefunktion fürs Spat.
def printSpat(A, B, C, D):
  print("Vektoren: ")
  print("Ergebnis: " + str(spat(A, B, C, D)))
  print()

# Ausgabefunktion für eine dreiseitige Pyramide.
def printDreiPyramide(A, B, C, D):
  print("Vektoren: ")
  print("Ergebnis: " + str(dreiPyramide(A, B, C, D)))
  print()

def printAll():
  printParallel(A, B, C),

  printDreieck(A, B, C)

  printSpat(A, B, C, E)

  printDreiPyramide(A, B, C, E)

printAll()

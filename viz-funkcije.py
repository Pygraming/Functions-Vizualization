# Import libraries 
import matplotlib.pyplot as plt 
import numpy as np 
  
# Unos pocetne i krajnje vrednosti  
start = float(input('Unesi pocetnu vrednost x: '))
end = float(input('Unesi krajnju vrednost x: '))

# Unos broja jednakih vrednosti za x
parts = int(input('Unesi broj jednakih vrednosti izmedju pocetne i kranje vrendosti: '))

# Unos visine i sirine
width = float(input('\nUnesi sirinu grafika: '))
height = float(input('Unesi visinu grafika: '))

# Kreiranje vektora x i y
x = np.linspace(start, end, parts) 
y = x ** 2
  
# Postavimo dimenzije prozora
fig = plt.figure(figsize = (width, height)) 
# Napravi grafik
plt.plot(x, y) 
# Napravi legendu
plt.legend(['y = x * x'])
  
# Prikazi grafik
plt.show()
# Este programa irá calcular as condições do ar que no processo de mistura não há 
# troca de calor com o ambiente.
# Dados do Ar externo
TBSe = 35; # ºC
TBUe = 25; # ºC
he = 76; # Kj / Kg
we= 0.016; # Kgvapor / Kgar
umre = 0, 2; # Kgvapor / Kgar


# Dados do Ar de refrigeração
TBSr = 24; # ºC 
hr = 47.5 # Kj / Kg
wr = 0.0093; # Kj / Kg
umrt = 0.5; # %
umrr = 0,8; 
hm = (0.25*he+hr)/1.25;
wm = (0.25*we+wr)/1.25;
print(hm)
print(wm)


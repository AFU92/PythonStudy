"""
distancia en km
tiempo en seg
retorna: "La velocidad es 36.0 km/h o 10.0 m/s"
"""
def velocidad(distancia, tiempo):
  resultado = ""
  velocidad_km_h = str(distancia/(tiempo/3600))
  velocidad_m_s = str((distancia*1000)/tiempo)
  resultado = "La velocidad es " + velocidad_km_h + " km/h o " + velocidad_m_s + "m/s"
  return resultado

def xor(a, b):
  xor = (a != b)
  return xor

print(velocidad(0.01, 1))
print(velocidad(1, 60))
print(xor(True, True))
print(xor(True, False))
print(xor(False, True))
print(xor(False, False))

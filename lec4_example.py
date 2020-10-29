import numpy as np

def grav_accel(phi=0,h=0):
  """Ускорение св.падения 
  phi - широта места наблюдения
  h - высота над пов-ю Земли"""
  g = 9.8(1+0.05*(np.sin(phi))**2 -0.000006*(np.sin(2*phi))**2)-0.000003086*h
  return g

def losing_weight_function(mass=50, phi_0=54, phi_end=0, h_0=0, h_end=3000):
  """Функция, определеяющая вес"""
  P_0 = grav_accel(phi_0, h_0)*mass  
  P_end = grav_accel(phi_end, h_end)*mass  
  delta_P = (P_0 - P_end)*100
  if delta_P>0:
    print('Вы похудеете на:',delta_P, 'г')
  elif delta_P<0:
    print('Вы поправитесь на:',delta_P*(-1), 'г')
  else:
   print('Я твой отец')


losing_weight_function(56, 0, 1000, 54, 0)
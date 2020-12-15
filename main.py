import numpy as np

def hamiltonian( spins, H ) : 
  energy = 0
  # Your code to calculate the hamiltonian goes here
  energy = -spins[0]*spins[-1] - H*spins[0]
  for i in range(1,len(spins)) : energy = energy - (spins[i-1] + H)*spins[i] 
  return energy
  
def ensemble_average( N, H, T ) :
  numerator, Z = 0, 0
  # Your code to calculate the ensemble average goes here
  spins = np.zeros(N)
  for index in range(2**N) :
      for i in range(N) :
          spins[i] = np.floor( index / 2**(N-1-i) )
          index = index - spins[i]*(2**(N-1-i))
          if spins[i]==0 : spins[i] = -1
      energy = hamiltonian(spins,H)
      bweight = np.exp( -energy / T )
      numerator = numerator + energy*bweight
      Z = Z + bweight
  return numerator / Z

# Calculate the ensemble average of the energy for a system of 5 spins 
# with no external field at a temperature of 0.1
print( ensemble_average(5,0,0.1) )

# Calculate the ensemble average for a system of 6 spins 
# with a magnetic field strength of 1 at a temperature of 0.5
print( ensemble_average(6,1,0.5) )

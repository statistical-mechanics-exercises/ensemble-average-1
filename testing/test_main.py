import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_ensemble_average(self) :
        for k in range(1,6) :
            numer1, numer2, numer3 = 0, 0, 0
            pfunc1, pfunc2, pfunc3 = 0, 0, 0
            for i in range(2**k) :
                num, spins = i, k*[0]
                for j in range(k) :
                   spins[j] = np.floor( num / 2**(k-1-j) )
                   num = num - spins[j]*2**(k-1-j)
                   if spins[j]==0 : spins[j] = -1
                eee = hamiltonian( spins, 0 )
                numer1 = numer1 + eee*np.exp( -eee / 0.5 )
                pfunc1 = pfunc1 + np.exp( -eee / 0.5 )
                eee = hamiltonian( spins, 1 )
                numer2 = numer2 + eee*np.exp( -eee / 0.1 )
                pfunc2 = pfunc2 + np.exp( -eee / 0.1 )
                eee = hamiltonian( spins, -2 )
                numer3 = numer3 + eee*np.exp( -eee / 0.8 )
                pfunc3 = pfunc3 + np.exp( -hamiltonian( spins, -2 ) / 0.8 )
        self.assertTrue( np.abs(numer1/pfunc1-ensemble_average(k,0,0.5))<1e-7, "The function for computing the ensemble averages is incorrect" )
        self.assertTrue( np.abs(numer2/pfunc2-ensemble_average(k,1,0.1))<1e-7, "The function for computing the ensemble averages is incorrect" )
        self.assertTrue( np.abs(numer3/pfunc3-ensemble_average(k,-2,0.8))<1e-7, "The function for computing the ensemble averages is incorrect" )
        
    def test_hamiltonian(self) :
        for i in range(2**5) :
            num, spins = i, 5*[0]
            for j in range(5) :
                spins[j] = np.floor( num / 2**(4-j) )
                num = num - spins[j]*2**(4-j)
                if spins[j]==0 : spins[j] = -1
            sumspins = sum( spins )
            coup_eng = spins[0]*spins[len(spins)-1]
            for i in range(len(spins)-1) : coup_eng = coup_eng + spins[i]*spins[i+1]
            self.assertTrue( np.abs(hamiltonian( spins, 1)+coup_eng+sumspins)<1e-7, "The energies computed by the Hamiltonian are incorrect" )
            self.assertTrue( np.abs(hamiltonian( spins, -1)+coup_eng-sumspins)<1e-7, "The energies computed by the Hamiltonian are incorrect" )
            self.assertTrue( np.abs(hamiltonian( spins, 0)+coup_eng)<1e-7, "The energies computed by the Hamiltonian are incorrect" )
            self.assertTrue( np.abs(hamiltonian( spins, 2)+coup_eng+2*sumspins)<1e-7, "The energies computed by the Hamiltonian are incorrect" )

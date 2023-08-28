# Ensemble averages

We have learned that if you have an analytic expression for the partition function you can extract the ensemble average for the energy and the magnetisation.  The problem is that we have not developed an analytic expression by performing these programming exercises.  In the last exercise we instead wrote a program that allowed us to calculate the value of the canonical partition function when the temperature and the magnetic field took on particular values.  In other words, the partition function we have learned to calculate is a single scalar and not an analytic function.  As it is not an analytic function we cannot extract values from ensemble averages from it.  

We must, therefore, calculate ensemble averages by a different means.  In this exercise we are, therefore, going to learn how to compute the ensemble average of the energy by using the following expression:

$$
\langle E\rangle=\frac{1}{Z}\sum_{j=1}^{M} E(\mathbf{x}_j)e^{-\beta E(\mathbf{x}_j)}
$$


In this expression ![](https://render.githubusercontent.com/render/math?math=Z) is the canonical partition function, which should be evaluated in the way that we just learned, ![](https://render.githubusercontent.com/render/math?math=\beta) is the inverse temperature and the sum runs over the M microstates, ![](https://render.githubusercontent.com/render/math?math=\mathbf{x}_j), that the system can adopt.  H, meanwhile, is one of the Hamiltonians that we learned how to compute during the first few of these exercises.  In this particular exercise we are going to use the Hamiltonian for the 1D Ising model in an external magnetic field, H:

![](https://render.githubusercontent.com/render/math?math=E=-\sum_{i=1}^{N}s_i\s_{i%2B1}-H\sum_{i=1}^{N}s_i)

The sums here run over the number of spins, N, and the geometry is closed so ![](https://render.githubusercontent.com/render/math?math=s_{N%2B1}=s_1).

When you fill in the code in `main.py` here the function `ensemble_average` should return the value of ![](https://render.githubusercontent.com/render/math?math=\langle\E\rangle) calculated using the formula above.  Within this function you will thus have a write a sum over all the possible microstates.  Notice, furthermore, that this function takes N (the number of spins), H (the magnetic field strength) and T (the temperature) as its input parameters. 

To compute ![](https://render.githubusercontent.com/render/math?math=\langle\E\rangle) you will need to compute the energy for each of the microstates that you generate.  In order to make the code more readable I have written a function called `hamiltonian` that takes the microscopic coordinates for all the spins and the magnetic field strength as its input parameters.  This function should calculate the energy for the input microstate using the Hamiltonian given above.   This function will need to be called for each of the microstates that you generate in the function called `ensemble_average`.

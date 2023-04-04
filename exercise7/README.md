# Lecture and exercise 7 primer

Dear students,

the files for tomorrow's exercise 7 -- including the Jupyter Notebook and the geometry and input files -- are now available on the GitHub repo. As mentioned in a previous post, we will forgo using the instance of JupyterHub on Euler for tomorrow, and instead run the Jupyter notebook locally while still running the calculations on Euler. Please make sure you have a local installation of python and jupyter for this (the simplest and most compact way, if you don't already have it, would just be to install an Anaconda distribution: https://www.anaconda.com/products/distribution). Please feel free to clone and peruse the exercise at your convenience after ssh'ing to Euler from a terminal:

```bash
$ ssh user@euler.ethz.ch
$ cd /Molecular-and-llaalla
# git stash: if necessary
# git init: if necessary
$ git clone https://github.com/ramador09/Molecular-and-Materials-Modelling-FS2023.git
```

After submitting the calculations on Euler, we will copy them via scp to our local machine in order to do the post-processing.
The content of the exercise will, as usual, be based on the lecture. The lecture will showcase the solution program of the Schrödinger equation, as it is conventionally carried out by computational physicists and chemists --- namely, in the framework of two mean-field theories, Hartree-Fock (HF) and density-functional theory (DFT).
With HF we had gotten acquainted with already last week (indeed, it was the method of solution in last week's exercise zwinkernd). We will deepen our discussion of HF by seeing them in rigorous matrix form, and investigate how they are actually solved.
This will naturally lead us to the important concept of basis sets -- we will learn what they are and get an introduction to the "zoology" of basis sets and basis functions: why they're used, why they're important, what different "flavours" they come in, including polarization and diffuse basis sets.
Our discussion of basis sets will then see the transition from HF to DFT, via the Hohenberg and Kohn theoremS (plural!) and up to and including exchange and correlation through the Kohn-Sham equations. The exercise will then employ the methods of DFT and will investigate the influence of different functionals as well as basis sets.
Of course, please do not hesitate to contact us with questions or concerns.

Best regards,

Ray

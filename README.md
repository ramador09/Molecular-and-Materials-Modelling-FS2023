# Molecular-and-Materials-Modelling-FS2023

Welcome, students!

My name is Raymond Amador, I am a PhD student with Daniele Passerone and I will be leading some of the exercise sessions this coming semester. As Daniele already mentioned in the first post, these exercises will make use of the Python language in Jupyter notebooks, and these notebooks will be run Euler. In order to make the most efficient use of our allotted time possible, there are some introductory steps to setting up Jupyter notebooks on Euler, which you are kindly requested to go through and have already completed before the start of the first exercise this Wed. 22.02.

1. This first step involves the almost trivial but nonetheless very important step of simply being connected to an ETHZ internal network: without being connected to an ETHZ network, none of the further steps will work and you will most likely get a network timeout error. This can either be done by being physically on the campus of the ETH and connecting via eduroam, or connecting from elsewhere via a VPN.

If you have already established network connections, both on the campus of the ETH and using a VPN, please continue to step 2; if you have already both established network connections and are able to ssh to Euler, please proceed to step 3.

  - Setting up the VPN: the initial installation of the VPN can be done using the following link: https://sslvpn.ethz.ch/
  - You will need to select and enter your appropriate credentials in order for the installation to proceed. Please note that the password for the VPN and ETH networks (so-called 'Radius password') is, in general different, from the one that you typically use to log in to MyStudies, Mail, etc. The activation of your Radius password is done via https://www.password.ethz.ch/authentication/login.html

2. Use ssh from a Terminal on your local computer in order to connect to Euler:

    $ ssh username@euler.ethz.ch
   
   and accept the Terms and Conditions (if you haven't already). More detailed information can be found here: https://scicomp.ethz.ch/wiki/Accessing_the_clusters

3. If you have already reached this step, you (hopefully, most likely) already fulfill all the prerequisites for opening an instance of JupyterLab on Euler. This can be done via the following link: https://jupyter.euler-dev.hpc.ethz.ch/hub/spawn

  - For reasons of priority in the initialisation queue, use the following startup parameters: 1 Core, 0 GPUs, 0.5GB of RAM, 3 hours of runtime.
    
4. Open a Terminal within this new environment and execute

    $ git clone 

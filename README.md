# SCS-network
Spinal cord stimulation (SCS) network model from Sagalajev et al. 2024

To simulate the SCS Network Model:

Install python3
Then from the terminal...

Install NEURON and NetPyNE:
% pip install neuron 
% pip install netpyne

Compile the mod files:
% nrnivmodl ./mods

Running the model in iPython:
% ipython run init.py

The output of this code reproduces the response of the SCS network model.

'''
Initialize NetPyNE file 

Running this code will use netParams and cfg for the network model

Steps:
In bash Terminal:
1. cd to directory (../SCS-Model)
2. compile .mods using >> nrnivmodl (arch -arch x86_64 nrnivmodl -- for M1 processor)
3. ipython
>> run init.py
'''

from netpyne import sim
from neuron import h
					
simConfig, netParams = sim.readCmdLineArgs(simConfigDefault='cfg.py', netParamsDefault='netParams.py')

# Create network and run simulation
sim.createSimulateAnalyze(netParams = netParams, simConfig = simConfig)
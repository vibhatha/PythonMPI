# Spawn Processes

The idea is to dynamically launch a new job using an existing MPI programme. 
The main advantage is without manually starting a complex job. A single programme can launch
multiple programmes. The most important thing is that the master programme can keep track on the
child processes that it has started up. Communication among the master task and the worker tasks
is also available.

In the master programme, you spawn the child processes. The 'Spawn' function returns an intercomm
 object which provides the capability in linking up with the child tasks. 
Similarly when the parent is fetched from the workers spawned by the master process, the
 intercomm object which opens up a link to the master can also be retrieved. 
At the master programme, an executable is called to launch the programme. This can be a bash
 script which provides specifics arguments in launching a python, java or any other programme. 
In order to learn more on this concept, please read the following references. 

# References

[Summary on Process Management](http://cw.squyres.com/columns/2005-02-CW-MPI-Mechanic.pdf)

[Spawn Example](http://etutorials.org/Linux+systems/cluster+computing+with+linux/Part+II+Parallel+Programming/Chapter+9+Advanced+Topics+in+MPI+Programming/)
 

 
 
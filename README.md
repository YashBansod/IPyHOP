# IPyHOP

Described in the Paper: [HTN Replanning from the Middle](https://journals.flvc.org/FLAIRS/article/download/130732/133891)

---
  
**If you use this repository please cite our work:**  

```bibtex
@inproceedings{bansod2022htn,
  title={HTN Replanning from the Middle},
  author={Bansod, Yash and Patra, Sunandita and Nau, Dana and Roberts, Mark},
  booktitle={The International FLAIRS Conference Proceedings},
  volume={35},
  year={2022}
}
```

Re-entrant Iterative PyHOP (Python Hierarchical Ordered Planner) written in Python 3.

IPyHOP uses HTN methods to decompose tasks into smaller and smaller subtasks, until it finds tasks that
correspond directly to actions. Some special features of IPyHOP are:

(1) In IPyHOP, one writes methods and actions as ordinary Python functions.  
(2) Instead of representing states as collections of logical assertions, IPyHOP uses state-variable representation:
    a state is a Python object that contains variable bindings.  
    
## Project Setup Instructions
- **Setup a virtual interpreter (optional)**  

```shell script
 python -m venv venv
```
- **Activate the virtual interpreter (if setup)**  

Ubuntu:  
```shell script
./venv/bin/activate
```
Windows:  
```shell script
./venv/Scripts/activate
```
- **Install project requirements**  

```shell script
pip install -r requirements.txt
```

## Run Instructions
- **Run an "example" file from the provided examples**  

To run any python file in the project  
Windows:  
```shell script
set PYTHONPATH=<path to project directory>
python <path to python file>
```
example:
```shell script
set PYTHONPATH=D:\GitHub\IPyHOP
python .\examples\robosub\robosub_example.py
```
Linux:  
```shell script
PYTHONPATH=<path to project directory> python <path to python file>
```
example:
```shell script
PYTHONPATH=/home/user/GitHub/IPyHOP python ./examples/robosub/robosub_example.py
```
*Note: The **PYTHONPATH** needs to be set up only once for your environment.*  

    
## TODO List:
*   Create a pip installable python package of IPyHOP.  
This would require writing the *setup.py* file and making the *.whl* (wheel) packages.
Follow the steps mentioned in the following link: https://packaging.python.org/tutorials/packaging-projects/ 
    
## Overview:

IPyHOP should work correctly in Python 3.5+.  
For examples of how to use it, see the example files that come with IPyHOP.

IPyHOP provides the following classes and functions:

* `state = State('foo')` tells IPyHOP to create an empty state object named 'foo'.  
    To put variables and values into it, you should do assignments such as `foo.var1 = val1`

* `methods = Methods()` tells IPyHOP to create an empty methods container.  
        To add tasks and associated task methods into it, you should use
        `methods.declare_task_methods(task_name, method_list)`.  
        To add tasks and associated goal methods into it, you should use
        `methods.declare_goal_methods(goal_name, method_list)`.  
        To add tasks and associated multigoal methods into it, you should use
        `methods.declare_multigoal_methods(goal_tag, method_list)`.  
        
* `actions = Actions()` tells IPyHOP to create an empty actions container.  
    To add actions into it, you should use `actions.declare_actions(action_list)`.  
    `declare_actions([a1, a2, ..., ak])` tells IPyHOP that a1, a2, ..., ak are all of the planning actions.
    This supersedes any previous call to `declare_actions([a1, a2, ..., ak])`.

* `planner = IPyHOP(methods, actions)` tells IPyHOP to create a IPyHOP planner object.  
    To plan using the planner, you should use `planner.plan(state, task_list)`.


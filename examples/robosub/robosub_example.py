#!/usr/bin/env python
"""
File Description: Robosub example file. Run this file to solve the Robosub planning problem.
"""

# ******************************************    Libraries to be imported    ****************************************** #
from __future__ import print_function
from examples.robosub.domain.robosub_methods import methods
from examples.robosub.domain.robosub_actions import actions
from examples.robosub.problem.robosub_problem_1 import init_state, task_list
from ipyhop import IPyHOP, planar_plot, post_failure_tasks


# ******************************************        Main Program Start      ****************************************** #
def main():
    print(methods)
    print(actions)
    print(init_state)

    planner = IPyHOP(methods, actions)
    planner.blacklist_command(('a_touch_back_v', 'v1', 'l2'))
    planner.blacklist_command(('a_touch_front_v', 'v1', 'l2'))
    plan = planner.plan(init_state, task_list, verbose=0)
    graph = planner.sol_tree

    planar_plot(graph, root_node=0)

    print('Plan: ')
    for action in plan:
        print('\t', action)

    fail_node = ('a_drop_garlic_closed_coffin', 'gm2', 'c1', 'l3')
    new_task_list = post_failure_tasks(graph, fail_node)
    print("If failure occurs at: ", fail_node)
    print("New task list will be: ", new_task_list)


# ******************************************        Main Program End        ****************************************** #
# ******************************************    Demo / Test Routine         ****************************************** #
if __name__ == '__main__':
    try:
        main()
        print('\nFile executed successfully!\n')
    except KeyboardInterrupt:
        print('\nProcess interrupted by user. Bye!')

"""
Author(s): Yash Bansod
Repository: https://github.com/YashBansod/IPyHOP
Organization: University of Maryland at College Park
"""
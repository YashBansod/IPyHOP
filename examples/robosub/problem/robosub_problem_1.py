#!/usr/bin/env python
"""
File Description: Robosub problem file. Initial state and task list for the planning problem is defined here.
"""

from ipyhop import State

init_state = State('init_state')
init_state.loc = {'r': 'base', 't1': 'r', 't2': 'r',
                  'g': 'l1', 'gm1': 'l1', 'cm1': 'l1', 'gp1': 'l1',
                  'v1': 'l2', 'v2': 'l2', 'gp2': 'l2',
                  'gm2': 'l3', 'c1': 'l3', 'ap1': 'l4', 'd1': 'l4',
                  'cm2': 'l5', 'ap2': 'l5', 's1': 'l5'}

init_state.found = {'g': False, 'gm1': False, 'cm1': False, 'gp1': False,
                    'v1': False, 'v2': False, 'gp2': False,
                    'gm2': False, 'c1': False, 'ap1': False, 'd1': False,
                    'cm2': False, 'ap2': False, 's1': False,
                    'base': True, 'l1': False, 'l2': False, 'l3': False, 'l4': False, 'l5': False}

init_state.crossed_gate = {'g': False}
init_state.traversed_path = {'gp1': False, 'gp2': False}
init_state.vampire_touched = {'v1': False, 'v2': False}
init_state.coffin_filled = {'c1': False}
init_state.opened = {'c1': False}
init_state.staked_dracula = {'d1': False}
init_state.decapitated = {'d1': False}
init_state.surfaced = {'r': False}

task_list = [('base_task', ), ('loc1_task', ), ('loc2_task', ), ('loc3_task', ), ('loc4_task', ), ('loc5_task', )]

"""
Author(s): Yash Bansod
Repository: https://github.com/YashBansod/GraphHOP
Organization: University of Maryland at College Park
"""

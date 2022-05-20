#!/usr/bin/env python
"""
File Description: Robosub methods file. All the methods for Robosub planning domain are defined here.
"""

from ipyhop import Methods

methods = Methods()


def tm1_move(state, l, l_):
    if state.loc['r'] == l:
        return [('a_search_for', l_), ('a_move', l, l_)]


methods.declare_task_methods('move_task', [tm1_move])


def tm1_base(state):
    if state.loc['r'] == 'base':
        return [('move_task', 'base', 'l1')]


methods.declare_task_methods('base_task', [tm1_base])


def tm1_loc1(state):
    if state.loc['r'] == 'l1':
        return [('cross_gate_task', 'g', 'l1'),
                ('pick_task', 'gm1', 'l1'),
                ('pick_task', 'cm1', 'l1'),
                ('trace_path_task', 'gp1', 'l1'),
                ('move_task', 'l1', 'l2')]


methods.declare_task_methods('loc1_task', [tm1_loc1])


def tm1_cross_gate(state, g, l):
    if state.loc['r'] == l and state.loc[g] == l:
        return [('a_localize', g, l), ('a_cross_gate_40', g, l)]


def tm2_cross_gate(state, g, l):
    if state.loc['r'] == l and state.loc[g] == l:
        return [('a_localize', g, l), ('a_cross_gate_60', g, l)]


methods.declare_task_methods('cross_gate_task', [tm1_cross_gate, tm2_cross_gate])


def tm1_pick(state, b, l):
    if state.loc['r'] == l and state.loc[b] == l:
        return [('a_localize', b, l), ('a_pick', b, l)]


def tm2_pick(state, b, l):
    if state.loc['r'] == l:
        return []


methods.declare_task_methods('pick_task', [tm1_pick, tm2_pick])


def tm1_trace_path(state, gp, l):
    if state.loc['r'] == l and state.loc[gp] == l:
        return [('a_localize', gp, l), ('a_trace_guide_path', gp, l)]


def tm2_trace_path(state, gp, l):
    if state.loc['r'] == l:
        return []


methods.declare_task_methods('trace_path_task', [tm1_trace_path, tm2_trace_path])


def tm1_loc2(state):
    if state.loc['r'] == 'l2':
        return [('slay_vampire_task', 'v1', 'l2'),
                ('slay_vampire_task', 'v2', 'l2'),
                ('trace_path_task', 'gp2', 'l2'),
                ('move_task', 'l2', 'l3')]


methods.declare_task_methods('loc2_task', [tm1_loc2])


def tm1_slay_vampire(state, v, l):
    if state.loc['r'] == l and state.loc[v] == l:
        return [('a_localize', v, l), ('a_touch_back_v', v, l)]


def tm2_slay_vampire(state, v, l):
    if state.loc['r'] == l and state.loc[v] == l:
        return [('a_localize', v, l), ('a_touch_front_v', v, l)]


def tm3_slay_vampire(state, v, l):
    if state.loc['r'] == l:
        return []


methods.declare_task_methods('slay_vampire_task', [tm1_slay_vampire, tm2_slay_vampire, tm3_slay_vampire])


def tm1_loc3(state):
    if state.loc['r'] == 'l3':
        return [('drop_garlic_task', 'gm1', 'c1', 'l3'),
                ('pick_task', 'gm2', 'l3'),
                ('drop_garlic_task', 'gm2', 'c1', 'l3'),
                ('localize_ap_task', 'ap1'),
                ('move_task', 'l3', 'l4')]


methods.declare_task_methods('loc3_task', [tm1_loc3])


def tm1_drop_garlic(state, gm, c, l):
    if state.loc['r'] == l and state.loc[c] == l:
        return [('a_localize', c, l), ('a_open_c', c, l), ('a_drop_garlic_closed_coffin', gm, c, l)]


def tm2_drop_garlic(state, gm, c, l):
    if state.loc['r'] == l and state.loc[c] == l:
        return [('a_localize', c, l), ('a_drop_garlic_open_coffin', gm, c, l)]


def tm3_drop_garlic(state, gm, c, l):
    if state.loc['r'] == l:
        return []


methods.declare_task_methods('drop_garlic_task', [tm1_drop_garlic, tm2_drop_garlic, tm3_drop_garlic])


def tm1_localize_ap(state, ap):
    return [('a_localize_ap', ap)]


def tm2_localize_ap(state, ap):
    return []


methods.declare_task_methods('localize_ap_task', [tm1_localize_ap, tm2_localize_ap])


def tm1_loc4(state):
    if state.loc['r'] == 'l4':
        return [('stake_through_heart_task', 'd1', 'l4'),
                ('localize_ap_task', 'ap2'),
                ('move_task', 'l4', 'l5')]


methods.declare_task_methods('loc4_task', [tm1_loc4])


def tm1_stake_through_heart(state, d, l):
    if state.loc['r'] == l and state.loc[d] == l:
        return [('a_localize', d, l), ('a_decapitate_d', d, l),
                ('a_stake_decapitated_dracula', 't1', d, l), ('a_stake_decapitated_dracula', 't2', d, l)]


def tm2_stake_through_heart(state, d, l):
    if state.loc['r'] == l and state.loc[d] == l:
        return [('a_localize', d, l), ('a_stake_dracula', 't1', d, l), ('a_stake_dracula', 't2', d, l)]


def tm3_stake_through_heart(state, d, l):
    if state.loc['r'] == l:
        return []


methods.declare_task_methods('stake_through_heart_task', [tm1_stake_through_heart,
                                                          tm2_stake_through_heart, tm3_stake_through_heart])


def tm1_loc5(state):
    if state.loc['r'] == 'l5':
        return [('a_localize', 's1', 'l5'), ('a_surface', 'cm1', 's1', 'l5')]


def tm2_loc5(state):
    if state.loc['r'] == 'l5':
        return [('pick_task', 'cm2', 'l5'), ('o_localize', 's1', 'l5'), ('o_surface', 'cm2', 's1', 'l5')]


methods.declare_task_methods('loc5_task', [tm1_loc5, tm2_loc5])

# ******************************************    Demo / Test Routine         ****************************************** #
if __name__ == '__main__':
    raise NotImplementedError("Test run / Demo routine for Robosub Methods isn't implemented.")

"""
Author(s): Yash Bansod
Repository: https://github.com/YashBansod/IPyHOP
Organization: University of Maryland at College Park
"""
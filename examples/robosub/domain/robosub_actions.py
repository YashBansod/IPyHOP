#!/usr/bin/env python
"""
File Description: Robosub actions file. All the actions for Robosub planning domain are defined here.
"""

from ipyhop import Actions


def a_search_for(state, l):
    state.found[l] = True
    return state


def a_localize(state, b, l):
    if state.loc['r'] == l and state.loc[b] == l:
        state.found[b] = True
        return state


def a_localize_ap(state, ap):
    state.found[ap] = True
    return state


def a_move(state, l, l_):
    if state.loc['r'] == l and state.found[l_] == True:
        state.loc['r'] = l_
        return state


def a_cross_gate_40(state, g, l):
    if state.loc['r'] == l and state.loc[g] == l and state.found[g] == True:
        state.crossed_gate[g] = 'T40'
        return state


def a_cross_gate_60(state, g, l):
    if state.loc['r'] == l and state.loc[g] == l and state.found[g] == True:
        state.crossed_gate[g] = 'T60'
        return state


def a_pick(state, b, l):
    if state.loc['r'] == l and state.loc[b] == l and state.found[b] == True:
        state.loc[b] = 'r'
        return state


def a_touch_front_v(state, v, l):
    if state.loc['r'] == l and state.loc[v] == l and state.found[v] == True:
        state.vampire_touched[v] = 'Tf'
        return state


def a_touch_back_v(state, v, l):
    if state.loc['r'] == l and state.loc[v] == l and state.found[v] == True:
        state.vampire_touched[v] = 'Tb'
        return state


def a_trace_guide_path(state, gp, l):
    if state.loc['r'] == l and state.loc[gp] == l and state.found[gp] == True:
        state.traversed_path[gp] = True
        return state


def a_open_c(state, c, l):
    if state.loc['r'] == l and state.loc[c] == l and state.found[c] == True:
        state.opened[c] = True
        return state


def a_drop_garlic_open_coffin(state, gm, c, l):
    if state.loc['r'] == l and state.loc[gm] == 'r' and state.loc[c] == l and state.found[c] == True:
        state.loc[gm] = c
        state.coffin_filled[c] = True
        return state


def a_drop_garlic_closed_coffin(state, gm, c, l):
    if state.loc['r'] == l and state.loc[gm] == 'r' and state.loc[c] == l and state.opened[c] == True:
        state.loc[gm] = c
        state.coffin_filled[c] = True
        return state


def a_decapitate_d(state, d, l):
    if state.loc['r'] == l and state.loc[d] == l and state.found[d] == True:
        state.decapitated[d] = True
        return state


def a_stake_dracula(state, t, d, l):
    if state.loc['r'] == l and state.loc[t] == 'r' and state.loc[d] == l and state.found[d] == True:
        state.loc[t] = d
        state.staked_dracula[d] = True
        return state


def a_stake_decapitated_dracula(state, t, d, l):
    if state.loc['r'] == l and state.loc[t] == 'r' and state.loc[d] == l and state.decapitated[d] == True:
        state.loc[t] = d
        state.staked_dracula[d] = True
        return state


def a_surface(state, cm, s, l):
    if state.loc['r'] == l and state.loc[cm] == 'r' and state.loc[s] == l and state.found[s] == True:
        state.surfaced['r'] = True
        return state


actions = Actions()
actions.declare_actions([a_search_for, a_localize, a_localize_ap, a_move, a_cross_gate_40, a_cross_gate_60, a_pick,
                             a_touch_front_v, a_touch_back_v, a_trace_guide_path, a_open_c, a_drop_garlic_open_coffin,
                             a_drop_garlic_closed_coffin, a_decapitate_d, a_stake_dracula, a_stake_decapitated_dracula,
                             a_surface])

# ******************************************    Demo / Test Routine         ****************************************** #
if __name__ == '__main__':
    raise NotImplementedError("Test run / Demo routine for Robosub Actions isn't implemented.")

"""
Author(s): Yash Bansod
Repository: https://github.com/YashBansod/IPyHOP
Organization: University of Maryland at College Park
"""
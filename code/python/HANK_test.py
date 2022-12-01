# -*- coding: utf-8 -*-
"""
Testing the HARK model
@author: Adrian
"""

from ConsIndShockModel import IndShockConsumerType #HARK.ConsumptionSaving.
import matplotlib.pyplot as plt
import numpy as np
import time

#Steady State values

def fiscal_ss(B, r, G): 
    T = (1 + r) * B + G - B
    
    return T


r_ss = 1.03 - 1
G_ss = .2
B_ss = .5 # this is lower than the tutorial by Straub et al. because need Higher MPC
Y_ss = 1.0


T_ss = fiscal_ss(B_ss,r_ss,G_ss)

print('T_ss: ' +str(T_ss))

Z_ss = Y_ss - T_ss

C_ss= Y_ss - G_ss
print('Z_ss: ' +str(Z_ss))

print('C_ss: ' +str(Y_ss - G_ss))

#%%
Dict={
    # Parameters shared with the perfect foresight model
    "CRRA": 2.0,                           # Coefficient of relative risk aversion
    "Rfree": 1.03,                         # Interest factor on assets
    "DiscFac": 0.96,                       # Intertemporal discount factor
    "LivPrb" : [0.98],                     # Survival probability
    "PermGroFac" :[1.01],                  # Permanent income growth factor
    
    # Parameters that specify the income distribution over the lifecycle
    "PermShkStd" : [0.1],                  # Standard deviation of log permanent shocks to income
    "PermShkCount" : 7,                    # Number of points in discrete approximation to permanent income shocks
    "TranShkStd" : [0.2],                  # Standard deviation of log transitory shocks to income
    "TranShkCount" : 7,                    # Number of points in discrete approximation to transitory income shocks
    "UnempPrb" : 0.05,                     # Probability of unemployment while working
    "IncUnemp" : 0.3,                      # Unemployment benefits replacement rate
    "UnempPrbRet" : 0.0005,                # Probability of "unemployment" while retired
    "IncUnempRet" : 0.0,                   # "Unemployment" benefits when retired
    "T_retire" : 0,                        # Period of retirement (0 --> no retirement)
    "tax_rate" : 0.0,                      # Flat income tax rate (legacy parameter, will be removed in future)
    
    # Parameters for constructing the "assets above minimum" grid
    "aXtraMin" : 0.001,                    # Minimum end-of-period "assets above minimum" value
    "aXtraMax" : 1000,                       # Maximum end-of-period "assets above minimum" value
    "aXtraCount" : 200,                     # Number of points in the base grid of "assets above minimum"
    "aXtraNestFac" : 3,                    # Exponential nesting factor when constructing "assets above minimum" grid
    "aXtraExtra" : [None],                 # Additional values to add to aXtraGrid
    
    # A few other paramaters
    "BoroCnstArt" : 0.0,                   # Artificial borrowing constraint; imposed minimum level of end-of period assets
    "vFuncBool" : True,                    # Whether to calculate the value function during solution   
    "CubicBool" : False,                   # Preference shocks currently only compatible with linear cFunc
    "T_cycle" : 1,                         # Number of periods in the cycle for this agent type        
    
    # Parameters only used in simulation
    "AgentCount" : 10000,                  # Number of agents of this type
    "T_sim" : 120,                         # Number of periods to simulate
    "aNrmInitMean" : -6.0,                 # Mean of log initial assets
    "aNrmInitStd"  : 1.0,                  # Standard deviation of log initial assets
    "pLvlInitMean" : 0.0,                  # Mean of log initial permanent income
    "pLvlInitStd"  : 0.0,                  # Standard deviation of log initial permanent income
    "PermGroFacAgg" : 1.0,                 # Aggregate permanent income growth factor
    "T_age" : None,                        # Age after which simulated agents are automatically killed
    
    # HANK parameters
    "taxrate" : [0.0], # set to 0.0 because we are going to assume that labor here is actually after tax income
    "labor": [Y_ss - T_ss],
    "wage": [1.0],
}
#%%
# from https://github.com/wdu9/RA_test_work/blob/main/RA_test_work/HANK_model/Reproducing%20Fiscal%20Policy%20HANK.ipynb
# to add taxes, labor and wage

# Update def construct_lognormal_income_process_unemployment(self):
# similar to https://github.com/wdu9/RA_test_work/blob/main/RA_test_work/HANK_model/ConsIndShockModel_HANK.py

def function(taxrate,labor,wage):
    
    z = (1- taxrate)*labor*wage
    
    return z

# def IncShkDstn_tax_labor_wage(
#     IncShkDstn, taxrate, labor, wage, T_retire, unemployed_indices=None, transitory_index=2
# ):
#     """
#     Applies a flat income tax rate to all employed income states during the working
#     period of life (those before T_retire).  Time runs forward in this function.
#
#     Parameters
#     ----------
#     IncShkDstn : [distribution.Distribution]
#         The discrete approximation to the income distribution in each time period.
#     tax_rate : float
#         A flat income tax rate to be applied to all employed income.
#     T_retire : int
#         The time index after which the agent retires.
#     unemployed_indices : [int]
#         Indices of transitory shocks that represent unemployment states (no tax).
#     transitory_index : int
#         The index of each element of IncShkDstn representing transitory shocks.
#
#     Returns
#     -------
#     IncShkDstn_new : [distribution.Distribution]
#         The updated income distributions, after applying the tax.
#     """
#     unemployed_indices = (
#         unemployed_indices if unemployed_indices is not None else list()
#     )
#     IncShkDstn_new = deepcopy(IncShkDstn)
#     i = transitory_index
#     for t in range(len(IncShkDstn)):
#         if t < T_retire:
#             for j in range((IncShkDstn[t][i]).size):
#                 if j not in unemployed_indices:
#                     IncShkDstn_new[t][i][j] = IncShkDstn[t][i][j] * (1 - taxrate) *labor * wage
#     return IncShkDstn_new

Dict['TranShkMean_Func'] = function
#%%
Agent = IndShockConsumerType(**Dict)

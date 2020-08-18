# ---
# jupyter:
#   jupytext:
#     formats: py,ipynb
#     notebook_metadata_filter: all
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.7.6
# ---

# ## A Sample Notebook in a Sample REMARK
#
# An example notebook which has some basic content which a REMARK may include.
#
# The REMARK notebook shouldn't just contain the code, use the markdown cells to explain the code and models.

# required imports
from HARK.ConsumptionSaving.ConsPrefShockModel import PrefShockConsumerType
import numpy as np
import matplotlib.pyplot as plt
from custom_code import plot_distribution

# Make and solve a preference shock consumer
PrefShockExample = PrefShockConsumerType()
PrefShockExample.cycles = 0  # Infinite horizon
PrefShockExample.solve()

# Unpack the consumption function for easier access.
PrefShockExample.unpack('cFunc')
PrefShockExample.unpack('mNrmMin')

# Plot the consumption function at each discrete shock
m = np.linspace(PrefShockExample.mNrmMin[0], 5, 200)
for j in range(PrefShockExample.PrefShkDstn[0].pmf.size):
    PrefShk = PrefShockExample.PrefShkDstn[0].X[j]
    c = PrefShockExample.cFunc[0](m, PrefShk * np.ones_like(m))
    plt.plot(m, c)
plt.xlim([0.0, None])
plt.ylim([0.0, None])
plt.savefig('../figures/cFunc.png')
plt.show()

# Import custom code and plot the figure.
# Save this figure in the figures directory.
path = '../figures/dist.png'
plot_distribution(100, 15, path)

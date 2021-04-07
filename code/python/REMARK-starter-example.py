# ---
# jupyter:
#   jupytext:
#     formats: py,ipynb
#     notebook_metadata_filter: all
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.2
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
#     version: 3.8.8
#   latex_envs:
#     LaTeX_envs_menu_present: true
#     autoclose: false
#     autocomplete: true
#     bibliofile: biblio.bib
#     cite_by: apalike
#     current_citInitial: 1
#     eqLabelWithNumbers: true
#     eqNumInitial: 1
#     hotkeys:
#       equation: Ctrl-E
#       itemize: Ctrl-I
#     labels_anchors: false
#     latex_user_defs: false
#     report_style_numbering: false
#     user_envs_cfg: false
# ---

# +

# ## A Sample Notebook in a Sample REMARK
# 
# An example notebook which has some basic content which a REMARK may include.
# 
# The REMARK notebook shouldn't just contain the code, use the markdown cells to explain the code and models.
# -

# required imports
from HARK.ConsumptionSaving.ConsPrefShockModel import KinkyPrefConsumerType
import numpy as np
import matplotlib.pyplot as plt


# Make and solve a preference shock consumer
PrefShockExample = KinkyPrefConsumerType()
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
plt.xlim([-1.0, None])
plt.ylim([0.0, None])
plt.savefig('../../figures/cFunc.pdf')
plt.ion() # Necessary so that when executed from the command line it does not wait for user input
plt.show()


# +
# Import custom code and plot the figure.

from custom_code import plot_distribution
# Save this figure in the figures directory.
path = '../../figures/dist.pdf'
plot_distribution(100, 15, path)


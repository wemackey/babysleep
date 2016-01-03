# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 20:14:21 2016

@author: wayne
"""

import plotly.plotly as py
import plotly.graph_objs as go

# get sleep data
df = data_kID.durationMin
sleepDur = df[(data_kID['activity'] == "Sleep")]
x = sleepDur[sleepDur>180]

data_plot = [
    go.Scatter(
        x=x.index,
        y=x
    )
]

plot_url = py.plot(data_plot, filename='python-datetime')
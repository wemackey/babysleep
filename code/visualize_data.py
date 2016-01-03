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

# get timestamps
dt = data_kID.startTime
sleepStart = dt[(data_kID['activity'] == "Sleep")]
y = sleepStart[sleepDur>180]

data_plot = [
    go.Scatter(
        x=x,
        y=y
    )
]

plot_url = py.plot(data_plot, filename='python-datetime')
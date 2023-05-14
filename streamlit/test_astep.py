# -*- coding: utf-8 -*-
"""
Created May 2023

@author: Ishtiak Ahmed
"""

####################
### IMPORTS PACKAGES
####################

import os
import sys
import streamlit as st
import json
import pandas as pd
import csv
import numpy as np
from numpy import genfromtxt

### Set Page Config
st.set_page_config(page_title=None, page_icon=None, 
                   layout="wide", 
                   initial_sidebar_state="auto", menu_items=None)

### Define Tab Names and Numbers
tab1, tab2,tab3, tab4 = st.tabs(["Inputs 1-3", "Inputs 4-7","Run Economic Assessment","Results"])

test_df = pd.read_csv("../coal_petrolium_red.csv", header=0,index_col = 0)
with tab1:
    st.write(os.getcwd())
    st.write(test_df)
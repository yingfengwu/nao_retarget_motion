"""
@author: yingfengwu
time: 2021/06/26

This file is to transform the angle of joint to the radian of joint
"""
import pandas as pd
import numpy as np

input_path = "../data/0005_2FeetJump001_worldpos.csv"
output_path = "../data/nao_jump_pos1.csv"

data = pd.read_csv(input_path)

for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        if j != 0:
            data.values[i][j] = data.values[i][j] * np.pi / 180

data.to_csv(output_path)

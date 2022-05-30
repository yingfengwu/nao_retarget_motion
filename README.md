# nao_retarget_motion
This is a code of retargeting motion on NAO robot and this code is based on this paper:

Peng, Xue & Coumans, Erwin & Zhang, Tingnan & Lee, Tsang-Wei & Tan, Jie & Levine, Sergey. (2020). Learning Agile Robotic Locomotion Skills by Imitating Animals.https://arxiv.org/pdf/2004.00784.pdf

First step:
Download the bvh file from https://mocap.cs.sfu.ca/, and run the __main__.py in retarget_motion/bvh_converter/ to convert the bvh data into 3D data 

Second step:
run the angle2radian.py in retarget_motion/util/ to convert angle into radian and delete some unused columns.

Third step:
run the run_nao_retarget.py in retarget_motion/ to acquire motion of the target joint angle.

Forth step:
run the run.py in motion_imitation/ to train or test.


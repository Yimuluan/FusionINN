import torch
import torch.nn as nn
import numpy as np
from pytorch_msssim import ssim, ms_ssim, SSIM, MS_SSIM
from scipy.io import savemat
import torchvision.io

#####################Plot the images##########################################################
total_val_images = 1153

val_data_tensor = torch.load('/home/h1/s8993054/INN_Fusion/INN/val_data_tensor.pt')
val_data_tensor = val_data_tensor.cpu().squeeze()
count = 0


fused_val_tensor = torch.load('/home/h1/s8993054/INN_Fusion/Half_UNET/val_fused_tensor.pt')
fused_val_tensor = fused_val_tensor.cpu().squeeze()

##############################################################################################
# DDFM 
##############################################################################################
ssim_average=torch.zeros(total_val_images)
for i in range(total_val_images):
    ssim_t1ce  = ssim(fused_val_tensor[i:i+1, None,:,:], val_data_tensor[i:i+1, 2:3, :, :], data_range=1)
    ssim_flair = ssim(fused_val_tensor[i:i+1, None, :,:].cuda(), val_data_tensor[i:i+1, 3:,  :, :].cuda(), data_range=1).cuda()
    ssim_average[i]=(ssim_t1ce + ssim_flair)/2


torch.save(ssim_average, '/home/h1/s8993054/INN_Fusion/MaskNet/ssim_scores.pt')
mdic = {"ssim": ssim_average}
savemat("/home/h1/s8993054/INN_Fusion/MaskNet/ssim.mat", mdic)
count += 1
print(torch.mean(ssim_average))
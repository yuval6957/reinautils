# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_TorchUtils.ipynb.

# %% auto 0
__all__ = ['device_by_name']

# %% ../nbs/01_TorchUtils.ipynb 3
from torch.utils.data import Dataset
import torch

# %% ../nbs/01_TorchUtils.ipynb 4
def device_by_name(name: str) -> torch.device:
    ''' Return reference to cuda device by using Part of it's name

        Args:
            name: part of the cuda device name (shuuld be distinct)

        Return:
            Reference to cuda device

        Updated: Yuval 12/10/19
    '''
    assert torch.cuda.is_available(), "No cuda device"
    device = None
    for i in range(torch.cuda.device_count()):
        dv = torch.device("cuda:{}".format(i))
        if name in torch.cuda.get_device_name(dv):
            device = dv
            break
    assert device, "device {} not found".format(name)
    return device
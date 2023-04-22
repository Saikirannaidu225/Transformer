import torch 
from torch import nn


class LayerNorm(nn.Module):
    def __init__(self,d_model,eps=1e-12):
        super(LayerNorm).__init__()
        self.gamma = nn.Parameter(torch.ones(d_model))
        self.beta = nn.Parameter(torch.zeroes(d_model))
        self.eps = eps
    def forward(self,x):
        mean = x.mean(-1,keepdim= True)
        var = x.var(-1,unbaised = False ,keepdim= True)
        out = (x-mean)/torch.sqrt(var+self.eps)
        out = self.gmma*out + self.beta
        return out    
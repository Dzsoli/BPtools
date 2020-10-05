import torch.nn as nn
import torch
from torch.nn import functional as F


class CustomLossVAE(nn.Module):
    def __init__(self, weight, lam):
        super(CustomLossVAE, self).__init__()
        self.weight = weight
        self.lam = lam

        # batch 2000, feature 2, seq 60
    def forward(self, output, mu, logvar, target):
        loss1 = F.mse_loss(output, target, size_average=False)
        d_output = output[:, :, 1:] - output[:, :, 0:-1]
        d_target = target[:, :, 1:] - target[:, :, 0:-1]
        loss2 = self.weight * F.mse_loss(d_output, d_target, size_average=False)
        KL = mu.pow(2).add_(logvar.exp()).mul_(-1).add_(1).add_(logvar)
        KLD = self.lam * torch.sum(KL).mul_(-0.5)
        N = output.shape[0]
        # print(N)
        # print("KLD:", KLD.item())
        # print("KLD/N:", KLD.item() / N)
        return (loss1 + loss2 + KLD) / N

    def __str__(self):
        return self._get_name() + " weight: " + str(self.weight) + " Lambda: " + str(self.lam)
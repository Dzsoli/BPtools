from BPtools.trainer.bptrainer import BPTrainer
from BPtools.utils.models import VariationalAutoEncoder, VarDecoderConv1d_3, VarEncoderConv1d, VAEDataModul
from BPtools.core.bpmodule import BPModule
from BPtools.metrics. criterions import CustomLossVAE
import inspect

encoder = VarEncoderConv1d(2, 60, 10)
decoder = VarDecoderConv1d_3(2, 60, 10)
my_model = VariationalAutoEncoder(encoder, decoder)
my_dm = VAEDataModul(path="data/X_Yfull_dataset.npy", split_ratio=0.1)
# print(inspect.getsource(CustomLossVAE(1,1).forward))
Trainer = BPTrainer(epochs=20000, criterion=CustomLossVAE(0.1, 1.0))
print(isinstance(my_model, BPModule))
Trainer.fit(model=my_model, datamodule=my_dm)
# print(my_model.parameters())
# print(my_model.state_dict())

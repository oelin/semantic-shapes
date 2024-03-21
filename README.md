# semantic-shapes

Semantic shapes for various modalities.

## Installation 

```sh
pip install git+https://github.com/oelin/semantic-shapes
```

## Usage

```python
import semantic_shapes as ss
import torch.nn as nn


class CNN(nn.Module):
  def __init__(
    self,
    input_shape: ss.ImageShape,
    factor_: ss.LayerShape,
  ) -> None:
    super().__init__()

    self.model = nn.Sequential(
      nn.Conv2d(
        in_channels=input_shape.channels,
        out_channels=layer_shape.layers[0],
      ),
      nn.ReLU(),
      nn.Conv2d(
      )
      nn.Conv2d(in_channels=32, out_channels=64, 3, 2, 1),
      nn.ReLU(),
      nn.Conv2d(in_channels=64, out_channels=256, 3, 2, 1),
    )
```

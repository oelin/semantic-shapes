# semantic-shapes

Semantic shapes for deep neural networks.

Installation 
------------

```sh
pip install git+https://github.com/oelin/semantic-shapes
```

Usage
-----

```python
import semantic_shapes as ss

image_shape = ss.ImageShape(channels=3, height=256, width=256)

volume_shape = ss.ImageShape(channels=3, depth=256, height=256, width=256)

video_shape = ss.VideoShape(duration=1024, channels=3, height=256, width=256)

audio_shape = ss.AudioShape(duration=1024, channels=32)

text_shape = ss.TextShape(length=1024)

sequence_shape = ss.SequenceShape(channels=256, length=1024)
```

# semantic-shapes

Semantic shapes for deep neural networks.

Installation 
------------

```sh
pip install git+https://github.com/oelin/semantic-shapes
```

Usage
-----

Use default shapes.

```python
import semantic_shapes as ss

image_shape = ss.ImageShape(channels=3, width=256, height=256)

video_shape = ss.VideoShape(duration=1024, channels=3, width=256, height=256)

audio_shape = ss.AudioShape(duration=1024, channels=32)

text_shape = ss.TextShape(length=1024)

sequence_shape = ss.SequenceShape(length=1024, channels=256)
```

Define custom shapes using `ss.partial` and `ss.compose`.

```python
RGBImageShape = ss.partial(ss.ImageShape, channels=3)

LargeImageShape = ss.partial(ss.ImageShape, width=1024, height=1024)

VolumeVideoShape = ss.compose(ss.Volume, ss.VideoShape)

volume_video_shape = VolumeVideoShape(duration=1024, channels=3, width=256, height=256, depth=256)
```

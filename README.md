# Changelog
V1 - Initial model. Included a few violin scores, 3 layers, 128 nodes.

V2 - removed violin scores. 3 layers, 128 nodes

V3 - 6 layers, 128 nodes, locally trained.

V4 - Discovered V3 had terrible accuracy. Reduced to 3 layers, 256 nodes.
> Learning as I'm going, I have no idea what I'm doing lol...

V5 - V4 was still pretty rubbish, but did much better. 3 layers, 512 nodes. Tried to add more training data.
> I actually have no idea what I'm doing.

V6 - V5 was much improved from V4. Realised that a thing called "overfitting" was happening. Reduced to 2 layers, 512 nodes.
- Post-training notes. Overfitting at 3000. 2500 may be more optimal.

V7 - Using a different neural network that doesn't care about dynamics.

# Other
Conda with Python 3.6 is highly recommended.
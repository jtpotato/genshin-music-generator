# Changelog
V1 - Initial model. Included a few violin scores, 3 layers, 128 nodes.

V2 - removed violin scores. 3 layers, 128 nodes

V3 - 6 layers, 128 nodes, locally trained.

V4 - Discovered V3 had terrible accuracy. Reduced to 4 layers, 128,256,256,128 nodes.

# Other
Conda with Python 3.6 is highly recommended.

# After properly installing CUDA 11.7
`export PATH=/usr/local/cuda-11.7/bin${PATH:+:${PATH}}`
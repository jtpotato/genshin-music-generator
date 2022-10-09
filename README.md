# Guide
WARNING: This is a hastily written guide that assumes a bunch of prerequesite information. Don't expect to be able to do anything without some experience in setting up Ubuntu/WSL, Tensorflow, Python and Bash.

In essence:
1. Install WSL 2.0
2. Use the Magenta preinstall script (https://github.com/magenta/magenta#automated-install-w-anaconda)
3. OPTIONAL - Set up CUDA, CuDNN and i have no idea what else... just make sure Tensorflow is *capable* of using the GPU - in some workloads this makes things slower - so by default `training.py` uses the CPU.
4. Run the python scripts. Any variables to tweak are in `variables.py`. Good luck! **You'll need it.**

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

V7 - Using a different neural network that doesn't care about dynamics. Reducing to 2 layers, 64 nodes, as this one works differently.

V8 - Trying to mitigate any plateaus, so we can reach approximately 90% accuracy.

V9 - Accelerating training speed to reach 95%. Decidedly, 95% is optimal.
# features_extraction

Repository for feature extraction from images and videos.

A basic list of features this repository extracts:

* Image features:
  - Dense SIFT (Scale-invariant feature transform) - Patented
  - SURF (Speeded-Up Robust Features) - Patented
  - HoG (Histogram of Oriented Gradients) - OK!
  - LBP (Local Binary Pattern)- OK!
  - GiST (Generalized Search Tree)
  - Color Histogram - OK!
  - Fc7layer from AlexNet or equivalent - (InceptionV3) OK!
  - ORB (Oriented FAST and Rotated BRIEF): An efficient alternative to SIFT or SURF - OK!
  - BRIEF (Binary Robust Independent Elementary Features)

* Audio features:
  - MFCC (Mel Frequency Cepstral Coefficients) - There is no audio.

* Video features:
  - C3D features - OK!
  - HMP (Histogram of Motion Patterns) - OK!

I used Python3.6 and OpenCV3.4.1_1 for this repository,
both you will need to install.
With those two installed, and working, you can use the *requirements.py* file for
installing python packages with pip.


Special thanks to:
* Bikramjot Singh Hanzra for http://hanzratech.in/2015/05/30/local-binary-patterns.html

Who dedicated themselves to publish technical knowledge and
change the world.

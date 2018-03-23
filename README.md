# features_extraction

Repository for feature extraction from images and videos.

A basic list of features this repository extracts and their references:

* Image features:
  - Dense SIFT (Scale-invariant feature transform) - Patented so NO!
  - SURF (Speeded-Up Robust Features) - Patented so NO!
  - HoG (Histogram of Oriented Gradients) - OK!
  - LBP (Local Binary Pattern) - OK!
    1. DC. He and L. Wang (1990), **Texture Unit, Texture Spectrum, And Texture Analysis**, Geoscience and Remote Sensing, IEEE Transactions on, vol. 28, pp. 509 - 512.
  - GiST (Generalized Search Tree)
  - Color Histogram - OK!
  - Fc7layer from InceptionV3(imagenet) - OK!
    1. SZEGEDY, Christian et al. **Rethinking the inception architecture for computer vision**. In: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2016. p. 2818-2826.
  - ORB (Oriented FAST and Rotated BRIEF): An efficient alternative to SIFT or SURF - OK!
    1. Ethan Rublee, Vincent Rabaud, Kurt Konolige, and Gary Bradski. **Orb: an efficient alternative to sift or surf**. In Computer Vision (ICCV), 2011 IEEE International Conference on, pages 2564–2571. IEEE, 2011.

* Audio features:
  - MFCC (Mel Frequency Cepstral Coefficients) - There is no audio.

* Video features:
  - C3D features - OK!
    1. D. Tran, L. Bourdev, R. Fergus, L. Torresani, and M. Paluri, **Learning Spatiotemporal Features with 3D Convolutional Networks**, ICCV 2015, PDF.
    2. Y. Jia, E. Shelhamer, J. Donahue, S. Karayev, J. Long, R. Girshick, S. Guadarrama, and T. Darrell, **Caffe: Convolutional Architecture for Fast Feature Embedding**, arXiv 2014.
    3. A. Karpathy, G. Toderici, S. Shetty, T. Leung, R. Sukthankar, and L. Fei-Fei, **Large-scale Video Classification with Convolutional Neural Networks**, CVPR 2014.
  - HMP (Histogram of Motion Patterns) - OK!
    1. ALMEIDA, Jurandy; LEITE, Neucimar J.; TORRES, Ricardo da S. Comparison of video sequences with histograms of motion patterns. In: **Image Processing (ICIP), 2011 18th IEEE International Conference on**. IEEE, 2011. p. 3673-3676.



I used Python3.6 and OpenCV3.4.1_1 for this repository.
With those two installed, and working, you can use the *requirements.py* file for
installing python packages with pip.

Some other references:
  OpenCV: BRADSKI, Gary; KAEHLER, Adrian. OpenCV. **Dr. Dobb’s journal of software tools**, v. 3, 2000.
  scikit-image: VAN DER WALT, Stefan et al. **scikit-image: image processing in Python**. PeerJ, v. 2, p. e453, 2014.


Special thanks to all involved in the publications cited here, they are helping change the world.

Who dedicated themselves to publish technical knowledge and
change the world.

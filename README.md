# features_extraction

Repository for feature extraction from images and videos.

A basic list of features this repository extracts and their references:

# Main references

* Image features:
  - HoG (Histogram of Oriented Gradients) - OK!
    1. Dalal, N. and B. Triggs. **Histograms of Oriented Gradients for Human Detection**, IEEE Computer Society Conference on Computer Vision and Pattern Recognition, Vol. 1 (June 2005), pp. 886–893.
  - LBP (Local Binary Pattern) - OK!
    1. DC. He and L. Wang (1990), **Texture Unit, Texture Spectrum, And Texture Analysis**, Geoscience and Remote Sensing, IEEE Transactions on, vol. 28, pp. 509 - 512.
  - GiST (Generalized Search Tree)
  - Color Histogram - OK!
  - Fc7layer from InceptionV3(imagenet) - OK!
    1. SZEGEDY, Christian et al. **Rethinking the inception architecture for computer vision**. In: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2016. p. 2818-2826.
  - ORB (Oriented FAST and Rotated BRIEF): An efficient alternative to SIFT or SURF - OK!
    1. Ethan Rublee, Vincent Rabaud, Kurt Konolige, and Gary Bradski. **Orb: an efficient alternative to sift or surf**. In Computer Vision (ICCV), 2011 IEEE International Conference on, pages 2564–2571. IEEE, 2011.

* Audio features:
  - MFCC (Mel Frequency Cepstral Coefficients) - To be implemented in future iterations. No audio for now.

* Video features:
  - C3D features - OK!
    1. D. Tran, L. Bourdev, R. Fergus, L. Torresani, and M. Paluri, **Learning Spatiotemporal Features with 3D Convolutional Networks**, ICCV 2015, PDF.
    2. Y. Jia, E. Shelhamer, J. Donahue, S. Karayev, J. Long, R. Girshick, S. Guadarrama, and T. Darrell, **Caffe: Convolutional Architecture for Fast Feature Embedding**, arXiv 2014.
    3. A. Karpathy, G. Toderici, S. Shetty, T. Leung, R. Sukthankar, and L. Fei-Fei, **Large-scale Video Classification with Convolutional Neural Networks**, CVPR 2014.
  - HMP (Histogram of Motion Patterns) - OK!
    1. ALMEIDA, Jurandy; LEITE, Neucimar J.; TORRES, Ricardo da S. Comparison of video sequences with histograms of motion patterns. In: **Image Processing (ICIP), 2011 18th IEEE International Conference on**. IEEE, 2011. p. 3673-3676.


# Running the code

I used Python3.6 and OpenCV3.4.1_1 for this repository.
With those two installed, and working, you can use the *requirements.py* file for
installing python packages with pip.

# Data format generated

Here is some explaining on the file format to access the featurer, how are they organized and were extracted.

## Images

* ColorHistogram - 
    1. file format: text file.
    2. 3 list of numbers in 255 bins representing the colors Red, Green and Blue (in that order).
    3. It's the sum of ocurrences of each value (or bin) for each color channel.

* Hog - 
    1. file format: text file.
    2. a single list of numbers.
    3. Gradients calculated on 32x32 pixels per cell on a grey scale version of the image.

* InceptionV3Imagenet - 
    1. file format: text file
    2. a single list of numbers in 1000 bins (InceptionV3 imagenet number of classes), if the class is equal to 0 the bin is omitted.
    3. Represents the activation of InceptionV3 1000 classes, trained on imagenet (object detection).

* LBP - 

* ORB - 

## Videos

For video features there are two 'kind' of features, image features extracted on key-frames and video specialized features.

### Image features on video

These features were extracted on key-frames, three to be exact, the first, middle and last frames. And are:

### Video specialized features

* HMP - 

## Sound

No sound features were extracted as the videos does not contain sound.

# Some other references:

  OpenCV: BRADSKI, Gary; KAEHLER, Adrian. OpenCV. **Dr. Dobb’s journal of software tools**, v. 3, 2000.
  scikit-image: VAN DER WALT, Stefan et al. **scikit-image: image processing in Python**. PeerJ, v. 2, p. e453, 2014.
  librosa: MCFEE, Brian et al. **librosa: Audio and music signal analysis in python**. In: Proceedings of the 14th python in science conference. 2015. p. 18-25.

Special thanks to all involved in the publications cited here, they are helping change the world.


003381586587

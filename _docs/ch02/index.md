---
title: The Machine Learning Approach for Analysis of Sound Scenes and Events
authors: Toni Heittola, Emre Cakir, and Tuomas Virtanen
category: Chapter  2
order: 1
---


### 2.4.2 Feature Extraction

Toolboxes for acoustic feature extraction:

| Toolbox                                                                    | Language | Description                                                                                                                                                                      |
|----------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Essentia](http://essentia.upf.edu/documentation/)                         | C++ / Python | Mostly developed for MIR community, but provides many tools and feature extractors applicable for environmental audio research. |
| [librosa](https://github.com/librosa/librosa/)                             | Python   | Mostly developed for MIR community, but provides many tools and feature extractors applicable for environmental audio research. |
| [rastamat](http://www.ee.columbia.edu/ln/rosa/matlab/rastamat/)            | Matlab   | Versatile MFCC implementation           |
| [VOICEBOX](http://www.ee.ic.ac.uk/hp/staff/dmb/voicebox/voicebox.html)     | Matlab   | Widely used MFCC implementation         |


## 2.5 Supervised Learning and Recognition

Toolboxes and libraries for machine learning 

| Toolbox                                                                    | Language | Description                                                                                                                                                                      |
|----------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Keras](https://github.com/fchollet/keras)                                 | Python   | Neural Network front-end library for fast experimentation with deep neural networks. Can used Theano, TensorFlow and Microsoft Cognitive Toolkit as backend.             |
| [TensorFlow](https://www.tensorflow.org/)                                  | Python   | A symbolic math library, which is widely used for machine learning applications such as deep neural networks. |
| [Theano](https://github.com/Theano/Theano)                                 | Python   | Numerical computation library. Active development ceased on 15th November 2017. |
| [Microsoft Cognitive Toolkit](https://www.microsoft.com/en-us/cognitive-toolkit/) | C++ | Deep learning framework.    |
| [Torch](torch.ch)                                                          | Lua      | Library for deep machine learning. |
| [PyTorch](http://pytorch.org/)                                             | Python   | Library for deep machine learning. | 
| [Caffe](http://caffe.berkeleyvision.org/)                                  | C++ / Python / Matlab | Deep learning framework. Originally develop by UC Berkeley.  |
| [scikit-learn](http://scikit-learn.org/stable/)                            | Python   | Machine learning library. |

## 2.6 An Example Approach Based on Neural Networks

Example systems presented in the chapter are released in [separate code repository](https://github.com/TUT-ARG/CASSE_book_ch2_examples).

### 2.6.1 Sound Classification

**Single-label classification**

[single_label_classification.py](https://github.com/TUT-ARG/CASSE_book_ch2_examples/blob/master/single_label_classification.py)  

This is an example application to demonstrate single-label classification. Acoustic scene classification application is used as an example application, and [TUT Sound Scenes 2017, development dataset](https://zenodo.org/record/400515#.WhbTm3U_UeM) is used as test data. The dataset contains 10 second long audio excerpts from 15 different acoustic scene classes. 

**Multi-label classification**

[multi_label_classification.py](https://github.com/TUT-ARG/CASSE_book_ch2_examples/blob/master/multi_label_classification.py)  

This is an example application to demonstrate multi-label classification. Audio tagging is used as an example application, and [CHiME-Home, development & evaluation dataset](https://archive.org/details/chime-home) is used as test data. The dataset contains 4 second long audio excerpts with varying amount of tags assigned to them. Total of seven tag classes are used in the dataset. 

### 2.6.2 Sound Event Detection

[sound_event_detection.py](https://github.com/TUT-ARG/CASSE_book_ch2_examples/blob/master/sound_event_detection.py)  

This is an example application to demonstrate detection. Sound event detection is used as an example application, and [TUT Sound events 2017, development dataset](https://zenodo.org/record/814831) is used as test data.

## Other helpful toolboxes

| Toolbox                                                 | Language | Description                                                                                        |
|---------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------|
| [sed_eval](https://github.com/TUT-ARG/sed_eval)         | Python   | Evaluation toolbox for Sound Event Detection. [Documentation](http://tut-arg.github.io/sed_eval)   |
| [dcase_util](https://github.com/DCASE-REPO/dcase_util)  | Python   | A collection of utilities for Detection and Classification of Acoustic Scenes and Events. [Documentation](https://dcase-repo.github.io/dcase_util/)   |

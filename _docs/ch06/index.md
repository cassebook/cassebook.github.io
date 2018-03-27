---
title: Datasets and evaluation
authors: Annamaria Mesaros, Toni Heittola, and Dan Ellis
category: Chapter  6
order: 1
---

## 6.3 Obtaining Reference Annotations

Tools for annotating environmental audio:

|                                                  |  Description                                                                                                                                                         |
|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Software**                                     |                                                                                                                                                                      |
| [Audacity](http://www.audacityteam.org/)         | Audio software with basic annotation capabilities. Use label tracks for the annotations, see more info [here](http://manual.audacityteam.org/man/label_tracks.html). |
| [ELAN](https://tla.mpi.nl/tools/tla-tools/elan/) | A linguistic annotation tool to create the textual annotations for audio and video files                                                                             |
| **Prototypes**                                   |                                                                                                                                                                      |
| [I-SED](http://www.bongjunkim.com/ised/)         | An interactive sound event detector, see [Kim2017](http://music.cs.northwestern.edu/publications/Kim_Pardo_IUI2017.pdf)                                              |
| [Soundscape annotation tool](http://www.ai.rug.nl/~vdlinden/annotationtool/index.html) | A tool for soundscape annotation                                                                                               |
| [BAT](https://github.com/BlaiMelendezCatalan/BAT) | BMAT Annotation Tool, see [Melendez-Catalan2017](http://eecs.qmul.ac.uk/~keno/17.pdf)                                                        |
| [audio-annotator](https://github.com/CrowdCurio/audio-annotator) | Audio-annotator, see [Cartwright2017](http://faculty.poly.edu/~onov/Cartwright_et_al_SONYC_CSCW_2017.pdf)                     | 

## 6.4 Datasets for Environmental Sound Classification and Detection

### 6.4.2 Available Datasets

Freely available datasets for sound classification and tagging and sound event detection:

| Dataset name                                                                    | Type        | Classes | Examples | Size (min) | Usage, publications |
|---------------------------------------------------------------------------------|-------------|---------|----------|------------|---------------------|
| **Sound Scenes**                                                                                                                                      |
| [Dares G1](http://www.daresounds.org/research.html)                             | recorded    | 28      | 123      | 123        | [Grootel2009](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.584.4451&rep=rep1&type=pdf), [Mesaros2013](http://www.cs.tut.fi/~mesaros/pubs/mesaros_icassp2013_cr.pdf) |
| [DCASE 2013 Scenes](https://archive.org/details/dcase2013_scene_classification) | recorded    | 10      | 100      | 50         | [Stowell2015](http://ieeexplore.ieee.org/document/7100934/) |
| [LITIS Rouen](https://sites.google.com/site/alainrakotomamonjy/home/audio-scene)| recorded    | 19      | 3026     | 1513       | [Bisot2015](http://ieeexplore.ieee.org/document/7362477/), [Rakotomamonjy2015](http://ieeexplore.ieee.org/document/6971128/) |
| [TUT Sound Scenes 2016](https://zenodo.org/record/45739#.WXXLiidLdhE)           | recorded    | 15      | 1170     | 585        | [DCASE2016](http://www.cs.tut.fi/sgn/arg/dcase2016/task-acoustic-scene-classification), [Mesaros2016](http://www.cs.tut.fi/~mesaros/pubs/mesaros_eusipco2016-dcase.pdf) |
| **Environmental Sounds**                                                                                                                                      |
| [ESC-10](https://github.com/karoldvl/ESC-10)                                    | collected   | 10      | 400      | 33         | [Piczak2015a](http://karol.piczak.com/papers/Piczak2015-ESC-ConvNet.pdf), [Hertel2016](http://www.ieeeexplore.ws/document/7727635/)  |
| [ESC-50](https://github.com/karoldvl/ESC-50)                                    | collected   | 50      | 2000     | 166        | [Piczak2015a](http://karol.piczak.com/papers/Piczak2015-ESC-ConvNet.pdf), [Piczak2015b](http://karol.piczak.com/papers/Piczak2015-ESC-Dataset.pdf) |
| [NYU Urban Sound8K](http://urbansounddataset.weebly.com/urbansound8k.html) | collected   | 10      | 8732     | 525        | [Salamon2014](http://www.justinsalamon.com/uploads/4/3/9/4/4394963/salamon_urbansound_acmmm14.pdf) |
| [CHIME-Home](https://archive.org/details/chime-home)                            | recorded    | 7       | 6137     | 409        | [DCASE2016](http://www.cs.tut.fi/sgn/arg/dcase2016/task-audio-tagging), [Foster2015](http://ieeexplore.ieee.org/abstract/document/7336899/?reload=true) |
| [Freefield 1010](http://c4dm.eecs.qmul.ac.uk/rdr/handle/123456789/35)           | collected   | 7       | 400      | 33         | [Stowell2014a](http://www.aes.org/tmpFiles/elib/20170724/17095.pdf) |
| [CICESE Sound Events](http://sound.natix.org/databases/allSounds.zip)           | collected   | 20      | 1367     | 92         | [Beltran2015](http://www.sciencedirect.com/science/article/pii/S0167865515002925) |
| [AudioSet](https://research.google.com/audioset/)                               | collected   | 632     | >2 mil   | > 340k     | [Gemmeke2017](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45857.pdf) |
| **Sound Events**                                                                                                                                      |
| [Dares G1](http://www.daresounds.org/research.html)                             | recorded    | 761     | 3214     | 123        | [Grootel2009](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.584.4451&rep=rep1&type=pdf), [Mesaros2013](http://www.cs.tut.fi/~mesaros/pubs/mesaros_icassp2013_cr.pdf) |
| [DCASE 2013 Office Live](https://archive.org/details/dcase2013_event_detection_development) | recorded    | 16      | 320      | 19         | DCASE2013, [Stowell2015](http://ieeexplore.ieee.org/document/7100934/) |
| [DCASE 2013 Office Synthetic](https://archive.org/details/dcase2013_event_detection_development_OS) | recorded    | 16      | 320      | 19         | DCASE2013, [Stowell2015](http://ieeexplore.ieee.org/document/7100934/) |
| [TUT Sound Events 2016](https://zenodo.org/record/45759)                        | recorded    | 18      | 954      | 78         | [DCASE2016](http://www.cs.tut.fi/sgn/arg/dcase2016/task-sound-event-detection-in-real-life-audio), [Mesaros2016b]()|
| [TUT Sound Events 2017](https://zenodo.org/record/400516)                       | recorded    | 6       | 729      | 92         | [DCASE2017](http://www.cs.tut.fi/sgn/arg/dcase2017/challenge/task-sound-event-detection-in-real-life-audio) |
| [NYU Urban Sound](http://urbansounddataset.weebly.com/urbansound.html) | collected   | 10      | 3075     | 1620       | [Salamon2014](http://www.justinsalamon.com/uploads/4/3/9/4/4394963/salamon_urbansound_acmmm14.pdf), [Salamon2015a](http://www.justinsalamon.com/uploads/4/3/9/4/4394963/salamon_bello_scattering_eusipco_2015.pdf), [Salomon2015b](http://www.justinsalamon.com/uploads/4/3/9/4/4394963/salamon_unsupervisedlearning_urbansound_icassp_2015.pdf) |
| [TU Dortmund Multichannel](http://patrec.cs.tu-dortmund.de/files/datasets/dcase2016_multichannel-aed_dortmund.7z) | recorded    | 15      | 1170     | 585        | [Kuerby2016](https://www.cs.tut.fi/sgn/arg/dcase2016/documents/workshop/Kuerby-DCASE2016workshop.pdf) |

### 6.4.3 Data Augmentation

Data augmentation refers to methods for increasing the amount of development data available without additional recordings.

Here are a few tools for modifying existing audio material:

| Toolbox                                                                    | Language | Description                                                                                                                                                                      |
|----------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [muda](https://github.com/bmcfee/muda)                                     | Python   | Annotation-aware musical data augmentation, partly applicable for environmental audio (pitch shifting, time stretching). [Documentation](https://muda.readthedocs.io/en/latest/)                                                                                                                          |
| [librosa](https://github.com/librosa/librosa/)                             | Python   | See [time stretching](https://librosa.github.io/librosa/generated/librosa.effects.time_stretch.html) and [pitch shifting](https://librosa.github.io/librosa/generated/librosa.effects.pitch_shift.html) effects. |
| [TSM toolbox](https://www.audiolabs-erlangen.de/resources/MIR/TSMtoolbox/) | Matlab   | MATLAB implementations of various classical time-scale modification (TSM) algorithm.                                                                                             |

## 6.5 Evaluation

#### 6.5.2.2 Metrics

| Toolbox                                        | Language |  Description                                                                                                                                    |
| -----------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [sklearn.metrics](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics) | Python | Basic score functions, performance metrics and pairwise metrics and distance computations for machine learning development. |
| [sed_eval](https://github.com/TUT-ARG/sed_eval)| Python   | Evaluation toolbox for Sound Event Detection. [Documentation](http://tut-arg.github.io/sed_eval)                                               |


Usage examples for different tasks by using basic Python, and both sed_eval and sklearn toolboxes.


**Acoustic Scene Classification**                                                               

|                        | example code                                     | 
| -----------------------|--------------------------------------------------|
| *sklearn.metrics*      | [ac_evaluation_sklearn.py]({{ site.url }}/code/ch06/ac_evaluation_sklearn.py.html) ([download]({{ site.url }}/code/ch06/ac_evaluation_sklearn.py)) |
| *sed_eval*             | [ac_evaluation_sedeval.py]({{ site.url }}/code/ch06/ac_evaluation_sedeval.py.html) ([download]({{ site.url }}/code/ch06/ac_evaluation_sedeval.py)) |


**Sound Event Detection**

|                        | example code                                     | 
| -----------------------|--------------------------------------------------|
| *basic Python*         | [sed_evaluation.py]({{ site.url }}/code/ch06/sed_evaluation.py.html) ([download]({{ site.url }}/code/ch06/sed_evaluation.py))                                                  |
| *sed_eval*             | [sed_evaluation_sedeval.py]({{ site.url }}/code/ch06/sed_evaluation_sedeval.py.html) ([download]({{ site.url }}/code/ch06/sed_evaluation_sedeval.py)) |

**Audio Tagging**

|                        | example code                                     | 
| -----------------------|--------------------------------------------------|
| *sed_eval*             | [tag_evaluation_sedeval.py]({{ site.url }}/code/ch06/tag_evaluation_sedeval.py.html) ([download]({{ site.url }}/code/ch06/tag_evaluation_sedeval.py)) |

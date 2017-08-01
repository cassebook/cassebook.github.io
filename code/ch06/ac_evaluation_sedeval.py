#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple example how to evaluate acoustic scene classification systems with
# sed_eval toolbox.
#
# Author: Toni Heittola (toni.heittola@tut.fi)

import sed_eval

reference = sed_eval.util.SceneList([
    {
        'scene_label': 'supermarket',
        'file': 'supermarket09.wav'
    },
    {
        'scene_label': 'tubestation',
        'file': 'tubestation10.wav'
    },
    {
        'scene_label': 'quietstreet',
        'file': 'quietstreet08.wav'
    },
    {
        'scene_label': 'office',
        'file': 'office10.wav'
    },
    {
        'scene_label': 'bus',
        'file': 'bus01.wav'
    },
])

estimated = sed_eval.util.SceneList([
    {
        'scene_label': 'supermarket',
        'file': 'supermarket09.wav'
    },
    {
        'scene_label': 'bus',
        'file': 'tubestation10.wav'
    },
    {
        'scene_label': 'quietstreet',
        'file': 'quietstreet08.wav'
    },
    {
        'scene_label': 'park',
        'file': 'office10.wav'
    },
    {
        'scene_label': 'car',
        'file': 'bus01.wav'
    },
])

# Get scene labels
scene_labels = sed_eval.sound_event.util.unique_scene_labels(reference)

# Initialize evaluator
scene_metrics = sed_eval.scene.SceneClassificationMetrics(scene_labels)

# Evaluate
scene_metrics.evaluate(
    reference_scene_list=reference,
    estimated_scene_list=estimated
)

# Print results
print(scene_metrics)

# Scene classification metrics
# ----------------------------------------------------------------------
#     Scene labels      :     5
#     Evaluated units   :     5
#
#   Class-wise average metrics (macro-average)
#   ===============
#   Accuracy
#     Accuracy          :  40.0 %
#
#   Class-wise metrics
#   ===============
#     Scene label       | Ncorr | Nref | Accuracy |
#     ------------------+-------+------+----------+
#     bus               |     0 |    1 |   0.0 %  |
#     office            |     0 |    1 |   0.0 %  |
#     quietstreet       |     1 |    1 | 100.0 %  |
#     supermarket       |     1 |    1 | 100.0 %  |
#     tubestation       |     0 |    1 |   0.0 %  |
#

% CASSE Chapter 9, CCA illustration figure matlab source code
% Required: linCCA.m from the following toolbox - http://ttic.uchicago.edu/~wwang5/knoi.html

clc
clear all

%Path to CCA toolbox
%addpath(path\to\toolbox)

%Load audio-video features along with segment annotations
load('aud_features.mat')
load('vid_features.mat')
load('basketball_segments.mat')

%Read a frame to overlay results
frm = imread('basketball_image.jpg');

[N, feat_vid] = size(vid_features);

%linear CCA regularization params
regX = 1e-3;
regY = 1e-3;


%Linear CCA
segment_corr = [];
for eachseg = 1 : feat_vid
    [alpha1, alpha2, ~, ~, beta] = linCCA(aud_features, vid_features(:,eachseg), 1, regX, regY);
    segment_corr = [segment_corr beta];
end


%Generating Figure
frm_cluster = zeros(size(seg_frame));
corr_scaled = segment_corr/max(segment_corr);

for j = 1:feat_vid
    clus_seg = ismember(seg_frame,j);
    frm_cluster(clus_seg) = 255*corr_scaled(j);
end

figure(1)
imshow( frm ); hold on;
colormap(flipud(hot)); 
h = imagesc(frm_cluster);
set( h, 'AlphaData', .5 );
% CASSE book Chapter 8, Approaches to Complex Sound Scene Analysis
% Figure 8.6 - NMF decomposition of an artificial sound scene

% Prerequisites:
% NMFLib toolbox: http://www.ee.columbia.edu/~grindlay/code.html

% Emmanouil Benetos 2016


% Read alarm and doorslam audio recordings, construct artificial sequence
[x1,fs] = audioread('alarm44.wav');
[x2,fs2] = audioread('doorslam006.wav');
x3 = zeros(200000,1);
x3(10000:10000+154800-1) = mean(x1(1:154800,:)');
x3(170000:170000+length(x2)-1) = 4*x2;


% Compute ERB spectrogram, initialise dictionary templates and run NMF
[X] = computeERB(x3,fs);
W1 = X(:,29);
W2 = mean(X(:,168:176)');
W = [W1 W2'];
W0=W;
[w1,h,errs,vout] = nmf_beta(X,2,'W0',W,'W',W,'niter', 10, 'verb', 1,'beta',0.6);


% Plot spectrogram and NMF outputs
figure;
subplot(2,2,[1 2]);
imagesc(X); axis xy
title('(a)');
ylabel('frequency bin');
xlabel('time (sec)');
xticklabels({'0.4','0.8','1.2','1.6','2.0','2.4','2.8','3.2','3,6'});
subplot(2,2,3);
multiplot(W');
title('(b)')
ylabel('k');
xlabel('frequency bin');
yticks([0.5 2.5]);
yticklabels({'1','2'})
subplot(2,2,4);
multiplot(h);
title('(c)');
xlabel('time (sec)');
ylabel('k');
xticks(20:20:180);
xticklabels({'0.4','0.8','1.2','1.6','2.0','2.4','2.8','3.2','3,6'});
yticks([0.5 2.5]);
yticklabels({'1','2'})


%%%

function [X] = computeERB(x,fs)

% Code for computing ERB T/F representation
% Adapted from code by Emmanuel Vincent:
% http://homepages.loria.fr/evincent/software/multipitch_tracking.m


% Initialize
nbfreq=250;


% Reading WAV file
%[x,fs]=wavread(wavfile);
x=resample(x,22050,fs).';
fs = 22050;
[I,T]=size(x);
wlen=2^nextpow2(.02*fs);    %20 ms window length
N=ceil(T/wlen);


% Computing ERBT coefficients and frequency scale
X=zeros(nbfreq,N,I);
for i=1:I,
    [X(:,:,i),f]=erbtm(x(i,:),fs,nbfreq,wlen);
end
X=(sum(X.^2,3)+1e-18).^.5;
fmin=f(1);
fmax=f(nbfreq);
%emin=9.26*log(.00437*fmin+1); emax=9.26*log(.00437*fmax+1);
%e=(0:nbfreq-1)*(emax-emin)/(nbfreq-1)+emin;
%a=.5*(nbfreq-1)/(emax-emin)*9.26*.00437*fs*exp(-e/9.26)-.5;
%alen=2*round(a)+1;
%f=f/fs;

end

function [X,f]=erbtm(x,fs,F,wlen)

% ERBTM Magnitude ERB Transform using a Hann window.
%
% [X,f]=erbtp(x,fs,F,wlen)
%
% Inputs:
% x: 1 x T vector containing a single-channel signal
% fs: sampling frequency in Hz
% F: number of frequency bins (the ratio between the bandwidth of each bin
% and the frequency difference between successive bins is constant)
% wlen: number of samples per frame (must be a multiple of the largest
% downsampling factor, typically a large power of 2)
%
% Output:
% X: F x N matrix containing the time-frequency magnitude (amplitude) coefficients
% f: F x 1 vector containing the center frequency of each frequency bin

%%% Errors and warnings %%%
if nargin<4, error('Not enough input arguments.'); end
[I,T]=size(x);
if I>1, error('The input signal must be a row vector.'); end
N=ceil(T/wlen);

%%% Computing ERBT coefficients %%%
x=hilbert(x);
X=zeros(F,N);
% Determining minimum and maximum frequency
fmax=.5*fs; fmin=0;
for j=1:100,
    emin=9.26*log(.00437*fmin+1);
    emax=9.26*log(.00437*fmax+1);
    fmin=1.5*(emax-emin)/(F-1)/9.26/.00437*exp(emin/9.26);
    fmax=.5*fs-1.5*(emax-emin)/(F-1)/9.26/.00437*exp(emax/9.26);
    if (fmax < 0) || (fmin > .5*fs), error('The number of frequency bins is too small.'); end
end
% Determining frequency and window length scales
emin=9.26*log(.00437*fmin+1);
emax=9.26*log(.00437*fmax+1);
e=(0:F-1)*(emax-emin)/(F-1)+emin;
f=(exp(e/9.26)-1)/.00437;
a=.5*(F-1)/(emax-emin)*9.26*.00437*fs*exp(-e/9.26)-.5;
% Determining dyadic downsampling bins (for fast computation)
fup=f+1.5*fs./(2*a+1);
subs=-log(2*fup/fs)/log(2);
subs=2.^max(0,floor(min(log2(wlen),subs)));
if (wlen/subs(1) ~= floor(wlen/subs(1))), error(['The number of samples per frame must be a multiple of ' int2str(subs(1)) '.']); end
down=(subs~=[subs(2:end),1]);
for bin=F:-1:1,
    % Dyadic downsampling
    if down(bin),
        x=resample(x,1,2,50);
    end
    % Convolution with a modulated sine window
    hwlen=round(a(bin)/subs(bin));
    win=hanning(2*hwlen+1).'.*exp(2i*pi*f(bin)/fs*subs(bin)*(-hwlen:hwlen));
    band=[fftfilt(win,[x,zeros(1,2*hwlen)]) zeros(1,wlen/subs(bin))];
    % Square-root energy on short time frames
    band=band(hwlen+1:hwlen+N*wlen/subs(bin));
    X(bin,:)=sqrt(sum(reshape(abs(band).^2,wlen/subs(bin),N),1)/(hwlen+1)^2*subs(bin));
end

return;

end


%%%


function multiplot( x, sz)
% Plot multiple vectors into one compact plot

% Paris Smaragdis, 2007, paris@media.mit.edu

% Cellify
if ~iscell( x)
	for i = 1:size( x, 1)
		X{i} = x(i,:);
	end
	x = X;
end
n = length( x);

% Default arrangement
if ~exist( 'sz')
	if n > 15
		sz = ceil(sqrt( length( x))) * [1 1];
	else
		sz = [n 1];
	end
end

% Find proper scaling
mx = 0;
for i = 1:n
	mx = max( mx, max( abs( x{i})));
end

% Plot them
cla reset
l = length( x{1});
for i = 1:n
	r = mod( i-1, sz(1));
	c = floor( (i-1)/sz(1));
	line( c*1.1*l + (1:l), 2*r + x{i}/max( abs(x{i})))
end
axis tight


end


% Brian Knisely
% ME311 Lab 11
% The purpose of Part A this code is to process a data file and determine the
% largest frequency contributor at 1000 Hz. The purpose of Part B is to
% generate a signal with multiple amplitudes and frequencies and then
% sample that signal.
close all; clear all; format compact;

% Part A - Process data file and determine largest frequency contributor
data = load('acc2.dat'); % Load datafile
fs=1000; % Set sampling frequency
N=length(data); % Determine number of data points
t=0:1/fs:N/fs-1/fs; % Define time interval
Ny=fs/2; % Calculate Nyquist frequency
f=(0:N-1)*(fs/N); % Calculate frequencies associate with each position
datanorm=data-mean(data); % normalize data by subtracting mean 
figure % Plot signal versus time in subplot #1 with axes labeled
subplot(2,1,1)
plot(t,datanorm);
xlabel('time');ylabel('signal');
Y=fft(datanorm); % Calculate FFT
PowerY=(abs(Y).^2)/N; % Calculate power
subplot(2,1,2)% plot power vs frequency and label axes
stem(f(1:Ny),PowerY(1:Ny));xlabel('Hz');ylabel('Power'); % stem plot

% Part B - Generate a signal at different amplitudes and frequencies, and
% then sample the signal
fs=500; % Sampling at 500 Hz
sampleTime = 10;
t = 0:1/fs:sampleTime-1/fs;
y = 4*cos(8*pi*t)+6*cos(12*pi*t)+10*cos(30*pi*t); 
% Construct signal with amp 4 @ 4Hz, 6 @ 6Hz, 10 @ 15Hz 
n = length(y); % Compute number of data points
f=(0:n-1)*fs/n; % Calculate frequencies associated with each point
Ny = fs/2; % Define Nyquist frequency
Y = fft(y); % Calculate FFT
yMag = 2*abs(fft(y))/n; % Compute magnitude
figure
subplot(2,1,1) 
plot(t,y) % Plot signal vs time
xlabel('time (t)');ylabel('Signal'); % label axes
subplot(2,1,2) % Plot magnitude vs frequency
stem(f(1:Ny),yMag(1:Ny));xlabel('Frequency (Hz)');ylabel('Magnitude');


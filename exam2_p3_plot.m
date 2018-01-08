DR = 1.6;
BR = 0.5:0.1:40;
VR = zeros(1,length(BR));
I = zeros(1,length(BR));
for n = 1:length(BR)
    VR(n) = BR(n)/DR;
    I(n) = BR(n)^2/DR;
end
figure;
plot(BR,VR);
xlabel('Blowing Ratio'); % Comment
ylabel('Velocity Ratio');

figure;
plot(BR,I);
xlabel('Blowing Ratio');
ylabel('Momentum Flux Ratio');


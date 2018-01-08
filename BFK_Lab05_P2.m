% Brian Knisely
% ME311 Lab 05, Problem 2
% The purpose of this code is to plot a data set, find and plot a quadratic
% regression line, and display the R-squared value.

close all 
clear all

x = [12.5, 25,37.5,50,62.5,75]; % x data
y = [20,59,118,197,299,420]; % y data
p = polyfit(x,y,2); % Create best-fit quadratic (n=2) line for x,y dataset
f = polyval(p,x); % Determine y value of best-fit line for each x point
SSE=sum((y-f).^2); 
SST=sum((y-mean(y)).^2);
Rsquared=1-SSE/SST; % R-squared calculation
fx = [min(x) max(x)];
fy = polyval(p,fx);

plot(x,y,'r*',x,f,'b');xlabel('speed (mph)');
ylabel('stopping distance (ft)'); % plot data and label axes
title('Stopping distance vs initial speed'); % add title
text(min(fx),max(fy),sprintf('d = %.3f v^2 + %.3f v + %.3f, R^2 = %.5f',p(1),...
    p(2),p(3),Rsquared))
% Add text to plot to describe function and show R-squared value

% Brian Knisely
% ME311 Lab 08 
% Problem 1a
clear all
close all
sigmaIJ = [40,20,-18;20,28,12;-18,12,14]; % Define stress vector
[vectors,values]=eig(sigmaIJ); % Calculate eigenvectors and eigenvalues
fprintf('Part A:\nPrinciple Stresses: | Direction cosines: \n');
for n = 1:3 % Start loop to display principle stresses and directions 
    fprintf('Sigma %d = %.2f ksi | (%.3f, %.3f, %.3f)\n',n,values(n,n),...
        vectors(1,n),vectors(2,n),vectors(3,n));
end

% Problem 1b
fprintf('\nPart B:\n'); % Display for Part B
m=1;L=1;g=9.8; % Define quanitites for mass, length, gravity
M1=[2*m*L, m*L;m*L,m*L]; % Define first matrix
M2=[2*m*g,0;0,m*g]; % Define second matrix
[vec,val]=eig(M2,M1); % calculate eigenvectors and eigenvalues
fprintf('Eigenvalues: %.4f, %.4f\nEigenvectors:\n',val(1,1),val(2,2));
disp(vec); % Display all the things

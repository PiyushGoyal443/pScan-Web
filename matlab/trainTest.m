function [xtrain,ytrain,xtest,ytest]=trainTest(x,y,m,n)
pkg load statistics;
r1=randperm(m); %Random Permutation
train=floor(0.7*m);
trainpos=r1(1:train);
xtrain=x(trainpos,1:n);
ytrain=y(trainpos);

testpos=r1(train:m);
xtest=x(testpos,1:n);
ytest=y(testpos);

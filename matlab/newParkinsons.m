function [theta1_final,theta2_final,success]=newParkinsons(X)
pkg load statistics;
%clc
%clear all
%X=load('train_data.csv');
n=size(X,2);
m=size(X,1);
x1=X(:,2:(n-1));
x = [ones(size(x1,1),1) x1];   %Adding Bias value

y=X(:,29);

n=size(x,2);
m=size(x,1);

[xtrain,ytrain,xtest,ytest]=trainTest(x,y,m,n);
TreeObject=TreeBagger(500,xtrain(:,1:27),xtrain(:,28),'method','regression','NVarToSample','all');
[YFIT,scores] = predict(TreeObject,xtrain(:,1:27));
xtrain(:,28)=YFIT;

m=size(xtrain,1);
neurons=12;
outIters=2;
sumSuccess=0;
max=0;

for i=1:outIters
    theta1=-1+2*rand(n,neurons);
    theta2=-1+2*rand(neurons,1);
    inIters=200000;
    error=zeros(inIters,1);
    g1=zeros(size(xtrain,1),neurons);
    g2=zeros(neurons,1);
    for i=1:inIters

        [g1,g2]=feedforward(xtrain,theta1,theta2);
        [theta1,theta2]=backpropagation(g1,g2,theta1,theta2,xtrain,ytrain);
        error(i)=sum((ytrain-g2).^2); %Mean Square Error Calculation

    end

    %plot(error);
    %hold on;
    [g2test,h,success]=testfuncNew(TreeObject,theta1,theta2,xtest,ytest);

    sumSuccess=sumSuccess+success;
    if(success>max)
        max=success;
        theta2_final=theta2;
        theta1_final=theta1;
    end
end
createTxtFile(theta1_final,theta2_final);
%xlabel('No. of Iterations');
%ylabel('Error');

function [YFIT,xtestNew]=randomForests(TreeObject,xtest1)
pkg load statistics;
%TreeObject=TreeBagger(500,xtrain1(:,1:27),xtrain1(:,28),'method','regression','NVarToSample','all');
[YFIT,scores] = predict(TreeObject,xtest1(:,1:27));
pos=find(YFIT<5);
YFIT(pos)=1;
xtestNew=[xtest1 YFIT];

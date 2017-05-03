function [updrs,xtestNew]=randomForestsClassify(TreeObject,xtest1)
pkg load statistics;
%TreeObject=TreeBagger(500,xtrain1(:,1:27),xtrain1(:,28),'method','regression','NVarToSample','all');
[YFIT,scores] = predict(TreeObject,xtest1(:,1:27));
updrs=YFIT;
if(updrs<5);
    YFIT=1;
end
xtestNew=[xtest1 YFIT];

function h=classify(theta1,theta2,xtest)
%pkg load statistics;
%TreeObject=TreeBagger(500,xtrain(:,1:27),xtrain(:,28),'method','regression','NVarToSample','all');
%[YFIT,scores] = predict(TreeObject,xtrain(:,1:27));
%xtrain(:,28)=YFIT;
%[updrs,xtestNew]=randomForestsClassify(TreeObject,xtest(:,1:27));

g1=sigmoid(xtest*theta1);
g2test=sigmoid(g1*theta2);

if(g2test>0.5)
    h=1;
else
    h=0;
end

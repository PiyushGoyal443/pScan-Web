function [g1,g2]=feedforward(xtrain,theta1,theta2)
pkg load statistics;
g1=sigmoid(xtrain*theta1);
g2=sigmoid(g1*theta2);

end

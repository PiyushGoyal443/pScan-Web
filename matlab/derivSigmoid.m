function [deriv]=derivSigmoid(x)
pkg load statistics;
deriv=x.*(1-x);

end

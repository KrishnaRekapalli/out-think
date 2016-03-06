function value2 = FWfn(lambda,x,xold,NetData,Nrows,initNodes,termNodes,capacity)
% This function calculates the value of the variatonal inequality and gives
% that as output as a function of lambda
%( which we solve for ZERO using fsolve function)
poly = (lambda*x+(1-lambda)*xold);

    for count1 = 1:Nrows
    TXdashvec(count1) = NetData(count1,4)*(1 + 0.15*(( poly(initNodes(count1),termNodes(count1)))/capacity(count1))^4);
    end
    
    for count5 = 1:Nrows   
        TXdashmat(initNodes(count5),termNodes(count5)) = TXdashvec(count5);
    end



value1 = TXdashmat.*(x-xold);
% value2 is the VI as a function of lambda
value2 = sum(value1(:));
end
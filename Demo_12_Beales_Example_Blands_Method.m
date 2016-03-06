clear all
close all
clc
% prompt ='Enter the A matrix with m rows and n columns';
% A = input(prompt);
% prompt = 'Enter the b vector with m rows and 1 column ';
% b = input(prompt);
% prompt = 'Enter the C vector with n rows and 1 column ';
% C = input(prompt);
% prompt = 'Enter the binary vector with n rows and 1 column ';
% BasisBin = input(prompt);
A =  [1 0 0 .25 -8 -1 9
      0 1 0  .5 -12 -0.5 3
      0 0 1  0   0   1  0];
b = [  0
       0
       1];
C = [ 0
      0
      0
      -0.75
      20
      -0.5
      6];
 
BasisBin = [ 1
             1
             1
             0
             0
             0
             0];

 count7 =0;
 count8 =0;
 %Recording which columns belong to the basis and which are non basic
 for count6 = 1:length(BasisBin)
     if BasisBin(count6) == 0
         count7 = count7+1;
         NBindex(count7) = count6;
     else
         count8 = count8+1;
         Bindex(count8) = count6;
     end
 end
 

[nRowsA, nColsA] = size(A) ;

count2 =0;
count3 =0;

for count1= 1:nColsA
    if BasisBin(count1)~= 0 
        count2 = count2+1;
        Basis(:,count2) = A(:,count1);
        Cb(count2) = C(count1);
    end      
    
    if BasisBin(count1) == 0
        count3 = count3+1;
        CNp(count3) = C(count1);
        ANp(:,count3) = A(:,count1);
    end    
    
end

%     CNp
%     ANp
 Basis
%     Cb
% Finding reduced costs
for iteration = 1:121
    %ANp
for count4 = 1:count3
    D(count4) = CNp(count4) - Cb*(Basis\ANp(:,count4));
    
    yb(:,count4) = Basis\ANp(:,count4);
    
end
    yb

if iteration==1 
    Xb = Basis\b;
end
% Xnb = [0;0;0];
% X = [Xold;Xnb];
D
[minD,j] = min(D);
j
for count9 = 1:length(D)
    if D(count9)<0
        j=count9;
        break;
    else
        break;
    end
end
if minD >= 0 
        optimalObj = Cb*(Basis\b);
        optimalObj
        Basis\b
        disp('This is the optimal solution');
        break;
else
    for count5 = 1:nRowsA
        if max(yb(:,j))<0 
            disp('problem is unbounded');
        end
        
        if yb(count5,j)>0
        theta(count5) = Xb(count5)/yb(count5,j);
        elseif yb(count5,j) == 0
            theta(count5) = 1000;
        else
            theta(count5) = 1000;
        end
    end
    theta
    [mintheta,k]= min(theta);
    k
%     Xold = Xold - mintheta*yb(:,j);
%     Xold(k) = mintheta;
    %Xold

    Temp1 = ANp(:,j);
    
    Temp3 =  NBindex(j);
    Temp4 = Bindex(k);
    
    NBindex(j)= Temp4;
    Bindex(k)= Temp3;
    
    ANp(:,j)= Basis(:,k);
    Basis(:,k) = Temp1;
    %A(:,NBindex(j));
    Temp2 = CNp(j);
    CNp(j) = Cb(k);
    Cb(k) = Temp2;
    
    Xb = Basis\b;
    
end
%disp(iteration);
%disp(Basis);
Basis
Basis\b
%Xold
Cb
CNp
ANp
iteration = iteration+1
end

index = [Bindex,NBindex];
for count10 = 1:length(Bindex)+length(NBindex)
   Avar(:,count10)= A(:,index(count10));
   
end







    

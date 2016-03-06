clc
clear all;
close all;
%Reading input data 
NetData = xlsread('InputNetSF.xlsx','Network','B9:E84');
ODMatrix = xlsread('InputNetSF.xlsx','ODmatrixMod','AL7:BI30');
% Defines No of iterations for UE problem
iter_max = 1000;

NetData_Master = NetData;
% Defining the arrays to store results
TSTT_NRI = zeros(1,76);
NRI = zeros(1,76);
rel_gap = zeros(1,iter_max);
AEC = zeros(1,iter_max);

for link_count = 1:77
    
    link_count
    if link_count ~= 1 
        NetData = NetData_Master;
        NetData(link_count-1,:) = [];
    end

total_trips = sum(ODMatrix(:));
[Nrows,Ncols] = size(NetData);

initNodes = NetData(:,1);
termNodes = NetData(:,2);


capacity = NetData(:,3);
 x = zeros(length(ODMatrix));
 T = zeros(length(ODMatrix));
 t = zeros(1,Nrows);
 
 for iteration = 1:iter_max
     
if iteration ==1

for count1 = 1:Nrows
    t(count1) = NetData(count1,4)*(1 + 0.15*(( x(initNodes(count1),termNodes(count1)))/capacity(count1))^4);
end

Graph = sparse(initNodes,termNodes,t);
k = 0;
for count2 = 1:length(Graph)
    
    for count3 = 1:length(Graph)
        
        if count2 ~= count3 
            k =k+1;
            k;
            count2;
            count3;
            [dist,path,pred] = graphshortestpath(Graph,count2,count3,'Method','Bellman-Ford');
            dist;
            path;
            for count4 = 1:length(path)-1
                x(path(count4),path(count4+1)) = x(path(count4),path(count4+1))+ ODMatrix(count2,count3);
                
            end
        end
        
    end
    
end

end

if iteration~=1 
    
    xold = x;
    
    for count1 = 1:Nrows
    t(count1) = NetData(count1,4)*(1 + 0.15*(( x(initNodes(count1),termNodes(count1)))/capacity(count1))^4);
    end
    
    x = zeros(length(ODMatrix));

    Graph = sparse(initNodes,termNodes,t);

    for count2 = 1:length(Graph)
    
        for count3 = 1:length(Graph)
        
            if count2 ~= count3 
            
                [dist,path,pred] = graphshortestpath(Graph,count2,count3,'Method','Bellman-Ford');
            
                for count4 = 1:length(path)-1
                x(path(count4),path(count4+1)) = x(path(count4),path(count4+1))+ ODMatrix(count2,count3);
                end
            end
        
        end
    
    end
    
    
    for count5 = 1:Nrows   
        T(initNodes(count5),termNodes(count5)) = t(count5);
    end
    
    xtSPTT = x.*T;
    SPTT = sum(xtSPTT(:));
    
   % x = (1/iteration)*x + (1-(1/iteration))*xold;    
    FW = @(lambda)FWfn(lambda,x,xold,NetData,Nrows,initNodes,termNodes,capacity);
    flowshift = fsolve(FW,0.3);
    
    if link_count ==1
        lamdaFW(iteration) = flowshift;
    end
    
    x = flowshift*x + (1-flowshift)*xold;
    xtTSTT = x.*T;
    TSTT = sum(xtTSTT(:));
    
    rel_gap(iteration) = (TSTT/SPTT)-1;
    AEC(iteration) = (TSTT-SPTT)/total_trips;
    
end  

  if link_count == 1 && iteration == iter_max
    Xequil = x;
  end
    
 end
 
 
 if link_count == 1
    TSTT_base = TSTT;
 else 
     TSTT_NRI(link_count-1) = TSTT;
     NRI(link_count-1) = TSTT_NRI(link_count-1)-TSTT_base;
 end
 
 
 
end

h = view(biograph(Graph,[],'ShowWeights','on'));



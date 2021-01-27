close all;
clear all;
clc;

Datos=[0.36 0.85; 0.65 0.89; 0.62 0.55; 0.50 0.75; 0.35 1.00;... 
    0.90 0.35; 1.00 0.24; 0.99 0.55; 0.83 0.36; 0.88 0.43];
r1=1;
r2=1.5*r1;
Di=zeros(1,10);
Di2=zeros(1,10);

for n=1:10
    for k=1:10
        distancia=sqrt((abs(Datos(n,1)-Datos(k,1))^2)+(abs(Datos(n,2)-Datos(k,2))^2));
        Di(n)=Di(n)+exp(-(distancia/(r1/2)^2));
    end
end
m=max(Di);
pos=find(Di==m);

for n=1:10
    for k=1:10
        distancia=sqrt((abs(Datos(n,1)-Datos(k,1))^2)+(abs(Datos(n,2)-Datos(k,2))^2));
        Di(n)=Di(n)+exp(-(distancia/(r1/2)^2));
    end
        distancia2=sqrt((abs(Datos(n,1)-Datos(pos,1))^2)+(abs(Datos(n,2)-Datos(pos,2))^2));
        Di2(n)=Di(n)-m*exp(-(distancia2/(r2/2)^2));
end

m2=max(Di2);
pos2=find(Di2==m2);

figure(1)
grid on;
hold on;
title('SubstractiveClustering 10 Datos')
plot(Datos(:,1),Datos(:,2),'*g');
plot(Datos(pos,1),Datos(pos,2),'xr');
plot(Datos(pos2,1),Datos(pos2,2),'xr');
legend('Data','Clusters')
xlabel('X');
ylabel('Y');
hold off;


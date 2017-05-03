function createTxtFile(theta1,theta2)
pkg load statistics;
fileID = fopen('theta1.txt','w');
for i=1:size(theta1,1)
    for j=1:size(theta1,2)
        fprintf(fileID,'%f ',theta1(i,j));
    end
     fprintf(fileID,'\n',theta1(i,j));
end
fclose(fileID);
fileID = fopen('theta2.txt','w');
for i=1:size(theta2,1)
    for j=1:size(theta2,2)
        fprintf(fileID,'%f ',theta2(i,j));
    end
     fprintf(fileID,'\n',theta2(i,j));
end
fclose(fileID);

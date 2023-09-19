#!/bin/sh

#clear out an old file (if not, you will concatenate instead of overwriting)
rm clusteringfrequency.csv

#pick out the cluster indices
awk -F" " '{print $1}' clusteringsize.xvg > first.csv

#add the cluster sizes to a temporary file
awk -F" " '{print $2}' clusteringsize.xvg > temp.txt

#removes the words from the cluster sizes temporary file
sed -e '1,18d' temp.txt > temp2.txt

#add the cluster sizes as a new column in the csv file
paste -d, first.csv temp.txt > second.csv

#remove all the unnecessary words
sed -e '1,18d' second.csv > third.csv

#change the csv delimiter from a comma to a tab
sed 's/,/	/' third.csv > fourth.csv

#get the sum total of all poses used in clustering
awk '{s+=$2} END {print s}' fourth.csv > sum.txt

#pass the sum total of all poses as a variable (or a hard number)
sum=`cat sum.txt`

#say how many poses went into how many clusters
end=$(tail -n1 first.csv | cut -d'	' -f1)
echo "Clusters contain" $sum "poses grouped into" $end "clusters"

#divides the cluster sizes by the total number of poses used in clustering and adds them to a new file
cat temp2.txt | while read i; do echo "scale = 5; $i/$sum" | bc >> temp3.txt; done

#convert the cluster sizes to percentages
cat temp3.txt | while read j; do echo "scale = 5; $j*100" | bc >> temp4.txt; done

#sum up the percentages to make sure they add to 1
awk '{s+=$1} END {print s}' temp4.txt > percentage.txt
percentage=$(head -n1 percentage.txt | cut -d'	' -f1)
echo "The cluster percentages sum to" $percentage"%, which may be more than 100%"

#add these cluster percentages to the cluster indices
paste -d, fourth.csv temp4.txt > fifth.csv

#change the delimiters from comma to tab
sed 's/,/          /' fifth.csv > sixth.csv

#add a helpful header
sed -i 1i"Number of clusters,Members in cluster,Percentage of total" fifth.csv

#change the delimiter from comma to tab
sed 's/,/	/' fifth.csv > sixth.csv
sed 's/,/	/' sixth.csv > seventh.csv

#rename to something more helpful
mv seventh.csv clusteringfrequency.csv

#remove now unnecessary intermediate files
rm first.csv
rm second.csv
rm third.csv
rm fourth.csv
rm fifth.csv
rm sixth.csv
rm temp.txt
rm temp2.txt
rm temp3.txt
rm temp4.txt
rm sum.txt
rm percentage.txt

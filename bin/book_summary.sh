# Get author information from a Project Gutenberg eBook.
# Usage: bash book_summary.sh /path/to/file.txt
head -n 17 $1 | tail -n 8 | grep Author



# Get desired information from a Project Gutenberg eBook.
# Usage: bash book_summary.sh /path/to/file.txt what_to_look_for
head -n 17 $1 | tail -n 8 | grep $2




for x in ../data/*.txt
do
   echo $x
   bash book_summary.sh $x Author
   done > authors.txt
for x in ../data/*.txt
 do
   echo $x
   bash book_summary.sh $x Release
 done > releases.txt
ls

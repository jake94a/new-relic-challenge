pwd=$(pwd)

for var in $@
do
    echo "
    \n 
    *********** READING $var ***********
    \n 
    "
    docker run -v $(pwd)/texts/$var:/texts/$var jake94a/jake-new-relic-word-search python main.py $var
done
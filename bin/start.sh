pwd=$(pwd)
echo $@

for var in $@
do
    docker run -v $(pwd)/texts/$var:/texts/$var test-relic python search.py $var
done
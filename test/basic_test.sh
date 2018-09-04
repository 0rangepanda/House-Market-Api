# !/bin/sh

#echo "First arg: $1"

echo "GET /api/:"
curl $1/api/

echo "\nCreate data:"
for (( i=0; i < 3; i++ )); do
  curl -X POST $1/api/users/ -d "username=user${i}&password=password${i}"
  echo "\n"

  for (( j=0; j < 3; j++ )); do
    curl --user user${i}:password${i} -X POST $1/api/houses/ -d\
     "name=Apartment${i}-${j}&address=${i}st room${j} &zipcode=${i}000${j}&description=This is fake data(${i}-${j})"
  done
done


echo "\n\nQuery and PUT Test:"
for (( i=0; i < 3; i++ )); do
  echo "\nView information:"
  curl --user user${i}:password${i} $1/api/users/
  echo "\n"

  for (( j=0; j < 3; j++ )); do
    curl --user user${i}:password${i} -X PUT $1/api/houses/ -d\
     "status=PD&name=Apartment${i}-${j}&address=${i}stroom${j}&zipcode=${i}000${j}&description=This is fake data(${i}-${j})"
  done

  echo "\nAll houses of user${i}:"
  curl $1/api/houses/?username=user${i}
done

echo "\n\nSearch Test:"
echo "\nAddress contains 1st:"
curl $1/api/houses/?address=1st
echo "\nzipcode=10002:"
curl $1/api/houses/?zipcode=10002

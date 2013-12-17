# Make file, sort of... really a bash script
echo "====== PYLINT ======="
epylint quick.py
epylint quick_docker.py

echo "==== CLEAN ===="
rm -rf docker/ flask/
mkdir docker flask
cp -a css docker
cp -a css flask

echo "====== EXECUTE ======="
python quick_flask.py > flask/quick_flask.html
python quick_docker.py > docker/quick_docker.html && echo "======= OPEN ======" && open docker/quick_docker.html


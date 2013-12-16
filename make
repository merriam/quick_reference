# Make file, sort of... really a bash script
echo "====== PYLINT ======="
epylint quick.py quick_docker.py
rm -f xquick.html
echo "====== EXECUTE ======="
python quick_docker.py > xquick.html && echo "======= OPEN ======" && open xquick.html

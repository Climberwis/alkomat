#!/bin/bash
cat ./help.sh > /dev/null 2>&1
czy_help=$?
if [[ ($czy_help -eq 0) ]]; then
	chmod +x help.sh
fi

while getopts ":h :v" opt ; do
case $opt in
h) 	./help.sh
	exit 0
	;;
v) 	printf "Alkomat v 1.0.0\n"
	exit 0
	;;
\?)
echo "Invalid option: -$OPTARG" >&2
exit 1
;;
esac
done


i=0
cat ./alkomat.py > /dev/null 2>&1
czy_alkompy=$?
cat ./alkomat_ui.py > /dev/null 2>&1
czy_alkouipy=$?
cat ./alko.py > /dev/null 2>&1
czy_alkopy=$?

if [[ ($czy_alkompy != 0) || ($czy_alkouipy != 0) || ($czy_alkopy != 0) ]]; then
printf "Missing files, would you like to download them now? (y,n):\n"
	while [ $i -eq 0 ]; do
		read a
		if [[ $a =~ ^[0-9]+$ ]]; then
			printf "(y,n) expected\n"
		fi
		if [[ $a == 'y' || $a == 'Y' ]]; then
			git clone git://github.com/Climberwis/alkomat 2>&1
			cp alkomat/alkomat.py ./ 2>&1
			cp alkomat/alkomat_ui.py ./ 2>&1
			cp alkomat/alko.py ./ 2>&1
			((i++))
		elif [[ $a == 'n' || $a == 'N' ]]; then
			exit 0
		else printf "(y,n) expected\n"
		fi
	done
fi
chmod +x alkomat.py
./alkomat.py

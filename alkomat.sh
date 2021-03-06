#!/bin/bash
dir="$(dirname $0)"

cat ./help.sh > /dev/null 2>&1
czy_help=$?
if [[ ($czy_help -eq 0) ]]; then
	chmod +x $dir/help.sh
fi

while getopts ":h :v" opt ; do
case $opt in
h) 	$dir/help.sh
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
cat $dir/alkomat.py > /dev/null 2>&1
czy_alkompy=$?
cat $dir/alkomat_ui.py > /dev/null 2>&1
czy_alkouipy=$?
cat $dir/alko.py > /dev/null 2>&1
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
			mv alkomat/alkomat.py $dir/ 2>&1
			mv alkomat/alkomat_ui.py $dir/ 2>&1
			mv alkomat/alko.py $dir/ 2>&1
			((i++))
		elif [[ $a == 'n' || $a == 'N' ]]; then
			exit 0
		else printf "(y,n) expected\n"
		fi
	done
fi
chmod +x $dir/alkomat.py
$dir/alkomat.py

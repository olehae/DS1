ersteZahl=$1
zweiteZahl=$2

if [ $ersteZahl -gt $zweiteZahl ]; then
    temp=$ersteZahl
    ersteZahl=$zweiteZahl
    zweiteZahl=$temp
fi
for (( i=$((ersteZahl+1)); i<$zweiteZahl ; i++ )); do
    printf "$i "
done

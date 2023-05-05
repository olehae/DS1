while true 
do
    read -p "Sind sie sicher [Ja oder Nein]?" ANTWORT
    if [ $ANTWORT = Ja ]; then
        exit 0
    fi
    if [ $ANTWORT = Nein ]; then
        exit 1
    fi
done

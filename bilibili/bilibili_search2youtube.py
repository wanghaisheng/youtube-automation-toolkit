#yt-dlp  --config-location config.txt https://www.youtube.com/results?search_query=%23dentaldigest
yt-dlp "bilisearch500:申鹤mmd" --config-location down.txt 

cd D:\\Download\\audio-visual\\UCBBj-A2EqL5pNApsLhoeM6w\\shenhe


#remove space in filename


while [ "$(find ./ -regex '.* .*' | wc -l)" -gt 0 ];
    do filename="$(find ./ -regex '.* .*' | head -n 1)"
    mv "$filename" "$(echo "$filename" | sed 's|'" "'|_|g')"
done


for filename in ./*.flv; do   
    echo $filename
    name=$(echo "$filename" | sed 's/\.[^.]*$//')
    echo $name
    if [ -e "${name}-shenhe.mp4" ]
    then
        echo "compilation video exist-----------"

        rm "${name}-overlay.mp4"   
    else
        duration=$(ffprobe -i $filename -show_entries format=duration -v quiet -of csv="p=0")
        echo $duration
        ffmpeg -n -stream_loop  -1 -i ../overlay.mp4 -t $duration -c copy  $name-overlay.mp4

        ffmpeg -n -i $filename  -i $name-overlay.mp4 -filter_complex "[1:v]colorkey=0x34d454:0.3:0.15[ckout];[0:v][ckout]overlay[despill];[despill] despill=green[colorspace];[colorspace]format=yuv420p[out]" -map "[out]" -map 0:a -c:a copy  $name-shenhe.mp4

        rm "${filename}-overlay.mp4"   

    fi      

done


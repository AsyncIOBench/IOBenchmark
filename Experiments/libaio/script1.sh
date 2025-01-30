types=("randrw" "randwrite" "randread")
sizes=(4 1)
numjobs=(1 4)

for type in "${types[@]}"; do
    for i in {0..1}; do
        output_file="${type}_$((i+1)).txt"
        
        echo "type: $type, size: ${sizes[i]}, numjobs= ${numjobs[i]}"
        echo "type: $type, size: ${sizes[i]}, numjobs= ${numjobs[i]}" > "$output_file"

        echo "genesis1:3" | sudo -S fio \
            --filename=/dev/nvme0n1 \
            --readwrite="$type" \
            --name=randwrite \
            --blocksize=4kb \
            --direct=1 \
            --ioengine=libaio \
            --size="${sizes[i]}"G \
            --numjobs="${numjobs[i]}" \
            --time_based=1 \
            --runtime=10 \
            --refill_buffers \
            --norandommap \
            --group_reporting >> "$output_file"
    done
done
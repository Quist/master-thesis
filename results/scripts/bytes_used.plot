set terminal postscript eps enhanced color solid
set output '|ps2pdf -dEPSCrop - packets_sent.pdf'

set ylabel "IP Packets"
set key autotitle columnhead

fontsize = 12
set style histogram gap 2
# Select histogram data
set style data histogram

set style fill solid border -1

#Grid lines
set grid ytics lt 0 lw 1
set xtic rotate by -45 scale 0

set style histogram clustered


set yrange [0:220]

plot filename using 2:xtic(1) title col, '' using 3:xtic(1)

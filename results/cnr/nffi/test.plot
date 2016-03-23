set terminal pdf
set output 'out.pdf'

set title "WIFI 2 - W3C Web service"
set ylabel "Average Time(ms)"

fontsize = 12
set style histogram errorbars gap 2 lw 1
# Select histogram data
set style data histogram
# Give the bars a plain fill pattern, and draw a solid line around them.
set style fill solid 1.00 border 0

#Grid lines
set grid ytics lt 0 lw 1

set style histogram clustered


set autoscale

plot for [COL=2:3] 'results.data' using COL:xticlabels(1) title columnheader

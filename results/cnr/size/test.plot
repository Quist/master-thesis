set terminal postscript eps enhanced color solid
set output '|ps2pdf -dEPSCrop - result.pdf'

set grid
set title 'CNR Size tests'
set xtics rotate by -45
set xtics nomirror scale 0
set style data linespoints
set ylabel "Average Time(ms)"
set xlabel "Payload size"
plot for [i=1:4] 'test.dat' using i+1:xticlabels(1) w lp title column(1 + i),

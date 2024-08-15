echo 0 > /sys/class/fpga_manager/fpga0/flags
cp FX32.bit /lib/firmware/
echo FX32.bit > /sys/class/fpga_manager/fpga0/firmware
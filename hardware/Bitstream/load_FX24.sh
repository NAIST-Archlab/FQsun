echo 0 > /sys/class/fpga_manager/fpga0/flags
cp FX24.bit /lib/firmware/
echo FX24.bit > /sys/class/fpga_manager/fpga0/firmware
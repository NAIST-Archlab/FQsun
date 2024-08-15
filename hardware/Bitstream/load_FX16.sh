echo 0 > /sys/class/fpga_manager/fpga0/flags
cp FX16.bit /lib/firmware/
echo FX16.bit > /sys/class/fpga_manager/fpga0/firmware
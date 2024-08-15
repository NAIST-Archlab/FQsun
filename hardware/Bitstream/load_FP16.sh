echo 0 > /sys/class/fpga_manager/fpga0/flags
cp FP16.bit /lib/firmware/
echo FP16.bit > /sys/class/fpga_manager/fpga0/firmware
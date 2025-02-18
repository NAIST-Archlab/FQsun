echo 0 > /sys/class/fpga_manager/fpga0/flags
cp FP32.bit /lib/firmware/
echo FP32.bit > /sys/class/fpga_manager/fpga0/firmware
echo 140000000 > /sys/devices/platform/fclk0/set_rate
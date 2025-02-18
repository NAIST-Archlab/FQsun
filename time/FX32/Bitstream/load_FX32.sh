echo 0 > /sys/class/fpga_manager/fpga0/flags
cp FX32.bit /lib/firmware/
echo FX32.bit > /sys/class/fpga_manager/fpga0/firmware
echo 110000000 > /sys/devices/platform/fclk0/set_rate
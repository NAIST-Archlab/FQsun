echo 0 > /sys/class/fpga_manager/fpga0/flags
cp FX24.bit /lib/firmware/
echo FX24.bit > /sys/class/fpga_manager/fpga0/firmware
echo 130000000 > /sys/devices/platform/fclk0/set_rate
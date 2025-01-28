[![Unitary Foundation](https://img.shields.io/badge/Supported%20By-UNITARY%20FOUNDATION-brightgreen.svg?style=for-the-badge)](https://unitary.foundation)

# An wave-function based quantum emulator on FPGA

Tuan Hai Vu, Vu Trung Duong Le, Hoai Luan Pham, Quoc Chuong Nguyen, Yasuhiko Nakashima

https://arxiv.org/abs/2411.04471

There are two value folders in this repo:
- Qsun: a wave-function based simulator, it's very simple. For any gate action, we looping through all elements on state-vector
- hardware (FPGA Qsun): the corresponding hardware accelerator for Qsun, design on ZCU102, the public codes are only the interface.
The detail design can be viewed in the paper.
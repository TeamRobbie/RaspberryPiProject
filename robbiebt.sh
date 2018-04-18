#!/bin/bash

sudo bluetoothctl connect 98:D3:32:11:64:0C
sudo rfcomm bind /dev/rfcomm1 98:D3:32:11:64:0C
sudo rfcomm watch hci1

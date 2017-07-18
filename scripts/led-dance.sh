#!/bin/bash

led()
{
  led-$1 $2
  sleep $3
  led-$1 off
}

ledSequece()
{
  led 1 $1 $2
  led 2 $1 $2
  led 3 $1 $2
}

delays= 

echo "LEDs dancing, CTRL-C to exit"

while true; do
  for delay in .5 .4 .3 .2 .1 .05 .05 .05 .05 .05 .05 .05 .05 .1 .2 .3 .4 .5; do
    ledSequece green $delay
    ledSequece amber $delay
    ledSequece red $delay
  done
done

#!/bin/bash
for i in {1..1}
do
   echo "=========================================================================="
   echo "Creating server m$i."
   echo "  "
   #touch t$i
   screen -dmS minecraft$i knife rackspace server create -A joeracker -K 1b8140addf7572b536c7d3d57819e086 -f 2 -I 80fbcb55-b206-41f9-9bc2-2dd7aac6c061 -N m$i -r "recipe[minecraft_class_server]" -S m$i
done

:'
### Other Knife Commands: ###
knife rackspace server create -A joeracker -K 1b8140addf7572b536c7d3d57819e086 -f 2 -I 80fbcb55-b206-41f9-9bc2-2dd7aac6c061 -N potato.woofcraft.net -r "recipe[minecraft_class_server]" -S potato.woofcraft.net
knife rackspace server list -A joeracker -K 1b8140addf7572b536c7d3d57819e086
knife rackspace server delete b11dcaad-a3ca-4e79-a683-cb0f103caacf -A joeracker -K 1b8140addf7572b536c7d3d57819e086
'
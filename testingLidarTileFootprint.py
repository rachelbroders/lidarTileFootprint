from WBT.whitebox_tools import WhiteboxTools

wbt = WhiteboxTools()

# since i=none, our input will be everything in the working directory
wbt.set_working_dir(
    "E:\\guelphAreaProject\\lasDir\\")

wbt.lidar_tile_footprint(
    output="E:\\guelphAreaProject\\grid.shp",
)

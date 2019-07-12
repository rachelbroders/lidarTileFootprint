from WBT.whitebox_tools import WhiteboxTools

wbt = WhiteboxTools()

# since i=none, our input will be everything in the working directory
wbt.set_working_dir("E:\\guelphAreaProject\\lasDir\\") #select directory containing LAS files of interest

wbt.lidar_tile_footprint( #this will create a polygon of a grid of square km tiles
    output="E:\\guelphAreaProject\\grid.shp", #choose output directory and file name
)

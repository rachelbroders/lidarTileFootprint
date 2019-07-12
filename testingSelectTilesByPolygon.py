import os
from os import path
from WBT.whitebox_tools import WhiteboxTools

def my_callback(value):
    if not "%" in value:
        print(value)

def main():
    polygon_dir = "E:\\projects\\londonSidewalksProject\\(2)polygonFiles\\"
    laz_files_dir = "E:\\projects\\londonSidewalksProject\\(3)lazDir\\"
    las_files_dir = "E:\\projects\\londonSidewalksProject\\(4)lasDir\\"
    hull_dir = "E:\\projects\\londonSidewalksProject\\(5)hullDir\\"
    hull_polygon_dir = "E:\\projects\\londonSidewalksProject\\(6)hullPolygonDir\\"
    clip_dir = "E:\\projects\\londonSidewalksProject\\(7)clipLidarToPolygon\\"
    tophat_dir = "E:\\projects\\londonSidewalksProject\\(8)tophatDir\\"
    joined_dir = "E:\\projects\\londonSidewalksProject\\(9)joinedDir\\"
    elevation_dir = "E:\\projects\\londonSidewalksProject\\(11)elevationDir\\"

    wbt = WhiteboxTools()
    wbt.default_callback = my_callback
    wbt.verbose = False

    ##################################################################################
    #                                convert laz->las                                #
    ##################################################################################
    # wbt.work_dir = laz_files_dir  # set working directory
    # for LAZfile in os.listdir(laz_files_dir):
    #     if LAZfile.endswith(".laz"):
    #         # convert to las
    #         command = "LASzip -i \"" + laz_files_dir + LAZfile + \
    #             "\" -o " + las_files_dir + LAZfile[0:-4] + ".las"
    #         os.system(command)
    #         print("->file" + LAZfile + "converted")
    # print("*********************ALL conversion done**************************")

    ##################################################################################
    #                                minimumConvexHull                               #
    ##################################################################################
    # wbt.work_dir = las_files_dir  # set working directory
    # for LASfile in os.listdir(las_files_dir):
    #     if LASfile.endswith(".las"):
    #         # minimumConvexHull
    #         wbt.lidar_tile_footprint(
    #             i = las_files_dir + LASfile,
    #             output = hull_dir + LASfile[1:-4] + ".shp"
    #         )
    #         print("->minimumConvexHull" + LASfile + " completed")
    # print("*********************ALL minimumConvexHull done**************************")

    ##################################################################################
    #                                      GRASS                                     #
    ##################################################################################
        #Comment out everything below, open GRASS and run script to cut 
        #'differencepolygon.shp' into square km portions according to tile.
        #ClipLidarToPolygon cannot handle entire differencePolygon.shp file at once.

    ##################################################################################
    #                                clipLidarToPolygon                              #
    ##################################################################################
    # wbt.work_dir = las_files_dir  # set working directory
    # for LASfile in os.listdir(las_files_dir):
    #     if LASfile.endswith(".las"):
    #         # clipLidarToPolygon
    #         wbt.clip_lidar_to_polygon(
    #             i = las_files_dir + LASfile,
    #             polygons = hull_polygon_dir + LASfile[1:-4] + ".shp",
    #             output = clip_dir + LASfile[0:-4] + "clipped.las"
    #         )
    #         print("->clipLidarToPolygon" + LASfile + " completed")
    # print("*********************ALL clipLidarToPolygon done**************************")

    ##################################################################################
    #                               lidarTophatTransform                             #
    ##################################################################################
    # wbt.work_dir = clip_dir  # set working directory
    # for LASfile in os.listdir(clip_dir):
    #     if LASfile.endswith(".las"):
    #         # lidarTophatTransform
    #         wbt.lidar_tophat_transform(
    #             i = clip_dir + LASfile,
    #             radius = 2.0,
    #             output = tophat_dir + LASfile[0:-11] + "tophat.las"
    #         )
    #         print("->lidarTophatTransform" + LASfile + " completed")
    # print("*********************ALL lidarTophatTransform done**************************")

    ###############################################################
    #                          lidarJoin                          #
    # #############################################################
    # Easiest to do this manually. Group files in sets that are 
    # around 400MB or smaller.

    ###############################################################
    #                     lidarElevationSlice                     #
    # #############################################################
    wbt.work_dir = joined_dir  # set working directory
    for LASfile in os.listdir(joined_dir):
        if LASfile.endswith(".las"):
            # lidarTophatTransform
            wbt.lidar_elevation_slice(
                i = joined_dir + LASfile,
                output = elevation_dir + LASfile[0:-4] + "elevation2.1m.las",
                minz = 0,
                maxz = 2.1,
                cls = False
            )
            print("->lidarElevationSlice" + LASfile + " completed")
    print("*********************ALL lidarElevationSlice done**************************")




main()
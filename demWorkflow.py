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
    raster_data_dir = "E:\\projects\\londonSidewalksProject\\(10)rasterDir\\"

    wbt = WhiteboxTools()
    wbt.default_callback = my_callback
    wbt.work_dir = las_files_dir  # set working directory
    wbt.verbose = False
    # if not os.path.exists(filtered_las_dir):
    #     os.makedirs(filtered_las_dir)

    ##################################################################################
    #             select Tiles by a polygon used select_tiles_by_polygon             #
    ##################################################################################

    # Sometimes, I like to extract all of the LAS tiles that overlap with a
    # particular area. For example, I might want to interpolate all the files
    # overlapping with a watershed. For this, you can use select_tiles_by_polygon.
    # Uncomment the four lines below if you want to do this.
    # indir = "E:\\LakeErie\\"
    # outdir = laz_files_dir
    # polygons = "E:\\guelphAreaProject\\shapeFiles\\guelphArea.shp"
    # wbt.select_tiles_by_polygon(las_files_dir, outdir, polygons)
    # print("*********************tile selection done**************************")

    ##################################################################################
    #                                convert laz->las                                #
    ##################################################################################
    # for LAZfile in os.listdir(laz_files_dir):
    #     if LAZfile.endswith(".laz"):
    #         # convert to las
    #         command = "LASzip -i \"" + laz_files_dir + LAZfile + \
    #             "\" -o " + las_files_dir + LAZfile[0:-4] + ".las"
    #         os.system(command)
    # print("*********************conversion done**************************")
    # ####################################################################

    ##################################################################################
    # Filter the ground points in the LAS files using lidar_ground_point_filter tool #
    ##################################################################################

    # This one is the SLOWEST part of the workflow and can be avoided if you are
    # confident that you have good point classification data, i.e. that the
    # vegetation and building classes have been properly populated.
    # processed_files = []
    # num_filtered = 1
    # flag = True
    # while flag:
    #     file_names = find_las_files(las_files_dir, processed_files)
    #     if len(file_names) > 0:  # and len(processed_files) < 3000:
    #         for i in range(len(file_names)):
    #             in_file = las_files_dir + file_names[i]
    #             out_file = filtered_las_dir + \
    #                 file_names[i].replace(".las", "_filtered.las")
    #             print("Processing LAS {} of {} (total filtered={}) {}".format(
    #                 i+1, len(file_names), num_filtered, file_names[i]))
    #             processed_files.append(file_names[i])
    #             wbt.lidar_ground_point_filter(in_file, out_file, radius=0.1, slope_threshold=45,
    #                                           height_threshold=0.05, min_neighbours=0, classify=False, slope_norm=True)
    #             num_filtered += 1
    #     else:
    #         flag = False
    # print("*********************filtering done**************************")

    ##############################
    # Interpolate the LAS files. #
    ##############################

    # If you don't use the above ground point filter the directory below must be
    # updated to point to the original LAS files.
    # wbt.work_dir = joined_dir

    # You can use either IDW, nearest neighbour, or TINing (Delaunay triangulation)
    # for the gridding step. TINing option is available as of WhiteboxTools v0.11.
    # wbt.lidar_idw_interpolation(parameter="elevation", returns="all", resolution=2.0, weight=1.0, radius=5.0, exclude_cls='3,4,5,6,7,18')
    # wbt.lidar_nearest_neighbour_gridding(returns="last", resolution=1.5, radius=2.5, exclude_cls='3,4,5,6,7,18')
    # wbt.lidar_tin_gridding(parameter="elevation", returns="all", resolution=1.0,
    #                        exclude_cls='1,3,4,5,6', max_triangle_edge_length=5)   #change exclusion classes for buildings!!!
    # print("*********************tinGridding done**************************")

    ###############################################################
    # Now mosaic the tiles; this is done using intermediate steps #
    # #############################################################
    # if not os.path.exists(raster_data_dir):
    #     os.makedirs(raster_data_dir)
    # wbt.work_dir = joined_dir  # set working directory   CHANGED THIS
    # wbt.verbose = False
    # processed_files = []
    # num_mosaiced = 1
    # flag = True
    # round = 0

    # while flag:
    #     # This will mosaic a maximum of 250 tiles together
    #     # these sub-files
    #     # will subsequently be merged. Mosaicing many hundreds of tiles
    #     # together at one time is otherwise too intensive.
    #     # changed first arguemnt from filtered_las_dir
    #     file_names = find_tiff_files(joined_dir, processed_files, 50)
    #     if len(file_names) > 1:
    #         round += 1
    #         in_files = ""
    #         for i in range(len(file_names)):
    #             if i < len(file_names)-1:
    #                 in_files += f"{file_names[i]};"
    #             else:
    #                 in_files += f"{file_names[i]}"
    #             processed_files.append(file_names[i])
    #             num_mosaiced += 1
    #         out_file = raster_data_dir + f"mosaic{round}.tif"
    #         wbt.mosaic(inputs=in_files, output=out_file, method="nn")
    #         print(
    #             f"Processing mosaic {round}; num. files = {num_mosaiced}")
    #         # print("infiles: " + str(in_files))
    #         # now clean up the individual tiles
    #         # for i in range(len(file_names)):
    #         #     os.remove(filtered_las_dir + file_names[i])
    #     else:
    #         flag = False

    mosaic_file = raster_data_dir + f"final_mosaic.tif"
    # if round > 1:
    #     print("Entered if")
    #     wbt.work_dir = raster_data_dir  # set working directory
    #     file_names = find_mosaic_files(raster_data_dir)
    #     if len(file_names) > 1:
    #         in_files = ""
    #         for i in range(len(file_names)):
    #             if i < len(file_names)-1:
    #                 in_files += f"{file_names[i]};"
    #             else:
    #                 in_files += f"{file_names[i]}"
    #             num_mosaiced += 1
    #         wbt.mosaic(inputs=in_files, output=mosaic_file, method="nn")
    #         # now clean up the intermediate mosaics
    #         for i in range(len(file_names)):
    #             os.remove(raster_data_dir + file_names[i])
    # else:
    #     print("Entered else")
    #     os.rename(raster_data_dir +
    #               f"mosaic1.tif", raster_data_dir + f"final_mosaic.tif")

    # print("*********************mosaic done**************************")

    ##############################################
    # Would you like to fill in the NoData gaps? #
    # ##############################################
    # dem_nodata_filled = raster_data_dir + f"DEM_gaps_filled.tif"
    # # experimented to find that the filter size of 25 works best
    # wbt.fill_missing_data(mosaic_file, dem_nodata_filled, filter=77)
    # print("*********************filling data done**************************")

    ######################################################################
    # I usually remove off-terrain objects, like any remaining buildings #
    # ######################################################################
    # dem_no_otos = raster_data_dir + f"DEM_no_OTOsF21S90.tif"
    # wbt.remove_off_terrain_objects(
    #     dem_nodata_filled, dem_no_otos, filter=21, slope=15.0)
    # print("*********************oto removal done**************************")

    #####################################
    # Would you like to smooth the DEM? #
    #####################################
    # dem_smoothed = raster_data_dir + f"DEM_smoothed.tif"
    # wbt.feature_preserving_denoise(dem_no_otos, dem_smoothed, filter=11, norm_diff=8.0)

    ################################
    # Want to fix the depressions? #
    ################################
    # dem_breached = raster_data_dir + f"DEM_breached.tif"
    # # Set the maximum breach depth appropriate for the terrain. You can
    # # also restrict breaching based on a maximum breach channel length.
    # wbt.breach_depressions(dem_smoothed, dem_breached, max_depth=5.0)

    # because we restricted the use of very deep breach channels, there
    # may still be depressions in the DEM. To get rid of these, we can
    # perform a subsequent depression filling operation.
    # dem_filled = raster_data_dir + f"DEM_filled.tif"
    # wbt.fill_depressions(dem_breached, dem_filled)

    ####################################################################
    # Okay, now we have a good base DEM from which we can extract      #
    # various land-surface parameters. There are really a large        #
    # number of these parameters available, but I'll just showcase     #
    # a few common ones here. See the User Manual for a complete list. #
    ####################################################################

    # # slope
    # slope_file = raster_data_dir + f"slope.tif"
    # wbt.slope(dem_filled, slope_file)

    # # plan curvature
    # plan_curv_file = raster_data_dir + f"plan_curv.tif"
    # wbt.plan_curvature(dem_filled, plan_curv_file)

    # # profile curvature; other curvatures are available too.
    # profile_curv_file = raster_data_dir + f"profile_curv.tif"
    # wbt.profile_curvature(dem_filled, profile_curv_file)

    # hillshade (shaded relief raster)
    hillshade_file = raster_data_dir + f"hillshadeNoFill.tif"
    wbt.hillshade(mosaic_file, hillshade_file)
    print("*********************hillshading done**************************")

    # # relative topographic position (RTP) index
    # rtp_file = raster_data_dir + f"relative_topographic_position.tif"
    # wbt.relative_topographic_position(dem_filled, rtp_file, filterx=11, filtery=11)

    # # or even better, multiscale topographic position
    # dev_max_mag = raster_data_dir + f"multiscale_topo_position_mag.tif"
    # dev_max_scale = raster_data_dir + f"multiscale_topo_position_scale.tif"
    # wbt.max_elevation_deviation(dem_filled, dev_max_mag, dev_max_scale, min_scale=1, max_scale=100, step=2)

    # # ruggedness index
    # ruggedness_index_file = raster_data_dir + f"ruggedness_index.tif"
    # wbt.ruggedness_index(dem_filled, ruggedness_index_file)

    # # or even better, multiscale roughness
    # roughness_mag = raster_data_dir + f"multiscale_roughness_mag.tif"
    # roughness_scale = raster_data_dir + f"multiscale_roughness_scale.tif"
    # wbt.multiscale_roughness(dem_filled, roughness_mag, roughness_scale, min_scale=1, max_scale=100, step=2)

    # # D-infinity flow accumulation
    # flow_accum_file = raster_data_dir + f"dinf_flow_accum.tif"
    # wbt.d_inf_flow_accumulation(dem_filled, flow_accum_file, log=True)

    # There literally hundreds of other useful parameters that could be
    # extracted from our DEM using WhiteboxTools. Take a look at the User Manual.

    print("Done!")


def find_las_files(input_dir, processed_files):
    files = os.listdir(input_dir)
    file_names = []
    for f in files:
        if f.endswith(".las") and f not in processed_files:
            file_names.append(f)

    return file_names


def find_tiff_files(input_dir, processed_files, max_num=10):
    files = os.listdir(input_dir)
    file_names = []
    for f in files:
        if f.endswith(".tif") and f not in processed_files:
            if len(file_names) < max_num:
                file_names.append(f)
            else:
                break
    return file_names


def find_mosaic_files(input_dir):
    files = os.listdir(input_dir)
    file_names = []
    for f in files:
        # changed by Rachel, added "or .sdat"
        if "mosaic" in f and (f.endswith(".sdat") or f.endswith(".dep") or f.endswith(".tif")):
            file_names.append(f)

    return file_names


main()

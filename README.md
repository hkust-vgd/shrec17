# SHREC 2017: RGB-D Object-to-CAD Retrieval 

This repository contains detailed description of the dataset and supplemental code for [SHREC 2017 track: RGB-D Object-to-CAD Retrieval](http://people.sutd.edu.sg/~saikit/projects/sceneNN/shrec17/index.html).
In this track, our goal is to retrieve a CAD model from ShapeNet using a SceneNN model as input.

# Download

* [3D models]((https://drive.google.com/drive/folders/0B2BQi-ql8CzeOTZaa2Fvem5xb2s)
* [Data viewer](https://github.com/scenenn/shrec17/releases)
* [Labels](https://drive.google.com/drive/folders/0B2BQi-ql8CzeaDNQQXNmZHdnSFE)
(optional)
* [Mask from label code](https://github.com/scenenn/shrec17/tree/master/mask_from_label)
* [RGB-D video and trajectory](https://drive.google.com/drive/folders/0B-aa7y5Ox4eZWE8yMkRkNkU4Tk0?usp=sharing) (optional)
* [ONI playback tool](https://github.com/scenenn/scenenn/tree/master/playback)

# Dataset 
In this dataset, we manually group 1667 SceneNN objects and 3308 ShapeNet models into 20 categories. Only indoor objects that are both available in SceneNN and Shapenet dataset are selected. The object distribution in this dataset are shown below.

![Object distribution in the dataset](images/objectDistribution.png?raw=true)

By following the idea in the ShapeNet dataset, we split our dataset into training, validation, and test set. The split ratio is 50/25/25%. 
All data could be downloaded [here](https://drive.google.com/drive/folders/0B2BQi-ql8CzeOTZaa2Fvem5xb2s). 

The objects in both SceneNN and ShapeNet are grouped into categories and subcategories, which are stored in CSV files. All categories and subcategories for training and validation are provided in `train.csv` and `validation.csv`. The `test.csv` has categories removed for evaluation purposes. In general, we will first consider categories in the evaluation. The subcategories could be used for more rigorous evaluation after using categories.

## Query data
Each SceneNN object is stored in 3D as a triangle mesh in PLY format. Each mesh vertex has a world position, normal, and color value. Additional information in 2D is also included such as (a) camera pose, (b) color image, (c) depth image, (d) label image for each RGB-D frame that contains the object.

Each SceneNN object has an ID formatted as `<sceneID>_<labelID>`, where `sceneID` is a three-digit scene number, and `labelID` is an `unsigned integer` that denotes a label. For example, `286_224114` identifies label `224114` in scene `286`. 

It is perhaps more convenient to work with the 3D data as they are more compact and manageable. For researchers who are interested in the 2.5D color and depth frames, you can: 

+ Download item (a), (b), and (c) in the SceneNN scene repository [here](https://drive.google.com/drive/folders/0B-aa7y5Ox4eZWE8yMkRkNkU4Tk0?usp=sharing). All images for each scene are packed in an ONI video file, which can be extracted using the `playback` tool [here](https://github.com/scenenn/scenenn/tree/master/playback). Note that to store images for all scenes, a hard drive with free space about 500 GB is preferred.

+ Download the labels in item (d) [here](https://drive.google.com/drive/folders/0B2BQi-ql8CzeaDNQQXNmZHdnSFE). To extract a binary mask for each object, use the (`mask_from_label`) code  [here](https://github.com/scenenn/shrec17/tree/master/mask_from_label).
 
## Target data
Each ShapeNet object is stored in 3D as a triangle mesh in OBJ format, with color in a separate material file in MTL format, and (optional) textures. The ShapeNet objects are a subset of ShapeNetSem. All object IDs are the same as those in the original ShapeNet dataset. 

## Tools
To assist dataset investigation, we provide a model viewer tool (Windows 64-bit only) which can display SceneNN and ShapeNet objects in categories:

![Dataset viewer](images/viewer.png?raw=true)

Please download the viewer [here](https://github.com/scenenn/shrec17/releases).

## Acknowledgement
The CAD models in this dataset are extracted from [ShapeNet](https://www.shapenet.org/), a richly annotated and large-scale dataset of 3D shapes by Stanford. 



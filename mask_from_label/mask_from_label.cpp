#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <string>
#include <iostream>

using namespace cv;

int main(int argc, char** argv )
{
    if ( argc != 4 )
    {
        printf("Parameters: <input label image>  <label ID>  <output mask image>\n");
        return -1;
    }

    Mat image;
    image = imread( argv[1], -1 );

    if ( !image.data )
    {
        printf("No image data \n");
        return -1;
    }

    unsigned int label = atoi(argv[2]);
    std::cout << "Input label: " << label << std::endl;

    int rows = image.rows;
    int cols = image.cols;

    Mat binary_image = Mat::zeros(image.rows, image.cols, CV_8UC3);

    for (int x = 0; x < rows; x++) {
        for (int y = 0; y < cols; y++) {
            unsigned int pixel_label = (unsigned int)image.at<cv::Vec4b>(x, y)[0] << 24 |
                          (unsigned int)image.at<cv::Vec4b>(x, y)[1] << 16 |
                          (unsigned int)image.at<cv::Vec4b>(x, y)[2] << 8  |
                          (unsigned int)image.at<cv::Vec4b>(x, y)[3];
            
            if (pixel_label == label) {
                binary_image.at<cv::Vec3b>(x,y)[0] = 255;
                binary_image.at<cv::Vec3b>(x,y)[1] = 255;
                binary_image.at<cv::Vec3b>(x,y)[2] = 255;
            }
        }
    }

    imwrite(argv[3], binary_image);

    return 0;
}

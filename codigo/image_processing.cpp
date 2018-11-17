#include <opencv2/opencv.hpp>
#include <vector>
#include <boost/python.hpp>
#include <boost/python/numpy.hpp>
#include <iostream>

namespace p = boost::python;
namespace np = boost::python::numpy;


np::ndarray findBalls ()
{
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.medianBlur(img, blur)

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,
                  1, #dp - proporcao maluca
                  minDist=min_dist,
                  param1=hough1,
                  param2=hough2,
                  minRadius=min_radius,
                  maxRadius=max_radius)
}

BOOST_PYTHON_MODULE (image_processing)
{
    boost::python::def("findBalls", findBalls);
    boost::python::def("findRacket", findRacket);
}

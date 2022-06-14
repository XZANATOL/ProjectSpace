## Thumbstack Logo Detect implementation using Python

This is an `opencv` + `numpy` based script used to detect an object from an image by providing it a template image of that object.

### Usage

To detect an object:

> `python3 Detector.py -i <image_filename>`

To detect an object using another template:

> `python3 Detector.py -t <template_filename> -i <image_filename>`

Note: put paths between quotes

### Output

* Display detection output for 5 seconds
* Autosave the output image under the name: `Output.png`

### Detailed Description of the implementation

`opencv` module provides a method to detect objects from image by providing a template image to be taken as a reference. It also provides multiple ways of object detection such as:
* cv.TM_CCOEFF
* cv.TM_CCOEFF_NORMED
* cv.TM_CCORR
* cv.TM_CCORR_NORMED
* cv.TM_SQDIFF
* cv.TM_SQDIFF_NORMED

However, `cv.TM_CCOEFF_NORMED` is better in most cases as it uses stastical detection using normalized correlation coefficient which gives more accurate detections. The one downside of this method is that if the provided dimensions of an image is much bigger than the template dimensions, accuracy errors in detection will take place. The workaround on this is to use multiple scales of the image and select the one with maximum value of normalized correlation coefficient. A more accurate example is shown below.

The detection will work fine on small-medium images without multiple scaling. Here is an example: ![image](./Tests/small_image.png) <br>
But when a large image is provided, the will be the result: ![image](./Tests/big_image.png) <br>
After applying multiple scales algorithm: ![image](./Tests/big_image_accurate.png) <br>

### Resources

* [Numpy linspace function](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
* [imutils resize function](https://github.com/jrosebr1/imutils)
* [opencv minmaxloc function](https://www.tutorialexample.com/learn-python-opencv-cv2-minmaxloc-by-examples-opencv-tutorial/)
* [Multi Scaling Idea](https://www.pyimagesearch.com/2015/01/26/multi-scale-template-matching-using-python-opencv/)

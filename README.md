# Straight Lane Detection

## Description

Given a dashcam video of a car, this project attempts to detect the lane inside which the car is travelling.


## Data

* Dashcam Video

![alt text](/data/data.gif)


## Approach

* For each frame, isolated the trapezoidal section by applying a mask using Bitwise AND operation

* The Hough Transform of the image was found and to filter out many of the overlapping lines, all the lines that made an angle of less than 12 degrees with any of the other lines were removed.

* The lengths of the remaining lines were found and the ones with whose lengths were greater than 200 were considered to be solid lanes and colored green.

* The ones whose lengths were less than 200 were considered as dashed and colored red.


## Output

* Isolating trapezoidal section

![alt text](/output/out1.jpg)

* Colored Lanes

![alt text](/output/out2.jpg)

* Final Output for Straight Lane Detection [Link](https://drive.google.com/file/d/1v8kkR4LeNifDvQGzbkCY7HUPcyHfM6hn/view?usp=sharing)

![alt text](/output/outvid.gif)


## Getting Started

### Dependencies

<p align="left"> 
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>&ensp; </a>
<a href="https://numpy.org/" target="_blank" rel="noreferrer"> <img src="https://www.codebykelvin.com/learning/python/data-science/numpy-series/cover-numpy.png" alt="numpy" width="40" height="40"/>&ensp; </a>
<a href="https://opencv.org/" target="_blank" rel="noreferrer"> <img src="https://avatars.githubusercontent.com/u/5009934?v=4&s=400" alt="opencv" width="40" height="40"/>&ensp; </a>

* [Python 3](https://www.python.org/)
* [NumPy](https://numpy.org/)
* [OpenCV](https://opencv.org/)


### Executing program

* Clone the repository into any folder of your choice.
```
git clone https://github.com/ninadharish/Straight-Lane-Detection.git
```

* Open the repository and navigate to the `src` folder.
```
cd Straight-Lane-Detection/src
```
* Depending on whether you want to superimpose athe image or 3D cube on the tag, comment/uncomment the proper line.

* Run the program.
```
python main.py
```


## Authors

👤 **Ninad Harishchandrakar**

* [GitHub](https://github.com/ninadharish)
* [Email](mailto:ninad.harish@gmail.com)
* [LinkedIn](https://linkedin.com/in/ninadharish)
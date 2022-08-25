# quixl
A pixel art maker written in python.

### Why did I name it quixl?
I forgot pixel had an 'e' in it so I thought qui(ck-pi)xl
but I like the name so I'm not changing it.

## To run quixl
pygame and Pillow are required  
Then, just run **main.py**

## How to Draw
Pixel art is simple with quixl!  
> **Left click** to draw  
> **Right click** to erase  
> **Middle click** to select color  

## File saving and loading
Files will be saved and loaded from the quixl.png file.
File names are a planned feature.

## Colors
We have 4 sliders. R, G, B, Grayscale.
The first 3 are self-explanatory, for selecting RGB colors.
The grayscale slider will control R, G, and B at the same time for easy selection of blacks, whites, and grays.
  
We also have some preset colors. Just click on them to select the color! These are not customizable at the moment.

## Commands/Keys
The key(s) to press are in bold
### Basic Commands
> Save - **s**  
> Open - **o**  
> Export - **e**  
> Open Folder<sup>1</sup>  - **f**

> Reset Canvas - **n**, **BACKSPACE**, **r**, or **n**  
> Exit - **ESCAPE**  

### Change Size Commands
This will clear your current artwork and resize
> 4x4 - **1**  
> 8x8 - **2**  
> 16x16 - **3**  
> 32x32 - **4**  
> 64x64 - **5**  
> 128x128 - **6**  

### Color Commands
> Lighten - **]**  
> Darken - **[**

### Other Commands
> Toggle Middle - **t**  
> Toggle Grid - **g**  
> Jumble - **j**  
> Toggle Watermark - **w**  
> Toggle Complex Color Mode - **c**

## Configuration
To modify quixl's config, open config.json.  

### Default Config
The default value/formatting of the current config.json file is the following:

    {
        "default-size": 3,
    }


### Config Options
In config.json, you can change the following of quixl's data:
> **default-size** - When starting quixl, this will be the size of the canvas.  
You can set this to the following:  
>> 4x4 - **1**  
8x8 - **2**  
16x16 - **3**  
32x32 - **4**  
>64x64 - **5**  
128x128 - **6**
>
> These are the same values as above in "Change Size Commands"

## Footnotes
**1 - This feature is only available on Windows devices.**
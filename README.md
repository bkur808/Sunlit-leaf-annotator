## Installation (Updated 2/23/25 for compatabilities)

### Windows/Linux Set-up

If using Windows - download and install Anaconda for Python 3, or alternatively, set up a virtual machine with any Linux distribution (for example Debian-Ubuntu on WSL2)

Open a terminal, then clone this repository into a directory.
Then, from the directory you can install the required libraries and packages using the below scripts.

```
$ cd path/to/your/project
```

```
$ pip install -r requirements.txt
```

### How to begin:

Place all images you wish to annotate in the data/train/ directory.

Once you are in the project's root folder run.

```
 $ cd src ; python3 main.py
```

#### Currently on startup this app version initializes with the default segmentation requirements almond segmentation for Fresno State's AIIS CIWA+ research group.

Once the UI is initialized go to File -> Open an Image and select one image from your "train" folder.

Segmentation -> Execute

After the segmentation finishes, you will see that the image is now split and each segment has a border around it.

### Annotation steps:

1.  By default all segments are annotated as Noise.
2.  Click on the Sunlit class (on the left of the panel) and annotate the sunlit leaves.

**If you missclick by accident, pick the correct class and click again**

**Guidelines for proper annotation**

- Click on ALL leafs that are sunlit (brighter)
- Completely avoid selecting ground, as it gives wrong thermal data.
- Completely avoid selecting fruit segments, even if they are sunlit.
- Mostly avoid sky: When selecting leaf segmentation that have partial sky, aim for 75% of leaf within segment (25% of sky at most), and only if it is worth it to select said leaf.

**!!! Warning, if you open an already annotated image, the annotation will be reset, so keep track of your completed images!!!**

You can find the generated mask for your image inside data/train_labels/.

### Checking your progress and review:

In order to review your progress, we can create a review folder of mask overlays, beginning from the project root folder:

```
cd data ; python3 mask_creator.py
```

This will print to the terminal a list of remaining files in your train folder which require annotations, as well as create overlay images in a folder /data/overlay_masks_review in order to review your work.

#### Happy Annotating!

For questions, please feel free to contact Brian (Fresno AIIS CIWA+ team) at bkurzeja@mail.fresnostate.edu

Original software found at http://git.inovisao.ucdb.br/inovisao/pynovisao .

NPOSL-30 https://opensource.org/licenses/NPOSL-3.0 - Free for non-profit use (E.g.: Education, scientific research, etc.). Contact Inovisão's Prof. Hemerson Pistori (pistori@ucdb.br), should any interest in commercial exploration of this software arise.

### Demos

- https://www.youtube.com/watch?v=lnoXL1hGTJI
- https://www.youtube.com/watch?v=Q-cjCxUqW_Q

# SketchStyler

Though it is easy to illustrate complicated ideas with a pen and paper, I 




<img src="original.jpg" title="Input" alt="original sketch" width="50%"/><img src="output.png" title="Output" alt="modified sketch" width="50%"/>


# Installation

As I haven't tested this thoroughly, it might be a good idea to use a dedicated virtual enviroment first. For example, make a new conda env called rgb:

```console
$ conda create --name rgb
```
activate it
```console
$ conda activate rgb
```

and install pip
```console
$ conda install pip
```

Then clone this repo (to current location)
```console
$ git clone https://github.com/mrbarkis/SketchStyler.git
```

and then install using
```console
$ pip install ./SketchStyler
```
(or run setup.py within SketchStyler folder)

You should now be aple to run the main script

```console
$ rgb2.py -h
```

or to use the modules. For example, install jupyter and run the example notebook, as in

```console
$ conda install jupyter
$ cd SketchStyler
$ jupyter notebook example.ipynb
```



# Tips

1. [Whitelines](https://www.whitelinespaper.com/) paper and its app makes digitizing sketches a breeze. 
2. Gimp's 'Filters -> Blur -> Mean-Curvature-Blur' can work wonders as well. It can smooth both the colors and the edges in a natural-seeming fashion. To use it on the edges, first select 'Layer -> Mask -> Add layer mask -> Transfer layer's alpha channel', and then apply the filter on the layer mask. As an example,

<img src="output_mean_curvature_blur.png" alt="Gimped sketch" width="100%"/>

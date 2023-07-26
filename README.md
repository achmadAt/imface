# imface

this cli project is depended on serengil deepface project
https://github.com/serengil/deepface


because the program not deployed in pypi yet you can copy the project using git and use pip to install
```
pip install .
```

to uninstall

```
pip uninstall imface
```

how to use

```
imface --represent image-path
```
to get the embedded vectors of an image

```
imface --extract image-path
```
to extract embedded vector of face in image, only just for one face per image

```
imface --treshold
```
to get the treshold that we use

```
imface distance -s [source-vector] -t [target-vector]
```
to get similiarity distance between image vector
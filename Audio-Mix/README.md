# Audio Mix Project File
The aim for this project is to create an "volume mixer" interface similar to on windows to enable the inputs of multiple media streams to be controlled independently.

## TODO
1. find a technology to interact with kernel?
2. decide on what language and interface style to create
3. create simple version without gui to interface with chosen technology from TODO 1
4. implement interface and connect to simple version as above

### TODO 1: find a technology
* Building an interface for Pipewire is the daemon needed to interact
* looking like writing in C is required

* Wireplumer -> Lua API
* Wireplumer -> wpctl set-volume ID VOL (DO not exceed 1.5)

# Work Done

# Plan

Use python to create a gui using customtkinter sliders

Use wp status > loaded.txt for the file to parse to pull audio sources

For each audio source create a slider (ranging 0 to 1.5)

Try find a way to distinguish sources from eachother (e.g firefox source 52 and firefox source 75)
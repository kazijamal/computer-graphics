# mks66-final

## Kazi Jamal and Alexander Zou, Period 4 Graphics

## Features

-   light
    -   Add a light to the symbol table
    -   When calculating diffuse and specular: loop through all the lights.
    -   MDL commands:
        -   light lightname x y z r g b
            -   creates a "light" datastructure with rgb values r,g,b at location x,y,z. This is inserted into the symbol table.
        -   ambient r g b
            -   specifies how much ambient light is in the scene
-   set
    -   Assign a value to a knob
    -   MDL commands:
        -   set knobname value
            -   sets a knobs value (in the symbol table).
-   saveknobs
    -   Save current knob values to a list
    -   MDL commands:
        -   save_knobs knoblist
            -   saves the current values of all knobs under the name "knoblist."
-   tween
    -   Produce an animation by going between two knob lists
    -   MDL commands:
        -   tween start_frame end_frame knoblist0 knoblist1
            -   generates a number of frames using basename
                as the base filename. It will start from
                start_frame and end at end_frame and
                interpolate the image using knoblist0 as
                the starting configuration and knoblist 2
                as the ending configuration.
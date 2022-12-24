# PhisEngine
Half working n-body engine
## Adding of new objects
In preview already preinstalled simulation of inner solar system, but you can easily make any other simularion as you like
### Step 1
For the first you need to add/replace new object in data/objects.json , like below:
````json
{
"<object_name>": {
    "sprite": true,
    "radius": 6051840,
    "mass": 48.685E23,
    "velocity": [2.90E+04, 1.89E+04, -1.41E+03],
    "pos": [5.80E+10, -9.11E+10, -4.65E+09]
  }
}
````
- **"<object_name>"** - place there name of new object
- **"sprite"** - defining, will it be rendering on screen
- **"radius"** - radius of object
- **"mass"** - mass of object
- **"velocity"** - velocity of object
- **"pos"** - position of object

### Step 2
Then add new line in data/UI/types_data.json by example:
````json
{
  ...
  },
  "placements": [
    {"name": "object_name", "pos": [0, 0], "type": "button", "groups": ["celestial_body"]}
  ]
}
````
- **"name"** - place there name of new object, exactly like in prevus file
- **"pos"** - pos of new object on screen ("[0, 0]" only)
- **"type"** - type of smaple ("button" only)
- **"groups"** - group ("["celestial_body"]" only)
